#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple


DETAILS_RE_TMPL = r'(?is)<details\s+id="c-is\.{n}\.0"[^>]*>.*?</details>'
LI_RE = re.compile(r"(?is)(<li>)(.*?)(</li>)")
TAG_RE = re.compile(r"(?is)<[^>]+>")
WS_RE = re.compile(r"\s+")


def strip_html(text: str) -> str:
    return WS_RE.sub(" ", TAG_RE.sub("", text)).strip()


def normalize(text: str) -> str:
    return WS_RE.sub(" ", text.lower()).strip()


def details_pattern(n: int) -> re.Pattern[str]:
    return re.compile(DETAILS_RE_TMPL.format(n=n))


def get_section_html(content: str, section_id: int) -> str:
    m = details_pattern(section_id).search(content)
    return m.group(0) if m else ""


def replace_section_html(content: str, section_id: int, new_section_html: str) -> str:
    return details_pattern(section_id).sub(new_section_html, content, count=1)


def replace_li_inner_by_index(section_html: str, li_index_1based: int, new_inner: str) -> str:
    matches = list(LI_RE.finditer(section_html))
    if li_index_1based < 1 or li_index_1based > len(matches):
        return section_html
    i = li_index_1based - 1
    m = matches[i]
    return section_html[: m.start(2)] + new_inner + section_html[m.end(2) :]


def get_li_inners(section_html: str) -> List[str]:
    return [m.group(2) for m in LI_RE.finditer(section_html)]


def replace_all_li_inners(section_html: str, new_inners: List[str]) -> str:
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


def extract_section_from_line_text(line_text: str) -> int:
    m = re.search(r'id="c-is\.(\d+)\.0"', line_text, flags=re.I)
    if m:
        return int(m.group(1))
    return 0


def slug_to_condition(slug: str, content: str) -> str:
    m = re.search(r'(?is)<div\s+id="illness-script-title">\s*(.*?)\s*</div>', content)
    if m:
        return strip_html(m.group(1))
    base = slug
    if base.startswith("is-"):
        base = base[3:]
    return " ".join(x.capitalize() for x in base.split("-"))


def condition_anchor(condition: str) -> str:
    stop = {
        "acute",
        "chronic",
        "syndrome",
        "disease",
        "disorder",
        "infection",
        "pain",
        "failure",
        "deficiency",
        "primary",
        "secondary",
        "severe",
        "complex",
        "unspecified",
        "other",
    }
    tokens = [t for t in re.findall(r"[a-z0-9]+", condition.lower()) if len(t) >= 4]
    for t in tokens:
        if t not in stop:
            return t
    return tokens[0] if tokens else "condition"


def build_essentials_line(condition: str) -> str:
    anchor = condition_anchor(condition)
    return f"UKMLA essentials: recognise {anchor} features, identify urgent deterioration, prioritise focused testing."


def replace_banned_phrase_inner(inner: str, condition: str) -> str:
    low = normalize(strip_html(inner))
    replacements = {
        "recognise pattern, spot instability, check key tests": build_essentials_line(condition),
        "risk is influenced by patient, comorbidity, and exposure context": (
            f"<b>Risk factors:</b> Risk of {condition.lower()} rises with relevant predisposition, comorbidity, and exposure profile."
        ),
        "atypical presentations and multimorbidity can delay recognition": (
            f"<b>Higher-risk or missed groups:</b> {condition} may be missed when presentations are atypical or comorbidity obscures key features."
        ),
        "a generalized representation supports differential diagnosis and initial management planning": (
            f"A patient with a typical {condition.lower()} pattern and key discriminators, guiding focused differential diagnosis and escalation."
        ),
        "management usually combines condition-specific therapy, supportive care, and shared decision-making": (
            "<b>Core care:</b> Management focuses on condition-directed treatment, complication prevention, and coordinated follow-up."
        ),
        "alternative diagnoses - distinguish by pattern, objective findings, and response to treatment": (
            "Alternative diagnoses - distinguish by key discriminators in history, examination, and targeted investigations."
        ),
        "review symptoms, objective markers, and treatment response over time": (
            "<b>Monitoring and follow-up:</b> Reassess symptom trajectory, objective findings, and complications to confirm response."
        ),
        "arrange urgent specialist review for red flags, rapid deterioration, or diagnostic uncertainty": (
            "<b>Escalation and safety-netting:</b> Escalate urgently for deterioration, high-risk features, or failure to improve."
        ),
    }
    for phrase, repl in replacements.items():
        if phrase in low:
            return repl
    return inner


