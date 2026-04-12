# Illness Script Master Working Doc

Status: Active working document for collaborative editing and platform design

Source of truth: `updated-illness-scripts-2026-final/is-pneumonia.html`

Last updated: `2026-03-18`

## Purpose
- This is the active collaboration workspace for illness-script quality across the platform.
- It combines the current pneumonia exemplar work with the operational decisions needed to scale to hundreds of scripts.
- It is designed so a human, Codex, or another LM can contribute without rereading the whole repo first.

## Current Decisions
### Locked decisions
- Source policy: UK-primary only
- Output style: tight illness-script
- BMJ role: structural and editorial reference only, not a primary authority
- Current exemplar candidate: `updated-illness-scripts-2026-final/is-pneumonia.html`
- Platform priority: illness-script first, guideline second
- Audience priority: UKMLA finals, MRCGP candidates, novice clinicians using scripts for bedside reasoning
- No dedicated scoring section in platform scripts
- Scoring tools, if used, are mentioned briefly in section `9` and linked externally to MDCalc
- Generic drug names in the section `12` prescribing subsection must use `jitl-medication`
- High-yield non-drug concepts may use selective `jitl-query`

### Do not change without review
- Do not let scripts drift into mini-guidelines or ward protocols.
- Do not use non-UK sources as primary authorities for production content.
- Do not move generic drug names outside the section `12` `Prescribing reference (JITL)` subsection.
- Do not reintroduce a dedicated scoring section or inline score-component breakdowns.
- Do not overuse `jitl-query`; maximum one per bullet and usually no more than 4–6 per script.
- Do not optimise for completeness at the expense of scan speed and recognisable illness-script patterning.

## Current Pneumonia Exemplar
### Files
- Current exemplar candidate: `updated-illness-scripts-2026-final/is-pneumonia.html`
- Older comparison version: `updated-illness-scripts-2026/is-respiratory-pneumonia.html`

### Current rating estimate
- Output quality: `8.8-9.1/10`
- Process reliability for scaling: `6-6.5/10`

### Why the rewrite is better than the old file
- Tighter illness-script shape
- Better scan speed for novice users
- Cleaner problem representation and differential section
- Less protocol-like treatment wording overall
- Better aligned with the platform brief of educational reasoning support rather than management instruction

### What still prevents 10/10
- Section 8 still needs slightly sharper atypical-pathogen patterning and clearer explanation of what changes diagnostically.
- Section 9 still risks reading like a compressed investigation note rather than a probability-shifting diagnostic frame.
- Section 12 still contains some management language that can drift toward operational instruction.
- Section 13 still explains complications partly through management consequences rather than mainly through danger pattern and reasoning implications.
- The generation process still relies too much on editorial judgement instead of a structured evidence-pack workflow.
- The exemplar set is not yet fully migrated to the new `MDCalc / jitl-medication / selective jitl-query` contract.

### Exact edit targets
- Section 8:
  - Add one compact atypical-pathogen discriminator bullet.
  - Keep only groups that materially alter recognition or severity judgement.
  - Make each bullet answer: what changes, why diagnosis is missed, what to watch for.
- Section 9:
  - Keep core tests framed around severity assessment and diagnostic uncertainty.
  - Remove dedicated score sections and mention scoring tools only briefly with an external MDCalc link.
  - Ensure each imaging bullet explains when it changes thinking, not just when it is used.
  - Avoid letting the list become a near-complete hospital workup.
- Section 12:
  - Soften any wording that sounds like a treatment pathway.
  - Emphasise what changes management setting rather than what clinicians should do step by step.
  - Keep drug-name detail confined to the pharmacology bullet only, using `jitl-medication` for every generic drug name.
- Section 13:
  - Focus on why the complication matters diagnostically and prognostically.
  - Prefer "signals severe disease / changes expected course" over procedure-heavy wording.
  - Keep timing language matched exactly to section 4 and section 7.
- JITL opportunities:
  - Add selective `jitl-query` links only where they materially improve pattern recognition or exam understanding.

### Recommended next edit
- Keep the inline pneumonia draft synced with the source-of-truth HTML file and use it as the pattern for PE and DVT migration.

## Canonical Exemplar Inventory
### Existing high-priority drafts already present in `updated-illness-scripts-2026`
- Pneumonia:
  - Canonical file: `updated-illness-scripts-2026-final/is-pneumonia.html`
  - Comparison file: `is-respiratory-pneumonia.html`
- Pulmonary embolism:
  - Canonical file: `updated-illness-scripts-2026-final/is-pulmonary-embolism.html`
  - Legacy / comparison file: `updated-illness-scripts-2026/is-pulmonary-embolism.html`
- Deep vein thrombosis:
  - Canonical file: `updated-illness-scripts-2026-final/is-deep-vein-thrombosis.html`
  - Parallel legacy-style file also exists: `updated-illness-scripts-2026/is-dvt.html`
- Heart failure cluster:
  - Canonical file: `updated-illness-scripts-2026-final/is-heart-failure.html`
  - Legacy / comparison file: `updated-illness-scripts-2026/is-heart-failure.html`
