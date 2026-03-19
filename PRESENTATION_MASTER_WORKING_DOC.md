# Presentation Master Working Doc

Status: Active working document for UKMLA presentation-folder build

Source of truth date: `2026-03-18`

Primary target format: `C:\Users\amjid\GitHub\drx-references\presentations`

Primary governance analogue: `C:\Users\amjid\GitHub\Illness scripts\ILLNESS_SCRIPT_MASTER_WORKING_DOC.md`

## Purpose
- This document is the build brief for creating a new UKMLA presentation folder in the same simplified format as `drx-references/presentations`.
- It is designed to be passed directly to another LLM such as Manus.
- It translates the illness-script governance rules into presentation-specific rules.
- It standardises output so the next 100+ presentation files do not drift in structure, tone, evidence quality, or file naming.

## Important Scope Clarification
- The repo gap analysis at `C:\Users\amjid\GitHub\drx-references\docs\UKMLA_DRx_Gap_Analysis.md` states that UKMLA Domain 5 contains `220` total presentations.
- The same document states that `136` are in-scope clinical presentations for the current DRx model and `84` are out of scope because they are procedural, obstetric, safeguarding, administrative, or otherwise not a good fit for a symptom-presentation DDx format.
- As of `2026-03-18`, the `drx-references/presentations` folder contains `91` `.html` files. Do not rely on the older README wording that refers to `72` published topics.
- Manus must not silently blur these counts.
- Working rule:
  - Build tracker universe: all `220` UKMLA Domain 5 presentations.
  - Auto-build folder files only for items that genuinely fit this presentation-DDx format.
  - For items that do not fit the format, mark them explicitly as `out-of-scope-for-presentation-folder` or `needs-owner-decision`.
  - Do not force procedural or administrative topics into fake symptom-DDx files just to inflate completion numbers.

## Current Decisions
### Locked decisions
- Source policy: UK-primary for clinical framing.
- Output style: simplified DRx presentation file, not full 11-section canonical source HTML.
- Audience priority: UKMLA learners, finals revision, early postgraduate learners, novice clinicians learning diagnostic reasoning.
- Educational priority: structured diagnostic reasoning, not management pathway writing.
- Folder style to mimic: the simplified exported format in `drx-references/presentations`, not the larger `drx-references/source` schema.
- Every new file must include:
  - triage DDx list
  - history section
  - examination section
  - red flags section
  - investigations section
  - evidence-based diagnosis section
  - other differential diagnoses section
  - references section
- Use UK English throughout.
- Maintain one canonical file per presentation title in the new folder.
- File naming must follow the visual pattern used in the current folder:
  - `0 {Presentation Title} DRx Full.html`

### Do not change without review
- Do not convert this build into full `kb-accordion` 11-section canonical source pages unless explicitly asked.
- Do not omit the bottom `<references>` block, even if some legacy files did.
- Do not copy formatting glitches, minified one-line blocks, broken encoding, or malformed tag structure from low-quality legacy files.
- Do not use non-UK guidance as the main authority for general clinical framing.
- Do not let sections drift into treatment algorithms, prescribing steps, or ward protocols.
- Do not invent evidence numbers where no trustworthy source supports them.
- Do not duplicate the same diagnosis across `Common causes`, `Must not miss!`, and `Easily missed` unless the distinction is explicit and materially different.
- Do not create duplicate active files with near-identical presentation names.

## Target Artifact
### This build is for the simplified presentation folder
- The output file is not a full article page.
- It is a concise educational block that starts with a `DDx list` heading and then moves into HTML fragments.
- It should resemble files such as:
  - `C:\Users\amjid\GitHub\drx-references\presentations\0 Acute Kidney Injury DRx Full.html`
  - `C:\Users\amjid\GitHub\drx-references\presentations\0 Amenorrhoea DRx Full.html`
  - `C:\Users\amjid\GitHub\drx-references\presentations\0 Chest Pain DRx Full.html`