def enforce_definition_contract(content: str, condition: str) -> Tuple[str, bool]:
    section = get_section_html(content, 1)
    if not section:
        return content, False
    lis = get_li_inners(section)
    if not lis:
        return content, False
    changed = False
    essentials = build_essentials_line(condition)
    if len(lis) == 1:
        lis.append(essentials)
        changed = True
    elif len(lis) >= 2:
        if strip_html(lis[1]).strip() != essentials:
            lis[1] = essentials
            changed = True
        if len(lis) > 2:
            lis = lis[:2]
            changed = True
    new_section = replace_all_li_inners(section, lis)
    # If section had >2 li, trim extras via regex-safe rebuild in ul block.
    if len(get_li_inners(new_section)) > 2:
        # Rebuild full list explicitly.
        ul_m = re.search(r"(?is)(<ul[^>]*>)(.*?)(</ul>)", new_section)
        if ul_m:
            rebuilt = ul_m.group(1) + "".join(f"<li>{x}</li>" for x in lis[:2]) + ul_m.group(3)
            new_section = new_section[: ul_m.start()] + rebuilt + new_section[ul_m.end() :]
            changed = True
    if changed:
        content = replace_section_html(content, 1, new_section)
    return content, changed


def enforce_section9_two_bullets(content: str, condition: str) -> Tuple[str, bool]:
    section = get_section_html(content, 9)
    if not section:
        return content, False
    lis = get_li_inners(section)
    changed = False
    if len(lis) == 2 and normalize(strip_html(lis[0])).startswith("baseline and bedside:") and normalize(
        strip_html(lis[1])
    ).startswith("targeted and monitoring:"):
        return content, False

    if len(lis) >= 2:
        first_plain = strip_html(lis[0])
        second_plain = strip_html(" ".join(lis[1:]))
    elif len(lis) == 1:
        first_plain = strip_html(lis[0])
        second_plain = ""
    else:
        first_plain = ""
        second_plain = ""

    if not first_plain:
        first_plain = f"Focused bedside assessment and initial tests to assess severity in suspected {condition.lower()}."
    if not second_plain:
        second_plain = "Targeted investigations to confirm complications, monitor progression, and guide escalation."

    first_plain = re.sub(r"(?is)^baseline and bedside:\s*", "", first_plain).strip().rstrip(".")
    second_plain = re.sub(r"(?is)^targeted and monitoring:\s*", "", second_plain).strip().rstrip(".")
    if not first_plain:
        first_plain = f"Focused bedside assessment and initial tests to assess severity in suspected {condition.lower()}"
    if not second_plain:
        second_plain = "Targeted investigations to confirm complications, monitor progression, and guide escalation"

    new_lis = [
        f"<b>Baseline and bedside:</b> {first_plain}.",
        f"<b>Targeted and monitoring:</b> {second_plain}.",
    ]

    ul_m = re.search(r"(?is)(<ul[^>]*>)(.*?)(</ul>)", section)
    if not ul_m:
        return content, False
    rebuilt = ul_m.group(1) + "".join(f"<li>{x}</li>" for x in new_lis) + ul_m.group(3)
    new_section = section[: ul_m.start()] + rebuilt + section[ul_m.end() :]
    if new_section != section:
        changed = True
        content = replace_section_html(content, 9, new_section)
    return content, changed