- Asthma cluster:
  - Canonical file: `updated-illness-scripts-2026-final/is-asthma.html`
  - Legacy / comparison file: `updated-illness-scripts-2026/is-asthma.html`
- Acute coronary syndromes:
  - Canonical file: `updated-illness-scripts-2026-final/is-acute-coronary-syndromes.html`
  - Legacy / comparison file: `updated-illness-scripts-2026/is-acute-coronary-syndrome.html`
- Pneumothorax cluster:
  - Canonical file: `updated-illness-scripts-2026-final/is-pneumothorax.html`
  - Legacy / comparison files: `updated-illness-scripts-2026/is-pneumothorax.html`, `updated-illness-scripts-2026/is-respiratory-pneumothorax.html`
- Meningitis cluster:
  - Canonical file: `updated-illness-scripts-2026-final/is-meningitis.html`
  - Source used: `updated-illness-scripts-2026/is-neurological-meningitis.html`
  - Legacy / comparison: `updated-illness-scripts-2026/is-meningitis.html` (near-empty template, legacy only)
- Aortic aneurysm cluster:
  - Canonical file: `updated-illness-scripts-2026-final/is-aortic-aneurysm.html` (AAA-focused)
  - Legacy / comparison: `updated-illness-scripts-2026/is-aortic-aneurysm.html`, `is-aortic-aneurysm-rupture-or-dissection.html`, `is-aortic-aneurysm-thoracic.html`, `is-cardiovascular-aortic-aneurysm.html` (all legacy)
  - Aortic dissection: separate UKMLA condition — Batch 3 create
- Infective endocarditis:
  - Canonical file: `updated-illness-scripts-2026-final/is-infective-endocarditis.html`
  - Legacy / comparison: `updated-illness-scripts-2026/is-infective-endocarditis.html` (near-empty template)
- Ectopic pregnancy:
  - Canonical file: `updated-illness-scripts-2026-final/is-ectopic-pregnancy.html`
  - Legacy / comparison: `updated-illness-scripts-2026/is-ectopic-pregnancy.html` (near-empty template, written from scratch)
- COPD:
  - Canonical file: `updated-illness-scripts-2026-final/is-copd.html`
  - Legacy / comparison: `updated-illness-scripts-2026/is-copd.html` (near-empty template, written from scratch)
  - Related legacy: `updated-illness-scripts-2026/is-copd-severe.html` (separate file, treat as legacy)

### Batch 3 — New UKMLA conditions (written from scratch)
- Aortic dissection:
  - Canonical file: `updated-illness-scripts-2026-final/is-aortic-dissection.html`
  - No legacy source; Stanford A vs B, thrombolysis-in-dissection hazard, false lumen
- Acute bronchitis:
  - Canonical file: `updated-illness-scripts-2026-final/is-acute-bronchitis.html`
  - Legacy reference: `updated-illness-scripts-2026/is-bronchitis.html` (near-empty)
- Empyema:
  - Canonical file: `updated-illness-scripts-2026-final/is-empyema.html`
  - No legacy source; three-stage model, MIST2 trial, Light's criteria
- Adverse drug effects:
  - Canonical file: `updated-illness-scripts-2026-final/is-adverse-drug-effects.html`
  - No legacy source; Type A/B, Yellow Card, Naranjo, SJS/TEN, serotonin syndrome
- Arterial thrombosis/embolism:
  - Canonical file: `updated-illness-scripts-2026-final/is-arterial-thrombosis-embolism.html`
  - No legacy source; acute limb ischaemia, six Ps, embolic vs thrombotic distinction, mesenteric ischaemia
- Cardiomyopathy:
  - Canonical file: `updated-illness-scripts-2026-final/is-cardiomyopathy.html`
  - No legacy source; DCM + HCM (LVOTO, Valsalva, sudden death), ARVC (epsilon wave), cardiac amyloid
- Cerebral venous sinus thrombosis (CVST):
  - Canonical file: `updated-illness-scripts-2026-final/is-cvst.html`
  - No legacy source; anticoagulation even with haemorrhage, VITT-associated CVST, empty delta sign
- Drug overdose:
  - Canonical file: `updated-illness-scripts-2026-final/is-drug-overdose.html`
  - No legacy source; paracetamol (NAC, Rumack-Matthew), opioid (naloxone), TCA (QRS widening, NaHCO3)

### Working rule for canonicalisation
- One condition should have one canonical exemplar file.
- Parallel files should be classified as one of:
  - canonical exemplar
  - comparison source
  - legacy file
  - subtype / separate condition
- Do not keep multiple near-duplicate files in active exemplar circulation once the canonical file is chosen.

### Immediate canonicalisation priorities
- First wave:
  - pneumonia
  - pulmonary embolism
  - deep vein thrombosis
  - heart failure
  - asthma
  - pneumothorax
  - meningitis
- Second wave:
  - aortic aneurysm / AAA cluster

### Current inventory risk
- The repo already contains enough good draft material to support exemplar review now.
- The larger risk is no longer missing drafts; it is duplicate-file drift, mixed naming conventions, and uneven house style across parallel files.

