# One-File Refactor System Plan (Operational, Deterministic)

## 1) Scope and Non-Negotiables
1. Process exactly one illness-script file per turn.
2. Never batch edit, never batch output, never propose bulk rewrites.
3. Source folder: `C:\Users\amjid\GitHub\Illness scripts\extracted-illness-scripts-2026`.
4. Destination folder: `C:\Users\amjid\GitHub\Illness scripts\updated-illness-scripts-2026`.
5. Workflow per file: copy source -> create/update destination copy -> refine destination only -> return output for that single file only.
6. Scaffold lock: do not change IDs, `<details>`, `<summary>`, `<div>`, `<ul>`, ordering, or shortcodes.
7. Edit scope: edit `<li>` text only; add/remove `<li>` only where hard contracts explicitly permit.
8. Quality target: Appendicitis gold-standard style (~9–9.5/10), UK-general, conservative, no invented stats/thresholds/citations.
9. `<div id="illness-script-title">` must remain and contain only the condition name.

## 2) Deterministic Queue and File Selection
1. Queue source each turn is computed from real directory listings in this environment.
2. Pending set each turn: all `is-*.html` in source minus filenames already present in destination.
3. Selection rules:
1. If input is an explicit slug, process that slug only.
2. If input is `next`, process the first slug in sorted pending set.
3. If no slug is given and no `STOP` is given, default behaviour is `next`.
4. If real directory listing is unavailable in a future turn, do not guess next slug; require explicit slug or user-provided ordered slug list.

### 2.4) Input format
Accepted inputs (whitespace-separated tokens):

next

STOP

slug=is-xxxx.html

mode=html|diff|html+audit

Example: slug=is-appendicitis.html mode=diff

If mode omitted, default mode=html.

## 3) CONTINUE / STOP Loop Behaviour
1. CONTINUE mode is default.
2. After a file is completed and returned, next turn automatically continues one-file processing unless user types `STOP`.
3. Input handling on each turn:
1. `STOP` -> stop processing and return progress summary only.
2. explicit slug -> process that slug only.
3. `next` or unspecified continuation -> process next pending slug deterministically.
4. STOP summary must include:
1. last completed slug,
2. next pending slug if listings are available,
3. explicit note that next slug is unavailable if listings cannot be computed.
5. If the user message contains no slug and is not STOP, interpret it as next.

## 4) Output Modes
1. `mode=html` (default): return full corrected HTML for the single file only.
2. `mode=diff`: return only changed `<li>` lines grouped by section ID (`c-is.X.0`) in `BEFORE -> AFTER` format.
3. `mode=html+audit`: return full corrected HTML plus short checklist pass/fail summary only.
4. If mode is omitted, use `mode=html`.

## 5) Hard Contract Enforcement
1. `c-is.1.0` Definition:
1. exactly 2 `<li>`;
2. bullet 2 exactly `UKMLA essentials: item1, item2, item3.`;
3. exactly 3 comma-separated items;
4. <=18 words after `UKMLA essentials:`;
5. condition-specific and non-generic.
2. `c-is.2.0` Epidemiology:
1. first shortcode `<li>` unchanged;
2. no unsourced numeric epidemiology claims;
3. condition-specific risk/missed-group framing.
3. `c-is.5.0` Symptoms:
1. default `<b>Ask about</b>`;
2. use `<b>Consider</b>` only for asymptomatic/screen-detected/incidental/partner-notified contexts.
4. `c-is.6.0` Signs:
1. use `<b>Check</b>` consistently.
5. `c-is.9.0` Diagnostic Tests:
1. exactly 2 `<li>`;
2. exact labels `<b>Baseline and bedside:</b>` and `<b>Targeted and monitoring:</b>`;
3. UK-realistic tests;
4. no vague filler.
6. `c-is.10.0` Problem Representation:
1. exactly 2 `<li>`;
2. bullet 1 = plausible vignette;
3. bullet 2 = clean generalised representation.
7. `c-is.11.0` Differentials:
1. 4–6 `<li>`;
2. each `Condition - discriminator clause.`
8. `c-is.12.0` Treatment:
1. **Option 2 (default minimal contract) is adopted**;
2. do not normalise bullet count unless a hard-contract failure requires correction;
3. refine only offending lines;
4. no dosing, no generic filler, educational framing.
9. Symptoms/signs bullet style: use `-` after the feature name (avoid mixed `:` formatting).

## 6) Internal Pre-Output Checklist (No Fake Claims)
1. Confirm scaffold and shortcodes unchanged.
2. Confirm all relevant hard contracts pass.
3. Remove truncations, garbling, duplicated fragments.
4. Ensure UK spelling and concise high-yield phrasing.
5. Remove or rewrite boilerplate and unsourced numerics.
6. Do not claim counts, lint status, or checks as passed unless actually verified in that turn.
7. Confirm no `<li>` contains multiple section headings (no merged `<b>Immediate priorities:</b><b>Core care:</b>` within one bullet).

## 7) Stopping Rule Per File
1. Iterate edits internally until all contract checks pass and text is clinically safe and scan-friendly.
2. Stop when remaining edits are cosmetic only and no material clarity/accuracy gain is expected.
3. If uncertain, choose conservative UK-general phrasing rather than speculative detail.

## 8) Error Handling
1. If slug not found in source, return a concise error and request valid slug or `next`.
2. If destination copy fails, return concise filesystem error and stop that turn.
3. If clinical precision is uncertain, avoid invention and use neutral, non-numeric phrasing.
4. If a requested change conflicts with scaffold lock, preserve scaffold and provide best compliant edit.
5. If destination file already exists, refine the destination file (do not overwrite from source) unless the user explicitly requests a fresh copy.

## 9) Internal Minimal Change Log (Not Output Unless Asked)
1. Keep per-file internal record: `timestamp | slug | sections_touched | key_contract_fixes | unresolved_conservative_choices`.
2. Do not output this log unless user explicitly asks for audit details.
