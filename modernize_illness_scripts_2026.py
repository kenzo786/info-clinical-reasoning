#!/usr/bin/env python3
"""Deterministic modernization pipeline for 2026 illness scripts.

Pass A: rewrite (minimal structural mutation; edit list-item content only).
Pass B: lint (hard checks for structure, epidemiology shortcode, and style gates).
"""

from __future__ import annotations

import argparse
import html
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


SECTION_IDS = list(range(1, 14))
DETAILS_TOKEN_RE = re.compile(r"(?is)<details\b|</details>")
TITLE_DIV_RE = re.compile(r'(?is)<div\s+id="illness-script-title">(.*?)</div>')
HTML_TAG_RE = re.compile(r"(?is)<[^>]+>")
SPACE_RE = re.compile(r"\s+")
LI_RE = re.compile(r"(?is)<li\b[^>]*>(.*?)</li>")
UL_RE = re.compile(r"(?is)<ul\b[^>]*>(.*?)</ul>")
ID_RE = re.compile(r'id="([^"]+)"')
SHORTCODE_RE = re.compile(r"(?is)\[sc\b.*?\[/sc\]")
ENCODING_ARTIFACT_RE = re.compile(r"(Â|â€™|â€œ|â€|�)")
UNSOURCED_EPI_NUMERIC_RE = re.compile(
    r"(?is)(\d+(?:\.\d+)?\s*%|\bincidence\b|\bprevalence\b|\bper\s+\d+\b|\b\d+\s+(cases|admissions)\b)"
)
ESSENTIALS_FORMAT_RE = re.compile(r"^UKMLA essentials:\s*[^,]+,\s*[^,]+,\s*[^,.]+\.$")
BOILERPLATE_BANNED_PHRASES = [
    "recognise pattern, spot instability, check key tests",
    "risk is influenced by patient, comorbidity, and exposure context",
    "atypical presentations and multimorbidity can delay recognition",
    "a generalized representation supports differential diagnosis and initial management planning",
    "management usually combines condition-specific therapy, supportive care, and shared decision-making",
    "alternative diagnoses - distinguish by pattern, objective findings, and response to treatment",
    "review symptoms, objective markers, and treatment response over time",
    "arrange urgent specialist review for red flags, rapid deterioration, or diagnostic uncertainty",
]
ESSENTIALS_GENERIC_TOKENS = ["pattern", "instability", "key tests", "check tests", "red flags"]
UK_SPELLING_VIOLATIONS = ["recognized", "stigmatizing", "pediatric", "edema"]
STI_SLUG_HINTS = ["chlamydia", "gonorrhoea", "gonorrhea", "hiv", "syphilis", "trichomon", "sti", "std"]
NON_GENERIC_MEDICAL_ANCHORS = [
    "naat",
    "pid",
    "epididymitis",
    "ectopic",
    "orchitis",
    "urethritis",
    "cervicitis",
    "partner",
    "screening",
]


def slug_to_title(slug: str) -> str:
    if slug.startswith("is-"):
        slug = slug[3:]
    return " ".join(p[:1].upper() + p[1:] for p in slug.split("-") if p)


def strip_html(value: str) -> str:
    value = HTML_TAG_RE.sub(" ", value)
    value = html.unescape(value)
    return SPACE_RE.sub(" ", value).strip()


def normalize(value: str) -> str:
    return SPACE_RE.sub(" ", strip_html(value).lower()).strip()


def word_count(value: str) -> int:
    return len(re.findall(r"\b\w+\b", strip_html(value)))


def find_matching_details_end(text: str, open_index: int) -> int:
    depth = 0
    seen_open = False
    for m in DETAILS_TOKEN_RE.finditer(text, open_index):
        token = m.group(0).lower()
        if token.startswith("<details"):
            depth += 1
            seen_open = True
        else:
            if seen_open:
                depth -= 1
                if depth == 0:
                    return m.end()
    return -1


def get_section_span(text: str, n: int) -> Optional[Tuple[int, int]]:
    opener = re.search(rf'(?is)<details\b[^>]*\bid="c-is\.{n}\.0"[^>]*>', text)
    if not opener:
        return None
    end = find_matching_details_end(text, opener.start())
    if end < 0:
        return None
    return opener.start(), end


def get_condition_name(text: str, slug: str) -> str:
    m = TITLE_DIV_RE.search(text)
    if not m:
        return slug_to_title(slug)
    content = m.group(1)
    content = re.sub(r'(?is)\[sc\s+name="ask-ai-\d+".*?\[/sc\]', "", content)
    content = strip_html(content)
    content = re.sub(r"\s*Illness\s+Script\s*$", "", content, flags=re.IGNORECASE).strip()
    return content or slug_to_title(slug)


def split_ul(section_html: str) -> Optional[Tuple[int, int, str, str]]:
    m = UL_RE.search(section_html)
    if not m:
        return None
    return m.start(), m.end(), section_html[m.start() : m.start(1)], section_html[m.end(1) : m.end()]


def extract_lis(ul_inner: str) -> List[str]:
    return [m.group(1).strip() for m in LI_RE.finditer(ul_inner)]


def normalize_detached_ul_wrapper(section_html: str, ul_start: int) -> str:
    before = section_html[:ul_start]
    # Repair patterns like: <div ...></div>\n<ul> ... by converting to open wrapper.
    m = re.search(r'(?is)<div\s+id="o-is\.\d+\.0"[^>]*></div>\s*$', before)
    if not m:
        return section_html
    tag = m.group(0)
    fixed = re.sub(r">\s*</div>\s*$", ">", tag)
    return section_html[: m.start()] + fixed + section_html[m.end() :]