## Agent Workflow
### Locked roles
- `Claude`:
  - Expand coverage quickly.
  - Draft or refresh one UKMLA condition at a time from the mapping JSON and gap tracker CSV.
  - Use legacy and archive scripts only as source material.
  - Write directly to the canonical final target file.
  - Must not create duplicate active files for the same condition.
- `Codex`:
  - Standardise to the pneumonia house style.
  - Remove management drift and excess guideline wording.
  - Enforce no `9a`, MDCalc links only in section `9`, `jitl-medication`, selective `jitl-query`, section density, and canonical naming.
  - Maintain the curriculum tracker, canonical inventory, and queue hygiene.
- `Clinician reviewer`:
  - Final fact and safety review only.
  - Confirm guideline alignment, omissions, and risky overstatement.
  - Approve publish / hold / revise.
- `Human owner`:
  - Chooses live publish order.
  - Decides when a file is good enough to replace the legacy site version.

### Per-condition workflow
1. Confirm exact UKMLA condition wording and category from the mapping JSON.
2. Check the gap tracker row and any matched scripts.
3. Decide the single canonical final filename.
4. Claude drafts or refreshes the canonical final file.
5. Codex standardises the file and removes duplicate-file drift.
6. Clinician reviewer performs final content and safety review.
7. Update tracker status and, if approved, promote the file for live replacement.

### Stop rules
- Stop creating new conditions if house-style consistency drops below the pneumonia anchor.
- Stop and resolve duplicate or overlapping files before continuing a condition cluster.
- Do not let Claude free-expand the final folder without Codex review.

## UKMLA Build Inputs
### Curriculum source files
- Condition map:
  - `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_condition_category_mapping.json`
- Gap tracker:
  - `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_gap_tracker_2026.csv`

### Working rules for UKMLA curriculum build
- Use the exact UKMLA condition wording from the mapping JSON when selecting or naming a curriculum build target.
- Use the category in the mapping JSON to decide the system grouping and canonical filename pattern.
- Use the gap tracker CSV to decide whether the target is:
  - covered-needs-refresh
  - missing
  - phase-1 pilot
  - phase-2 refresh
  - phase-3 create
- If a UKMLA condition already has matched scripts in the gap tracker, refresh the best candidate first before creating a new file.
- Prefer high-priority and phase-1 or phase-3-priority conditions before medium-priority backlog work.

### Current operational interpretation
- The gap tracker is now the build queue for the remaining UKMLA curriculum.
- The final folder is the canonical destination for signed-off replacements.
- Legacy and archive files are source material, not publishing targets.
- `updated-illness-scripts-2026-final/UKMLA_CONDITION_TRACKER_2026.md` is the full curriculum source of execution truth.
- `UKMLA_REPLACEMENT_QUEUE_2026.md` is the short-term active queue only.