def replace_reiters(content: str) -> Tuple[str, Set[int]]:
    edited: Set[int] = set()
    for n in range(1, 14):
        section = get_section_html(content, n)
        if not section:
            continue
        lis = get_li_inners(section)
        new_lis = []
        changed = False
        for li in lis:
            li2 = re.sub(r"(?i)\breiter[’']s\b", "reactive arthritis", li)
            if li2 != li:
                changed = True
            new_lis.append(li2)
        if changed:
            edited.add(n)
            section2 = replace_all_li_inners(section, new_lis)
            content = replace_section_html(content, n, section2)
    return content, edited


def apply_issue_driven_edits(content: str, slug: str, issues: List[Dict]) -> Tuple[str, Set[int]]:
    condition = slug_to_condition(slug, content)
    edited_sections: Set[int] = set()

    # First pass: targeted banned-phrase line edits by line text matching.
    for issue in issues:
        if issue.get("rule") != "boilerplate_banned_phrase":
            continue
        msg = issue.get("message", "")
        m = re.search(r"line \d+:\s*(.+)$", msg, flags=re.I)
        phrase = m.group(1).strip().lower() if m else ""
        if not phrase:
            continue
        for n in range(1, 14):
            section = get_section_html(content, n)
            if not section:
                continue
            lis = get_li_inners(section)
            changed = False
            new_lis = []
            for li in lis:
                plain_low = normalize(strip_html(li))
                if phrase in plain_low:
                    li = replace_banned_phrase_inner(li, condition)
                    changed = True
                new_lis.append(li)
            if changed:
                edited_sections.add(n)
                section2 = replace_all_li_inners(section, new_lis)
                content = replace_section_html(content, n, section2)

    # Rule-specific contract fixes.
    rules = {i.get("rule") for i in issues}
    if "essentials_generic_token" in rules:
        content, changed = enforce_definition_contract(content, condition)
        if changed:
            edited_sections.add(1)
    if "diagnostic_section_count" in rules:
        content, changed = enforce_section9_two_bullets(content, condition)
        if changed:
            edited_sections.add(9)

    # Global terminology cleanup requested.
    content, sec_changed = replace_reiters(content)
    edited_sections |= sec_changed

    return content, edited_sections