### This build is not for the full canonical source pages
- The full canonical source pages live in `C:\Users\amjid\GitHub\drx-references\source`.
- Those files use the 11-section `kb-accordion` schema described in `C:\Users\amjid\GitHub\drx-references\README.md`.
- They are useful source material, but they are not the target output format for this project.

## Preferred Source Hierarchy
### Primary sources for clinical framing
- `NICE`
- `NICE CKS`
- `BNF` when drug context matters
- `GPnotebook`
- `NHS`
- UK Royal College guidance where relevant

### Secondary sources
- `BMJ Best Practice` for structure, wording checks, and cross-checking, but not as sole primary authority
- High-quality systematic reviews or major diagnostic studies for EBD when UK-specific evidence is not available

### Repo source material
- Existing simplified exemplars:
  - `C:\Users\amjid\GitHub\drx-references\presentations`
- Canonical full DRx source pages:
  - `C:\Users\amjid\GitHub\drx-references\source`
- Build guidance:
  - `C:\Users\amjid\GitHub\drx-references\README.md`
  - `C:\Users\amjid\GitHub\drx-references\templates\drx_generation_prompt.md`
- Coverage inventory:
  - `C:\Users\amjid\GitHub\drx-references\docs\UKMLA_DRx_Gap_Analysis.md`

## Exemplar Files
### Positive anchors
- `C:\Users\amjid\GitHub\drx-references\presentations\0 Acute Kidney Injury DRx Full.html`
  - Good overall section shape and solid educational flow.
- `C:\Users\amjid\GitHub\drx-references\presentations\0 Amenorrhoea DRx Full.html`
  - Good specialty-specific adaptation.
- `C:\Users\amjid\GitHub\drx-references\presentations\0 Chest Pain DRx Full.html`
  - Broad, high-stakes presentation with a rich DDx range.

### Anti-examples to avoid copying
- `C:\Users\amjid\GitHub\drx-references\presentations\0 Dyspnoea DRx Full.html`
  - Compressed/minified formatting, inconsistent list style, reduced readability.
- `C:\Users\amjid\GitHub\drx-references\presentations\0 Weight Gain DRx Full.html`
  - Inconsistent top-list bulleting, spelling issues, and category drift.
- `C:\Users\amjid\GitHub\drx-references\presentations\0 Lower Abdominal Pain DRx Full.html`
  - Corrupted/unusable file. Treat as invalid source material.

## House Style
### Overall voice
- Clear, concise, educational, and diagnostic-reasoning focused.
- Written for a learner who needs help discriminating between important diagnoses.
- Avoid florid prose.
- Avoid textbook filler.
- Avoid protocol language such as "admit immediately and start X" unless the purpose is explicitly to explain why a red flag matters.

### What each file should help the learner do
- Recognise the broad diagnostic frame of a presentation.
- Separate common, dangerous, and easily missed causes.
- Ask better history questions.
- Perform a targeted exam.
- Recognise red flags quickly.
- Choose initial investigations sensibly.
- Understand which findings meaningfully shift probability.

### Tone rules
- Use UK English: `haematuria`, `oesophageal`, `anaemia`, `paediatric`.
- Prefer short paragraphs and short bullets.
- Summaries should be clinically meaningful, not generic.
- Every item should answer one of these:
  - what is being asked/looked for
  - why it matters diagnostically
  - how it shifts the differential

## Exact Output Shape
### Mandatory top block
- Start every file with:

```text
DDx list
*Common causes
Diagnosis 1
Diagnosis 2
...
*Must not miss!
Diagnosis 1
Diagnosis 2
...
*Easily missed
Diagnosis 1
Diagnosis 2
...
```

### Rules for the top block
- Use plain lines, not HTML, for the triage DDx block.
- Do not use `-` bullets in this block.
- Do not use `*` before each diagnosis.
- One diagnosis per line.
- Use title case or standard disease naming consistently.
- Typical counts:
  - `Common causes`: `5-8`
  - `Must not miss!`: `6-10`
  - `Easily missed`: `3-6`