### Current pneumonia draft
```html
<div id="illness-script-title">Pneumonia  [sc name="ask-ai-100" Q="Pneumonia"][/sc]</div>

<details id="c-is.1.0" class="kb-accordion kb-parent" open>
    <summary id="s-is.1.0">Definition [sc name="ask-ai-101" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.1.0" class="kb-child-div">
        <ul>
            <li>Pneumonia is acute infection of the lung parenchyma in which alveolar inflammation and exudate produce consolidation, impaired gas exchange, and systemic illness; this script focuses on adult community-acquired pneumonia (CAP).</li>
            <li><b>UKMLA learning outcome:</b> Recognise the illness script of adult CAP, use CRB-65 in primary care and CURB-65 in hospital alongside clinical judgement, identify patients needing admission or escalation, and distinguish pneumonia from important mimics such as pulmonary embolism and acute heart failure.</li>
        </ul>
    </div>
</details>

<details id="c-is.2.0" class="kb-accordion kb-parent">
    <summary id="s-is.2.0">Epidemiology [sc name="ask-ai-102" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.2.0" class="kb-child-div">
        <ul>
            <li>[sc name="1095-jitl-epidemiology-link" Q="Pneumonia"][/sc]</li>
            <li>NICE NG250 states that community-acquired pneumonia affects around 5 to 10 per 1,000 adults each year in the UK, accounts for 5% to 12% of lower respiratory tract infections managed in primary care, and leads to hospital care in about 22% to 42% of cases; 30-day mortality is about 5% to 15% in hospitalised CAP and rises further in critical care.</li>
            <li>Risk rises with older age, frailty, smoking, COPD, heart failure, diabetes, chronic kidney or liver disease, alcohol dependence, aspiration risk, and immunosuppression; pregnancy, frailty, and major comorbidity may also make severity scores less reliable and can lower the threshold for admission.</li>
        </ul>
    </div>
</details>

<details id="c-is.3.0" class="kb-accordion kb-parent">
    <summary id="s-is.3.0">Pathophysiology [sc name="ask-ai-103" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.3.0" class="kb-child-div">
        <ul>
            <li>Inhaled or aspirated organisms overcome upper airway, mucociliary, and alveolar macrophage defences, allowing infection to establish in the distal airways and alveoli.</li>
            <li>Alveolar inflammation then produces oedema and exudate, causing consolidation and [sc name="jitl-query" Q="Ventilation-perfusion mismatch: what is it and why does it matter clinically?" text="ventilation-perfusion mismatch"][/sc]; this drives cough, pleuritic pain, dyspnoea, fever, tachypnoea, and hypoxaemia.</li>
            <li>If unchecked, infection may extend into the pleural space or bloodstream, leading to empyema, sepsis, respiratory failure, and occasionally cavitating or necrotising disease.</li>
        </ul>
    </div>
</details>

<details id="c-is.4.0" class="kb-accordion kb-parent">
    <summary id="s-is.4.0">Time Course [sc name="ask-ai-104" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.4.0" class="kb-child-div">
        <ul>
            <li><b>Early phase:</b> Fever, malaise, cough, and myalgia may develop over hours to a few days; atypical pathogens often produce a more insidious prodrome.</li>
            <li><b>Progressive phase:</b> Productive cough, pleuritic chest pain, dyspnoea, tachypnoea, and focal chest signs usually become clearer over 24-72 hours as consolidation evolves.</li>
            <li><b>Late phase:</b> Failure to improve or complications such as pleural infection, sepsis, or respiratory failure become more likely particularly beyond 48-72 hours, especially in severe or undertreated disease.</li>
        </ul>
    </div>
</details>

<details id="c-is.5.0" class="kb-accordion kb-parent" open>
    <summary id="s-is.5.0">Symptoms [sc name="ask-ai-105" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.5.0" class="kb-child-div">
        <ul>
            <li><b>Ask about</b> cough and sputum character - a new productive cough supports alveolar infection, while foul-smelling sputum raises concern for aspiration or abscess and a persistently dry cough can point towards atypical pathogens.</li>
            <li><b>Ask about</b> pleuritic chest pain - sharp pain worsened by breathing or coughing suggests pleural irritation and makes isolated cardiac chest pain less likely.</li>
            <li><b>Ask about</b> dyspnoea and functional decline - breathlessness at rest, reduced exercise tolerance, or inability to speak comfortably suggests more significant gas-exchange impairment and a higher-risk presentation.</li>
            <li><b>Ask about</b> fever, rigors, sweats, or confusion - systemic upset supports infection, but confusion may be the dominant presenting symptom in older adults even when fever or cough is modest.</li>
            <li><b>Ask about</b> the onset pattern and associated features - abrupt fever with pleuritic pain and productive cough fits typical bacterial CAP, whereas a slower onset with headache, myalgia, diarrhoea, or dry cough is more in keeping with atypical infection.</li>
        </ul>
    </div>
</details>

<details id="c-is.6.0" class="kb-accordion kb-parent" open>
    <summary id="s-is.6.0">Signs [sc name="ask-ai-106" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.6.0" class="kb-child-div">
        <ul>
            <li><b>Check</b> for focal consolidation signs - bronchial breathing, dullness to percussion, increased vocal resonance, or localised crackles make alveolar consolidation more likely and help localise the process.</li>
            <li><b>Check</b> work of breathing and oxygen saturation - tachypnoea, accessory muscle use, and hypoxia indicate clinically important respiratory compromise and weigh more heavily than the chest examination alone.</li>
            <li><b>Check</b> for pleural involvement - reduced breath sounds with stony dullness suggest parapneumonic effusion rather than uncomplicated lobar consolidation and may indicate a need for pleural imaging or drainage.</li>
            <li><b>Check</b> temperature, pulse, blood pressure, and mental state - fever with tachycardia supports systemic inflammation, while hypotension or new confusion raises concern for sepsis and severe CAP.</li>
        </ul>
    </div>
</details>

<details id="c-is.7.0" class="kb-accordion kb-parent" open>
    <summary id="s-is.7.0">Red Flag Features [sc name="ask-ai-107" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.7.0" class="kb-child-div">
        <ul>
            <li><b>Hypoxia or escalating work of breathing</b> - suggests significant gas-exchange failure and often warrants urgent hospital-level assessment even if the rest of the examination is not dramatic.</li>
            <li><b>New confusion or reduced consciousness</b> - may represent severe infection, delirium, or sepsis; in older adults it can be the main clue to serious pneumonia rather than a late add-on feature.</li>
            <li><b>Haemodynamic compromise</b> - hypotension, poor peripheral perfusion, or persistent tachycardia suggests sepsis physiology and raises the risk of rapid deterioration and multi-organ dysfunction.</li>
            <li><b>Failure to improve particularly beyond 48-72 hours</b> - should prompt reassessment for empyema, abscess, resistant or atypical organisms, pulmonary embolism, or an underlying obstructing lesion.</li>
        </ul>
    </div>
</details>

<details id="c-is.8.0" class="kb-accordion kb-parent">
    <summary id="s-is.8.0">Atypical Presentations [sc name="ask-ai-108" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.8.0" class="kb-child-div">
        <ul>
            <li><b>Lower lobe pneumonia:</b> May present with upper abdominal pain, vomiting, or relatively little cough, creating diagnostic overlap with biliary, gastric, or intra-abdominal pathology.</li>
            <li><b>Atypical-pathogen pattern:</b> Dry cough, headache, myalgia, or diarrhoea with relatively sparse focal chest signs can delay recognition because the illness looks more viral or systemic than lobar.</li>
            <li><b>Pregnancy:</b> Breathlessness is harder to interpret because physiological respiratory changes reduce the usefulness of baseline symptoms, and severity scores may underestimate risk; the threshold for hospital assessment is often lower.</li>
            <li><b>Older adults:</b> Fever, pleuritic pain, and productive cough may be absent or muted; falls, delirium, reduced oral intake, or functional decline may be the presenting pattern and delay diagnosis.</li>
            <li><b>Immunosuppressed patients:</b> Symptoms and inflammatory markers may be blunted despite extensive disease, and the differential broadens to include opportunistic infection and non-bacterial causes, making CT imaging or specialist input more likely.</li>
        </ul>
    </div>
</details>

<details id="c-is.9.0" class="kb-accordion kb-parent">
    <summary id="s-is.9.0">Diagnostic Tests [sc name="ask-ai-109" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.9.0" class="kb-child-div">
        <ul>
            <li><b>Core for suspected pneumonia:</b> Bedside observations including oxygen saturation are essential for severity assessment; FBC, CRP, and U&amp;Es may support the diagnosis and help assess severity, but normal inflammatory markers do not exclude early or atypical pneumonia; in hospital, blood cultures and sputum sampling are most useful in moderate or high-severity disease or when the course is not straightforward.</li>
            <li><b>Severity tools:</b> CRB-65 in primary care and CURB-65 in hospital can support severity stratification, but they should sit alongside clinical judgement rather than replace it; a calculator is available at <a href="https://www.mdcalc.com/calc/324/curb-65-score-pneumonia-severity" target="_blank" rel="noopener noreferrer">CURB-65 on MDCalc</a>.</li>
            <li><b>If an alternative diagnosis is plausible:</b> Consider BNP or echocardiography for acute heart failure, D-dimer followed by CTPA for pulmonary embolism when clinically appropriate, and tuberculosis or viral testing when the history or imaging pattern points away from routine CAP.</li>
            <li><b>Imaging - chest X-ray:</b> First-line hospital imaging that may show lobar or patchy consolidation, pleural effusion, or multilobar disease; a normal film does not exclude very early pneumonia or disease in dehydrated or immunosuppressed patients, so a reassuring X-ray should not outweigh a strong evolving clinical pattern.</li>
            <li><b>Imaging - lung ultrasound:</b> NICE NG250 notes that this can support rapid point-of-care diagnosis in a sick or deteriorating patient and can help identify [sc name="jitl-query" Q="Parapneumonic effusion: what is it and why does it matter clinically?" text="pleural complications"][/sc]; it is operator dependent and complements rather than replaces the wider clinical assessment.</li>
            <li><b>Imaging - CT chest:</b> Consider when chest X-ray is equivocal, the patient is immunosuppressed, complications such as abscess or empyema are suspected, or non-resolving consolidation raises concern for malignancy or another diagnosis.</li>
            <li><b>Serial reassessment:</b> Repeated observations, oxygenation, chest findings, and inflammatory markers over 48-72 hours are most useful in inpatient or closely monitored pathways, where evolving signs can clarify whether the diagnosis and severity assessment still fit.</li>
        </ul>
    </div>
</details>

<details id="c-is.10.0" class="kb-accordion kb-parent">
    <summary id="s-is.10.0">Problem Representation [sc name="ask-ai-110" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.10.0" class="kb-child-div">
        <ul>
            <li>A 72-year-old man presents with 3 days of fever, productive cough, right-sided pleuritic chest pain, and worsening breathlessness, with tachypnoea, hypoxia, and focal right basal crackles with bronchial breathing on assessment.</li>
            <li>Older adult with an acute febrile lower respiratory illness, focal consolidation signs, and systemic upset, concerning for community-acquired pneumonia with possible pleural complication.</li>
        </ul>
    </div>
</details>

<details id="c-is.11.0" class="kb-accordion kb-parent">
    <summary id="s-is.11.0">Differential Diagnosis [sc name="ask-ai-111" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.11.0" class="kb-child-div">
        <ul>
            <li>Pulmonary embolism - may cause pleuritic pain and dyspnoea, but focal infective symptoms and new consolidation signs are usually absent; the history often includes thromboembolic risk factors.</li>
            <li>Acute heart failure - bilateral crackles, orthopnoea, elevated JVP, and peripheral oedema favour cardiogenic pulmonary oedema over a focal infective process.</li>
            <li>COPD exacerbation - wheeze and prolonged expiration dominate, and there may be no focal percussion or auscultatory findings to suggest consolidation.</li>
            <li>Viral lower respiratory tract infection or viral pneumonitis - systemic symptoms may be prominent, but focal lobar signs are often less marked and imaging may show a more diffuse interstitial pattern.</li>
            <li>Pulmonary tuberculosis - usually has a more subacute course with weight loss, night sweats, haemoptysis, and upper-zone disease rather than abrupt pleuritic CAP.</li>
            <li>Lung cancer with [sc name="jitl-query" Q="Post-obstructive change: what is it and why does it matter clinically?" text="post-obstructive change"][/sc] - recurrent or non-resolving consolidation in the same area, haemoptysis, or weight loss should prompt concern for an underlying obstructing lesion.</li>
        </ul>
    </div>
</details>

<details id="c-is.12.0" class="kb-accordion kb-parent">
    <summary id="s-is.12.0">Treatment [sc name="ask-ai-112" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.12.0" class="kb-child-div">
        <ul>
            <li><b>Immediate priorities:</b> Hypoxia, sepsis, haemodynamic instability, or respiratory failure early in the presentation often change the monitoring setting and usually prompt senior review. Supportive care often includes oxygen, fluids, analgesia, and closer observation in line with local acute pathways.</li>
            <li><b>Definitive management:</b> CAP treatment is usually severity-stratified antimicrobial therapy guided by clinical judgement plus CRB-65 or CURB-65, with oral treatment more plausible in lower-severity disease and hospital pathways more likely when severity is higher or oral therapy is not feasible.</li>
            <li><b>Adjunctive management:</b> Pleural infection or persistent deterioration should raise concern for a more complicated course, often changing imaging needs, procedural planning, or senior respiratory review; selected adults in hospital with high-severity CAP may also be considered for adjunctive corticosteroids under current guideline criteria and local policy.</li>
            <li><b>Monitoring and follow-up:</b> Reassess observations, oxygen requirement, mental state, oral intake, and inflammatory markers over 48-72 hours to confirm improvement; NICE NG250 advises that follow-up chest X-ray is not routine after discharge but may be considered at 6 weeks in those with lung cancer risk factors, persistent symptoms, unexplained weight loss, or suspected underlying respiratory disease.</li>
            <li><b>Escalation and safety-netting:</b> Worsening breathlessness, new confusion, haemoptysis, pleuritic pain with enlarging effusion, or failure to improve particularly beyond 48-72 hours should prompt reassessment for empyema, abscess, resistant or atypical infection, pulmonary embolism, or underlying malignancy.</li>
            <li><b>Exam pharmacology reference (UKMLA/MRCGP):</b> NICE NG250 describes [sc name="jitl-medication" Q="Amoxicillin use in Pneumonia" text="amoxicillin"][/sc] as typically first-line for low-severity adult CAP; [sc name="jitl-medication" Q="Doxycycline use in Pneumonia" text="doxycycline"][/sc] or [sc name="jitl-medication" Q="Clarithromycin use in Pneumonia" text="clarithromycin"][/sc] are alternatives when penicillin allergy is documented or atypical pathogens are suspected; moderate-severity CAP often uses [sc name="jitl-medication" Q="Amoxicillin use in Pneumonia" text="amoxicillin"][/sc] with [sc name="jitl-medication" Q="Clarithromycin use in Pneumonia" text="clarithromycin"][/sc], and high-severity CAP often uses [sc name="jitl-medication" Q="Co-amoxiclav use in Pneumonia" text="co-amoxiclav"][/sc] with [sc name="jitl-medication" Q="Clarithromycin use in Pneumonia" text="clarithromycin"][/sc], with [sc name="jitl-medication" Q="Erythromycin use in Pneumonia" text="erythromycin"][/sc] used as the macrolide option in pregnancy. No doses or frequencies are cited here - always verify against your local antimicrobial/prescribing formulary before prescribing.</li>
        </ul>
    </div>
</details>

<details id="c-is.13.0" class="kb-accordion kb-parent">
    <summary id="s-is.13.0">Complications [sc name="ask-ai-115" Q="Pneumonia"][/sc]</summary>
    <div id="o-is.13.0" class="kb-child-div">
        <ul>
            <li><b>Parapneumonic effusion or empyema:</b> Infection can extend into the pleural space; pleural sepsis becomes more likely particularly beyond 48-72 hours and should make the case feel less like uncomplicated CAP.</li>
            <li><b>Sepsis and septic shock:</b> Bloodstream spread or overwhelming inflammatory response can cause haemodynamic collapse and organ dysfunction, signalling severe disease with high short-term risk.</li>
            <li><b>Respiratory failure:</b> Progressive consolidation and ventilation-perfusion mismatch can cause worsening hypoxaemia and exhaustion, marking a shift from routine CAP to life-threatening respiratory compromise.</li>
            <li><b>Necrotising or cavitating pneumonia:</b> A rare but exam-relevant complication in which tissue destruction leads to persistent fever, systemic toxicity, and delayed radiological resolution, raising concern when the illness course stops fitting simple CAP.</li>
        </ul>
    </div>
</details>
```

