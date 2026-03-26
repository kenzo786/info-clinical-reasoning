# Primary-Care Minor-Illness Scaffold

This staged resource uses a DRx-like scaffold for novice first-contact clinicians in UK primary care, including pharmacist prescribers, nurses in minor illness clinics, and junior GPs.

## Core rules

- Source reference is the canonical asset.
- Markmap is derived from the source and must not introduce stronger claims than the source.
- Every source file uses stable numeric anchors `101-112`.
- History and examination sections must be prescriptive and action-linked.
- Default depth target is DRx-equivalent, not summary-level.
- Management must distinguish self-care, primary-care treatment, and same-day / emergency escalation.
- Role-aware notes stay inside the unified source rather than being split into separate CP and GP articles.
- If a drug is mentioned in source or map, it should normally be simple enough to attach a reusable JITL drug link.

## Standard section model

- `101` Overview and key guidance
- `102` Pathophysiology / why this presentation matters
- `103` Differential diagnosis framework
- `104` Focused history taking
- `105` Focused examination strategy
- `106` Red flag synthesis and escalation triggers
- `107` Investigations / point-of-care tests / decision points
- `108` Evidence and guideline pearls
- `109` Diagnostic timeout and common pitfalls
- `110` Management, follow-up, and safety-netting
- `111` Special populations and role-aware notes
- `112` Illustrative cases

## History / examination standard

Each child subsection in `104` and `105` should state:

1. the question or manoeuvre
2. why it matters
3. what a positive answer or finding raises or lowers
4. what action it should trigger

This same explicit structure should also be pushed into:

- `107` investigations and decision points
- `108` evidence, guideline pearls, and prescribing caveats
- `110` management pathways, counselling, and safety-netting

## Markmap standard

- Keep it shorter than the source.
- Prioritise reasoning over encyclopaedic detail.
- Use the live `chest-pain.md` interaction pattern as the benchmark.
- Link back into the source using section and child anchors.
- Add section-tail JITL prompts consistently.
- Add inline JITL links for high-yield diagnoses, tests, syndromes, and every drug mention.
- Cover, at minimum:
  - overview
  - DDx framework
  - key history
  - key examination
  - red flags
  - tests / investigations
  - diagnostic pitfalls
  - management