### Mandatory HTML blocks after the DDx list
1. `<div class="ddx-history">`
2. `<div class="ddx-exam">`
3. `<div class="ddx-rfx">`
4. `<div class="ddx-investigations">`
5. `<div class="ddx-ebd">`
6. `<details class="other-ddx-conditions">`
7. `<references>`

### Mandatory shortcode end markers
- History must include:
  - `[sc name="ddx-hx-opening-question"][/sc]`
  - `[sc name="ddx-hx-end"][/sc]`
- Examination must end with:
  - `[sc name="ddx-ex-end"][/sc]`
- Red flags must end with:
  - `[sc name="ddx-rfx-end"][/sc]`
- Investigations must end with:
  - `[sc name="ddx-ix-end"][/sc]`
- EBD must end with:
  - `[sc name="ddx-ebd-end"][/sc]`

## Section-by-Section Rules
### 1. History
- Opening title format:
  - `History taking for {Presentation} presentation`
- Use `8-11` `<details class="symptoms-details">` blocks.
- End with an ICE block or clearly labelled ICE item.
- Summaries should be natural and presentation-specific, not generic placeholders like `Question`.
- Each item should usually contain:
  - one content bullet describing what to ask
  - one `<strong>Relevance:</strong>` bullet

### 2. Examination
- Opening title format:
  - `Examination for {Presentation}`
- Use `5-8` `<details class="signs-details">` blocks.
- Focus on targeted clinical examination, not full clerking.
- Each item should explain diagnostic relevance, not just list body systems.

### 3. Red Flags
- Opening title format:
  - `Red Flags for {Presentation}`
- Use `5-8` `<details class="rfx-details">` blocks.
- Every red flag must describe:
  - the feature
  - why it is dangerous
  - what diagnosis cluster it raises
- Keep significance focused on urgency and diagnostic consequences, not management steps.

### 4. Investigations
- Opening title format:
  - `Investigations for {Presentation}`
- Use `6-9` `<details class="investigations-details">` blocks.
- Investigations should reflect realistic first-line diagnostic reasoning.
- Each item should contain:
  - what the test is for
  - `<strong>Result Significance:</strong>` explaining how results alter the differential

### 5. Evidence-Based Diagnosis
- Opening title format:
  - `Evidence-Based Diagnosis for {Presentation}`
- Use `3-6` `<details class="ebd-details">` blocks.
- Prioritise high-yield findings, validated rules, or key tests that actually shift probability.
- Each item should contain:
  - a concise description of the finding or tool
  - `<strong>Evidence:</strong>`
  - `<strong>Reference:</strong>`
  - `<strong>Significance:</strong>`
- If precise sensitivity/specificity data are not trustworthy, say so honestly rather than fabricating numbers.
- International diagnostic studies are allowed here when needed, but the overall file must still be UK-framed.

### 6. Other Differential Diagnoses to consider
- Always include this block.
- Use `5-10` additional diagnoses.
- Each item should be one concise sentence with distinguishing features.
- This is for breadth without overloading the top triage DDx block.

### 7. References
- Always include a bottom `<references>` block.
- Every source cited in EBD should appear in the references list.
- Preferred size:
  - `3-8` references
- Use numbered references consistently, for example `[1]`, `[2]`, `[3]`.
- If EBD items include inline numbered citations, the bottom block must match them.

## Canonical Template
Use this exact skeleton and adapt only the presentation-specific content.