## Gap To 10/10
### Current gap
- Current script quality is close to exemplar level, but the production process is not yet robust enough for consistent high-quality output across hundreds of topics.

### Missing process elements
- Evidence-pack workflow before drafting
- Locked exemplar bank across multiple systems
- Per-condition metadata layer
- Automated quality gates beyond basic structure
- Stricter prompt contract for density, scope, and management drift
- A weighted review rubric that enforces illness-script purity

## BMJ Takeaways
### Borrow
- Strong summary-first framing
- Clear separation of history/exam, investigations, differentials, complications, and follow-up
- Good handling of older-adult and atypical presentations
- Good emphasis on what changes severity and what changes expected recovery

### Do not borrow
- Full management algorithm detail
- Operational treatment timing targets
- Long complication inventories
- Broad mini-reference completeness
- Procedure-heavy or pathway-heavy wording

## Platform Working Standard
### Content contract for all scripts
- What is it?
- What pattern should I recognise?
- What makes it dangerous today?
- What else could this be?
- What usually changes next?

### Approved source hierarchy
1. NICE
2. SIGN / BTS / BNF / RCGP / UKHSA
3. UK specialty guidance where relevant
4. BMJ Best Practice only for framing or explanatory support

### Required metadata per condition
- Population scope
- Whether the pharmacology bullet is required
- Mandatory dangerous mimics
- Mandatory high-risk groups
- Mandatory diagnostic caveats
- Whether pregnancy / children / immunosuppression must be included
- Whether operative or procedural language is allowed
- Whether any score link is likely to be needed in section `9`
- Whether `jitl-query` is useful for high-yield concepts in this condition

