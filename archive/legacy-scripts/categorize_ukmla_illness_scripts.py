#!/usr/bin/env python3
"""Categorize extracted illness scripts into UKMLA clinical practice folders.

Reads the UKMLA PDF appendix mapping (conditions -> areas of clinical practice),
matches each `is-*.html` illness script to a UKMLA condition where possible, copies
scripts into category folders, and writes a coverage gap report.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
import sys
import unicodedata
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple
import xml.etree.ElementTree as ET


PROJECT_ROOT = Path(__file__).resolve().parent
VENDOR_DIR = PROJECT_ROOT / ".vendor"
if str(VENDOR_DIR) not in sys.path:
    sys.path.insert(0, str(VENDOR_DIR))

import pdfplumber  # type: ignore

DEFAULT_UPDATED_XLSX = (
    r"c:\Users\amjid\Downloads\updated-mla-content-map---english-language_xlsx-113423262 (1).xlsx"
)

HIGH_PRIORITY_CATEGORY_HINTS = {
    "acute and emergency",
    "heart and vasculature",
    "lungs, pleura and airways",
    "brain and spinal cord",
    "child health",
    "pregnancy and the puerperium",
    "infections",
    "drugs and drug effects",
}

UKMLA_CATEGORIES = [
    "Acute and emergency",
    "Cancer",
    "Cardiovascular",
    "Child health",
    "Clinical haematology",
    "Clinical imaging",
    "Dermatology",
    "Ear, nose and throat",
    "Endocrine and metabolic",
    "Gastrointestinal including liver",
    "General practice and primary healthcare",
    "Infection",
    "Medicine of older adult",
    "Mental health",
    "Musculoskeletal",
    "Neurosciences",
    "Obstetrics and gynaecology",
    "Ophthalmology",
    "Palliative and end of life care",
    "Perioperative medicine and anaesthesia",
    "Renal and urology",
    "Respiratory",
    "Sexual health",
    "Surgery",
    "All areas of clinical practice",
]


# Manual aliases for common abbreviations/variants in script titles.
CONDITION_ALIAS_TO_UKMLA = {
    "acs": "Acute coronary syndromes",
    "acute coronary syndrome": "Acute coronary syndromes",
    "gord": "Gastro-oesophageal reflux disease",
    "dka": "Diabetic ketoacidosis",
    "pe": "Pulmonary embolism",
    "copd": "Chronic obstructive pulmonary disease",
    "ckd": "Chronic kidney disease",
    "aki": "Acute kidney injury",
    "ibs": "Irritable bowel syndrome",
    "ibd": "Inflammatory bowel disease",
    "bppv": "Benign paroxysmal positional vertigo",
    "uti": "Urinary tract infection",
    "urti": "Upper respiratory tract infection",
    "tia": "Transient ischaemic attacks",
    "dementia": "Dementias",
    "cataract": "Cataracts",
    "arrhythmia": "Arrhythmias",
    "benign prostatic hypertrophy": "Benign prostatic hyperplasia",
}


TITLE_RE = re.compile(r'<div\s+id="illness-script-title">(.*?)</div>', re.IGNORECASE | re.DOTALL)
SHORTCODE_RE = re.compile(r'\[sc\s+name="ask-ai-100".*?\[/sc\]', re.IGNORECASE | re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")


@dataclass
class ScriptTopic:
    slug: str
    file_path: Path
    title: str


@dataclass
class MatchResult:
    ukmla_condition: str | None
    match_method: str
    categories: List[str]


def normalize_text(value: str) -> str:
    value = html.unescape(value)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.lower()
    value = value.replace("&", " and ")
    value = value.replace("/", " ")
    value = value.replace("+", " plus ")
    value = re.sub(r"[^a-z0-9\s-]+", " ", value)
    value = SPACE_RE.sub(" ", value).strip()
    return value


def clean_cell(cell: str | None) -> str:
    if not cell:
        return ""
    return SPACE_RE.sub(" ", str(cell).strip())


def extract_headings_in_order(page_text: str) -> List[str]:
    found: List[str] = []
    for raw_line in page_text.splitlines():
        line = raw_line.strip()
        for category in UKMLA_CATEGORIES:
            if line == category or line == f"{category} (cont.)":
                if not found or found[-1] != category:
                    found.append(category)
                break
    return found


def assign_tables_to_headings(headings: List[str], table_count: int) -> List[str]:
    if not headings:
        return []
    if len(headings) == 1:
        return [headings[0]] * table_count
    if len(headings) == table_count:
        return headings
    # Fall back to sequential assignment; any extra tables use final heading.
    return [headings[min(i, len(headings) - 1)] for i in range(table_count)]


def extract_conditions_from_table(table: List[List[str | None]]) -> List[str]:
    has_presentations = False
    has_conditions = False
    for row in table:
        for cell in row:
            if not cell:
                continue
            low = str(cell).lower()
            if "presentations" in low:
                has_presentations = True
            if "conditions" in low:
                has_conditions = True

    condition_only_table = has_conditions and not has_presentations
    conditions: List[str] = []

    for row in table:
        cells = [clean_cell(c) for c in row]
        cells = [c for c in cells if c]
        if not cells:
            continue

        joined = " ".join(cells).lower()
        if "presentations" in joined or joined == "conditions":
            continue

        if condition_only_table:
            candidate = cells[-1]
        else:
            if len(cells) < 2:
                continue
            candidate = cells[-1]

        candidate = clean_cell(candidate)
        if not candidate:
            continue
        if candidate.lower() in {"conditions", "presentations"}:
            continue
        if re.fullmatch(r"\d+", candidate):
            continue
        conditions.append(candidate)

    return conditions


def parse_ukmla_condition_mapping(
    pdf_path: Path,
) -> Tuple[Dict[str, Set[str]], Dict[str, Set[str]], Dict[str, Set[str]], Dict[str, Set[str]]]:
    category_to_conditions: Dict[str, Set[str]] = {c: set() for c in UKMLA_CATEGORIES}
    category_to_presentations: Dict[str, Set[str]] = {c: set() for c in UKMLA_CATEGORIES}

    with pdfplumber.open(str(pdf_path)) as pdf:
        # Appendix mapping starts at page 18 in the PDF (0-index 17) and ends at page 38 (0-index 37).
        for page_index in range(17, 38):
            page = pdf.pages[page_index]
            text = page.extract_text() or ""
            headings = extract_headings_in_order(text)
            tables = page.extract_tables() or []
            if not headings or not tables:
                continue

            assignments = assign_tables_to_headings(headings, len(tables))
            for table, category in zip(tables, assignments):
                has_presentations = False
                has_conditions = False
                for row in table:
                    for cell in row:
                        if not cell:
                            continue
                        low = str(cell).lower()
                        if "presentations" in low:
                            has_presentations = True
                        if "conditions" in low:
                            has_conditions = True

                condition_only_table = has_conditions and not has_presentations
                for row in table:
                    cells = [clean_cell(c) for c in row]
                    cells = [c for c in cells if c]
                    if not cells:
                        continue

                    joined = " ".join(cells).lower()
                    if "presentations" in joined or joined == "conditions":
                        continue

                    if condition_only_table:
                        condition = cells[-1]
                        if condition and condition.lower() not in {"conditions", "presentations"}:
                            category_to_conditions[category].add(condition)
                        continue

                    if len(cells) < 2:
                        continue

                    presentation = cells[0]
                    condition = cells[-1]
                    if presentation and presentation.lower() not in {"conditions", "presentations"}:
                        category_to_presentations[category].add(presentation)
                    if condition and condition.lower() not in {"conditions", "presentations"}:
                        category_to_conditions[category].add(condition)

    # Build reverse mapping: condition -> set(categories).
    condition_to_categories: Dict[str, Set[str]] = defaultdict(set)
    for category, conditions in category_to_conditions.items():
        for condition in conditions:
            condition_to_categories[condition].add(category)

    presentation_to_categories: Dict[str, Set[str]] = defaultdict(set)
    for category, presentations in category_to_presentations.items():
        for presentation in presentations:
            presentation_to_categories[presentation].add(category)

    return category_to_conditions, condition_to_categories, category_to_presentations, presentation_to_categories


def parse_ukmla_xlsx_appendix_mapping(xlsx_path: Path) -> Tuple[List[str], Dict[str, Set[str]], Dict[str, Set[str]]]:
    """Parse updated UKMLA workbook Appendix A (conditions by body system)."""
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    rel_ns = "{http://schemas.openxmlformats.org/package/2006/relationships}"
    off_rel_ns = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

    with zipfile.ZipFile(xlsx_path) as zf:
        wb = ET.fromstring(zf.read("xl/workbook.xml"))
        rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        rid_to_target = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in rels.findall(f"{rel_ns}Relationship")
        }

        appendix_target = None
        sheets = wb.find("m:sheets", ns)
        if sheets is None:
            raise RuntimeError("Workbook has no sheets.")
        for sheet in sheets.findall("m:sheet", ns):
            name = sheet.attrib.get("name", "").strip().lower()
            rid = sheet.attrib.get(f"{off_rel_ns}id")
            if name == "appendix a" and rid in rid_to_target:
                appendix_target = rid_to_target[rid]
                break
        if appendix_target is None:
            raise RuntimeError("Could not find 'Appendix A' sheet in workbook.")
        if not appendix_target.startswith("xl/"):
            appendix_target = f"xl/{appendix_target}"

        shared_strings: List[str] = []
        if "xl/sharedStrings.xml" in zf.namelist():
            ss_root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
            for si in ss_root.findall("m:si", ns):
                text = "".join((t.text or "") for t in si.findall(".//m:t", ns))
                shared_strings.append(text)

        sheet_xml = ET.fromstring(zf.read(appendix_target))
        rows = sheet_xml.findall(".//m:sheetData/m:row", ns)
        if not rows:
            raise RuntimeError("Appendix A sheet has no rows.")

        # Heading rows and condition rows use different styles; infer heading style from first non-empty row.
        heading_style = None
        first_style = None
        for row in rows:
            cell = row.find("m:c", ns)
            if cell is None:
                continue
            style = cell.attrib.get("s")
            v = cell.find("m:v", ns)
            if style is not None and v is not None and (v.text or "").strip():
                first_style = style
                break
        heading_style = first_style

        category_order: List[str] = []
        category_to_conditions: Dict[str, Set[str]] = {}
        current_category: str | None = None

        def cell_text(cell: ET.Element) -> str:
            ctype = cell.attrib.get("t")
            v = cell.find("m:v", ns)
            if ctype == "s" and v is not None and v.text is not None:
                idx = int(v.text)
                return shared_strings[idx] if 0 <= idx < len(shared_strings) else ""
            if ctype == "inlineStr":
                t = cell.find("m:is/m:t", ns)
                return t.text or "" if t is not None else ""
            return v.text or "" if v is not None else ""

        for row in rows:
            cells = row.findall("m:c", ns)
            if not cells:
                continue
            first = cells[0]
            value = clean_cell(cell_text(first))
            if not value:
                continue
            value = html.unescape(value).strip()
            if not value:
                continue
            # Ignore alpha section rows if present.
            if re.fullmatch(r"[A-Z]", value):
                continue

            style = first.attrib.get("s")
            is_heading = (heading_style is not None and style == heading_style)
            if is_heading:
                current_category = value
                if current_category not in category_to_conditions:
                    category_to_conditions[current_category] = set()
                    category_order.append(current_category)
                continue

            if current_category is None:
                continue
            category_to_conditions[current_category].add(value)

    condition_to_categories: Dict[str, Set[str]] = defaultdict(set)
    for category, conditions in category_to_conditions.items():
        for condition in conditions:
            condition_to_categories[condition].add(category)

    return category_order, category_to_conditions, condition_to_categories


def extract_script_title(file_text: str, slug: str) -> str:
    match = TITLE_RE.search(file_text)
    if match:
        title = match.group(1)
        title = SHORTCODE_RE.sub("", title)
        title = HTML_TAG_RE.sub("", title)
        title = html.unescape(title)
        title = SPACE_RE.sub(" ", title).strip()
        title = re.sub(r"\s*Illness\s+Script\s*$", "", title, flags=re.IGNORECASE)
        if title:
            return title

    # Fallback from slug.
    return slug.replace("is-", "", 1).replace("-", " ").strip()


def load_script_topics(source_dir: Path) -> List[ScriptTopic]:
    topics: List[ScriptTopic] = []
    for file_path in sorted(source_dir.glob("is-*.html")):
        slug = file_path.stem
        content = file_path.read_text(encoding="utf-8", errors="replace")
        title = extract_script_title(content, slug)
        topics.append(ScriptTopic(slug=slug, file_path=file_path, title=title))
    return topics


def candidate_strings(topic: ScriptTopic) -> List[str]:
    base_slug = topic.slug.replace("is-", "", 1).replace("-", " ")
    title_norm = normalize_text(topic.title)
    slug_norm = normalize_text(base_slug)

    candidates: List[str] = [title_norm, slug_norm]

    for sep in [":", "-", "/"]:
        if sep in topic.title:
            for part in topic.title.split(sep):
                part_norm = normalize_text(part)
                if part_norm:
                    candidates.append(part_norm)

    slug_tokens = slug_norm.split()
    for n in [4, 3, 2, 1]:
        if len(slug_tokens) >= n:
            candidates.append(" ".join(slug_tokens[-n:]))

    alias_expanded: List[str] = []
    for c in candidates:
        aliased = CONDITION_ALIAS_TO_UKMLA.get(c)
        if aliased:
            alias_expanded.append(normalize_text(aliased))
    candidates.extend(alias_expanded)

    # Plural/singular variants to improve exact matching.
    variants: List[str] = []
    for c in candidates:
        if not c:
            continue
        if c.endswith("s"):
            variants.append(c[:-1].strip())
        else:
            variants.append(f"{c}s".strip())
    candidates.extend(variants)

    out: List[str] = []
    seen: Set[str] = set()
    for c in candidates:
        c = c.strip()
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def match_topic_to_condition(
    topic: ScriptTopic,
    normalized_to_condition: Dict[str, str],
) -> Tuple[str | None, str]:
    candidates = candidate_strings(topic)

    for cand in candidates:
        if cand in normalized_to_condition:
            return normalized_to_condition[cand], "exact"

    # Conservative fuzzy token matching for partial-title scripts.
    best_condition: str | None = None
    best_score = -1.0

    for cand in candidates:
        cand_tokens = set(cand.split())
        if not cand_tokens:
            continue
        for normalized_condition, condition_name in normalized_to_condition.items():
            cond_tokens = set(normalized_condition.split())
            if not cond_tokens:
                continue

            if cond_tokens.issubset(cand_tokens):
                # Strong when topic includes full UKMLA condition plus extra context.
                score = 1.2 + (len(cond_tokens) / 10.0) - ((len(cand_tokens) - len(cond_tokens)) / 20.0)
            elif len(cand_tokens) >= 2 and cand_tokens.issubset(cond_tokens):
                score = 1.0 + (len(cand_tokens) / 10.0) - ((len(cond_tokens) - len(cand_tokens)) / 25.0)
            else:
                overlap = len(cand_tokens & cond_tokens)
                if overlap == 0:
                    continue
                score = (2.0 * overlap) / (len(cand_tokens) + len(cond_tokens))

            if score > best_score:
                best_score = score
                best_condition = condition_name

    if best_condition is not None and best_score >= 1.05:
        return best_condition, f"fuzzy:{best_score:.2f}"

    return None, "unmatched"


def sanitize_folder_name(name: str) -> str:
    # Keep readable category names while removing filesystem-problematic characters.
    return re.sub(r'[<>:"/\\|?*]+', "-", name).strip()


def write_mapping_csv(rows: Iterable[Dict[str, str]], output_csv: Path) -> None:
    headers = [
        "slug",
        "title",
        "matched_condition",
        "matched_presentation",
        "match_basis",
        "match_method",
        "match_confidence",
        "requires_manual_review",
        "coverage_status",
        "categories",
        "source_file",
    ]
    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def get_match_confidence(match_method: str, match_basis: str) -> float:
    if match_basis == "unmatched":
        return 0.0
    if match_method == "exact":
        return 0.95
    if match_method.startswith("fuzzy:"):
        return 0.65
    return 0.5


def get_priority_for_categories(categories: List[str]) -> str:
    normalized = {c.lower().strip() for c in categories}
    if normalized & HIGH_PRIORITY_CATEGORY_HINTS:
        return "high"
    return "medium"


def write_gap_tracker_csv(
    output_csv: Path,
    all_conditions: List[str],
    condition_to_categories: Dict[str, Set[str]],
    mapping_rows: List[Dict[str, str]],
) -> None:
    scripts_by_condition: Dict[str, Set[str]] = defaultdict(set)
    for row in mapping_rows:
        cond = row.get("matched_condition", "").strip()
        if cond:
            scripts_by_condition[cond].add(row["slug"])

    headers = [
        "condition",
        "status",
        "priority",
        "phase",
        "categories",
        "matched_script_count",
        "matched_scripts",
    ]
    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for condition in all_conditions:
            categories = sorted(condition_to_categories.get(condition, set()))
            matched_slugs = sorted(scripts_by_condition.get(condition, set()))
            matched_count = len(matched_slugs)

            if matched_count == 0:
                status = "missing"
                priority = get_priority_for_categories(categories)
                phase = "phase-3-create-priority" if priority == "high" else "phase-3-create-backlog"
            else:
                # Default all existing legacy scripts to refresh-needed until clinical review is completed.
                status = "covered-needs-refresh"
                priority = get_priority_for_categories(categories)
                phase = "phase-1-pilot" if priority == "high" else "phase-2-refresh"

            writer.writerow(
                {
                    "condition": condition,
                    "status": status,
                    "priority": priority,
                    "phase": phase,
                    "categories": "; ".join(categories),
                    "matched_script_count": matched_count,
                    "matched_scripts": "; ".join(matched_slugs),
                }
            )


def write_coverage_report(
    output_path: Path,
    source_dir: Path,
    category_to_conditions: Dict[str, Set[str]],
    category_order: List[str],
    matched_conditions: Set[str],
    unmatched_topics: List[ScriptTopic],
    categorized_counts: Dict[str, int],
    total_topics: int,
    matched_topics: int,
    matched_by_condition: int,
    matched_by_presentation: int,
) -> None:
    all_ukmla_conditions = sorted(set().union(*category_to_conditions.values()))
    uncovered_conditions = sorted(set(all_ukmla_conditions) - matched_conditions)

    lines: List[str] = []
    lines.append("# UKMLA Illness Script Coverage Report")
    lines.append("")
    lines.append(f"- Generated (UTC): {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"- Source scripts folder: `{source_dir}`")
    lines.append(f"- UKMLA conditions extracted from appendix: **{len(all_ukmla_conditions)}**")
    lines.append(f"- Illness script files scanned: **{total_topics}**")
    lines.append(f"- Script files categorized (condition or presentation match): **{matched_topics}**")
    lines.append(f"- Categorized via condition match: **{matched_by_condition}**")
    lines.append(f"- Categorized via presentation match: **{matched_by_presentation}**")
    lines.append(f"- UKMLA conditions currently covered by at least one script: **{len(matched_conditions)}**")
    lines.append(f"- UKMLA conditions not yet covered: **{len(uncovered_conditions)}**")
    lines.append("")
    lines.append("## Files Per UKMLA Category")
    lines.append("")
    for category in category_order:
        lines.append(f"- {category}: {categorized_counts.get(category, 0)}")
    lines.append(f"- _Unmapped: {categorized_counts.get('_Unmapped', 0)}")
    lines.append("")
    lines.append("## UKMLA Conditions Not Yet Covered")
    lines.append("")
    for condition in uncovered_conditions:
        lines.append(f"- {condition}")
    lines.append("")
    lines.append("## Unmatched Illness Script Topics")
    lines.append("")
    for topic in unmatched_topics:
        lines.append(f"- {topic.slug}: {topic.title}")
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Categorize illness scripts by UKMLA clinical practice categories.")
    parser.add_argument(
        "--pdf",
        default=r"c:\Users\amjid\Downloads\ukmla-content-map-_pdf.pdf",
        help="Path to UKMLA content map PDF.",
    )
    parser.add_argument(
        "--xlsx",
        default=DEFAULT_UPDATED_XLSX,
        help="Path to updated UKMLA content map XLSX (Appendix A). If present, this is used for categorization.",
    )
    parser.add_argument(
        "--source-dir",
        default="extracted-illness-scripts-2026",
        help="Directory containing is-*.html files.",
    )
    parser.add_argument(
        "--output-dir",
        default="ukmla-categorized-illness-scripts-2026",
        help="Directory for categorized output folders.",
    )
    parser.add_argument(
        "--report-file",
        default="UKMLA_COVERAGE_GAPS_2026.md",
        help="Markdown report path for uncovered UKMLA conditions.",
    )
    parser.add_argument(
        "--gap-tracker-file",
        default="",
        help="Optional explicit CSV path for condition-level coverage tracker. Defaults inside output-dir.",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    xlsx_path = Path(args.xlsx) if args.xlsx else None
    source_dir = Path(args.source_dir)
    output_dir = Path(args.output_dir)
    report_file = Path(args.report_file)
    gap_tracker_file = Path(args.gap_tracker_file) if args.gap_tracker_file else (output_dir / "ukmla_gap_tracker_2026.csv")

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    used_source = ""
    if xlsx_path is not None and xlsx_path.exists():
        category_order, category_to_conditions, condition_to_categories = parse_ukmla_xlsx_appendix_mapping(xlsx_path)
        presentation_to_categories: Dict[str, Set[str]] = {}
        used_source = str(xlsx_path)
    else:
        if not pdf_path.exists():
            raise FileNotFoundError(f"UKMLA PDF not found: {pdf_path}")
        (
            category_to_conditions,
            condition_to_categories,
            _category_to_presentations,
            presentation_to_categories,
        ) = parse_ukmla_condition_mapping(pdf_path)
        category_order = [c for c in UKMLA_CATEGORIES if c in category_to_conditions]
        used_source = str(pdf_path)
    all_conditions = sorted(condition_to_categories.keys())
    normalized_to_condition: Dict[str, str] = {}
    for condition in all_conditions:
        n = normalize_text(condition)
        # Keep first encountered canonical string for each normalized key.
        if n and n not in normalized_to_condition:
            normalized_to_condition[n] = condition
    all_presentations = sorted(presentation_to_categories.keys())
    normalized_to_presentation: Dict[str, str] = {}
    for presentation in all_presentations:
        n = normalize_text(presentation)
        if n and n not in normalized_to_presentation:
            normalized_to_presentation[n] = presentation

    topics = load_script_topics(source_dir)

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Ensure category folders exist.
    category_folder_map: Dict[str, Path] = {}
    for category in UKMLA_CATEGORIES:
        if category not in category_order:
            continue
        folder = output_dir / sanitize_folder_name(category)
        folder.mkdir(parents=True, exist_ok=True)
        category_folder_map[category] = folder
    for category in category_order:
        if category in category_folder_map:
            continue
        folder = output_dir / sanitize_folder_name(category)
        folder.mkdir(parents=True, exist_ok=True)
        category_folder_map[category] = folder
    unmapped_folder = output_dir / "_Unmapped"
    unmapped_folder.mkdir(parents=True, exist_ok=True)

    mapping_rows: List[Dict[str, str]] = []
    unmatched_topics: List[ScriptTopic] = []
    categorized_counts: Dict[str, int] = defaultdict(int)
    matched_conditions: Set[str] = set()
    matched_topics_count = 0
    matched_by_condition = 0
    matched_by_presentation = 0

    for topic in topics:
        matched_condition, method = match_topic_to_condition(topic, normalized_to_condition)
        matched_presentation: str | None = None
        match_basis = "condition" if matched_condition else "unmatched"

        if not matched_condition and presentation_to_categories:
            matched_presentation, method = match_topic_to_condition(topic, normalized_to_presentation)
            match_basis = "presentation" if matched_presentation else "unmatched"

        if matched_condition:
            categories = sorted(condition_to_categories.get(matched_condition, set()))
            if not categories:
                categories = []
            for category in categories:
                destination = category_folder_map[category] / topic.file_path.name
                shutil.copy2(topic.file_path, destination)
                categorized_counts[category] += 1
            matched_conditions.add(matched_condition)
            matched_topics_count += 1
            matched_by_condition += 1
            coverage_status = "covered-needs-refresh"
        elif matched_presentation:
            categories = sorted(presentation_to_categories.get(matched_presentation, set()))
            for category in categories:
                destination = category_folder_map[category] / topic.file_path.name
                shutil.copy2(topic.file_path, destination)
                categorized_counts[category] += 1
            matched_topics_count += 1
            matched_by_presentation += 1
            coverage_status = "covered-needs-refresh"
        else:
            categories = []
            destination = unmapped_folder / topic.file_path.name
            shutil.copy2(topic.file_path, destination)
            categorized_counts["_Unmapped"] += 1
            unmatched_topics.append(topic)
            coverage_status = "not_covered"

        match_confidence = get_match_confidence(method, match_basis)
        requires_manual_review = (
            "true" if (match_basis == "unmatched" or method.startswith("fuzzy:")) else "false"
        )

        mapping_rows.append(
            {
                "slug": topic.slug,
                "title": topic.title,
                "matched_condition": matched_condition or "",
                "matched_presentation": matched_presentation or "",
                "match_basis": match_basis,
                "match_method": method,
                "match_confidence": f"{match_confidence:.2f}",
                "requires_manual_review": requires_manual_review,
                "coverage_status": coverage_status,
                "categories": "; ".join(categories),
                "source_file": str(topic.file_path),
            }
        )

    # Export mapping artifacts.
    mapping_csv = output_dir / "ukmla_script_category_map.csv"
    write_mapping_csv(mapping_rows, mapping_csv)

    mapping_json = output_dir / "ukmla_condition_category_mapping.json"
    coverage_status_counts: Dict[str, int] = defaultdict(int)
    for row in mapping_rows:
        coverage_status_counts[row["coverage_status"]] += 1
    json_payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "pdf_source": str(pdf_path),
        "mapping_source": used_source,
        "source_dir": str(source_dir),
        "ukmla_category_count": len(category_order),
        "ukmla_condition_count": len(all_conditions),
        "ukmla_presentation_count": len(all_presentations),
        "script_file_count": len(topics),
        "matched_topic_count": matched_topics_count,
        "matched_by_condition": matched_by_condition,
        "matched_by_presentation": matched_by_presentation,
        "unmatched_topic_count": len(unmatched_topics),
        "coverage_status_counts": dict(coverage_status_counts),
        "category_to_conditions": {k: sorted(v) for k, v in category_to_conditions.items()},
    }
    mapping_json.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")

    write_gap_tracker_csv(
        output_csv=gap_tracker_file,
        all_conditions=all_conditions,
        condition_to_categories=condition_to_categories,
        mapping_rows=mapping_rows,
    )

    write_coverage_report(
        output_path=report_file,
        source_dir=source_dir,
        category_to_conditions=category_to_conditions,
        category_order=category_order,
        matched_conditions=matched_conditions,
        unmatched_topics=unmatched_topics,
        categorized_counts=categorized_counts,
        total_topics=len(topics),
        matched_topics=matched_topics_count,
        matched_by_condition=matched_by_condition,
        matched_by_presentation=matched_by_presentation,
    )

    print(f"Source scripts scanned: {len(topics)}")
    print(f"UKMLA conditions extracted: {len(all_conditions)}")
    print(f"Matched script topics: {matched_topics_count}")
    print(f"Unmatched script topics: {len(unmatched_topics)}")
    print(f"Categorized output: {output_dir}")
    print(f"Coverage report: {report_file}")
    print(f"Gap tracker: {gap_tracker_file}")


if __name__ == "__main__":
    main()