```html
DDx list
*Common causes
Diagnosis 1
Diagnosis 2
Diagnosis 3
*Must not miss!
Diagnosis 1
Diagnosis 2
Diagnosis 3
*Easily missed
Diagnosis 1
Diagnosis 2
Diagnosis 3

<div class="ddx-history">
    <div class="ddx-title history">History taking for {Presentation} presentation</div>
    [sc name="ddx-hx-opening-question"][/sc]
    <details class="symptoms-details">
        <summary class="symptoms-summary"><b>{History domain}</b>: {Natural question}</summary>
        <div class="symptoms-div">
            <ul>
                <li>{What to ask and why}</li>
                <li><b>Relevance:</b> {Why it matters diagnostically}</li>
            </ul>
        </div>
    </details>
    <!-- Repeat for remaining history blocks -->
    <details class="symptoms-details">
        <summary class="symptoms-summary"><b>Ideas, Concerns, and Expectations (ICE)</b></summary>
        <div class="symptoms-div">
            <ul>
                <li>{ICE explanation}</li>
                <li><b>Relevance:</b> {Why ICE matters in this presentation}</li>
            </ul>
        </div>
    </details>
    [sc name="ddx-hx-end"][/sc]
</div>

<div class="ddx-exam">
    <div class="ddx-title exam">Examination for {Presentation}</div>
    <details class="signs-details">
        <summary class="signs-summary"><b>{Exam area}</b>: {What to examine}</summary>
        <div class="signs-div">
            <ul>
                <li>{Finding focus}</li>
                <li><b>Relevance:</b> {Why it matters diagnostically}</li>
            </ul>
        </div>
    </details>
    <!-- Repeat -->
    [sc name="ddx-ex-end"][/sc]
</div>

<div class="ddx-rfx">
    <div class="ddx-title rfx">Red Flags for {Presentation}</div>
    <details class="rfx-details">
        <summary class="rfx-summary"><b>{Red flag}</b></summary>
        <div class="rfx-div">
            <ul>
                <li>{What the feature is}</li>
                <li><b>Significance:</b> {Why it is dangerous or changes the diagnostic frame}</li>
            </ul>
        </div>
    </details>
    <!-- Repeat -->
    [sc name="ddx-rfx-end"][/sc]
</div>

<div class="ddx-investigations">
    <div class="ddx-title investigations">Investigations for {Presentation}</div>
    <details class="investigations-details">
        <summary class="investigations-summary"><b>{Investigation}</b></summary>
        <div class="investigations-div">
            <ul>
                <li>{Why the test is used}</li>
                <li><b>Result Significance:</b> {How positive or negative results shift the differential}</li>
            </ul>
        </div>
    </details>
    <!-- Repeat -->
    [sc name="ddx-ix-end"][/sc]
</div>

<div class="ddx-ebd">
    <div class="ddx-title ebd">Evidence-Based Diagnosis for {Presentation}</div>
    <details class="ebd-details">
        <summary class="ebd-summary"><b>{Finding or diagnostic tool}</b></summary>
        <div class="ebd-div">
            <ul>
                <li>{Brief description}</li>
                <li><b>Evidence:</b> {Sensitivity/specificity/LR or honest evidence description}</li>
                <li><b>Reference:</b> {Citation} [1]</li>
                <li><b>Significance:</b> {Interpretation}</li>
            </ul>
        </div>
    </details>
    <!-- Repeat -->
    [sc name="ddx-ebd-end"][/sc]
</div>

<details class="other-ddx-conditions">
    <summary class="symptoms-summary">Other Differential Diagnoses to consider</summary>
    <div class="other-ddx-div">
        <ul>
            <li><b>{Diagnosis}</b>: {Short distinguishing sentence}</li>
            <!-- Repeat -->
        </ul>
    </div>
</details>

<references>
    <div class="ddx-title references">References</div>
    <ul>
        <li>[1] {Reference 1}</li>
        <li>[2] {Reference 2}</li>
        <li>[3] {Reference 3}</li>
    </ul>
</references>
```

## File Naming and Mapping Rules
### Canonical filename rule
- Use one canonical file per presentation.
- Filename pattern:
  - `0 {Display Title} DRx Full.html`

### Display title rule
- Start from the exact UKMLA wording.
- If the official wording is too awkward for a human-readable filename, create a clean display title but record the exact official wording in a tracker.
- Do not create multiple synonymous files such as:
  - `0 Scrotal Pain DRx Full.html`
  - `0 Testicular Pain DRx Full.html`
  - `0 Scrotal and Testicular Pain DRx Full.html`