### Required automated checks
- Section structure and shortcode correctness
- Open-state validation
- Timing language consistency across sections 4, 7, and 13
- Forbidden imperative language
- Drug-name containment
- No dedicated scoring-section block or legacy scoring shortcode
- If a score is mentioned, it must be brief, in section `9`, and externally linked
- `jitl-medication` wrapping for every generic drug name in section `12`
- `jitl-query` density and placement checks
- Missing dangerous mimics in differentials
- Overlong section detection
- Epidemiology anchor presence
- Treatment/complication wording drift toward protocol language

### Exemplar-set plan
- Create and lock 10 signed-off exemplars before scaling broadly
- Use those exemplars as prompt anchors and review benchmarks
- Do not scale from prompts alone

### Pass/fail rubric for future scripts
- Illness-script clarity
- Safety framing
- Source fidelity
- Exam utility
- Bedside utility
- Consistency with platform style

## Process Improvement Backlog
### Prompt changes
- Change Pass 1 from direct drafting to evidence-pack extraction plus composition
- Add a gold-standard exemplar and an anti-example to the Pass 1 prompt
- Add explicit section density limits
- Instruct the model to prefer omission over speculative completeness

### Review rubric changes
- Add illness-script purity as a formal criterion
- Add scan speed and novice usability as formal criteria
- Add a management-drift check to sections 12 and 13
- Require explicit flagging of unsupported epidemiology claims

