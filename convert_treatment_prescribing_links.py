#!/usr/bin/env python3
"""Convert section 12 pharmacology bullets into a JITL prescribing list."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DETAILS_TOKEN_RE = re.compile(r"(?is)<details\b|</details>")
UL_TOKEN_RE = re.compile(r"(?is)<ul\b[^>]*>|</ul>")
LIST_TOKEN_RE = re.compile(r"(?is)<li\b[^>]*>|</li>|<ul\b[^>]*>|</ul>")
PHARM_LABEL_RE = re.compile(r"(?is)<b>\s*Exam pharmacology reference(?:\s*\(UKMLA/MRCGP\))?:\s*</b>")
MED_SHORTCODE_RE = re.compile(r'(?is)\[sc\s+name="jitl-medication".*?\[/sc\]')
SAFETY_LINE = (
    "No doses or frequencies are cited here — always verify against your local "
    "antimicrobial/prescribing formulary before prescribing."
)


def find_matching_details_end(text: str, open_index: int) -> int:
    depth = 0
    seen_open = False
    for match in DETAILS_TOKEN_RE.finditer(text, open_index):
        token = match.group(0).lower()
        if token.startswith("<details"):
            depth += 1
            seen_open = True
        else:
            if seen_open:
                depth -= 1
                if depth == 0:
                    return match.end()
    return -1


def get_section_12_span(text: str) -> tuple[int, int] | None:
    opener = re.search(r'(?is)<details\b[^>]*\bid="c-is\.12\.0"[^>]*>', text)
    if not opener:
        return None
    end = find_matching_details_end(text, opener.start())
    if end < 0:
        return None
    return opener.start(), end


def find_top_level_ul_bounds(section_html: str) -> tuple[int, int, int, int] | None:
    opener = re.search(r"(?is)<ul\b[^>]*>", section_html)
    if not opener:
        return None
    depth = 0
    close_start = -1
    close_end = -1
    for match in UL_TOKEN_RE.finditer(section_html, opener.start()):
        token = match.group(0).lower()
        if token.startswith("<ul"):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                close_start = match.start()
                close_end = match.end()
                break
    if close_start < 0:
        return None
    return opener.start(), opener.end(), close_start, close_end


def top_level_li_spans(ul_inner: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    li_depth = 0
    ul_depth = 0
    block_start: int | None = None
    for match in LIST_TOKEN_RE.finditer(ul_inner):
        token = match.group(0).lower()
        if token.startswith("<ul"):
            ul_depth += 1
            continue
        if token == "</ul>":
            ul_depth -= 1
            continue
        if token.startswith("<li"):
            if li_depth == 0 and ul_depth == 0:
                block_start = match.start()
            li_depth += 1
            continue
        li_depth -= 1
        if li_depth == 0 and ul_depth == 0 and block_start is not None:
            spans.append((block_start, match.end()))
            block_start = None
    return spans


def dedupe_shortcodes(shortcodes: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for shortcode in shortcodes:
        cleaned = shortcode.strip()
        if cleaned and cleaned not in seen:
            ordered.append(cleaned)
            seen.add(cleaned)
    return ordered


def build_prescribing_block(indent: str, shortcodes: list[str]) -> str:
    nested_ul_indent = indent + "    "
    nested_li_indent = indent + "        "
    body = [
        "<li><b>Prescribing reference (JITL):</b>",
        f"{nested_ul_indent}<ul>",
    ]
    body.extend(f"{nested_li_indent}<li>{shortcode}</li>" for shortcode in shortcodes)
    body.extend(
        [
            f"{nested_ul_indent}</ul>",
            f"{nested_ul_indent}{SAFETY_LINE}",
            f"{indent}</li>",
        ]
    )
    return "\n".join(body)


def rewrite_file(path: Path, *, write: bool) -> tuple[bool, str]:
    original = path.read_text(encoding="utf-8")
    span = get_section_12_span(original)
    if not span:
        return False, "missing_section_12"
    start, end = span
    section_html = original[start:end]

    ul_bounds = find_top_level_ul_bounds(section_html)
    if not ul_bounds:
        return False, "missing_top_level_ul"
    ul_start, ul_open_end, ul_close_start, ul_end = ul_bounds
    ul_inner = section_html[ul_open_end:ul_close_start]

    replacement_inner = ul_inner
    changed = False
    for block_start, block_end in top_level_li_spans(ul_inner):
        block = ul_inner[block_start:block_end]
        if not PHARM_LABEL_RE.search(block):
            continue
        shortcodes = dedupe_shortcodes(MED_SHORTCODE_RE.findall(block))
        if not shortcodes:
            return False, "pharmacology_block_has_no_jitl_medication"
        line_start = ul_inner.rfind("\n", 0, block_start)
        if line_start < 0:
            indent = ""
        else:
            indent = ul_inner[line_start + 1 : block_start]
        new_block = build_prescribing_block(indent, shortcodes)
        replacement_inner = ul_inner[:block_start] + new_block + ul_inner[block_end:]
        changed = replacement_inner != ul_inner
        break

    if not changed:
        return False, "no_convertible_pharmacology_block"

    new_section = section_html[:ul_open_end] + replacement_inner + section_html[ul_close_start:]
    rewritten = original[:start] + new_section + original[end:]
    if rewritten == original:
        return False, "unchanged"
    if write:
        path.write_text(rewritten, encoding="utf-8")
    return True, "updated"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="HTML files or directories to rewrite. Defaults to updated-illness-scripts-2026-final.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Persist changes. Without this flag the script reports what would change.",
    )
    args = parser.parse_args()

    inputs = [Path(p) for p in args.paths] or [Path("updated-illness-scripts-2026-final")]
    files: list[Path] = []
    for input_path in inputs:
        if input_path.is_dir():
            files.extend(sorted(input_path.glob("*.html")))
        elif input_path.is_file():
            files.append(input_path)

    updated = 0
    skipped = 0
    for path in files:
        changed, reason = rewrite_file(path, write=args.write)
        if changed:
            updated += 1
            action = "UPDATED" if args.write else "WOULD UPDATE"
            print(f"{action} {path}")
        else:
            skipped += 1
            print(f"SKIPPED {path} :: {reason}")

    print(f"Summary: updated={updated} skipped={skipped} total={len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
