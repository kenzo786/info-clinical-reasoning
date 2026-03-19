#!/usr/bin/env python3
"""Generate phased modernization plan document from UKMLA gap tracker CSV."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List


def load_rows(csv_path: Path) -> List[Dict[str, str]]:
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    parser = argparse.ArgumentParser(description="Build phased 2026 modernization markdown plan.")
    parser.add_argument(
        "--gap-tracker",
        default="ukmla-categorized-illness-scripts-2026/ukmla_gap_tracker_2026.csv",
    )
    parser.add_argument(
        "--output-file",
        default="CONTENT_MODERNIZATION_PLAN_2026.md",
    )
    parser.add_argument("--pilot-size", type=int, default=50)
    args = parser.parse_args()

    gap_tracker = Path(args.gap_tracker)
    output_file = Path(args.output_file)

    if not gap_tracker.exists():
        raise FileNotFoundError(f"Gap tracker not found: {gap_tracker}")

    rows = load_rows(gap_tracker)

    covered_high = [
        r for r in rows if r["status"] == "covered-needs-refresh" and r["priority"] == "high"
    ]
    covered_medium = [
        r for r in rows if r["status"] == "covered-needs-refresh" and r["priority"] != "high"
    ]
    missing_high = [r for r in rows if r["status"] == "missing" and r["priority"] == "high"]
    missing_medium = [r for r in rows if r["status"] == "missing" and r["priority"] != "high"]

    covered_high.sort(key=lambda r: r["condition"])
    covered_medium.sort(key=lambda r: r["condition"])
    missing_high.sort(key=lambda r: r["condition"])
    missing_medium.sort(key=lambda r: r["condition"])

    pilot = covered_high[: args.pilot_size]

    category_counts: Dict[str, int] = defaultdict(int)
    for r in pilot:
        cats = [c.strip() for c in r.get("categories", "").split(";") if c.strip()]
        for c in cats:
            category_counts[c] += 1

    lines: List[str] = []
    lines.append("# 2026 Content Modernization Plan")
    lines.append("")
    lines.append(f"- Generated (UTC): {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"- Gap tracker source: `{gap_tracker}`")
    lines.append(f"- Total conditions in tracker: **{len(rows)}**")
    lines.append(f"- Covered-needs-refresh (high): **{len(covered_high)}**")
    lines.append(f"- Covered-needs-refresh (medium): **{len(covered_medium)}**")
    lines.append(f"- Missing (high): **{len(missing_high)}**")
    lines.append(f"- Missing (medium): **{len(missing_medium)}**")
    lines.append("")
    lines.append("## Phase 1 Pilot (Refresh)")
    lines.append("")
    lines.append(
        f"High-priority covered conditions selected for first-pass clinical modernization: **{len(pilot)}**"
    )
    lines.append("")
    for r in pilot:
        lines.append(f"- {r['condition']} ({r.get('categories', '')})")
    lines.append("")
    lines.append("### Pilot Category Mix")
    lines.append("")
    for cat, count in sorted(category_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"- {cat}: {count}")
    lines.append("")
    lines.append("## Phase 2 (Refresh Remaining Covered)")
    lines.append("")
    lines.append(
        f"Remaining covered-needs-refresh conditions after pilot: **{len(covered_high) - len(pilot) + len(covered_medium)}**"
    )
    lines.append("")
    lines.append("## Phase 3 (Create Missing Topics)")
    lines.append("")
    lines.append(f"- Missing high-priority conditions: **{len(missing_high)}**")
    lines.append(f"- Missing medium-priority conditions: **{len(missing_medium)}**")
    lines.append("")
    lines.append("### Missing High-Priority Conditions")
    lines.append("")
    for r in missing_high:
        lines.append(f"- {r['condition']} ({r.get('categories', '')})")
    lines.append("")

    output_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Plan document written: {output_file}")


if __name__ == "__main__":
    main()