def ensure_child_div_closed(section_html: str, section_id: int) -> str:
    div_open = re.search(rf'(?is)<div\s+id="o-is\.{section_id}\.0"[^>]*>', section_html)
    if not div_open:
        return section_html
    details_pos = section_html.lower().rfind("</details>")
    if details_pos < 0:
        details_pos = len(section_html)
    between = section_html[div_open.end() : details_pos]
    if "</div>" in between:
        return section_html
    ul_match = re.search(r"(?is)<ul\b.*?</ul>", between)
    if not ul_match:
        return section_html
    insert_at = div_open.end() + ul_match.end()
    return section_html[:insert_at] + "\n    </div>" + section_html[insert_at:]


def render_li_block(section_html: str, li_values: List[str]) -> str:
    ul_split = split_ul(section_html)
    if ul_split:
        ul_start, ul_end, ul_prefix, ul_suffix = ul_split
        section_html = normalize_detached_ul_wrapper(section_html, ul_start)
        ul_split = split_ul(section_html)
        if not ul_split:
            return section_html
        ul_start, ul_end, ul_prefix, ul_suffix = ul_split
        inner = section_html[ul_start + len(ul_prefix) : ul_end - len(ul_suffix)]
        li_indent = "            "
        m_indent = re.search(r"(?m)^([ \t]*)<li\b", inner)
        if m_indent:
            li_indent = m_indent.group(1)
        rendered = "".join(f"\n{li_indent}<li>{v}</li>" for v in li_values)
        if rendered:
            rendered += "\n"
        new_ul = f"{ul_prefix}{rendered}{ul_suffix}"
        return section_html[:ul_start] + new_ul + section_html[ul_end:]

    div_match = re.search(r"(?is)<div\b[^>]*>", section_html)
    if not div_match:
        return section_html
    ul_block = "        <ul>\n" + "".join(f"            <li>{v}</li>\n" for v in li_values) + "        </ul>"
    idx = div_match.end()
    return section_html[:idx] + "\n" + ul_block + section_html[idx:]


def ensure_essentials_line(section_html: str, essentials_text: str) -> str:
    if "UKMLA essentials:" in section_html:
        return section_html
    ul_match = re.search(r"(?is)<ul\b[^>]*>(.*?)</ul>", section_html)
    if not ul_match:
        return section_html
    inner = ul_match.group(1)
    li_count = len(re.findall(r"(?is)<li\b[^>]*>.*?</li>", inner))
    if li_count >= 2:
        return section_html
    li_indent = "            "
    m_indent = re.search(r"(?m)^([ \t]*)<li\b", inner)
    if m_indent:
        li_indent = m_indent.group(1)
    insert_at = ul_match.end(1)
    inject = f"\n{li_indent}<li>{essentials_text}</li>"
    return section_html[:insert_at] + inject + section_html[insert_at:]


def tokens(value: str) -> set:
    return set(re.findall(r"[a-z0-9]+", normalize(value)))


def trim_words(value: str, max_words: int) -> str:
    words = value.split()
    if len(words) <= max_words:
        return value
    out = " ".join(words[:max_words]).rstrip(",;:-")
    return out + "."


def clean_li_text(li: str) -> str:
    txt = strip_html(li)
    txt = txt.replace(" :", ":").replace(" .", ".")
    return SPACE_RE.sub(" ", txt).strip()


def strip_shortcodes(value: str) -> str:
    return SPACE_RE.sub(" ", SHORTCODE_RE.sub(" ", value)).strip()


def first_sentence(text: str) -> str:
    text = clean_li_text(text)
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text)
    first = parts[0].strip()
    if not first.endswith("."):
        first = first.rstrip(".") + "."
    return first


def ensure_action_prefix(li: str, action: str) -> str:
    if "[sc " in li.lower():
        if normalize(li).startswith(action.lower()):
            return li
        return f"<b>{action}</b> {li}"
    txt = clean_li_text(li)
    txt = re.sub(r"(?is)^ask about\b[:\-\s]*", "", txt)
    txt = re.sub(r"(?is)^check\b[:\-\s]*", "", txt)
    txt = txt[0].lower() + txt[1:] if txt else txt
    txt = trim_words(txt, 24)
    return f"<b>{action}</b> {txt}"


def sanitize_prescriptive_text(li: str) -> str:
    txt = li
    txt = re.sub(
        r"(?is)\b(start|give|administer|prescribe)\b[^.]*?\b\d+(\.\d+)?\s*(mg|mcg|g|ml|units?)\b[^.]*\.?",
        "Management should follow local protocol and specialist guidance.",
        txt,
    )
    txt = re.sub(r"(?is)\bdose of\b[^.]*\.?", "Use local protocol-directed treatment.", txt)
    return txt


def classify_keep_compress_drop(old_lis: List[str], new_lis: List[str], section_id: int) -> Dict[str, int]:
    result = {"keep": 0, "compress": 0, "drop": 0}
    new_norm = [normalize(x) for x in new_lis]
    new_tokens = [tokens(x) for x in new_lis]
    for old in old_lis:
        old_norm = normalize(old)
        if not old_norm:
            continue
        if old_norm in new_norm:
            result["keep"] += 1
            continue
        old_t = tokens(old)
        best = 0.0
        for nt in new_tokens:
            if not old_t or not nt:
                continue
            inter = len(old_t & nt)
            union = len(old_t | nt)
            score = inter / union if union else 0.0
            best = max(best, score)
        if section_id == 2 and UNSOURCED_EPI_NUMERIC_RE.search(strip_html(old)):
            result["drop"] += 1
        elif best >= 0.35:
            result["compress"] += 1
        else:
            result["drop"] += 1
    return result


