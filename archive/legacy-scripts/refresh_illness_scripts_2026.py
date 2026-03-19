#!/usr/bin/env python3
"""Build 2026 illness scripts set from v2 with epidemiology JITL enforcement.

Rules enforced for every output file:
1. Section c-is.2.0 summary becomes:
   <summary id="s-is.2.0">Epidemiology [sc name="ask-ai-102" Q="Condition"][/sc]</summary>
2. First <li> in section c-is.2.0 first <ul> is:
   <li>[sc name="1095-jitl-epidemiology-link" Q="Condition"][/sc]</li>
3. Existing JITL epidemiology <li> entries in c-is.2.0 are deduplicated.
4. If section 2 has no <ul>, a minimal <ul> is created.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple


TITLE_DIV_RE = re.compile(r'(?is)<div\s+id="illness-script-title">(.*?)</div>')
DETAILS_OPEN_RE = re.compile(r'(?is)<details\b[^>]*\bid="c-is\.2\.0"[^>]*>')
DETAILS_TOKEN_RE = re.compile(r"(?is)<details\b|</details>")
SUMMARY_RE = re.compile(r"(?is)<summary\b[^>]*>.*?</summary>")
EPI_LI_RE = re.compile(
    r'(?is)\s*<li>\s*\[sc\s+name="1095-jitl-epidemiology-link"\s+Q=".*?"\]\[/sc\]\s*</li>\s*'
)


@dataclass
class RefreshStats:
    total_files: int = 0
    processed_files: int = 0
    skipped_files: int = 0
    inserted_ul_count: int = 0
    fixed_first_li_count: int = 0
    skipped_reasons: Dict[str, int] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.skipped_reasons is None:
            self.skipped_reasons = {}

    def add_skip(self, reason: str) -> None:
        self.skipped_files += 1
        self.skipped_reasons[reason] = self.skipped_reasons.get(reason, 0) + 1


def slug_to_title(slug: str) -> str:
    base = slug.replace("is-", "", 1)
    parts = [p for p in base.split("-") if p]
    return " ".join(p[:1].upper() + p[1:] for p in parts)


def clean_condition_name(text: str, slug: str) -> str:
    m = TITLE_DIV_RE.search(text)
    if m:
        raw = m.group(1)
        raw = re.sub(r'(?is)\[sc\s+name="ask-ai-\d+".*?\[/sc\]', "", raw)
        raw = re.sub(r"(?is)<[^>]+>", "", raw)
        raw = html.unescape(raw)
        raw = re.sub(r"\s+", " ", raw).strip()
        raw = re.sub(r"\s*Illness\s+Script\s*$", "", raw, flags=re.IGNORECASE).strip()
        if raw:
            return raw
    return slug_to_title(slug)


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


def enforce_epi_section(section_html: str, condition_name: str) -> Tuple[str, bool, bool]:
    changed = False
    inserted_ul = False

    q_value = condition_name.replace('"', "&quot;")
    summary_target = (
        f'<summary id="s-is.2.0">Epidemiology [sc name="ask-ai-102" Q="{q_value}"][/sc]</summary>'
    )
    epi_li = f'<li>[sc name="1095-jitl-epidemiology-link" Q="{q_value}"][/sc]</li>'

    summary_match = SUMMARY_RE.search(section_html)
    if not summary_match:
        return section_html, changed, inserted_ul

    if summary_match.group(0) != summary_target:
        section_html = section_html[: summary_match.start()] + summary_target + section_html[summary_match.end() :]
        changed = True

    # Remove existing epidemiology shortcode list item(s) so we can reinsert as first item.
    stripped_section = EPI_LI_RE.sub("\n", section_html)
    if stripped_section != section_html:
        section_html = stripped_section
        changed = True

    ul_match = re.search(r"(?is)<ul\b[^>]*>", section_html)
    if ul_match:
        insert_at = ul_match.end()
        li_indent = "            "
        next_li = re.search(r"(?m)^([ \t]*)<li\b", section_html[insert_at:])
        if next_li:
            li_indent = next_li.group(1)
        insert_text = f"\n{li_indent}{epi_li}"
        section_html = section_html[:insert_at] + insert_text + section_html[insert_at:]
        changed = True
        return section_html, changed, inserted_ul

    # No <ul> exists in section 2: create minimal ul after first child div if possible.
    div_match = re.search(r"(?is)<div\b[^>]*>", section_html)
    ul_block = f"\n        <ul>\n            {epi_li}\n        </ul>"
    if div_match:
        insert_at = div_match.end()
        section_html = section_html[:insert_at] + ul_block + section_html[insert_at:]
    else:
        # Fallback: insert immediately after summary.
        summary_match_after = SUMMARY_RE.search(section_html)
        if summary_match_after:
            section_html = (
                section_html[: summary_match_after.end()]
                + "\n"
                + ul_block
                + section_html[summary_match_after.end() :]
            )
        else:
            return section_html, changed, inserted_ul
    changed = True
    inserted_ul = True
    return section_html, changed, inserted_ul


def has_required_sections(text: str) -> bool:
    for i in range(1, 14):
        if f'id="c-is.{i}.0"' not in text:
            return False
        if f'id="s-is.{i}.0"' not in text:
            return False
    return True


def validate_epi_first_li(text: str, condition_name: str) -> bool:
    m = DETAILS_OPEN_RE.search(text)
    if not m:
        return False
    end = find_matching_details_end(text, m.start())
    if end < 0:
        return False
    section = text[m.start() : end]
    ul = re.search(r"(?is)<ul\b[^>]*>(.*?)</ul>", section)
    if not ul:
        return False
    first_li = re.search(r"(?is)<li\b[^>]*>(.*?)</li>", ul.group(1))
    if not first_li:
        return False
    expected = f'[sc name="1095-jitl-epidemiology-link" Q="{condition_name.replace(chr(34), "&quot;")}"][/sc]'
    actual = re.sub(r"\s+", " ", first_li.group(1)).strip()
    return actual == expected


def refresh_file(content: str, slug: str) -> Tuple[str, bool, bool]:
    condition_name = clean_condition_name(content, slug)
    m = DETAILS_OPEN_RE.search(content)
    if not m:
        return content, False, False
    end = find_matching_details_end(content, m.start())
    if end < 0:
        return content, False, False
    section = content[m.start() : end]
    new_section, changed, inserted_ul = enforce_epi_section(section, condition_name)
    if not changed:
        return content, False, inserted_ul
    out = content[: m.start()] + new_section + content[end:]
    return out, True, inserted_ul


def main() -> None:
    parser = argparse.ArgumentParser(description="Create 2026 illness scripts set with epidemiology JITL enforcement.")
    parser.add_argument("--source-dir", default="extracted-illness-scripts-v2")
    parser.add_argument("--output-dir", default="extracted-illness-scripts-2026")
    parser.add_argument("--report-file", default="extracted-illness-scripts-2026/refresh_report_2026.json")
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    output_dir = Path(args.output_dir)
    report_file = Path(args.report_file)

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    stats = RefreshStats()
    files = sorted(source_dir.glob("is-*.html"))
    stats.total_files = len(files)

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for path in files:
        slug = path.stem
        content = path.read_text(encoding="utf-8", errors="replace")

        if not has_required_sections(content):
            stats.add_skip("missing_required_sections")
            continue

        refreshed, changed, inserted_ul = refresh_file(content, slug)
        condition_name = clean_condition_name(refreshed, slug)
        if inserted_ul:
            stats.inserted_ul_count += 1
        if changed:
            stats.fixed_first_li_count += 1

        if not validate_epi_first_li(refreshed, condition_name):
            stats.add_skip("failed_epi_validation")
            continue

        out_path = output_dir / path.name
        out_path.write_text(refreshed, encoding="utf-8")
        stats.processed_files += 1

    report_file.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_dir": str(source_dir.resolve()),
        "output_dir": str(output_dir.resolve()),
        "total_files": stats.total_files,
        "processed_files": stats.processed_files,
        "skipped_files": stats.skipped_files,
        "inserted_ul_count": stats.inserted_ul_count,
        "fixed_or_set_epi_first_li_count": stats.fixed_first_li_count,
        "skipped_reasons": stats.skipped_reasons,
    }
    report_file.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Source files: {stats.total_files}")
    print(f"Processed files: {stats.processed_files}")
    print(f"Skipped files: {stats.skipped_files}")
    print(f"Output dir: {output_dir}")
    print(f"Report: {report_file}")


if __name__ == "__main__":
    main()