### Lint and automation changes
- Add deterministic checks for section count, shortcode names, open states, timing phrases, score-link placement, and drug-name placement
- Add section-length thresholds
- Add forbidden-pattern detection for protocol-like language

### Exemplar programme
- Pneumonia
- Pulmonary embolism
- Deep vein thrombosis
- Acute heart failure
- Acute coronary syndrome
- COPD exacerbation
- Asthma
- Sepsis
- Meningitis
- Ectopic pregnancy

## Open Questions / Pending Decisions
### Open items
- Whether to allow limited shared decision-making language in non-treatment sections
  - Recommended default: no
- Whether to include prognosis as a separate section in future scripts
  - Recommended default: no
- Whether to include explicit follow-up bullets for every condition or only selected ones
  - Recommended default: only when it materially changes exam or bedside reasoning
- Whether to maintain one or two exemplar variants for each condition
  - Recommended default: one

## Action Queue

> **Updated 2026-03-18:** Phase 2.1, 2.2, and 2.3 are complete. 247 canonical HTML files are now in `updated-illness-scripts-2026-final/`. The immediate priority is clinician review and live replacement.

1. **Clinician review of all 247 canonical files** — prioritise Batch 1 (Pneumonia, PE, DVT, Heart Failure, Asthma) first, then Batch 2 (ACS, Pneumothorax, Meningitis, Ectopic Pregnancy, COPD, Infective Endocarditis, Aortic Aneurysm), then Phase 2.2 high-priority missing conditions.
2. **Live replacement of Batch 1 files** — once clinician-approved, replace legacy WordPress shortcodes with canonical final files.
3. **Run Codex QA pass** across all new Phase 2.2 and 2.3 files to enforce structure, shortcode placement, timing language consistency, and management drift checks.
4. **Update UKMLA_CONDITION_TRACKER_2026.md** to mark all Phase 2.1/2.2/2.3 conditions as `canonical-final-exists` and `drafted`.
5. **Resolve Phase 2.3 cluster conditions** (e.g. Bursitis, Osteoarthritis, Polymyalgia Rheumatica, Peripheral Neuropathy, Constipation, Hernias, Irritable Bowel Syndrome, Hepatitis, Urinary Tract Infection, Rhabdomyolysis, Chronic Kidney Disease, Prostate Cancer, Otitis Externa, Autonomic Neuropathy) — these were produced as unified canonical scripts but should be reviewed for cluster-resolution accuracy.
6. **Rewrite the Pass 2 prompt** to score illness-script purity, density, and management drift.
7. **Build deterministic QA checks** for structure, language, timing, score-link placement, pharmacology containment, and duplicate-file detection.
8. **Freeze the pneumonia rewrite** as the first signed-off style exemplar if the side-by-side review holds up.
9. **Phase 3 backlog** — medium-priority missing conditions (not yet produced) remain as future work once Phase 2 review is complete.