def default_rules() -> Dict:
    return {
        "forbidden_prescriptive_patterns": [
            r"(?is)\b(start|give|administer|prescribe)\b.{0,40}\b\d+(\.\d+)?\s*(mg|mcg|g|ml|units?)\b",
            r"(?is)\bdose of\b",
        ],
        "prescriptive_whitelist_patterns": [
            r"(?is)\bserum magnesium\b",
            r"(?is)\bphosphate\b",
        ],
        "section_budgets": {
            "1": [1, 2],
            "2": [3, 5],
            "3": [1, 3],
            "4": [2, 4],
            "5": [3, 5],
            "6": [3, 5],
            "7": [4, 6],
            "8": [2, 4],
            "9": [2, 2],
            "10": [2, 2],
            "11": [4, 6],
            "12": [4, 6],
            "13": [4, 6],
        },
        "condition_templates": {
            "is-anorexia-nervosa": {
                "1": [
                    "Anorexia nervosa is an eating disorder marked by persistent energy restriction, intense fear of weight gain, and distorted weight or shape beliefs causing low body weight and medical risk.",
                    "UKMLA essentials: recognise pattern, spot instability, check ECG.",
                ],
                "2": [
                    '__EPI_SHORTCODE__',
                    "<b>Risk factors:</b> Adolescence, family history of eating disorders, perfectionism, anxiety traits, autistic traits, trauma or adverse events, and social pressure around weight and shape.",
                    "<b>Higher-risk or missed groups:</b> People with rapid weight loss at any BMI, males, and older adults may be under-recognized despite comparable medical risk.",
                    "<b>Prevention and risk reduction:</b> Early recognition of restrictive eating, non-stigmatizing conversations, and early referral to eating-disorder services can reduce deterioration.",
                ],
                "3": [
                    "Anorexia nervosa is multifactorial, combining biological vulnerability, psychological drivers, and social context.",
                    "Sustained energy restriction triggers adaptive endocrine and metabolic changes that produce bradycardia, hypotension, cold intolerance, and menstrual disturbance.",
                    "Undernutrition affects cardiovascular, endocrine, bone, and cognitive systems, explaining broad physical morbidity.",
                ],
                "4": [
                    "<b>Onset:</b> Often gradual with progressive restriction, meal avoidance, and increasing preoccupation with food, weight, and shape.",
                    "<b>Progression:</b> Without intervention, physiological compromise and cognitive rigidity usually increase over weeks to months.",
                    "<b>Recovery pattern:</b> Improvement is possible with specialist treatment, but relapse risk means follow-up should be sustained.",
                ],
                "5": [
                    "<b>Ask about</b> restrictive eating patterns and avoidance rituals - indicates persistent energy restriction driving weight loss.",
                    "<b>Ask about</b> fear of weight gain and body-image overvaluation - supports core eating-disorder psychopathology.",
                    "<b>Ask about</b> fatigue, poor concentration, and cold intolerance - suggests reduced energy availability and metabolic adaptation.",
                    "<b>Ask about</b> menstrual change or amenorrhoea - may indicate hypothalamic suppression from undernutrition.",
                    "<b>Ask about</b> social withdrawal, low mood, or anxiety - common comorbidity that worsens risk and function.",
                ],
                "6": [
                    "<b>Check</b> weight trajectory and BMI context - quantifies nutritional compromise even when BMI is not low.",
                    "<b>Check</b> pulse and postural blood pressure - identifies cardiovascular instability from starvation and volume depletion.",
                    "<b>Check</b> temperature, skin, and lanugo - supports chronic undernutrition on examination.",
                    "<b>Check</b> muscle bulk and power - reflects catabolic loss and frailty risk.",
                    "<b>Check</b> peripheral oedema - can occur in severe malnutrition or during refeeding.",
                ],
                "7": [
                    "<b>Physiological instability:</b> Marked bradycardia, hypotension, syncope, or chest symptoms need urgent medical assessment.",
                    "<b>Biochemical risk:</b> Significant electrolyte disturbance, especially phosphate, potassium, or magnesium abnormalities, can precede sudden deterioration.",
                    "<b>Neurological risk:</b> Confusion, reduced consciousness, seizures, or severe weakness suggests urgent escalation.",
                    "<b>Psychiatric and safeguarding risk:</b> Suicidal ideation, severe self-neglect, or inability to maintain intake requires urgent specialist escalation.",
                ],
                "8": [
                    "Atypical anorexia can present with substantial weight loss and equivalent medical risk despite BMI not being underweight.",
                    "How it gets missed: symptoms may be attributed to stress, fitness goals, or gastrointestinal complaints unless eating-disorder cognition is directly explored.",
                ],
                "9": [
                    "<b>Baseline and bedside:</b> FBC, U and E, glucose, phosphate, magnesium, LFTs, ECG, and orthostatic observations to assess immediate medical stability.",
                    "<b>Targeted and monitoring:</b> Repeat electrolytes and ECG trends, plus structured psychiatric risk assessment, to guide escalation and safe nutritional rehabilitation.",
                ],
                "10": [
                    "A young person with progressive dietary restriction, weight loss, fear of weight gain, and body-image distortion, with bradycardia or postural instability indicating combined psychiatric and medical risk.",
                    "An eating disorder causing self-reinforcing restriction and multisystem undernutrition that requires integrated medical and mental-health management.",
                ],
                "11": [
                    "<b>Bulimia nervosa</b> - recurrent binge-purge behavior is more prominent and persistent low weight is less typical.",
                    "<b>Depression or anxiety disorders</b> - appetite change can occur but weight or shape overvaluation is not the central driver.",
                    "<b>Hyperthyroidism</b> - weight loss with adrenergic or thyroid features rather than restrictive eating cognition.",
                    "<b>Chronic gastrointestinal or inflammatory disease</b> - weight loss is linked to organic symptoms and objective inflammatory or malabsorptive findings.",
                    "<b>Malignancy</b> - progressive systemic red flags without eating-disorder psychopathology.",
                ],
                "12": [
                    "<b>Immediate priorities:</b> Assess physiological stability, identify refeeding risk, and correct fluid or electrolyte abnormalities.",
                    "<b>Core care:</b> Management usually involves multidisciplinary eating-disorder treatment combining nutritional rehabilitation and psychological therapy, with family-based approaches commonly used in adolescents.",
                    "<b>Monitoring and follow-up:</b> Track weight trajectory, observations, ECG, and biochemical markers alongside mental-state and risk review.",
                    "<b>Escalation and safety-netting:</b> Urgent specialist referral or admission is required for severe instability, rapid deterioration, high psychiatric risk, or inability to maintain oral intake.",
                ],
                "13": [
                    "<b>Cardiovascular instability</b> - arrhythmia and circulatory collapse are major life-threatening risks in severe malnutrition.",
                    "<b>Refeeding syndrome</b> - rapid nutritional restoration without monitoring can trigger critical electrolyte shifts.",
                    "<b>Bone and endocrine morbidity</b> - reduced bone density, menstrual disturbance, and reduced fertility risk can persist with prolonged illness.",
                    "<b>Psychiatric and social sequelae</b> - chronic mood symptoms, isolation, and relapse risk are common without sustained follow-up.",
                ],
            }
        },
    }


