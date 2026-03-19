# UKMLA Replacement Queue 2026

Status: Active production queue for replacing live legacy scripts with canonical final files and prioritising the next UKMLA builds

Primary execution truth:
- `updated-illness-scripts-2026-final/UKMLA_CONDITION_TRACKER_2026.md`
- This file is the short-term active queue only.

Source files:
- `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_condition_category_mapping.json`
- `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_gap_tracker_2026.csv`

Canonical destination:
- `updated-illness-scripts-2026-final/`

## How to use this file
- Treat this as the operational queue for UKMLA-condition work.
- Replace live site content first where a strong canonical final file already exists.
- Refresh existing matched scripts before creating new files.
- Use legacy and archive files as source material only, not as publishing targets.
- Use the pneumonia final file as the current style anchor for tone, section density, and treatment wording.

## Batch 1: Ready to replace on the live site now
- Pneumonia
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-pneumonia.html`
  - Gap-tracker matched scripts: `is-pneumonia`, `is-hiv-associated-pneumocystis-pneumonia`
  - Decision: replace the live legacy pneumonia page with the canonical final file now
- Pulmonary embolism
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-pulmonary-embolism.html`
  - Gap-tracker matched script: `is-pulmonary-embolism`
  - Decision: replace the live legacy PE page with the canonical final file now
- Deep vein thrombosis
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-deep-vein-thrombosis.html`
  - Gap-tracker matched script: `is-dvt`
  - Decision: replace the live legacy DVT page with the canonical final file now
- Heart failure
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-heart-failure.html`
  - Gap-tracker matched script: `is-heart-failure`
  - Decision: replace the live legacy heart failure page with the canonical final file now
- Asthma
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-asthma.html`
  - Gap-tracker matched script: `is-asthma`
  - Decision: replace the live legacy asthma page with the canonical final file now

## Batch 2: Refresh next from existing matched scripts
- Acute coronary syndromes
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Matched script: `is-acute-coronary-syndrome`
  - Canonical final candidate: `updated-illness-scripts-2026-final/is-acute-coronary-syndromes.html`
  - Reason to prioritise: core UKMLA cardiovascular emergency and only one matched script to refresh
- Pneumothorax
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Matched script: `is-pneumothorax`
  - Canonical final candidate: `updated-illness-scripts-2026-final/is-pneumothorax.html`
  - Repo note: parallel respiratory-named file exists and can now be treated as comparison source rather than the active draft
- Meningitis
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-meningitis.html`
  - Source used: `updated-illness-scripts-2026/is-neurological-meningitis.html` (best source; `is-meningitis.html` legacy was a near-empty template)
  - Repo note: `is-neurological-meningitis.html` treated as comparison source; `is-meningitis.html` legacy treated as legacy only
  - Decision: replace live legacy meningitis page with canonical final file
- Ectopic pregnancy
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-ectopic-pregnancy.html`
  - Source used: `updated-illness-scripts-2026/is-ectopic-pregnancy.html` as legacy reference only (near-empty template); canonical file written from scratch
  - Decision: replace live legacy ectopic pregnancy page with canonical final file
- Chronic obstructive pulmonary disease (COPD)
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-copd.html`
  - Source used: `updated-illness-scripts-2026/is-copd.html` as legacy reference only (near-empty template); canonical file written from scratch
  - Decision: replace live legacy COPD page with canonical final file