- Ectopic pregnancy cluster:
  - Canonical file: `updated-illness-scripts-2026-final/is-ectopic-pregnancy.html`
  - Legacy / comparison: `updated-illness-scripts-2026/is-ectopic-pregnancy.html` (near-empty template, written from scratch)
- COPD cluster:
  - Canonical file: `updated-illness-scripts-2026-final/is-copd.html`
  - Legacy / comparison: `updated-illness-scripts-2026/is-copd.html` (near-empty template, written from scratch)
  - Related: `updated-illness-scripts-2026/is-copd-severe.html` (separate file, not merged; treat as legacy)

## Change Log
- `2026-03-06` `Codex`: Created the shared master working document. Added current decisions, the active pneumonia exemplar draft, BMJ takeaways, platform standards, backlog, open items, and action queue.
- `2026-03-06` `Codex`: Updated the platform contract to remove the dedicated scoring section, moved score handling to brief MDCalc-linked mentions in section `9`, added `jitl-medication` for pharmacology bullets, added selective `jitl-query`, and migrated the pneumonia, PE, and DVT exemplar files accordingly.
- `2026-03-06` `Codex`: Added a canonical exemplar inventory, flagged duplicate-file clusters already present in `updated-illness-scripts-2026`, and rewrote the action queue around review, canonicalisation, and style-tightening of existing drafts.
- `2026-03-06` `Codex`: Created `updated-illness-scripts-2026-final` and moved the first-wave canonical files into it with clean condition-based filenames for pneumonia, PE, DVT, heart failure, and asthma.
- `2026-03-06` `Codex`: Created `UKMLA_REPLACEMENT_QUEUE_2026.md` to turn the gap tracker into an operational replacement/build queue, and updated this master doc to point at that queue.
- `2026-03-10` `Codex`: Added a formal `Claude -> Codex -> clinician` workflow, made the full curriculum tracker the execution source of truth, and aligned the master doc with the new full-tracker / short-queue split.
- `2026-03-10` `Claude`: Created canonical final files for infective endocarditis (written from scratch) and aortic aneurysm (written from scratch, cluster resolved — AAA as canonical; dissection confirmed as separate Batch 3 condition). Updated canonical inventory and queue.
- `2026-03-10` `Claude`: Created Batch 3 canonical files for aortic dissection, acute bronchitis, and empyema (all written from scratch; all pass structural validation checks). 15 canonical files now in final folder. Remaining Batch 3: adverse drug effects, arterial thrombosis/embolism, cardiomyopathy, CVST, drug overdose.
- `2026-03-10` `Claude`: Completed remaining Batch 3 — created canonical final files for adverse drug effects, arterial thrombosis/embolism, cardiomyopathy, CVST, and drug overdose (all written from scratch). Fixed missing `class="kb-accordion kb-parent"` attributes on all `<details>` tags in these 5 files (agent generation omission). All 5 pass full structural QA. Canonical inventory now at 20 files.
- `2026-03-10` `Claude`: Created canonical final files for meningitis (from `is-neurological-meningitis.html` source), ectopic pregnancy (written from scratch — legacy source was near-empty), and COPD (written from scratch — legacy source was near-empty). All three aligned to pneumonia exemplar standard with jitl-medication, selective jitl-query, no 9a, controlled oxygen language, and educational treatment framing. Updated UKMLA_REPLACEMENT_QUEUE_2026.md and canonical inventory accordingly.
- `2026-03-18` `Manus`: **Phase 2 complete.** Produced 227 new canonical illness script HTML files across three sub-phases using parallel production:
  - **Phase 2.1 (Batch 2 refresh, 7 conditions):** ACS, Pneumothorax, Meningitis, Ectopic Pregnancy, COPD, Infective Endocarditis, Aortic Aneurysm — all refreshed and finalised to pneumonia exemplar standard.
  - **Phase 2.2 (High-priority missing, 79 conditions):** All UKMLA high-priority conditions with no prior canonical file produced from scratch, including all obstetrics/pregnancy conditions, child health, infections, neurology, cardiology, and endocrinology.
  - **Phase 2.3 (Medium-priority refresh, 156 conditions):** All phase-2-refresh conditions across all UKMLA categories produced from legacy source material, including GI, liver/pancreas, musculoskeletal, mental health, ENT, renal, gynaecology, breast, and multi-system.
  - **Total canonical files in final folder: 247** (20 pre-existing + 227 new).
  - All files saved to `updated-illness-scripts-2026-final/`. File inventory written to `file-inventory-2026-03-18.txt`.
  - **Next step:** Clinician review of all files, then Codex QA pass, then live replacement starting with Batch 1.