@dataclass
class FileRewriteMeta:
    slug: str
    sections_changed: List[int] = field(default_factory=list)
    keep_count: int = 0
    compress_count: int = 0
    drop_count: int = 0
    old_word_count: int = 0
    new_word_count: int = 0

    @property
    def word_count_delta(self) -> int:
        return self.new_word_count - self.old_word_count


@dataclass
class LintIssue:
    rule: str
    message: str
    section: Optional[int] = None


def get_section_lis(section_html: str) -> List[str]:
    ul_m = UL_RE.search(section_html)
    if not ul_m:
        return []
    return extract_lis(ul_m.group(1))


def build_generic_section_lis(
    section_id: int,
    old_lis: List[str],
    condition: str,
    q_value: str,
) -> List[str]:
    base = [x for x in old_lis if clean_li_text(x)]
    if section_id == 1:
        definition = first_sentence(base[0]) if base else f"{condition} is a clinical condition requiring structured assessment and management."
        essentials = "UKMLA essentials: recognise pattern, spot instability, check key tests."
        return [trim_words(definition, 30), essentials]

    if section_id == 2:
        epi_shortcode = f'[sc name="1095-jitl-epidemiology-link" Q="{q_value}"][/sc]'
        kept = []
        for li in base:
            if "1095-jitl-epidemiology-link" in li:
                continue
            plain = clean_li_text(li)
            if UNSOURCED_EPI_NUMERIC_RE.search(plain):
                continue
            kept.append(li)
        if not kept:
            kept = [
                "<b>Risk factors:</b> Risk is influenced by patient, comorbidity, and exposure context.",
                "<b>Higher-risk or missed groups:</b> Atypical presentations and multimorbidity can delay recognition.",
            ]
        return [epi_shortcode] + kept[:4]

    if section_id == 5:
        items = base[:5] if base else [f"{condition} symptom profile varies with severity and disease stage."]
        return [ensure_action_prefix(x, "Ask about") for x in items]

    if section_id == 6:
        items = base[:5] if base else [f"Objective signs of {condition} may indicate severity and instability."]
        return [ensure_action_prefix(x, "Check") for x in items]

    if section_id == 9:
        if any("[sc " in x.lower() for x in base):
            return base[:4]
        plain = [clean_li_text(x).rstrip(".") for x in base]
        if not plain:
            plain = ["Bedside observations and baseline blood tests", "Targeted tests to confirm diagnosis and monitor progression"]
        split = max(1, len(plain) // 2)
        first = "; ".join(plain[:split])
        second = "; ".join(plain[split:]) if plain[split:] else plain[0]
        first = trim_words(first, 24).rstrip(".") + "."
        second = trim_words(second, 24).rstrip(".") + "."
        return [
            f"<b>Baseline and bedside:</b> {first}",
            f"<b>Targeted and monitoring:</b> {second}",
        ]

    if section_id == 10:
        if any("[sc " in x.lower() for x in base):
            if len(base) >= 2:
                return base[:2]
            if len(base) == 1:
                return base + ["A generalized representation supports differential diagnosis and initial management planning."]
            return [
                f"A patient with features suggestive of {condition} requiring clinical risk assessment.",
                "A likely working diagnosis requiring focused tests and timely escalation when unstable.",
            ]
        plain = [trim_words(clean_li_text(x), 30) for x in base[:2]]
        if not plain:
            plain = [
                f"A patient with features suggestive of {condition} requiring clinical risk assessment.",
                "A likely working diagnosis requiring focused tests and timely escalation when unstable.",
            ]
        if len(plain) == 1:
            plain.append("A generalized representation supports differential diagnosis and initial management planning.")
        return plain[:2]

    if section_id == 11:
        out: List[str] = []
        items = base[:6]
        for item in items:
            if "[sc " in item.lower():
                plain_sc = clean_li_text(item)
                if " - " in plain_sc:
                    out.append(item)
                else:
                    out.append(item + " - distinguish by focused history, examination, and targeted investigations.")
                continue
            plain = clean_li_text(item)
            if " - " in plain:
                left, right = plain.split(" - ", 1)
            elif ":" in plain:
                left, right = plain.split(":", 1)
            else:
                left = trim_words(plain, 8).rstrip(".")
                right = "distinguish by focused history, examination, and targeted investigations."
            right = trim_words(right.strip(), 14).rstrip(".") + "."
            out.append(f"{left.strip()} - {right}")
        if len(out) < 4:
            out.append("Alternative diagnoses - distinguish by pattern, objective findings, and response to treatment.")
        return out[:6]

    if section_id == 12:
        return [
            "<b>Immediate priorities:</b> Assess severity, physiological stability, and immediate complications.",
            "<b>Core care:</b> Management usually combines condition-specific therapy, supportive care, and shared decision-making.",
            "<b>Monitoring and follow-up:</b> Review symptoms, objective markers, and treatment response over time.",
            "<b>Escalation and safety-netting:</b> Arrange urgent specialist review for red flags, rapid deterioration, or diagnostic uncertainty.",
        ]

    if section_id == 8:
        out = base[:4]
        has_missed = any("missed" in normalize(x) for x in out)
        if not has_missed:
            out.append("How it gets missed: atypical features or comorbidity can mask the underlying diagnosis.")
        return out[:4]

    if section_id == 13 and base:
        return base[:6]

    return base


def rewrite_content(content: str, slug: str, rules: Dict) -> Tuple[str, FileRewriteMeta]:
    condition = get_condition_name(content, slug)
    q_value = condition.replace('"', "&quot;")
    template = rules.get("condition_templates", {}).get(slug, {})

    meta = FileRewriteMeta(slug=slug, old_word_count=word_count(content))
    out = content

    for n in SECTION_IDS:
        span = get_section_span(out, n)
        if not span:
            continue
        start, end = span
        section_html = out[start:end]
        has_complex_shortcode = '[sc name="lmm-clickable-term"' in section_html.lower()
        if has_complex_shortcode and str(n) not in template:
            # Regex li/ul rewriting is unsafe when shortcode instructions include embedded html lists.
            if n == 1:
                essentials = "UKMLA essentials: recognise pattern, spot instability, check key tests."
                safe_section = ensure_essentials_line(section_html, essentials)
                if safe_section != section_html:
                    out = out[:start] + safe_section + out[end:]
                    meta.sections_changed.append(n)
            continue
        old_lis = get_section_lis(section_html)

        new_lis = template.get(str(n))
        if new_lis is None:
            new_lis = build_generic_section_lis(n, old_lis.copy(), condition, q_value)
        if n == 2:
            epi_shortcode = f'[sc name="1095-jitl-epidemiology-link" Q="{q_value}"][/sc]'
            rendered_shortcode = epi_shortcode
            replaced = False
            normalized_new = []
            for v in new_lis:
                if "__EPI_SHORTCODE__" in v:
                    normalized_new.append(v.replace("__EPI_SHORTCODE__", rendered_shortcode))
                    replaced = True
                else:
                    normalized_new.append(v)
            new_lis = normalized_new
            if not replaced:
                new_lis = [rendered_shortcode] + [x for x in new_lis if rendered_shortcode not in x]
            else:
                deduped = []
                seen_shortcode = False
                for v in new_lis:
                    if rendered_shortcode in v:
                        if seen_shortcode:
                            continue
                        seen_shortcode = True
                    deduped.append(v)
                new_lis = deduped
            if not new_lis or rendered_shortcode not in new_lis[0]:
                new_lis = [rendered_shortcode] + [x for x in new_lis if rendered_shortcode not in x]

        new_lis = [sanitize_prescriptive_text(x) for x in new_lis]

        new_section = render_li_block(section_html, new_lis)
        new_section = ensure_child_div_closed(new_section, n)
        if new_section != section_html:
            out = out[:start] + new_section + out[end:]
            meta.sections_changed.append(n)
            classified = classify_keep_compress_drop(old_lis, new_lis, n)
            meta.keep_count += classified["keep"]
            meta.compress_count += classified["compress"]
            meta.drop_count += classified["drop"]

    meta.new_word_count = word_count(out)
    return out, meta


def check_required_ids(content: str) -> List[LintIssue]:
    issues: List[LintIssue] = []
    for n in SECTION_IDS:
        for prefix in ("c", "s", "o"):
            wanted = f'id="{prefix}-is.{n}.0"'
            if wanted not in content:
                issues.append(LintIssue("required_ids", f"Missing {wanted}", section=n))
    return issues


def check_duplicate_ids(content: str) -> List[LintIssue]:
    issues: List[LintIssue] = []
    ids = ID_RE.findall(content)
    counts: Dict[str, int] = {}
    for i in ids:
        counts[i] = counts.get(i, 0) + 1
    for k, v in sorted(counts.items()):
        if v > 1 and (k == "illness-script-title" or re.match(r"[cso]-is\.\d+\.\d+", k)):
            issues.append(LintIssue("duplicate_ids", f'Duplicate id="{k}" occurs {v} times'))
    return issues


def get_section_html(content: str, n: int) -> str:
    span = get_section_span(content, n)
    if not span:
        return ""
    return content[span[0] : span[1]]


def first_li_text(section_html: str) -> str:
    ul_m = UL_RE.search(section_html)
    if not ul_m:
        return ""
    li_m = LI_RE.search(ul_m.group(1))
    if not li_m:
        return ""
    return SPACE_RE.sub(" ", li_m.group(1)).strip()


def find_banned_phrase_hits(content: str) -> List[Dict[str, str | int]]:
    hits: List[Dict[str, str | int]] = []
    for i, line in enumerate(content.splitlines(), start=1):
        low = line.lower()
        for phrase in BOILERPLATE_BANNED_PHRASES:
            if phrase in low:
                hits.append({"phrase": phrase, "line": i, "line_text": line.strip()})
    return hits


def is_sti_script(slug: str, condition: str) -> bool:
    hay = f"{slug} {condition}".lower()
    return any(h in hay for h in STI_SLUG_HINTS)


def lint_essentials_line(sec1_lis: List[str], condition: str) -> Tuple[List[LintIssue], Dict[str, object]]:
    issues: List[LintIssue] = []
    result: Dict[str, object] = {
        "exists": False,
        "item_count_ok": False,
        "format_ok": False,
        "word_count": 0,
        "word_count_ok": False,
        "specificity_ok": False,
        "line": "",
    }
    if len(sec1_lis) != 2:
        issues.append(LintIssue("definition_li_count", "Section 1 must contain exactly 2 list items", section=1))
        return issues, result

    line = strip_html(sec1_lis[1]).strip()
    result["exists"] = True
    result["line"] = line
    result["item_count_ok"] = line.count(",") == 2
    result["format_ok"] = bool(ESSENTIALS_FORMAT_RE.match(line))
    word_count_val = len(re.findall(r"\b[\w-]+\b", line))
    result["word_count"] = word_count_val
    result["word_count_ok"] = word_count_val <= 18

    if not result["item_count_ok"] or not result["format_ok"]:
        issues.append(
            LintIssue(
                "definition_essentials_format",
                "Section 1 bullet 2 must be 'UKMLA essentials: <item1>, <item2>, <item3>.'",
                section=1,
            )
        )
    if not result["word_count_ok"]:
        issues.append(LintIssue("definition_essentials_wordcount", "Section 1 essentials line exceeds 18 words", section=1))

    low = line.lower()
    condition_tokens = {t for t in re.findall(r"[a-z0-9]+", normalize(condition)) if len(t) >= 4}
    has_anchor = any(t in low for t in condition_tokens) or any(a in low for a in NON_GENERIC_MEDICAL_ANCHORS)
    generic_hit = any(token in low for token in ESSENTIALS_GENERIC_TOKENS)
    specificity_ok = (not generic_hit) or has_anchor
    result["specificity_ok"] = specificity_ok
    if not specificity_ok:
        issues.append(
            LintIssue(
                "essentials_generic_token",
                "Section 1 essentials line contains generic tokens without condition-specific anchors",
                section=1,
            )
        )
    return issues, result


def lint_content(
    content: str, slug: str, rules: Dict
) -> Tuple[bool, List[LintIssue], Dict, List[Dict[str, str | int]], Dict[str, object]]:
    issues: List[LintIssue] = []
    condition = get_condition_name(content, slug)
    q_value = condition.replace('"', "&quot;")
    banned_phrase_hits = find_banned_phrase_hits(content)
    for hit in banned_phrase_hits:
        issues.append(
            LintIssue(
                "boilerplate_banned_phrase",
                f'Banned boilerplate phrase at line {hit["line"]}: {hit["phrase"]}',
            )
        )

    issues.extend(check_required_ids(content))
    issues.extend(check_duplicate_ids(content))

    if content.lower().count("<details") != content.lower().count("</details>"):
        issues.append(LintIssue("nesting", "Mismatched <details> opening/closing count"))

    sec1 = get_section_html(content, 1)
    sec1_lis = get_section_lis(sec1)
    essentials_issues, essentials_validation = lint_essentials_line(sec1_lis, condition)
    issues.extend(essentials_issues)

    sec2 = get_section_html(content, 2)
    if not sec2:
        issues.append(LintIssue("epi_section", "Missing section c-is.2.0", section=2))
    else:
        expected = f'[sc name="1095-jitl-epidemiology-link" Q="{q_value}"][/sc]'
        first = first_li_text(sec2)
        if first != expected:
            issues.append(
                LintIssue(
                    "epi_shortcode_first_li",
                    f'Section 2 first <li> mismatch. Expected {expected}, got {first or "<missing>"}',
                    section=2,
                )
            )
        sec2_lis = get_section_lis(sec2)
        for idx, li in enumerate(sec2_lis[1:], start=2):
            if UNSOURCED_EPI_NUMERIC_RE.search(strip_html(li)):
                issues.append(
                    LintIssue(
                        "epi_unsourced_numeric",
                        f"Section 2 list item {idx} has unsourced numeric epidemiology claim",
                        section=2,
                    )
                )

    if is_sti_script(slug, condition):
        for sec_id in (2, 5, 13):
            sec = get_section_html(content, sec_id)
            for i, li in enumerate(get_section_lis(sec), start=1):
                if "1095-jitl-epidemiology-link" in li:
                    continue
                if UNSOURCED_EPI_NUMERIC_RE.search(strip_html(li)):
                    issues.append(
                        LintIssue(
                            "unsourced_numeric_in_sti",
                            f"Section {sec_id} list item {i} has unsourced numeric claim in STI script",
                            section=sec_id,
                        )
                    )

    sec5 = get_section_html(content, 5)
    for i, li in enumerate(get_section_lis(sec5), start=1):
        norm_li = normalize(li)
        if norm_li.startswith("ask about"):
            continue
        if norm_li.startswith("consider"):
            # Allow "Consider" only for asymptomatic/screen-detected/partner-notified bullets.
            if any(
                token in norm_li
                for token in (
                    "asymptomatic",
                    "screen",
                    "screen-detected",
                    "screen detected",
                    "partner-notified",
                    "partner notified",
                    "detected by screening",
                )
            ):
                continue
        issues.append(
            LintIssue(
                "symptoms_action_verb",
                f'Section 5 list item {i} must start with "Ask about" (or "Consider" for asymptomatic/screen-detected/partner-notified points)',
                section=5,
            )
        )

    sec6 = get_section_html(content, 6)
    for i, li in enumerate(get_section_lis(sec6), start=1):
        if not normalize(li).startswith("check"):
            issues.append(
                LintIssue(
                    "signs_action_verb",
                    f'Section 6 list item {i} must start with "Check"',
                    section=6,
                )
            )

    sec11 = get_section_html(content, 11)
    for i, li in enumerate(get_section_lis(sec11), start=1):
        plain = strip_html(li)
        if " - " not in plain:
            issues.append(
                LintIssue(
                    "differential_discriminator",
                    f"Section 11 list item {i} must include discriminator delimiter ' - '",
                    section=11,
                )
            )
        len_basis = strip_shortcodes(plain)
        if len(re.findall(r"\b\w+\b", len_basis)) > 26:
            issues.append(
                LintIssue(
                    "differential_length",
                    f"Section 11 list item {i} exceeds 26 words",
                    section=11,
                )
                )

    sec9 = get_section_html(content, 9)
    sec9_lis = get_section_lis(sec9)
    if len(sec9_lis) != 2:
        issues.append(LintIssue("diagnostic_section_count", "Section 9 must contain exactly 2 list items", section=9))
    for i, li in enumerate(sec9_lis, start=1):
        low = normalize(li)
        if "diagnose clinically while awaiting results" in low or "diagnosis is clinical while awaiting results" in low:
            issues.append(
                LintIssue(
                    "diagnostics_clinical_diagnosis_phrase",
                    f"Section 9 list item {i} contains discouraged clinical diagnosis phrase",
                    section=9,
                )
            )

    whitelist = [re.compile(p) for p in rules.get("prescriptive_whitelist_patterns", [])]
    forbidden = [re.compile(p) for p in rules.get("forbidden_prescriptive_patterns", [])]
    for n in SECTION_IDS:
        section = get_section_html(content, n)
        for i, li in enumerate(get_section_lis(section), start=1):
            txt = strip_html(li)
            allowed = any(w.search(txt) for w in whitelist)
            if allowed:
                continue
            for p in forbidden:
                if p.search(txt):
                    issues.append(
                        LintIssue(
                            "prescriptive_language",
                            f"Section {n} list item {i} contains prescriptive pattern: {p.pattern}",
                            section=n,
                        )
                    )
                    break

    if ENCODING_ARTIFACT_RE.search(content):
        issues.append(LintIssue("encoding_artifact", "Found mojibake encoding artifact"))

    li_text_joined = "\n".join(strip_html(x) for x in LI_RE.findall(content))
    for token in UK_SPELLING_VIOLATIONS:
        if re.search(rf"(?i)\b{re.escape(token)}\b", li_text_joined):
            issues.append(LintIssue("uk_spelling_violation", f"Found non-UK spelling token: {token}"))

    checks = {
        "boilerplate_banned_phrase": not any(i.rule == "boilerplate_banned_phrase" for i in issues),
        "required_ids": not any(i.rule == "required_ids" for i in issues),
        "duplicate_ids": not any(i.rule == "duplicate_ids" for i in issues),
        "details_nesting": not any(i.rule == "nesting" for i in issues),
        "definition_contract": not any(
            i.rule in {"definition_li_count", "definition_essentials_format", "definition_essentials_wordcount"} for i in issues
        ),
        "essentials_generic_token": not any(i.rule == "essentials_generic_token" for i in issues),
        "epi_shortcode_first_li": not any(i.rule == "epi_shortcode_first_li" for i in issues),
        "epi_unsourced_numeric": not any(i.rule == "epi_unsourced_numeric" for i in issues),
        "unsourced_numeric_in_sti": not any(i.rule == "unsourced_numeric_in_sti" for i in issues),
        "symptoms_action_verb": not any(i.rule == "symptoms_action_verb" for i in issues),
        "signs_action_verb": not any(i.rule == "signs_action_verb" for i in issues),
        "diagnostic_section_contract": not any(i.rule == "diagnostic_section_count" for i in issues),
        "diagnostics_clinical_diagnosis_phrase": not any(i.rule == "diagnostics_clinical_diagnosis_phrase" for i in issues),
        "differential_format": not any(
            i.rule in {"differential_discriminator", "differential_length"} for i in issues
        ),
        "prescriptive_language": not any(i.rule == "prescriptive_language" for i in issues),
        "uk_spelling_violation": not any(i.rule == "uk_spelling_violation" for i in issues),
        "encoding_artifacts": not any(i.rule == "encoding_artifact" for i in issues),
    }

    return len(issues) == 0, issues, checks, banned_phrase_hits, essentials_validation


def load_rules(config_path: Path) -> Dict:
    rules = default_rules()
    if config_path.exists():
        loaded = json.loads(config_path.read_text(encoding="utf-8"))
        for key, value in loaded.items():
            if isinstance(value, dict) and isinstance(rules.get(key), dict):
                merged = dict(rules[key])
                merged.update(value)
                rules[key] = merged
            else:
                rules[key] = value
    return rules


def choose_slugs(source_dir: Path, single_slug: str, slug_list_file: str) -> List[str]:
    if single_slug:
        return [single_slug]
    if slug_list_file:
        path = Path(slug_list_file)
        rows = [x.strip() for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
        return rows
    return [p.stem for p in sorted(source_dir.glob("is-*.html"))]


def main() -> None:
    parser = argparse.ArgumentParser(description="Modernize 2026 illness scripts with rewrite and lint passes.")
    parser.add_argument("--source-dir", default="extracted-illness-scripts-2026")
    parser.add_argument("--output-dir", default="updated-illness-scripts-2026")
    parser.add_argument("--single-slug", default="")
    parser.add_argument("--slug-list-file", default="")
    parser.add_argument("--mode", choices=["rewrite", "lint", "rewrite-and-lint"], default="rewrite-and-lint")
    parser.add_argument(
        "--report-file",
        default="updated-illness-scripts-2026/modernization-report-2026.json",
    )
    parser.add_argument(
        "--lint-report-file",
        default="updated-illness-scripts-2026/lint-report-2026.json",
    )
    parser.add_argument("--config-file", default="modernization_rules_2026.json")
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    output_dir = Path(args.output_dir)
    report_file = Path(args.report_file)
    lint_report_file = Path(args.lint_report_file)
    config_file = Path(args.config_file)

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    rules = load_rules(config_file)
    slugs = choose_slugs(source_dir, args.single_slug, args.slug_list_file)

    rewrite_rows = []
    lint_rows = []
    processed = 0
    lint_passed = 0

    for slug in slugs:
        src_file = source_dir / f"{slug}.html"
        if not src_file.exists():
            lint_rows.append(
                {
                    "slug": slug,
                    "passed": False,
                    "issues": [{"rule": "missing_source", "message": f"Missing source file: {src_file}"}],
                    "checks": {},
                }
            )
            continue

        source_text = src_file.read_text(encoding="utf-8", errors="replace")
        target_text = source_text
        meta = FileRewriteMeta(slug=slug, old_word_count=word_count(source_text), new_word_count=word_count(source_text))

        if args.mode in {"rewrite", "rewrite-and-lint"}:
            target_text, meta = rewrite_content(source_text, slug, rules)
            (output_dir / src_file.name).write_text(target_text, encoding="utf-8")
            rewrite_rows.append(
                {
                    "slug": slug,
                    "source_file": str(src_file),
                    "output_file": str((output_dir / src_file.name).resolve()),
                    "sections_changed": meta.sections_changed,
                    "keep_count": meta.keep_count,
                    "compress_count": meta.compress_count,
                    "drop_count": meta.drop_count,
                    "old_word_count": meta.old_word_count,
                    "new_word_count": meta.new_word_count,
                    "word_count_delta": meta.word_count_delta,
                }
            )
        else:
            out_file = output_dir / src_file.name
            if out_file.exists():
                target_text = out_file.read_text(encoding="utf-8", errors="replace")

        if args.mode in {"lint", "rewrite-and-lint"}:
            passed, issues, checks, banned_phrase_hits, essentials_validation = lint_content(target_text, slug, rules)
            if not passed and args.mode == "rewrite-and-lint":
                # Targeted second pass for failing rules.
                fixed_text, _ = rewrite_content(target_text, slug, rules)
                if fixed_text != target_text:
                    target_text = fixed_text
                    (output_dir / src_file.name).write_text(target_text, encoding="utf-8")
                passed, issues, checks, banned_phrase_hits, essentials_validation = lint_content(target_text, slug, rules)

            if passed:
                lint_passed += 1
            lint_rows.append(
                {
                    "slug": slug,
                    "passed": passed,
                    "issues": [
                        {"rule": i.rule, "message": i.message, "section": i.section} for i in issues
                    ],
                    "checks": checks,
                    "banned_phrase_hits": banned_phrase_hits,
                    "essentials_validation": essentials_validation,
                }
            )

        processed += 1

    if rewrite_rows:
        report_file.parent.mkdir(parents=True, exist_ok=True)
        modernization_report = {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "mode": args.mode,
            "source_dir": str(source_dir.resolve()),
            "output_dir": str(output_dir.resolve()),
            "processed_files": processed,
            "files": rewrite_rows,
        }
        report_file.write_text(json.dumps(modernization_report, indent=2), encoding="utf-8")

    if lint_rows:
        lint_report_file.parent.mkdir(parents=True, exist_ok=True)
        lint_report = {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "mode": args.mode,
            "processed_files": processed,
            "passed_files": lint_passed,
            "failed_files": processed - lint_passed,
            "files": lint_rows,
        }
        lint_report_file.write_text(json.dumps(lint_report, indent=2), encoding="utf-8")

    print(f"Mode: {args.mode}")
    print(f"Processed files: {processed}")
    if rewrite_rows:
        print(f"Modernization report: {report_file}")
    if lint_rows:
        print(f"Lint report: {lint_report_file}")


if __name__ == "__main__":
    main()