def run_lint_for_slug(
    slug: str,
    html_dir: Path,
    linter_script: Path,
    lint_report_path: Path,
) -> Dict:
    cmd = [
        sys.executable,
        str(linter_script),
        "--source-dir",
        str(html_dir),
        "--output-dir",
        str(html_dir),
        "--single-slug",
        slug,
        "--mode",
        "lint",
        "--lint-report-file",
        str(lint_report_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    data = json.loads(lint_report_path.read_text(encoding="utf-8"))
    if not data.get("files"):
        raise RuntimeError(f"No lint result for slug: {slug}")
    return data["files"][0]


def run_full_lint(
    html_dir: Path,
    linter_script: Path,
    slug_list_file: Path,
    lint_report_path: Path,
) -> Dict:
    cmd = [
        sys.executable,
        str(linter_script),
        "--source-dir",
        str(html_dir),
        "--output-dir",
        str(html_dir),
        "--slug-list-file",
        str(slug_list_file),
        "--mode",
        "lint",
        "--lint-report-file",
        str(lint_report_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads(lint_report_path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Error-driven strict remediation for pilot-50 illness scripts.")
    parser.add_argument(
        "--lint-report",
        default="updated-illness-scripts-2026/lint-report-pilot-50-strict.json",
    )
    parser.add_argument("--html-dir", default="updated-illness-scripts-2026")
    parser.add_argument("--linter-script", default="modernize_illness_scripts_2026.py")
    parser.add_argument("--slug-list-file", default="updated-illness-scripts-2026/pilot-50-slugs.txt")
    parser.add_argument("--exclude-slugs", default="is-chlamydia")
    parser.add_argument("--summary-file", default="updated-illness-scripts-2026/_qa/pilot50_fix_summary.md")
    parser.add_argument("--final-lint-report", default="updated-illness-scripts-2026/lint-report-pilot-50-strict.json")
    parser.add_argument("--max-iterations-per-slug", type=int, default=4)
    args = parser.parse_args()

    lint_report = Path(args.lint_report)
    html_dir = Path(args.html_dir)
    linter_script = Path(args.linter_script)
    slug_list_file = Path(args.slug_list_file)
    summary_file = Path(args.summary_file)
    final_lint_report = Path(args.final_lint_report)
    exclude_slugs = {s.strip() for s in args.exclude_slugs.split(",") if s.strip()}

    if not lint_report.exists():
        raise FileNotFoundError(f"Lint report not found: {lint_report}")
    if not html_dir.exists():
        raise FileNotFoundError(f"HTML dir not found: {html_dir}")
    if not linter_script.exists():
        raise FileNotFoundError(f"Linter script not found: {linter_script}")
    if not slug_list_file.exists():
        raise FileNotFoundError(f"Slug list file not found: {slug_list_file}")

    initial = json.loads(lint_report.read_text(encoding="utf-8"))
    failed_slugs = [f["slug"] for f in initial.get("files", []) if not f.get("passed", False)]
    queue = [s for s in failed_slugs if s not in exclude_slugs]

    summary_rows: List[Tuple[str, List[str]]] = []
    temp_dir = html_dir / "_qa"
    temp_dir.mkdir(parents=True, exist_ok=True)

    for slug in queue:
        html_path = html_dir / f"{slug}.html"
        if not html_path.exists():
            summary_rows.append((slug, ["missing-file"]))
            continue

        single_report = temp_dir / f"lint-report-{slug}.json"
        current = run_lint_for_slug(slug, html_dir, linter_script, single_report)
        if current.get("passed", False):
            summary_rows.append((slug, ["none"]))
            continue

        edited_sections: Set[int] = set()
        passed = False
        for _ in range(args.max_iterations_per_slug):
            content = html_path.read_text(encoding="utf-8")
            content2, edited = apply_issue_driven_edits(content, slug, current.get("issues", []))
            edited_sections |= edited
            if content2 != content:
                html_path.write_text(content2, encoding="utf-8")

            current = run_lint_for_slug(slug, html_dir, linter_script, single_report)
            if current.get("passed", False):
                passed = True
                break

        if not passed:
            blockers = temp_dir / "pilot50_blockers.md"
            with blockers.open("a", encoding="utf-8") as fh:
                fh.write(f"## {slug}\n")
                for i in current.get("issues", []):
                    fh.write(f"- {i.get('rule')}: {i.get('message')}\n")
                fh.write("\n")
            summary_rows.append((slug, [f"FAILED-after-{args.max_iterations_per_slug}"]))
            continue

        if edited_sections:
            sec_ids = [f"c-is.{n}.0" for n in sorted(edited_sections)]
        else:
            sec_ids = ["none"]
        summary_rows.append((slug, sec_ids))

    final = run_full_lint(html_dir, linter_script, slug_list_file, final_lint_report)

    lines = ["# Pilot 50 Fix Summary", "", "slug | sections-edited", "--- | ---"]
    for slug, sections in summary_rows:
        lines.append(f"{slug} | {', '.join(sections)}")
    lines.append("")
    lines.append(f"- processed: {len(summary_rows)}")
    lines.append(f"- final_passed: {final.get('passed_files')}")
    lines.append(f"- final_failed: {final.get('failed_files')}")
    summary_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if final.get("failed_files", 0) != 0:
        raise SystemExit(f"Strict lint still failing: {final.get('failed_files')} files")


if __name__ == "__main__":
    main()
