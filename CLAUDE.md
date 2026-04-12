# Illness Scripts — Project Context

## What this is
Educational illness scripts for **clinicalreasoning.io**, targeting:
- **UKMLA finals** and **MRCGP** candidates
- **Novice clinicians** using scripts at the bedside for diagnostic reasoning

**Critical constraint: This is an educational resource, not a medical device.** All clinical content must be framed educationally — not as clinical instructions. Doses, frequencies, and brand names are never permitted. Drug generic names follow the two-tier rule (see quality rules). Always defer prescribing decisions to local guidelines.

---

## File structure

| Path | Purpose |
|---|---|
| `updated-illness-scripts-2026/` | ~700 live HTML illness script files |
| `modernize_illness_scripts_2026.py` | Deterministic edit pipeline (Pass A: rewrite, Pass B: lint) |
| `modernization_rules_2026.json` | Machine-readable quality rules for the Python pipeline |
| `CONTENT_MODERNIZATION_PLAN_2026.md` | Phase plan and condition priority list |
| `UKMLA_COVERAGE_GAPS_2026.md` | Coverage gap tracker |
| `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_condition_category_mapping.json` | Exact UKMLA condition names and categories |
| `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_gap_tracker_2026.csv` | UKMLA condition status, priority, phase, and matched scripts |

### File naming convention
`is-[system-category]-[condition-slug].html`

Examples: `is-abdominal-pain-appendicitis.html`, `is-respiratory-pneumonia.html`

### UKMLA build workflow
- When building a UKMLA curriculum condition, use the exact condition wording and category from `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_condition_category_mapping.json`.
- Before drafting a new or replacement script, check `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_gap_tracker_2026.csv` for status, priority, phase, and matched legacy scripts.
- Prefer refreshing an existing matched script before creating a new duplicate file for the same UKMLA condition.

---

## HTML template structure

Every illness script uses 13 `<details>` sections with fixed IDs (`c-is.1.0` through `c-is.13.0`). Sections 5, 6, and 7 are `open` by default.

### Shortcode pattern
Shortcodes use a `1xx` numbering prefix (matching WordPress shortcode definitions):
- **Title div**: `[sc name="ask-ai-100" Q="[Condition Name]"][/sc]`
- **Sections 1–12**: `[sc name="ask-ai-1NN" Q="[Condition Name]"][/sc]` where NN is the zero-padded section number — e.g., `ask-ai-101`, `ask-ai-109`, `ask-ai-112`
- **Complications section (13)**: `[sc name="ask-ai-115" Q="[Condition Name]"][/sc]` — always `115`, never `113`
- **Epidemiology section (2)** includes as its **first list item**: `[sc name="1095-jitl-epidemiology-link" Q="[Condition Name]"][/sc]`
- **Medication JITL**: `[sc name="jitl-medication" Q="[Drug] use in [Condition]" text="[drug name]"][/sc]`
- **General JITL**: `[sc name="jitl-query" Q="[Term]: what is it and why does it matter clinically?" text="[term]"][/sc]`

---

## Section map

| ID | Section | Default open? | Notes |
|---|---|---|---|
| c-is.1.0 | Definition | yes | Includes UKMLA learning outcome |
| c-is.2.0 | Epidemiology | no | Quantitative anchors required |
| c-is.3.0 | Pathophysiology | no | 3-bullet: trigger → progression → consequence |
| c-is.4.0 | Time Course | no | Early / Progressive / Late phases |
| c-is.5.0 | Symptoms | yes | "Ask about" format |
| c-is.6.0 | Signs | yes | "Check" format |
| c-is.7.0 | Red Flag Features | yes | Bold flag + specific implication |
| c-is.8.0 | Atypical Presentations | no | Anatomical variants + special populations |
| c-is.9.0 | Diagnostic Tests | no | Core / Extended / Imaging / Serial reassessment |
| c-is.10.0 | Problem Representation | no | Vignette sentence + semantic qualifier summary |
| c-is.11.0 | Differential Diagnosis | no | Each DDx needs a distinguishing feature |
| c-is.12.0 | Treatment | no | Immediate → Definitive → Non-operative → Monitoring → Safety-netting |
| c-is.13.0 | Complications | no | Shortcode uses `[PREFIX]15` |

