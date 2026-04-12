# CRx Master Condition Export Plan 2026

## Decision

Do **not** switch authoring to hand-maintained JSON yet.

Do switch to a **generated JSON export layer now**.

That means:

- `updated-illness-scripts-2026-final/*.html` stays the authoring source during modernization
- WordPress `post_id` becomes legacy metadata, not the operational publishing target
- `Knowledge Base` becomes the first app to consume the structured export
- `CRx Conditions` and `DDx Explorer` should later consume generated projections from the same master export

This keeps the active modernization workflow stable while removing the WordPress copy/paste bottleneck.

## Why This Is The Right Timing

The repo state suggests the content build is much further ahead than the tracking metadata:

- `CONTENT_MODERNIZATION_PLAN_2026.md` still describes the UKMLA-first phase plan for `429` conditions
- `ILLNESS_SCRIPT_MASTER_WORKING_DOC.md` states that Phase 2 produced `247` canonical files and that the next step is clinician review plus live replacement
- `updated-illness-scripts-2026-final/` now contains `429` HTML illness-script files
- `ukmla_canonical_manifest.csv` shows a mixed transition state:
  - `209` rows with `post_id`
  - `200` rows marked `published`
  - `9` rows marked `pending-transfer`
  - `217` rows without `post_id`

So the bottleneck is no longer raw content creation alone. The real bottleneck is that the publishing architecture is still WordPress-led.

## Current Problem

Right now the same illness script is trying to serve too many roles:

1. authoring artifact
2. WordPress publishing payload
3. Knowledge Base source
4. CRx Conditions deep-dive target
5. DDx full-script iframe target

That creates repeated transfer work and makes every update expensive.

## Target Architecture

### Layer 1: Canonical Authoring Source

Keep this in `info-clinical-reasoning`:

- `updated-illness-scripts-2026-final/*.html`
- `ukmla_canonical_manifest.csv`
- `UKMLA_CONDITION_TRACKER_2026.md`

These remain the editorial and modernization source-of-truth assets.

### Layer 2: Master Structured Export

Create a deterministic export step in `info-clinical-reasoning`:

- input: canonical final HTML + manifest/tracker metadata
- output: `exports/crx-master-conditions/*.json`

Each exported JSON file should represent one exact UKMLA condition in a clean, app-neutral structure.

This becomes the **single machine-readable condition truth** for the wider CRx family.

### Layer 3: App-Specific Projections

Generate downstream projections from the master export, not from WordPress and not from hand-authored duplicate files.

- Knowledge Base:
  - consumes the master export directly or a lightly normalized KB article export
- CRx Conditions / Reasoning Compass:
  - generated topic bundle from the master export
- DDx Explorer:
  - generated condition reference / full-script link payload from the master export
- Later:
  - Foundations
  - Investigations
  - TRx
  - Pharm
  - QuickNotes

## Downstream App Requirements

### 1. Knowledge Base

Knowledge Base needs:

- full long-form article content
- 13 canonical sections
- metadata
- JITL references
- legacy `post_id`
- related family links

This is the closest consumer to the raw illness-script source.

### 2. CRx Conditions / Reasoning Compass

Reasoning Compass currently uses hand-authored topic bundles such as:

- `reasoning-compass/src/data/topics/type-2-diabetes/*`
- `reasoning-compass/src/data/topics/heart-failure/*`

Those bundles are richer than the illness scripts. They include:

- `meta.ts`
- `overview.ts`
- `sections.ts`

So the exporter should not try to replace those files 1:1 with raw HTML.

Instead, the exporter should provide a structured base that a generator can transform into:

- `meta.ts`
- `overview.ts`
- `sections.ts`
- optionally `reasoningMap.ts`

The goal is:

- source condition truth lives in the master export
- `reasoning-compass` keeps its polished card-based teaching format
- card bundles become generated or semi-generated from structured inputs rather than written from scratch every time

### 3. DDx Explorer

`ddx-explorer` currently still points to `info.clinicalreasoning.io` in multiple places and uses external/embedded script URLs.

That should change.

The new target should be:

- no dependence on WordPress iframes
- no direct dependency on `info.clinicalreasoning.io`
- condition library rows point to `kb.clinicalreasoning.io/topic/:slug`

Recommended DDx integration modes:

- primary: open the full Knowledge Base topic in a new tab
- secondary: optional bounded embedded KB panel only if the KB page can be rendered safely and cleanly

Do not keep the iframe architecture as the long-term design.

## Export Contract

The master export should be app-neutral and condition-led.

### Top-Level Fields

- `schemaVersion`
- `exportedAt`
- `conditionId`
- `slug`
- `title`
- `subtitle`
- `conditionType`
- `ukmla`
- `source`
- `publication`
- `taxonomy`
- `signals`
- `sections`
- `jitl`
- `downstreamHints`

### Source Block

This preserves traceability back to the HTML corpus:

- source repo
- source HTML file
- source filename
- legacy `post_id`
- tracker status
- manifest status
- review status

### UKMLA Block

