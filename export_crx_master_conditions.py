#!/usr/bin/env python3
"""Export canonical illness scripts into CRx master-condition JSON.

Default behavior exports four exemplar conditions:
- Asthma
- Heart failure
- Pneumonia
- Pulmonary embolism

Use --all to export the full manifest-backed corpus.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
FINAL_DIR = ROOT / "updated-illness-scripts-2026-final"
MANIFEST_PATH = FINAL_DIR / "ukmla_canonical_manifest.csv"
TRACKER_PATH = FINAL_DIR / "UKMLA_CONDITION_TRACKER_2026.md"
DEFAULT_EXPORT_ROOT = ROOT / "exports" / "crx-master-conditions"
SCHEMA_VERSION = "2026-04-12"

DEFAULT_EXEMPLARS = [
    "Asthma",
    "Heart failure",
    "Pneumonia",
    "Pulmonary embolism",
]

SHORTCODE_RE = re.compile(r'\[sc\s+name="([^"]+)"([^\]]*)\]\[/sc\]')
DETAILS_TOKEN_RE = re.compile(r"<details\b|</details>", re.IGNORECASE)
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
SUPPORTED_SHORTCODE_NAMES = {"jitl-medication", "jitl-query", "1095-jitl-epidemiology-link"}
SUPPORTED_SHORTCODE_PREFIXES = ("ask-ai",)

SECTION_DEFINITIONS = [
    {"key": "overview", "title": "Overview", "source_numbers": [1], "source_ids": ["c-is.1.0"], "anchor": "#s-is.1.0"},
    {"key": "risk-factors", "title": "Risk Factors", "source_numbers": [2], "source_ids": ["c-is.2.0"], "anchor": "#s-is.2.0"},
    {"key": "pathophysiology", "title": "Pathophysiology", "source_numbers": [3], "source_ids": ["c-is.3.0"], "anchor": "#s-is.3.0"},
    {"key": "time-course", "title": "Time Course", "source_numbers": [4], "source_ids": ["c-is.4.0"], "anchor": "#s-is.4.0"},
    {"key": "clinical-features", "title": "Clinical Features", "source_numbers": [5, 6], "source_ids": ["c-is.5.0", "c-is.6.0"], "anchor": "#s-is.5.0"},
    {"key": "red-flags", "title": "Red Flags", "source_numbers": [7], "source_ids": ["c-is.7.0"], "anchor": "#s-is.7.0"},
    {"key": "atypical-presentations", "title": "Atypical Presentations", "source_numbers": [8], "source_ids": ["c-is.8.0"], "anchor": "#s-is.8.0"},
    {"key": "investigations", "title": "Investigations", "source_numbers": [9], "source_ids": ["c-is.9.0"], "anchor": "#s-is.9.0"},
    {"key": "problem-representation", "title": "Problem Representation", "source_numbers": [10], "source_ids": ["c-is.10.0"], "anchor": "#s-is.10.0"},
    {"key": "key-differentials", "title": "Key Differentials", "source_numbers": [11], "source_ids": ["c-is.11.0"], "anchor": "#s-is.11.0"},
    {"key": "management-thinking", "title": "Management Thinking", "source_numbers": [12], "source_ids": ["c-is.12.0"], "anchor": "#s-is.12.0"},
    {"key": "prescribing", "title": "Prescribing", "source_numbers": [12], "source_ids": ["c-is.12.0"], "anchor": "#s-is.12.0"},
    {"key": "complications", "title": "Complications", "source_numbers": [13], "source_ids": ["c-is.13.0"], "anchor": "#s-is.13.0"},
]

SPECIALTY_BY_CATEGORY = {
    "Blood and lymph": "Haematology",
    "Brain and spinal cord": "Neurology",
    "Child health": "Paediatrics",
    "Drugs and drug effects": "Clinical Pharmacology",
    "Ear, nose and throat": "ENT",
    "Endocrine and metabolic": "Endocrinology",
    "Eye": "Ophthalmology",
    "Gastrointestinal tract": "Gastroenterology",
    "Heart and vasculature": "Cardiology",
    "Infections": "Infectious Diseases",
    "Kidneys and urinary tract": "Renal",
    "Lungs, pleura and airways": "Respiratory",
    "Mental health": "Psychiatry",
    "Musculoskeletal": "Rheumatology",
    "Other knowledge": "General Medicine",
    "Pregnancy and the puerperium": "Obstetrics & Gynaecology",
    "Skin and soft tissue": "Dermatology",
}

ACCENT_THEME_BY_CATEGORY = {
    "Blood and lymph": "purple",
    "Brain and spinal cord": "purple",
    "Child health": "amber",
    "Drugs and drug effects": "blue",
    "Ear, nose and throat": "amber",
    "Endocrine and metabolic": "amber",
    "Eye": "purple",
    "Gastrointestinal tract": "green",
    "Heart and vasculature": "red",
    "Infections": "red",
    "Kidneys and urinary tract": "blue",
    "Lungs, pleura and airways": "green",
    "Mental health": "slate",
    "Musculoskeletal": "green",
    "Other knowledge": "slate",
    "Pregnancy and the puerperium": "amber",
    "Skin and soft tissue": "amber",
}


def normalize_value(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def slugify(value: str) -> str:
    plain = strip_html(value)
    plain = plain.lower().replace("’", "").replace("'", "")
    plain = re.sub(r"[^a-z0-9]+", "-", plain)
    return plain.strip("-")


def parse_attributes(attr_string: str) -> dict[str, str]:
    return {match.group(1): match.group(2) for match in ATTR_RE.finditer(attr_string)}


def strip_html(value: str) -> str:
    text = re.sub(r"<[^>]+>", " ", value)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def strip_ask_ai_shortcodes(value: str) -> str:
    return re.sub(r'\[sc\s+name="ask-ai-[^"]+".*?\]\[/sc\]', "", value, flags=re.IGNORECASE | re.DOTALL).strip()


def strip_all_shortcodes(value: str) -> str:
    return SHORTCODE_RE.sub("", value).strip()


def shortcodes_to_text(value: str) -> str:
    def replace(match: re.Match[str]) -> str:
        name, attr_string = match.group(1), match.group(2)
        attrs = parse_attributes(attr_string)
        if name.startswith(SUPPORTED_SHORTCODE_PREFIXES):
            return ""
        return attrs.get("text") or attrs.get("Q") or attrs.get("q") or ""

    return SHORTCODE_RE.sub(replace, value)


def first_sentence(value: str) -> str:
    match = re.match(r".+?[.!?](?:\s|$)", value.strip())
    return (match.group(0) if match else value).strip()


def ensure_supported_shortcodes(value: str, title: str, source_path: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        attr_string = match.group(2)
        if name not in SUPPORTED_SHORTCODE_NAMES and not name.startswith(SUPPORTED_SHORTCODE_PREFIXES):
            raise ValueError(f'Unsupported shortcode "{name}" in {source_path.name}')
        if name == "1095-jitl-epidemiology-link":
            attrs = parse_attributes(attr_string)
            topic = attrs.get("Q") or title
            return f'[sc name="jitl-query" Q="{topic} epidemiology" text="Epidemiology deep dive"][/sc]'
        return match.group(0)

    return SHORTCODE_RE.sub(replace, value)


def collect_jitl_references(value: str, source_section_key: str) -> list[dict[str, str]]:
    references: list[dict[str, str]] = []
    for match in SHORTCODE_RE.finditer(value):
        name, attr_string = match.group(1), match.group(2)
        if name not in {"jitl-medication", "jitl-query"}:
            continue
        attrs = parse_attributes(attr_string)
        references.append(
            {
                "type": "medication" if name == "jitl-medication" else "query",
                "query": attrs.get("Q") or attrs.get("q") or attrs.get("text") or "",
                "text": attrs.get("text") or attrs.get("Q") or "Open JITL",
                "sourceShortcode": match.group(0),
                "sourceSectionKey": source_section_key,
            }
        )
    return references


def find_matching_details_end(text: str, open_index: int) -> int:
    depth = 0
    seen_open = False
    for match in DETAILS_TOKEN_RE.finditer(text):
        if match.start() < open_index:
            continue
        token = match.group(0).lower()
        if token.startswith("<details"):
            depth += 1
            seen_open = True
        elif seen_open:
            depth -= 1
            if depth == 0:
                return match.end()
    return -1


def get_section_span(text: str, number: int) -> tuple[int, int] | None:
    opener = re.search(rf'<details\b[^>]*\bid="c-is\.{number}\.0"[^>]*>', text, flags=re.IGNORECASE | re.DOTALL)
    if not opener:
        return None
    end = find_matching_details_end(text, opener.start())
    if end < 0:
        return None
    return opener.start(), end


def extract_section(text: str, number: int) -> dict[str, str] | None:
    span = get_section_span(text, number)
    if not span:
        return None
    start, end = span
    block = text[start:end]
    summary_match = re.search(rf'<summary\b[^>]*id="s-is\.{number}\.0"[^>]*>(.*?)</summary>', block, flags=re.IGNORECASE | re.DOTALL)
    div_match = re.search(rf'<div\b[^>]*id="o-is\.{number}\.0"[^>]*>(.*?)</div>\s*</details>', block, flags=re.IGNORECASE | re.DOTALL)
    return {
        "title": strip_ask_ai_shortcodes(strip_html(summary_match.group(1) if summary_match else "")),
        "inner_html": (div_match.group(1) if div_match else "").strip(),
    }


def split_ul_block(value: str) -> dict[str, str] | None:
    opener = re.search(r"<ul\b[^>]*>", value, flags=re.IGNORECASE)
    if not opener:
        return None
    start = opener.start()
    open_end = opener.end()
    depth = 0
    close_start = -1
    close_end = -1
    for match in re.finditer(r"<ul\b[^>]*>|</ul>", value, flags=re.IGNORECASE):
        if match.start() < start:
            continue
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
    return {
        "before": value[:start],
        "inner": value[open_end:close_start],
        "after": value[close_end:],
    }


def extract_top_level_li_blocks(ul_inner: str) -> list[str]:
    blocks: list[str] = []
    li_depth = 0
    ul_depth = 0
    block_start: int | None = None
    for match in re.finditer(r"<li\b[^>]*>|</li>|<ul\b[^>]*>|</ul>", ul_inner, flags=re.IGNORECASE):
        token = match.group(0).lower()
        index = match.start()
        if token.startswith("<ul"):
            ul_depth += 1
            continue
        if token == "</ul>":
            ul_depth -= 1
            continue
        if token.startswith("<li"):
            if li_depth == 0 and ul_depth == 0:
                block_start = index
            li_depth += 1
            continue
        li_depth -= 1
        if li_depth == 0 and ul_depth == 0 and block_start is not None:
            blocks.append(ul_inner[block_start:match.end()].strip())
            block_start = None
    return blocks


def strip_outer_li(block: str) -> str:
    return re.sub(r"^<li\b[^>]*>", "", block, flags=re.IGNORECASE).rstrip().removesuffix("</li>").strip()


def split_treatment_section(section_html: str) -> tuple[str, str]:
    ul_block = split_ul_block(section_html)
    default_prescribing = "<p>No dedicated prescribing reference is included in the source script for this condition.</p>"
    if not ul_block:
        return section_html or "<p>No management-thinking content was imported.</p>", default_prescribing

    li_blocks = extract_top_level_li_blocks(ul_block["inner"])
    prescribing_li = next(
        (
            block
            for block in li_blocks
            if re.search(
                r"<b>\s*(Prescribing reference \(JITL\)|Exam pharmacology reference(?:\s*\(UKMLA/MRCGP\))?)\s*:\s*</b>",
                block,
                flags=re.IGNORECASE,
            )
        ),
        None,
    )
    management_blocks = [block for block in li_blocks if block != prescribing_li]
    management_html = (
        f'{ul_block["before"]}<ul>{"".join(management_blocks)}</ul>{ul_block["after"]}'.strip()
        if management_blocks
        else "<p>No management-thinking content was preserved from the treatment section.</p>"
    )
    if not prescribing_li:
        return management_html, default_prescribing

    prescribing_html = strip_outer_li(prescribing_li)
    prescribing_html = re.sub(
        r"<b>\s*(Prescribing reference \(JITL\)|Exam pharmacology reference(?:\s*\(UKMLA/MRCGP\))?)\s*:\s*</b>",
        "",
        prescribing_html,
        flags=re.IGNORECASE,
    ).strip()
    return management_html, (prescribing_html or default_prescribing)


def combine_clinical_features(symptoms_html: str, signs_html: str) -> str:
    return (
        '<section class="crx-export-clinical-features">'
        "<h3>Symptoms</h3>"
        f"{symptoms_html or '<p>No symptom content was imported.</p>'}"
        "<h3>Signs</h3>"
        f"{signs_html or '<p>No sign content was imported.</p>'}"
        "</section>"
    )


def load_manifest() -> list[dict[str, str]]:
    with MANIFEST_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_tracker_rows() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    lines = TRACKER_PATH.read_text(encoding="utf-8").splitlines()
    for line in lines:
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Condition "):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 11:
            continue
        condition = parts[0]
        rows[normalize_value(condition)] = {
            "condition": condition,
            "category": parts[1],
            "gapTrackerStatus": parts[2],
            "priority": parts[3],
            "phase": parts[4],
            "matchedScripts": parts[5],
            "canonicalFinalTarget": parts[6],
            "currentFinalFileStatus": parts[7],
            "nextAction": parts[8],
            "reviewStatus": parts[9],
            "notes": parts[10],
        }
    return rows


def resolve_manifest_rows(selected_terms: list[str], manifest_rows: list[dict[str, str]], export_all: bool) -> list[dict[str, str]]:
    if export_all:
        return manifest_rows
    selected_keys = {normalize_value(term) for term in selected_terms}
    rows = [row for row in manifest_rows if normalize_value(row["title"]) in selected_keys]
    missing = selected_keys - {normalize_value(row["title"]) for row in rows}
    if missing:
        raise ValueError(f"Could not resolve manifest rows for: {sorted(missing)}")
    return rows


def build_plain_text(value: str) -> str:
    return strip_html(shortcodes_to_text(value))


def dedupe_references(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str, str, str]] = set()
    unique: list[dict[str, str]] = []
    for item in items:
        key = (item["type"], item["query"], item["text"], item["sourceSectionKey"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def extract_title(source_text: str, fallback_title: str) -> str:
    match = re.search(r'<div\s+id="illness-script-title">(.*?)</div>', source_text, flags=re.IGNORECASE | re.DOTALL)
    explicit = strip_ask_ai_shortcodes(strip_html(match.group(1) if match else ""))
    return explicit or fallback_title


def build_export_record(row: dict[str, str], tracker_rows: dict[str, dict[str, str]]) -> dict[str, Any]:
    title = row["title"].strip()
    normalized_title = normalize_value(title)
    tracker = tracker_rows.get(normalized_title, {})
    html_path = FINAL_DIR / row["canonical_file"]
    if not html_path.exists():
        raise FileNotFoundError(f"Canonical HTML file not found: {html_path}")

    source_text = html_path.read_text(encoding="utf-8")
    extracted_title = extract_title(source_text, title)
    slug = slugify(extracted_title)

    sections_by_number: dict[int, dict[str, str]] = {}
    for section_number in range(1, 14):
        extracted = extract_section(source_text, section_number)
        if extracted:
            sections_by_number[section_number] = extracted

    symptoms_html = strip_ask_ai_shortcodes(ensure_supported_shortcodes(sections_by_number.get(5, {}).get("inner_html", ""), extracted_title, html_path))
    signs_html = strip_ask_ai_shortcodes(ensure_supported_shortcodes(sections_by_number.get(6, {}).get("inner_html", ""), extracted_title, html_path))
    treatment_html = strip_ask_ai_shortcodes(ensure_supported_shortcodes(sections_by_number.get(12, {}).get("inner_html", ""), extracted_title, html_path))
    management_html, prescribing_html = split_treatment_section(treatment_html)

    section_records: list[dict[str, Any]] = []
    all_references: list[dict[str, str]] = []

    for order, definition in enumerate(SECTION_DEFINITIONS, start=1):
        if definition["key"] == "clinical-features":
            raw_html = combine_clinical_features(symptoms_html, signs_html)
        elif definition["key"] == "management-thinking":
            raw_html = management_html
        elif definition["key"] == "prescribing":
            raw_html = prescribing_html
        else:
            source_number = definition["source_numbers"][0]
            raw_html = sections_by_number.get(source_number, {}).get("inner_html", "")
            raw_html = strip_ask_ai_shortcodes(ensure_supported_shortcodes(raw_html, extracted_title, html_path))

        if not raw_html:
            raw_html = f"<p>No {definition['title'].lower()} content was imported for this condition.</p>"

        section_references = collect_jitl_references(raw_html, definition["key"])
        all_references.extend(section_references)

        section_records.append(
            {
                "id": definition["key"],
                "key": definition["key"],
                "title": definition["title"],
                "order": order,
                "sourceSectionIds": definition["source_ids"],
                "rawHtml": raw_html,
                "plainText": build_plain_text(raw_html),
                "jitlReferences": section_references,
                "deepDiveAnchor": definition["anchor"],
            }
        )

    overview_section = next(section for section in section_records if section["key"] == "overview")
    clinical_features_section = next(section for section in section_records if section["key"] == "clinical-features")
    red_flags_section = next(section for section in section_records if section["key"] == "red-flags")

    post_id = row.get("post_id", "").strip() or None
    published = row.get("published", "").strip().lower()
    legacy_wordpress_status = {
        "yes": "published",
        "pending-transfer": "pending-transfer",
    }.get(published, "not-published")

    knowledge_base_url = f"https://kb.clinicalreasoning.io/topic/{slug}"
    specialty = SPECIALTY_BY_CATEGORY.get(row["ukmla_categories"], "General Medicine")
    accent_theme = ACCENT_THEME_BY_CATEGORY.get(row["ukmla_categories"], "slate")
    unique_references = dedupe_references(all_references)

    return {
        "schemaVersion": SCHEMA_VERSION,
        "exportedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
        "conditionId": f"ukmla-{slug}",
        "slug": slug,
        "title": extracted_title,
        "subtitle": f"{row['ukmla_categories']} UKMLA condition master export",
        "conditionType": "condition",
        "ukmla": {
            "conditionLabel": title,
            "category": row["ukmla_categories"],
            "gapTrackerStatus": tracker.get("gapTrackerStatus", ""),
            "priority": tracker.get("priority", ""),
            "phase": tracker.get("phase", ""),
        },
        "source": {
            "repo": "info-clinical-reasoning",
            "htmlFile": f"updated-illness-scripts-2026-final/{html_path.name}",
            "canonicalFile": html_path.name,
            "legacyPostId": post_id,
            "postIdSource": row.get("post_id_source", "").strip() or None,
        },
        "publication": {
            "legacyWordpressStatus": legacy_wordpress_status,
            "knowledgeBaseStatus": "exported",
            "conditionsProjectionStatus": "not-generated",
            "ddxProjectionStatus": "not-generated",
            "reviewStatus": row.get("review_status", "").strip() or tracker.get("reviewStatus", "not-started"),
        },
        "taxonomy": {
            "specialty": specialty,
            "tags": [
                "UKMLA",
                "illness-script",
                row["ukmla_categories"],
                specialty,
            ]
            + (["prescribing"] if any(ref["type"] == "medication" for ref in unique_references) else []),
        },
        "signals": {
            "clusterResolutionNeeded": tracker.get("nextAction") == "cluster-resolution-first",
            "clinicianPriority": row.get("review_status", "").strip() or tracker.get("reviewStatus", "not-started"),
            "notes": [
                note
                for note in [
                    f"manifest-current-file-status={row.get('current_file_status', '').strip()}",
                    f"tracker-next-action={tracker.get('nextAction', '')}" if tracker.get("nextAction") else "",
                    tracker.get("notes", ""),
                ]
                if note
            ],
        },
        "sections": section_records,
        "jitl": {
            "medications": [ref for ref in unique_references if ref["type"] == "medication"],
            "queries": [ref for ref in unique_references if ref["type"] == "query"],
        },
        "downstreamHints": {
            "knowledgeBase": {
                "canonicalTopicUrl": knowledge_base_url,
            },
            "reasoningCompass": {
                "topicSlug": slug,
                "suggestedAccentTheme": accent_theme,
                "sectionKeys": [section["key"] for section in section_records],
            },
            "ddxExplorer": {
                "knowledgeBaseUrl": knowledge_base_url,
                "summary": first_sentence(overview_section["plainText"]),
                "redFlagSummary": first_sentence(red_flags_section["plainText"]),
                "featureSummary": first_sentence(clinical_features_section["plainText"]),
            },
        },
    }


def write_exports(records: list[dict[str, Any]], export_root: Path) -> None:
    conditions_dir = export_root / "conditions"
    conditions_dir.mkdir(parents=True, exist_ok=True)

    index_payload = []
    for record in records:
        output_path = conditions_dir / f"{record['slug']}.json"
        output_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        index_payload.append(
            {
                "conditionId": record["conditionId"],
                "slug": record["slug"],
                "title": record["title"],
                "category": record["ukmla"]["category"],
                "legacyPostId": record["source"]["legacyPostId"],
                "reviewStatus": record["publication"]["reviewStatus"],
                "knowledgeBaseUrl": record["downstreamHints"]["knowledgeBase"]["canonicalTopicUrl"],
                "file": f"conditions/{record['slug']}.json",
            }
        )

    (export_root / "index.json").write_text(
        json.dumps(
            {
                "schemaVersion": SCHEMA_VERSION,
                "exportedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
                "count": len(index_payload),
                "conditions": index_payload,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export CRx master-condition JSON from canonical illness scripts.")
    parser.add_argument("titles", nargs="*", help="Condition titles to export. Defaults to exemplar set.")
    parser.add_argument("--all", action="store_true", help="Export the full manifest-backed corpus.")
    parser.add_argument(
        "--output-root",
        default=str(DEFAULT_EXPORT_ROOT),
        help="Destination folder for export artifacts.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest_rows = load_manifest()
    tracker_rows = load_tracker_rows()
    selected_titles = args.titles or DEFAULT_EXEMPLARS
    resolved_rows = resolve_manifest_rows(selected_titles, manifest_rows, args.all)
    records = [build_export_record(row, tracker_rows) for row in resolved_rows]
    write_exports(records, Path(args.output_root))
    print(f"Exported {len(records)} master-condition JSON files to {args.output_root}")


if __name__ == "__main__":
    main()