- Choose one canonical display title and map the official wording to it.

### Tracker requirement
- Maintain a tracker with these fields:
  - official UKMLA presentation wording
  - display title
  - filename
  - category/system
  - status
  - source files used
  - notes
- Suggested statuses:
  - `existing-good`
  - `refresh-existing`
  - `new-build`
  - `covered-within-broader-topic`
  - `out-of-scope-for-presentation-folder`
  - `needs-owner-decision`

## Workflow
### Per-presentation workflow
1. Confirm the exact UKMLA presentation wording from the gap-analysis document or owner-supplied list.
2. Check whether a related file already exists in `drx-references/presentations`.
3. Check whether richer source material exists in `drx-references/source`.
4. Decide the single canonical display title and filename.
5. Draft or refresh the simplified presentation file in the exact house style above.
6. Verify section completeness, HTML integrity, evidence honesty, and UK English.
7. Update the tracker.

### Refresh-vs-create rule
- If a strong related presentation file already exists, refresh it instead of creating a duplicate.
- If the current file is corrupted, malformed, or too inconsistent to salvage, rebuild it cleanly.
- If a UKMLA presentation is only partially covered inside a broader topic, record that explicitly before deciding whether to create a dedicated standalone file.

## Quality Gates
### Every file must pass these checks
- Starts with `DDx list`.
- Contains all three top DDx categories.
- Contains all mandatory HTML blocks.
- Contains all five shortcode end markers.
- Contains an ICE item in history.
- Contains an `Other Differential Diagnoses to consider` block.
- Contains a `<references>` block.
- Uses UK English.
- No obvious spelling errors.
- No broken encoding.
- No minified or single-line unreadable output.
- No malformed or missing closing tags.
- No invented evidence numbers.
- No duplicated diagnosis entries across top categories without explicit justification.
- No management drift into guideline/protocol prose.

### Preferred density
- History: `8-11` items
- Exam: `5-8` items
- Red flags: `5-8` items
- Investigations: `6-9` items
- EBD: `3-6` items
- Other DDx: `5-10` items
- References: `3-8` items

## Anti-Drift Rules
- Do not use generic summary labels like `Question` when a clinically meaningful label is possible.
- Do not write empty filler such as `helps narrow the differential` without specifying how.
- Do not write broad lists of investigations without explaining interpretation.
- Do not overuse rare diagnoses in the `Common causes` block.
- Do not put non-dangerous but memorable rare causes into `Must not miss!` unless they are truly high-stakes.
- Do not omit pregnancy-related causes in relevant reproductive presentations.
- Do not omit paediatric-vs-adult context where it meaningfully changes the differential.
- Do not let EBD become a fake precision section full of unsupported statistics.

## Recommended Build Order
Use the repo gap-analysis document as the default sequencing source. If no owner override is given, prioritise:
- high-frequency, high-stakes core presentations first
- presentations already partially covered but lacking a strong standalone file
- systems where multiple related files can be standardised together

## Manus Prompt Wrapper
If passing this to Manus, give these instructions first:

```text
Use `C:\Users\amjid\GitHub\Illness scripts\PRESENTATION_MASTER_WORKING_DOC.md` as the governing brief.

Target output: simplified DRx presentation files in the same format as `C:\Users\amjid\GitHub\drx-references\presentations`.

Do not build the full 11-section canonical `source/` articles unless explicitly asked.

Before writing each file:
1. Confirm the exact UKMLA presentation wording.
2. Check for an existing related presentation file.
3. Choose one canonical filename.
4. Follow the master doc template exactly.
5. Update the tracker status.

Do not create duplicates.
Do not omit references.
Do not invent evidence.
Do not copy formatting glitches from bad legacy files.
```

## Bottom Line
- The goal is not just more files.
- The goal is a clean, scalable, canonical UKMLA presentation folder with a stable house style.
- Manus should treat this document as the production contract.