- Infective endocarditis
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-infective-endocarditis.html`
  - Source used: `updated-illness-scripts-2026/is-infective-endocarditis.html` as legacy reference only (near-empty template); canonical file written from scratch
  - Decision: replace live legacy IE page with canonical final file
- Aortic aneurysm
  - UKMLA status: `covered-needs-refresh`, `high`, `phase-1-pilot`
  - Canonical final file: `updated-illness-scripts-2026-final/is-aortic-aneurysm.html`
  - Cluster resolution: `is-aortic-aneurysm.html` is canonical (AAA-focused); `is-aortic-aneurysm-rupture-or-dissection.html` and `is-aortic-aneurysm-thoracic.html` treated as legacy; aortic dissection is a separate Batch 3 condition
  - Decision: replace live legacy AAA page with canonical final file

## Batch 3: Create next where UKMLA says missing and high priority

### Batch 3 — Completed
- Aortic dissection
  - UKMLA status: `missing`, `high`, `phase-3-create-priority`
  - Canonical final file: `updated-illness-scripts-2026-final/is-aortic-dissection.html`
  - Written from scratch; no legacy source file
- Acute bronchitis
  - UKMLA status: `missing`, `high`, `phase-3-create-priority`
  - Canonical final file: `updated-illness-scripts-2026-final/is-acute-bronchitis.html`
  - Legacy: `updated-illness-scripts-2026/is-bronchitis.html` used as comparison only (near-empty template)
- Empyema
  - UKMLA status: `missing`, `high`, `phase-3-create-priority`
  - Canonical final file: `updated-illness-scripts-2026-final/is-empyema.html`
  - Written from scratch; no legacy source file

### Batch 3 — Completed (continued)
- Adverse drug effects
  - UKMLA status: `missing`, `high`, `phase-3-create-priority`
  - Canonical final file: `updated-illness-scripts-2026-final/is-adverse-drug-effects.html`
  - Written from scratch; Type A/B classification, Yellow Card, Naranjo algorithm, SJS/TEN
  - QA: passed structural validation 2026-03-10
- Arterial thrombosis/ embolism
  - UKMLA status: `missing`, `high`, `phase-3-create-priority`
  - Canonical final file: `updated-illness-scripts-2026-final/is-arterial-thrombosis-embolism.html`
  - Written from scratch; acute limb ischaemia focus, six Ps, embolic vs thrombotic distinction
  - QA: passed structural validation 2026-03-10
- Cardiomyopathy
  - UKMLA status: `missing`, `high`, `phase-3-create-priority`
  - Canonical final file: `updated-illness-scripts-2026-final/is-cardiomyopathy.html`
  - Written from scratch; DCM + HCM (LVOTO, Valsalva murmur, sudden death in athletes), ARVC (epsilon wave)
  - QA: passed structural validation 2026-03-10
- Cerebral venous sinus thrombosis (CVST)
  - UKMLA status: `missing`, `high`, `phase-3-create-priority`
  - Canonical final file: `updated-illness-scripts-2026-final/is-cvst.html`
  - Written from scratch; anticoagulation even with haemorrhage, VITT-associated CVST, empty delta sign
  - QA: passed structural validation 2026-03-10
- Drug overdose
  - UKMLA status: `missing`, `high`, `phase-3-create-priority`
  - Canonical final file: `updated-illness-scripts-2026-final/is-drug-overdose.html`
  - Written from scratch; paracetamol (NAC, Rumack-Matthew), opioid (naloxone), TCA (QRS widening, sodium bicarbonate)
  - QA: passed structural validation 2026-03-10

## Conditions to avoid tackling first
- Abscess
  - Many overlapping subtype scripts; too broad for a clean first-pass canonical file
- ARDS
  - Current matched script appears to be neonatal, so this needs careful remapping before rewrite
- Congenital heart disease
  - Multiple overlapping topics; better handled after the first adult core exemplar set is frozen
- Childhood hip/ leg disorders
  - Composite topic; likely needs a deliberate subtype strategy rather than a quick refresh

## Working rule for each queued condition
- Step 1: confirm exact UKMLA wording and category from the mapping JSON
- Step 2: check the gap tracker row for status, priority, phase, and matched scripts
- Step 3: pick or create one canonical file in `updated-illness-scripts-2026-final/`
- Step 4: use existing archive and legacy scripts as source material only
- Step 5: match the pneumonia standard for:
  - section density
  - no `9a`
  - brief MDCalc-linked scoring mention only in section `9`
  - `jitl-medication` only in the section `12` pharmacology bullet
  - selective `jitl-query`
  - educational rather than protocol-like treatment language

## Current recommendation
- Publish Batch 1 replacements first.
- Then refresh Batch 2 before starting broad new creation.
- Start Batch 3 only after the first 10-12 refreshed exemplars feel stylistically stable.