This should store:

- exact curriculum wording
- category
- gap-tracker status
- priority
- phase

### Publication Block

This should separate:

- `legacyWordpressStatus`
- `knowledgeBaseStatus`
- `conditionsProjectionStatus`
- `ddxProjectionStatus`

### Section Model

The exporter should normalize every illness script into the canonical 13-section scaffold:

1. `overview`
2. `risk-factors`
3. `pathophysiology`
4. `time-course`
5. `clinical-features`
6. `red-flags`
7. `atypical-presentations`
8. `investigations`
9. `problem-representation`
10. `key-differentials`
11. `management-thinking`
12. `prescribing`
13. `complications`

Each section should include:

- `id`
- `key`
- `title`
- `order`
- `sourceSectionIds`
- `rawHtml`
- `plainText`
- `jitlReferences`
- `deepDiveAnchor`

## Proposed Schema

The machine-readable schema lives at:

- `schemas/crx-master-condition.schema.json`

That schema is intentionally designed to support:

- Knowledge Base long-form rendering
- Reasoning Compass topic generation
- DDx Explorer full-script linking

## Mapping Rules

### HTML -> Master Export

- Keep raw HTML in the export for fidelity
- Also emit normalized plain text for search, indexing, and projection logic
- Keep JITL shortcodes as structured references, not just string fragments
- Preserve `post_id` but mark it as legacy publication metadata

### Master Export -> Knowledge Base

- render the `sections[].rawHtml`
- use `deepDiveAnchor` for section share links
- use `legacyPostId` for old URL redirects only

### Master Export -> CRx Conditions

Generate from the master export:

- `meta.ts`
- `overview.ts`
- `sections.ts`

Proposed generation logic:

- `meta.ts`
  - title, subtitle, summary, tags, audience, reading time, accent theme
  - `illnessScriptUrl` should point to Knowledge Base, not WordPress
- `overview.ts`
  - built from `overview`, `red-flags`, `management-thinking`, and key signals
- `sections.ts`
  - generated from the 13 canonical section blocks
  - card extraction should use deterministic chunking rules plus optional manual refinement

### Master Export -> DDx Explorer

Generate from the master export:

- canonical KB URL
- section deep links
- red flag summary
- key features summary
- problem representation summary
- differential list

Recommended DDx data fields:

- `knowledgeBaseUrl`
- `knowledgeBaseEmbeddedUrl` optional
- `conditionSummary`
- `keyFeatures`
- `redFlags`
- `keyDifferentials`
- `legacyPostId`

## Important Rule: Do Not Author Projections By Hand

Manual app bundles should become the exception, not the default.

Preferred model:

- author the condition once in `info-clinical-reasoning`
- export the master JSON once
- generate downstream projections
- allow app-level refinement only where the app truly needs extra pedagogy or UI-specific condensation

## Recommended Rollout

### Phase A: Stabilise Source Metadata

Before broad exporter work:

1. Reconcile `ukmla_canonical_manifest.csv` with the actual `updated-illness-scripts-2026-final/` folder
2. Reconcile the tracker statuses with the current file inventory
3. Mark which files are:
   - canonical final
   - needs clinician review
   - publish-ready
   - post-id assigned

This is the most important immediate cleanup.

### Phase B: Build The Exporter

Create:

- `export_crx_master_conditions.py`

Inputs:

- canonical HTML files
- manifest CSV
- tracker metadata

Outputs:

- `exports/crx-master-conditions/index.json`
- `exports/crx-master-conditions/conditions/<slug>.json`

### Phase C: Point Knowledge Base At Exported JSON

Knowledge Base should stop parsing raw HTML files from a sibling repo at build time.

Instead:

- `info-clinical-reasoning` exports the condition JSON
- `crx-knowledge-library` consumes the export artifacts

That gives cleaner boundaries and removes HTML parsing from the app repo.

### Phase D: Generate Reasoning Compass Topics

Create a generator that converts a master condition export into:

- `meta.ts`
- `overview.ts`
- `sections.ts`

This should begin with exemplar conditions:

- Heart failure
- Type 2 diabetes
- Asthma
- Pneumonia
- Pulmonary embolism

### Phase E: Migrate DDx Explorer

Replace `info.clinicalreasoning.io` links and iframe assumptions with:

- `kb.clinicalreasoning.io/topic/:slug`

Use the master export as the full-script reference layer.

## What Not To Do

- Do not move the active authoring source into WordPress
- Do not maintain two editable copies of the same condition
- Do not hand-convert 429 conditions into standalone JSON one by one
- Do not make Knowledge Base, CRx Conditions, and DDx each invent their own condition truth independently

## Immediate Next Step

The best next step is:

1. add the schema
2. build the exporter against a small exemplar set
3. validate it on:
   - asthma
   - heart failure
   - pneumonia
   - pulmonary embolism
4. then wire Knowledge Base to the exported JSON

That will let the Knowledge Base become the first clean consumer of the condition-truth layer, after which the rest of the family can cascade from it.