---

## Quality rules (apply to all sections)

### Language and tone
- **UK English** throughout: faecalith, periumbilical, localised, haemodynamic, ischaemia, laparoscopic, oedema, recognised
- **No imperative clinical instructions**: use "often includes", "may support", "consider", "typically", "often warrants" — never "give", "start", "administer", "prescribe" with clinical specifics
- **Drug naming — two-tier rule**:
  - **Doses, frequencies, and brand names**: never permitted under any circumstances
  - **Drug classes** (β-lactam, macrolide, SSRI, SGLT2 inhibitor, etc.): always allowed anywhere
  - **Generic drug names**: allowed in the **Treatment section only**, inside a clearly labelled **"Prescribing reference (JITL)"** bullet or subsection. Prefer a short nested list of `jitl-medication` links rather than prose-heavy pharmacology paragraphs. If a guideline frame is helpful, keep it to one short introductory sentence before the list. End with: *"No doses or frequencies are cited here — always verify against your local antimicrobial/prescribing formulary before prescribing."* Plain generic drug names appearing outside this subsection, or without `jitl-medication`, must be removed.
- **JITL query use**:
  - Use `[sc name="jitl-query" ...]` only for high-yield non-drug concepts that materially improve reasoning, discrimination, or exam understanding
  - Default limit: maximum **1** `jitl-query` per bullet and **4–6** per script unless an exemplar proves higher density remains readable
  - Prefer sections **3, 6, 8, 9, and 11**; use sparingly in sections **5 and 7**
- **No false precision in timing** — use "particularly beyond 48–72 hours" not "after exactly 72 hours"
- **Consistent timing language** across sections (check Time Course, Red Flags, and Complications all use the same phrasing)

### Section-specific rules

**Definition**: UKMLA learning outcome line should describe what the candidate must *recognise and do*, not duplicate later content.

**Symptoms**: "**Ask about** [symptom] - [why it matters]" format. Include a sequence/discriminator bullet where one exists.

**Signs**: "**Check** [sign] - [what it implies]" format. Peritonism bullets should mention movement/coughing. Always include a vitals bullet.

**Red flags**: Bold the flag name. Each flag needs a specific "so what" — not generic "seek urgent review".

**Diagnostic tests**: Split into:
1. Core for suspected [condition]
2. If an alternative diagnosis is plausible
3. Imaging — one bullet per modality with indication and limitation
4. Serial reassessment — framed as urgent care/inpatient context
If a validated score matters clinically, mention it briefly in section 9 only and link to an external tool such as MDCalc. Do not create a dedicated scoring section or reproduce full score components.

**Differential diagnosis**: Every entry needs a distinguishing feature — not just a name list. For pelvic/abdominal conditions in females: include ectopic pregnancy and PID.

**Treatment**:
- "Immediate priorities" → recognition + escalation + supportive care (defer to local pathways)
- Separate "Operative/Definitive" and "Non-operative/Conservative" where both are relevant
- Include trial citations where evidence base is well established (e.g., APPAC for appendicitis)
- "start supportive measures" → "supportive care often includes..."
- Include a **"Prescribing reference (JITL)"** bullet when drug knowledge is commonly tested for this condition. Prefer a nested list of `jitl-medication` links rather than inline sentences. If you need context, add a single short introductory sentence above the list with guideline attribution. End the subsection with: *"No doses or frequencies are cited here — always verify against your local antimicrobial/prescribing formulary before prescribing."*

**Complications**: Use timing language consistent with Time Course section. Include mechanism and management approach, not just the complication name.

---

## Python pipeline

- **Pass A** (`modernize_illness_scripts_2026.py`): rewrites list-item content, minimal structural mutation
- **Pass B**: lints structure, epidemiology shortcode, style gates, forbidden prescriptive patterns
- Rules encoded in `modernization_rules_2026.json`
- The pipeline **edits existing scripts** — it does not generate new ones from scratch

For generating new scripts from scratch, use the `/illness-script` skill.
