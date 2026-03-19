#!/usr/bin/env python3
import re
from pathlib import Path


DETAILS_RE_TMPL = r'(?is)<details\s+id="c-is\.{n}\.0"[^>]*>.*?</details>'
LI_RE = re.compile(r"(?is)(<li>)(.*?)(</li>)")
TAG_RE = re.compile(r"(?is)<[^>]+>")
WS_RE = re.compile(r"\s+")


TRUNC_END_RE = re.compile(r"(?i)\b(and|or|with|without|in|on|at|to|from|of|for|the|a|an|if|when|which)\.$")


def strip_html(text: str) -> str:
    return WS_RE.sub(" ", TAG_RE.sub("", text)).strip()


def normalize(text: str) -> str:
    return WS_RE.sub(" ", text.lower()).strip()


def details_pattern(n: int) -> re.Pattern[str]:
    return re.compile(DETAILS_RE_TMPL.format(n=n))


def get_section_html(content: str, section_id: int) -> str:
    m = details_pattern(section_id).search(content)
    return m.group(0) if m else ""


def replace_section_html(content: str, section_id: int, section_html: str) -> str:
    return details_pattern(section_id).sub(section_html, content, count=1)


def get_li_inners(section_html: str):
    return [m.group(2) for m in LI_RE.finditer(section_html)]


def replace_all_li_inners(section_html: str, new_inners):
    matches = list(LI_RE.finditer(section_html))
    if not matches:
        return section_html
    out = []
    cursor = 0
    for i, m in enumerate(matches):
        out.append(section_html[cursor : m.start(2)])
        out.append(new_inners[i] if i < len(new_inners) else m.group(2))
        cursor = m.end(2)
    out.append(section_html[cursor:])
    return "".join(out)


def condition_from_content(slug: str, content: str) -> str:
    m = re.search(r'(?is)<div\s+id="illness-script-title">\s*(.*?)\s*</div>', content)
    if m:
        return strip_html(m.group(1))
    base = slug[3:] if slug.startswith("is-") else slug
    return " ".join(x.capitalize() for x in base.split("-"))


def fix_generic_lines(section_id: int, li: str, condition: str) -> str:
    low = normalize(strip_html(li))
    cond_low = condition.lower()
    if "risk of " in low and "rises with relevant predisposition, comorbidity, and exposure profile" in low:
        return (
            f"<b>Risk factors:</b> Risk factors for {cond_low} depend on cause; assess relevant predisposition, "
            "comorbidity, and exposure history."
        )
    if "may be missed when presentations are atypical or comorbidity obscures key features" in low:
        return (
            f"<b>Higher-risk or missed groups:</b> {condition} may be under-recognised when presentations are non-specific "
            "or masked by coexisting illness."
        )
    if "a patient with a typical " in low and "pattern and key discriminators" in low:
        return (
            f"A clinical presentation consistent with {cond_low}, with discriminating features that guide focused "
            "investigation and escalation."
        )
    if "management focuses on condition-directed treatment, complication prevention, and coordinated follow-up" in low:
        return (
            f"<b>Core care:</b> Management targets {cond_low} and underlying cause, with early specialist input for high-risk presentations."
        )
    if "reassess symptom trajectory, objective findings, and complications to confirm response" in low:
        return (
            f"<b>Monitoring and follow-up:</b> Monitor symptoms, observations, and objective markers relevant to {cond_low} "
            "to confirm response and detect complications early."
        )
    if "escalate urgently for deterioration, high-risk features, or failure to improve" in low:
        return (
            f"<b>Escalation and safety-netting:</b> Escalate urgently for physiological deterioration, evolving red flags, "
            f"or concern for life-threatening complications of {cond_low}."
        )
    if "alternative diagnoses - distinguish by key discriminators in history, examination, and targeted investigations" in low:
        return "Key differentials - distinguish by defining history, examination findings, and targeted investigations."
    return li


def fix_truncation(section_id: int, li: str, condition: str) -> str:
    plain = strip_html(li)
    if not TRUNC_END_RE.search(plain):
        return li

    cond_low = condition.lower()
    if section_id == 11 and " - " in plain:
        lhs = plain.split(" - ", 1)[0].strip()
        return f"{lhs} - differentiate from {cond_low} using history, examination, and targeted investigations."

    if section_id == 9:
        low = normalize(plain)
        if low.startswith("baseline and bedside:"):
            return (
                f"<b>Baseline and bedside:</b> Focused clinical assessment with relevant observations and first-line tests "
                f"to assess severity and immediate risk in suspected {cond_low}."
            )
        if low.startswith("targeted and monitoring:"):
            return (
                f"<b>Targeted and monitoring:</b> Use targeted tests to confirm diagnosis, define complications, and monitor "
                f"response or progression in {cond_low}."
            )

    if section_id == 10:
        return (
            f"A patient with symptoms and signs concerning for {cond_low}, requiring prompt risk stratification and focused investigation."
        )

    if section_id == 5 and " - " in li:
        lhs = li.split(" - ", 1)[0].strip()
        return f"{lhs} - may indicate clinically significant {cond_low} and should be interpreted with examination findings."

    return li.rstrip(".") + " in this clinical context."


def enforce_symptom_consider_exception(section_id: int, li: str) -> str:
    if section_id != 5:
        return li
    low = normalize(strip_html(li))
    if low.startswith("ask about") and any(
        x in low for x in ("asymptomatic", "screen", "screen-detected", "partner-notified", "partner notified")
    ):
        return re.sub(r"(?is)^<b>\s*ask about\s*</b>", "<b>Consider</b>", li, count=1)
    return li


def patch_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    slug = path.stem
    condition = condition_from_content(slug, content)
    original = content

    for n in range(1, 14):
        section = get_section_html(content, n)
        if not section:
            continue
        lis = get_li_inners(section)
        if not lis:
            continue
        new_lis = []
        changed = False
        for li in lis:
            li2 = fix_generic_lines(n, li, condition)
            li2 = fix_truncation(n, li2, condition)
            li2 = enforce_symptom_consider_exception(n, li2)
            if li2 != li:
                changed = True
            new_lis.append(li2)
        if changed:
            section2 = replace_all_li_inners(section, new_lis)
            content = replace_section_html(content, n, section2)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main() -> None:
    base = Path("updated-illness-scripts-2026")
    slug_list = base / "pilot-50-slugs.txt"
    slugs = [s.strip() for s in slug_list.read_text(encoding="utf-8").splitlines() if s.strip()]
    changed = 0
    for slug in slugs:
        p = base / f"{slug}.html"
        if not p.exists():
            continue
        if patch_file(p):
            changed += 1
    print(f"patched_files={changed}")


if __name__ == "__main__":
    main()
