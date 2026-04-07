# UKMLA Condition Tracker 2026

Status: Full curriculum execution tracker for UKMLA illness-script coverage in the canonical final folder

Source of truth inputs:
- `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_condition_category_mapping.json`
- `archive/categorized-variants/ukmla-categorized-illness-scripts-2026/ukmla_gap_tracker_2026.csv`
- `ukmla_canonical_manifest.csv`

Canonical file note:
- The tracker keeps the original `Canonical final target` slug form for planning continuity.
- The current on-disk canonical filename may now be post-id-prefixed, for example `1318-is-ukmla-heart-failure.html`.
- Use `ukmla_canonical_manifest.csv` as the current source of truth for `post_id`, canonical filename, and category-driven shortcode generation.

Working rules:
- One row per exact UKMLA condition.
- `Canonical final target` is the intended final-folder filename, even when the file does not yet exist.
- `Current final file status` uses only: `canonical-final-exists`, `legacy-source-only`, `no-final-file-yet`.
- `Next action` uses only: `replace-live-now`, `refresh-existing`, `create-new`, `cluster-resolution-first`, `defer`.
- `Review status` uses only: `not-started`, `drafted`, `codex-standardised`, `clinician-review-needed`, `ready-to-publish`, `published`.

Summary: `429` UKMLA conditions, grouped by category in mapping order. Current canonical final files already present in this folder are reflected into the tracker rather than recreated.

## Blood and lymph

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Abnormal blood film | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-abnormal-blood-film.html | no-final-file-yet | create-new | not-started |  |
| Anaemia | Blood and lymph | covered-needs-refresh | medium | phase-2-refresh | is-anaemia; is-anaemia-sob; is-aplastic-anaemia; is-childhood-anaemia; is-haemolytic-anaemia; is-iron-deficiency-anaemia; is-macrocytic-anaemia; is-medication-induced-anaemia; is-microcytic-anaemia; is-normocytic-anaemia; is-sideroblastic-anaemia | is-anaemia.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Coagulation disorders | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-coagulation-disorders-including-haemophilia-von-willebrand-disease-and-thrombophilia-and-secondary-to-illness-or-medication.html | no-final-file-yet | create-new | not-started |  |
| Disseminated intravascular coagulation (DIC) | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-disseminated-intravascular-coagulation-dic.html | no-final-file-yet | create-new | not-started |  |
| Haemoglobinopathies | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-haemoglobinopathies.html | no-final-file-yet | create-new | not-started |  |
| Hyposplenism/ splenectomy | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-hyposplenism-splenectomy.html | no-final-file-yet | create-new | not-started |  |
| Idiopathic thrombocytopenic purpura (ITP) | Blood and lymph | covered-needs-refresh | medium | phase-2-refresh | is-thrombocytopenic-purpura | is-idiopathic-thrombocytopenic-purpura-itp.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Leukaemia | Blood and lymph | covered-needs-refresh | medium | phase-2-refresh | is-leukaemia | is-leukaemia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Lymphoma | Blood and lymph | covered-needs-refresh | medium | phase-2-refresh | is-lymphoma; is-mediastinal-lymphoma | is-lymphoma.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Multiple myeloma | Blood and lymph | covered-needs-refresh | medium | phase-2-refresh | is-multiple-myeloma | is-multiple-myeloma.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Myeloproliferative disorders | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-myeloproliferative-disorders.html | no-final-file-yet | create-new | not-started |  |
| Neutropenia (including neutropenic sepsis) | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-neutropenia-including-neutropenic-sepsis.html | no-final-file-yet | create-new | not-started |  |
| Pancytopenia | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-pancytopenia.html | no-final-file-yet | create-new | not-started |  |
| Platelet disorders (including thrombocytosis, thrombocytopaenia) | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-platelet-disorders-including-thrombocytosis-thrombocytopaenia.html | no-final-file-yet | create-new | not-started |  |
| Polycythaemia | Blood and lymph | covered-needs-refresh | medium | phase-2-refresh | is-polycythaemia | is-polycythaemia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Sickle cell disease | Blood and lymph | covered-needs-refresh | medium | phase-2-refresh | is-sickle-cell-disease | is-sickle-cell-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Transfusion reactions | Blood and lymph | missing | medium | phase-3-create-backlog |  | is-transfusion-reactions.html | no-final-file-yet | create-new | not-started |  |

## Skin and soft tissue

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Acne vulgaris | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-acne-vulgaris.html | no-final-file-yet | create-new | not-started |  |
| Atopic dermatitis/ eczema | Skin and soft tissue | covered-needs-refresh | medium | phase-2-refresh | is-atopic-dermatitis | is-atopic-dermatitis-eczema.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Benign skin lesion (including melanocytic naevi, epidermal cyst, dermatofibroma, seborrheic keratosis, actinic keratosis) | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-benign-skin-lesion-including-melanocytic-naevi-epidermal-cyst-dermatofibroma-seborrheic-keratosis-actinic-keratosis.html | no-final-file-yet | create-new | not-started |  |
| Burns | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-burns.html | no-final-file-yet | create-new | not-started |  |
| Cellulitis | Skin and soft tissue | covered-needs-refresh | medium | phase-2-refresh | is-cellulitis; is-orbital-cellulitis | is-cellulitis.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Contact dermatitis | Skin and soft tissue | covered-needs-refresh | medium | phase-2-refresh | is-contact-dermatitis | is-contact-dermatitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Cutaneous fungal infection | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-cutaneous-fungal-infection.html | no-final-file-yet | create-new | not-started |  |
| Cutaneous warts | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-cutaneous-warts.html | no-final-file-yet | create-new | not-started |  |
| Erythema nodosum | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-erythema-nodosum.html | no-final-file-yet | create-new | not-started |  |
| Folliculitis and Hidradenitis suppurativa | Skin and soft tissue | covered-needs-refresh | medium | phase-2-refresh | is-hidradenitis-suppurativa | is-folliculitis-and-hidradenitis-suppurativa.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Haemangioma | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-haemangioma.html | no-final-file-yet | create-new | not-started |  |
| Impetigo | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-impetigo.html | no-final-file-yet | create-new | not-started |  |
| Lichen planus | Skin and soft tissue | covered-needs-refresh | medium | phase-2-refresh | is-lichen-planus | is-lichen-planus.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Lipoma | Skin and soft tissue | covered-needs-refresh | medium | phase-2-refresh | is-lipoma | is-lipoma.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Malignant/ pre-malignant skin lesions (including Bowen disease, malignant melanoma, basal cell carcinoma, squamous cell carcinoma) | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-malignant-pre-malignant-skin-lesions-including-bowen-disease-malignant-melanoma-basal-cell-carcinoma-squamous-cell-carcinoma.html | no-final-file-yet | create-new | not-started |  |
| Necrotising fasciitis | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-necrotising-fasciitis.html | no-final-file-yet | create-new | not-started |  |
| Pressure sores | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-pressure-sores.html | no-final-file-yet | create-new | not-started |  |
| Psoriasis | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-psoriasis.html | no-final-file-yet | create-new | not-started |  |
| Rosacea | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-rosacea.html | no-final-file-yet | create-new | not-started |  |
| Scabies | Skin and soft tissue | covered-needs-refresh | medium | phase-2-refresh | is-scabies | is-scabies.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Skin manifestations of systemic disease (including acanthosis nigricans, livedo reticularis and petechiae/ purpura) | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-skin-manifestations-of-systemic-disease-including-acanthosis-nigricans-livedo-reticularis-and-petechiae-purpura.html | no-final-file-yet | create-new | not-started |  |
| Skin ulcers (including arterial, venous and neuropathic ulcers) | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-skin-ulcers-including-arterial-venous-and-neuropathic-ulcers.html | no-final-file-yet | create-new | not-started |  |
| Stevens-Johnson Syndrome/ toxic epidermal necrolysis (TEN) | Skin and soft tissue | missing | medium | phase-3-create-backlog |  | is-stevens-johnson-syndrome-toxic-epidermal-necrolysis-ten.html | no-final-file-yet | create-new | not-started |  |
| Urticaria | Skin and soft tissue | covered-needs-refresh | medium | phase-2-refresh | is-urticaria | is-urticaria.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Eye

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Acute glaucoma | Eye | covered-needs-refresh | medium | phase-2-refresh | is-acute-glaucoma | is-acute-glaucoma.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Benign eyelid disorders (including blepharitis, ectropion/ entropion, chalazion, hordeolum) | Eye | missing | medium | phase-3-create-backlog |  | is-benign-eyelid-disorders-including-blepharitis-ectropion-entropion-chalazion-hordeolum.html | no-final-file-yet | create-new | not-started |  |
| Cataracts | Eye | covered-needs-refresh | medium | phase-2-refresh | is-cataract | is-cataracts.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Central retinal arterial occlusion | Eye | missing | medium | phase-3-create-backlog |  | is-central-retinal-arterial-occlusion.html | no-final-file-yet | create-new | not-started |  |
| Central retinal vein occlusion | Eye | covered-needs-refresh | medium | phase-2-refresh | is-retinal-vein-occlusion | is-central-retinal-vein-occlusion.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Chronic glaucoma | Eye | covered-needs-refresh | medium | phase-2-refresh | is-chronic-glaucoma | is-chronic-glaucoma.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Conjunctivitis | Eye | covered-needs-refresh | medium | phase-2-refresh | is-conjunctivitis | is-conjunctivitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Corneal ulcer/ abrasion | Eye | covered-needs-refresh | medium | phase-2-refresh | is-corneal-abrasion; is-corneal-ulcer | is-corneal-ulcer-abrasion.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Hypertensive retinopathy | Eye | missing | medium | phase-3-create-backlog |  | is-hypertensive-retinopathy.html | no-final-file-yet | create-new | not-started |  |
| Infective keratitis | Eye | missing | medium | phase-3-create-backlog |  | is-infective-keratitis.html | no-final-file-yet | create-new | not-started |  |
| Inflammatory conditions of the eye (including scleritis, episcleritis, uveitis) | Eye | missing | medium | phase-3-create-backlog |  | is-inflammatory-conditions-of-the-eye-including-scleritis-episcleritis-uveitis.html | no-final-file-yet | create-new | not-started |  |
| Macular degeneration | Eye | covered-needs-refresh | medium | phase-2-refresh | is-macular-degeneration | is-macular-degeneration.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Optic neuritis | Eye | covered-needs-refresh | medium | phase-2-refresh | is-optic-neuritis | is-optic-neuritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Papilloedema | Eye | missing | medium | phase-3-create-backlog |  | is-papilloedema.html | no-final-file-yet | create-new | not-started |  |
| Periorbital and orbital cellulitis | Eye | missing | medium | phase-3-create-backlog |  | is-periorbital-and-orbital-cellulitis.html | no-final-file-yet | create-new | not-started |  |
| Retinal detachment | Eye | covered-needs-refresh | medium | phase-2-refresh | is-retinal-detachment | is-retinal-detachment.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Subconjunctival haemorrhage | Eye | covered-needs-refresh | medium | phase-2-refresh | is-subconjunctival-haemorrhage | is-subconjunctival-haemorrhage.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Visual field defects | Eye | missing | medium | phase-3-create-backlog |  | is-visual-field-defects.html | no-final-file-yet | create-new | not-started |  |

## Endocrine and metabolic

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Acromegaly | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-acromegaly.html | no-final-file-yet | create-new | not-started |  |
| Adrenal insufficiency (including primary and secondary) | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-adrenal-insufficiency-including-primary-and-secondary.html | no-final-file-yet | create-new | not-started |  |
| Arginine vasopressin deficiency/ resistance (diabetes insipidus) | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-arginine-vasopressin-deficiency-resistance-diabetes-insipidus.html | no-final-file-yet | create-new | not-started |  |
| Cushing syndrome | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-cushings-syndrome | is-cushing-syndrome.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Diabetes mellitus | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-type-1-diabetes-mellitus | is-diabetes-mellitus.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Diabetic ketoacidosis (DKA) | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-diabetic-ketoacidosis | is-diabetic-ketoacidosis-dka.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Diabetic nephropathy | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-diabetic-nephropathy | is-diabetic-nephropathy.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Diabetic neuropathy | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-diabetic-neuropathy | is-diabetic-neuropathy.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Diabetic retinopathy | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-diabetic-retinopathy | is-diabetic-retinopathy.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Graves disease (including thyroid eye disease) | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-graves-disease-including-thyroid-eye-disease.html | no-final-file-yet | create-new | not-started |  |
| Haemochromatosis | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-haemochromatosis | is-haemochromatosis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hyperlipidaemia | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-hyperlipidaemia.html | no-final-file-yet | create-new | not-started |  |
| Hyperosmolar hyperglycaemic state (HHS) | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-hhs | is-hyperosmolar-hyperglycaemic-state-hhs.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hyperparathyroidism/ hypoparathyroidism | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-hyperparathyroidism-hypoparathyroidism.html | no-final-file-yet | create-new | not-started |  |
| Hyperprolactinaemia | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-hyperprolactinaemia | is-hyperprolactinaemia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hyperthyroidism/ thyrotoxicosis | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-hyperthyroidism-thyrotoxicosis.html | no-final-file-yet | create-new | not-started |  |
| Hypoglycaemia | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-hypoglycaemia | is-hypoglycaemia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hypopituitarism | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-hypopituitarism.html | no-final-file-yet | create-new | not-started |  |
| Hypothyroidism | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-hypothyroidism; is-hypothyroidism-myxoedema | is-hypothyroidism.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Metabolic syndrome | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-metabolic-syndrome | is-metabolic-syndrome.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Phaeochromocytoma | Endocrine and metabolic | covered-needs-refresh | medium | phase-2-refresh | is-phaeochromocytoma | is-phaeochromocytoma.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Pituitary tumours | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-pituitary-tumours.html | no-final-file-yet | create-new | not-started |  |
| Prediabetes | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-prediabetes.html | no-final-file-yet | create-new | not-started |  |
| Primary aldosteronism | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-primary-aldosteronism.html | no-final-file-yet | create-new | not-started |  |
| Refeeding syndrome | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-refeeding-syndrome.html | no-final-file-yet | create-new | not-started |  |
| Syndrome of inappropriate antidiuretic hormone secretion (SIADH) | Endocrine and metabolic | missing | medium | phase-3-create-backlog |  | is-syndrome-of-inappropriate-antidiuretic-hormone-secretion-siadh.html | no-final-file-yet | create-new | not-started |  |

## Heart and vasculature

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Acute coronary syndromes | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-acute-coronary-syndrome | is-acute-coronary-syndromes.html | canonical-final-exists | refresh-existing | clinician-review-needed | Canonical final file present in final folder. |
| Aneurysms, ischaemic limb and occlusions | Heart and vasculature | missing | high | phase-3-create-priority |  | is-aneurysms-ischaemic-limb-and-occlusions.html | no-final-file-yet | create-new | not-started |  |
| Aortic aneurysm | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-aortic-aneurysm; is-aortic-aneurysm-rupture-or-dissection; is-aortic-aneurysm-thoracic | is-aortic-aneurysm.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. Current canonical target is AAA-focused. |
| Aortic dissection | Heart and vasculature | missing | high | phase-3-create-priority |  | is-aortic-dissection.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. Separate UKMLA condition from AAA. |
| Aortic valve disease | Heart and vasculature | missing | high | phase-3-create-priority |  | is-aortic-valve-disease.html | no-final-file-yet | create-new | not-started |  |
| Arterial thrombosis/ embolism | Heart and vasculature | missing | high | phase-3-create-priority |  | is-arterial-thrombosis-embolism.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Bradyarrhythmias (including AV block) | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-av-block | is-bradyarrhythmias-including-av-block.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Cardiac arrest | Heart and vasculature | missing | high | phase-3-create-priority |  | is-cardiac-arrest.html | no-final-file-yet | create-new | not-started |  |
| Cardiomyopathy | Heart and vasculature | missing | high | phase-3-create-priority |  | is-cardiomyopathy.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Carotid dissection | Heart and vasculature | missing | high | phase-3-create-priority |  | is-carotid-dissection.html | no-final-file-yet | create-new | not-started |  |
| Congenital heart disease | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-congenital-heart-disease; is-valvular-heart-disease | is-congenital-heart-disease.html | legacy-source-only | defer | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. Explicitly deferred in short priority queue. |
| Deep vein thrombosis | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-dvt | is-deep-vein-thrombosis.html | canonical-final-exists | replace-live-now | clinician-review-needed | Canonical final file present in final folder. Batch 1 live-replacement candidate. |
| Gangrene | Heart and vasculature | missing | high | phase-3-create-priority |  | is-gangrene.html | no-final-file-yet | create-new | not-started |  |
| Heart failure | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-heart-failure | is-heart-failure.html | canonical-final-exists | replace-live-now | clinician-review-needed | Canonical final file present in final folder. Batch 1 live-replacement candidate. |
| Hypertension (essential or secondary) | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-essential-hypertension | is-hypertension-essential-or-secondary.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Infective endocarditis | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-infective-endocarditis | is-infective-endocarditis.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Ischaemic heart disease (including stable angina) | Heart and vasculature | missing | high | phase-3-create-priority |  | is-ischaemic-heart-disease-including-stable-angina.html | no-final-file-yet | create-new | not-started |  |
| Mitral valve disease | Heart and vasculature | missing | high | phase-3-create-priority |  | is-mitral-valve-disease.html | no-final-file-yet | create-new | not-started |  |
| Myocarditis | Heart and vasculature | missing | high | phase-3-create-priority |  | is-myocarditis.html | no-final-file-yet | create-new | not-started |  |
| Orthostatic/ postural hypotension | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-orthostatic-hypotension | is-orthostatic-postural-hypotension.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Pericardial disease (including pericarditis, pericardial effusion, cardiac tamponade) | Heart and vasculature | missing | high | phase-3-create-priority |  | is-pericardial-disease-including-pericarditis-pericardial-effusion-cardiac-tamponade.html | no-final-file-yet | create-new | not-started |  |
| Peripheral vascular disease | Heart and vasculature | missing | high | phase-3-create-priority |  | is-peripheral-vascular-disease.html | no-final-file-yet | create-new | not-started |  |
| Pulmonary embolism | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-pulmonary-embolism | is-pulmonary-embolism.html | canonical-final-exists | replace-live-now | clinician-review-needed | Canonical final file present in final folder. Batch 1 live-replacement candidate. |
| Pulmonary hypertension | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-pulmonary-hypertension | is-pulmonary-hypertension.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Right heart valve disease | Heart and vasculature | missing | high | phase-3-create-priority |  | is-right-heart-valve-disease.html | no-final-file-yet | create-new | not-started |  |
| Shock | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-hypovolaemic-shock | is-shock.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Superior vena cava obstruction | Heart and vasculature | missing | high | phase-3-create-priority |  | is-superior-vena-cava-obstruction.html | no-final-file-yet | create-new | not-started |  |
| Syncope (including vasovagal, cardiac) | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-vasovagal-syncope | is-syncope-including-vasovagal-cardiac.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Tachyarrhythmias (including atrial fibrillation, atrial flutter, supraventricular tachycardia, torsades de pointes, ventricular tachycardia, ventricular fibrillation) | Heart and vasculature | missing | high | phase-3-create-priority |  | is-tachyarrhythmias-including-atrial-fibrillation-atrial-flutter-supraventricular-tachycardia-torsades-de-pointes-ventricular-tachycardia-ventricular-fibrillation.html | no-final-file-yet | create-new | not-started |  |
| Venous insufficiency (including varicose veins) | Heart and vasculature | covered-needs-refresh | high | phase-1-pilot | is-chronic-venous-insufficiency; is-varicose-veins | is-venous-insufficiency-including-varicose-veins.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |

## Lungs, pleura and airways

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Acute bronchitis | Lungs, pleura and airways | missing | high | phase-3-create-priority |  | is-acute-bronchitis.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Acute respiratory distress syndrome (ARDS) | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-neonatal-respiratory-distress-syndrome | is-acute-respiratory-distress-syndrome-ards.html | legacy-source-only | defer | not-started | Legacy/archive source scripts exist in gap tracker. Explicitly deferred in short priority queue. |
| Asthma | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-asthma | is-asthma.html | canonical-final-exists | replace-live-now | clinician-review-needed | Canonical final file present in final folder. Batch 1 live-replacement candidate. |
| Asthma-chronic obstructive pulmonary disease (COPD) overlap | Lungs, pleura and airways | missing | high | phase-3-create-priority |  | is-asthma-chronic-obstructive-pulmonary-disease-copd-overlap.html | no-final-file-yet | create-new | not-started |  |
| Bronchiectasis | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-bronchiectasis | is-bronchiectasis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Chronic obstructive pulmonary disease (COPD) | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-copd | is-copd.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. Canonical final filename intentionally shortened to is-copd.html. |
| Empyema | Lungs, pleura and airways | missing | high | phase-3-create-priority |  | is-empyema.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Interstitial lung disease (including fibrotic lung disease) | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-interstitial-lung-disease | is-interstitial-lung-disease-including-fibrotic-lung-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Lower respiratory tract infection | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-lrti | is-lower-respiratory-tract-infection.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Lung abscess | Lungs, pleura and airways | missing | high | phase-3-create-priority |  | is-lung-abscess.html | no-final-file-yet | create-new | not-started |  |
| Lung cancer | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-lung-cancer | is-lung-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Obstructive sleep apnoea | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-obstructive-sleep-apnoea | is-obstructive-sleep-apnoea.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Occupational lung disease | Lungs, pleura and airways | missing | high | phase-3-create-priority |  | is-occupational-lung-disease.html | no-final-file-yet | create-new | not-started |  |
| Pleural effusion | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-pleural-effusion | is-pleural-effusion.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Pneumonia | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-hiv-associated-pneumocystis-pneumonia; is-pneumonia | is-pneumonia.html | canonical-final-exists | replace-live-now | clinician-review-needed | Canonical final file present in final folder. Batch 1 live-replacement candidate. |
| Pneumothorax | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-pneumothorax | is-pneumothorax.html | canonical-final-exists | refresh-existing | clinician-review-needed | Canonical final file present in final folder. |
| Respiratory arrest | Lungs, pleura and airways | missing | high | phase-3-create-priority |  | is-respiratory-arrest.html | no-final-file-yet | create-new | not-started |  |
| Respiratory failure | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-respiratory-failure | is-respiratory-failure.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Sarcoidosis | Lungs, pleura and airways | covered-needs-refresh | high | phase-1-pilot | is-ocular-sarcoidosis; is-sarcoidosis | is-sarcoidosis.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |

## Gastrointestinal tract

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Anal fissure | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-anal-fissure | is-anal-fissure.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Appendicitis | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-abdominal-pain-appendicitis; is-appendicitis | is-appendicitis.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Coeliac disease | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-coeliac-disease | is-coeliac-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Colorectal cancer | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-colorectal-cancer | is-colorectal-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Constipation | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-constipation; is-constipation-induced-delirium; is-medication-induced-constipation; is-simple-constipation | is-constipation.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Diverticular disease and diverticulitis | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-diverticular-disease | is-diverticular-disease-and-diverticulitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Gastric cancer | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-gastric-cancer | is-gastric-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Gastro-oesophageal reflux disease (including Barrett oesophagus) | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-gord | is-gastro-oesophageal-reflux-disease-including-barrett-oesophagus.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Gastrointestinal bleeding (upper and lower GI bleeding) | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-severe-upper-gastrointestinal-bleeding | is-gastrointestinal-bleeding-upper-and-lower-gi-bleeding.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Gastrointestinal perforation | Gastrointestinal tract | missing | medium | phase-3-create-backlog |  | is-gastrointestinal-perforation.html | no-final-file-yet | create-new | not-started |  |
| Haemorrhoids | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-haemorrhoids | is-haemorrhoids.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hernias | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-hernia; is-incarcerated-hernia; is-inguinal-or-femoral-hernia | is-hernias.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Hiatus hernia | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-hiatus-hernia | is-hiatus-hernia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Infectious colitis (including Clostridium difficile) | Gastrointestinal tract | missing | medium | phase-3-create-backlog |  | is-infectious-colitis-including-clostridium-difficile.html | no-final-file-yet | create-new | not-started |  |
| Infectious diarrhoea (including infective gastroenteritis) | Gastrointestinal tract | missing | medium | phase-3-create-backlog |  | is-infectious-diarrhoea-including-infective-gastroenteritis.html | no-final-file-yet | create-new | not-started |  |
| Inflammatory bowel disease (including Crohn disease, ulcerative colitis) | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-inflammatory-bowel-disease | is-inflammatory-bowel-disease-including-crohn-disease-ulcerative-colitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Intestinal ischaemia | Gastrointestinal tract | missing | medium | phase-3-create-backlog |  | is-intestinal-ischaemia.html | no-final-file-yet | create-new | not-started |  |
| Intestinal obstruction and ileus | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-intestinal-obstruction | is-intestinal-obstruction-and-ileus.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Irritable bowel syndrome | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-irritable-bowel-syndrome; is-irritable-bowel-syndrome-adolescents; is-short-bowel-syndrome | is-irritable-bowel-syndrome.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Malabsorption | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-malabsorption | is-malabsorption.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Mallory-Weiss tear | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-mallory-weiss-tear | is-mallory-weiss-tear.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Oesophageal cancer | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-oesophageal-cancer | is-oesophageal-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Peptic ulcer disease and gastritis | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-peptic-ulcer-disease | is-peptic-ulcer-disease-and-gastritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Perianal abscesses and fistulae | Gastrointestinal tract | missing | medium | phase-3-create-backlog |  | is-perianal-abscesses-and-fistulae.html | no-final-file-yet | create-new | not-started |  |
| Peritonitis | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-peritonitis | is-peritonitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Rectal prolapse | Gastrointestinal tract | missing | medium | phase-3-create-backlog |  | is-rectal-prolapse.html | no-final-file-yet | create-new | not-started |  |
| Toxic megacolon | Gastrointestinal tract | missing | medium | phase-3-create-backlog |  | is-toxic-megacolon.html | no-final-file-yet | create-new | not-started |  |
| Variceal disease (including oesophageal varices) | Gastrointestinal tract | covered-needs-refresh | medium | phase-2-refresh | is-oesophageal-varices | is-variceal-disease-including-oesophageal-varices.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Volvulus | Gastrointestinal tract | missing | medium | phase-3-create-backlog |  | is-volvulus.html | no-final-file-yet | create-new | not-started |  |

## Liver, pancreas, biliary system

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Acute cholangitis | Liver, pancreas, biliary system | missing | medium | phase-3-create-backlog |  | is-acute-cholangitis.html | no-final-file-yet | create-new | not-started |  |
| Acute pancreatitis | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-acute-pancreatitis | is-acute-pancreatitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Alcohol related liver disease | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-alcoholic-liver-disease | is-alcohol-related-liver-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Ascites (including spontaneous bacterial peritonitis) | Liver, pancreas, biliary system | missing | medium | phase-3-create-backlog |  | is-ascites-including-spontaneous-bacterial-peritonitis.html | no-final-file-yet | create-new | not-started |  |
| Cholecystitis | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-cholecystitis | is-cholecystitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Chronic liver disease (including decompensation and cirrhosis of the liver) | Liver, pancreas, biliary system | missing | medium | phase-3-create-backlog |  | is-chronic-liver-disease-including-decompensation-and-cirrhosis-of-the-liver.html | no-final-file-yet | create-new | not-started |  |
| Chronic pancreatitis | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-chronic-pancreatitis | is-chronic-pancreatitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Gallstones and biliary colic | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-biliary-colic | is-gallstones-and-biliary-colic.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hepatitis (including viral, autoimmune, alcoholic) | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-autoimmune-hepatitis; is-viral-hepatitis | is-hepatitis-including-viral-autoimmune-alcoholic.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Hepatocellular carcinoma | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-hepatocellular-carcinoma | is-hepatocellular-carcinoma.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Liver abscess | Liver, pancreas, biliary system | missing | medium | phase-3-create-backlog |  | is-liver-abscess.html | no-final-file-yet | create-new | not-started |  |
| Liver failure | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-liver-failure | is-liver-failure.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Metabolic dysfunction-associated steatotic liver disease (MASLD) | Liver, pancreas, biliary system | missing | medium | phase-3-create-backlog |  | is-metabolic-dysfunction-associated-steatotic-liver-disease-masld.html | no-final-file-yet | create-new | not-started |  |
| Pancreatic cancer | Liver, pancreas, biliary system | covered-needs-refresh | medium | phase-2-refresh | is-pancreatic-cancer | is-pancreatic-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Genetic and congenital

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Cystic fibrosis | Genetic and congenital | covered-needs-refresh | medium | phase-2-refresh | is-cystic-fibrosis | is-cystic-fibrosis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Down syndrome | Genetic and congenital | missing | medium | phase-3-create-backlog |  | is-down-syndrome.html | no-final-file-yet | create-new | not-started |  |
| Ehlers-Danlos syndrome | Genetic and congenital | missing | medium | phase-3-create-backlog |  | is-ehlers-danlos-syndrome.html | no-final-file-yet | create-new | not-started |  |
| Huntington's disease | Genetic and congenital | covered-needs-refresh | medium | phase-2-refresh | is-huntingtons-disease | is-huntington-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Klinefelter syndrome | Genetic and congenital | missing | medium | phase-3-create-backlog |  | is-klinefelter-syndrome.html | no-final-file-yet | create-new | not-started |  |
| Marfan syndrome | Genetic and congenital | missing | medium | phase-3-create-backlog |  | is-marfan-syndrome.html | no-final-file-yet | create-new | not-started |  |
| Turner syndrome | Genetic and congenital | missing | medium | phase-3-create-backlog |  | is-turner-syndrome.html | no-final-file-yet | create-new | not-started |  |

## Gynaecological tract

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Bacterial vaginosis | Gynaecological tract | missing | medium | phase-3-create-backlog |  | is-bacterial-vaginosis.html | no-final-file-yet | create-new | not-started |  |
| Cervical cancer | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-cervical-cancer | is-cervical-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Cervical ectropion | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-cervical-ectropion | is-cervical-ectropion.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Cervical screening (human papilloma virus) | Gynaecological tract | missing | medium | phase-3-create-backlog |  | is-cervical-screening-human-papilloma-virus.html | no-final-file-yet | create-new | not-started |  |
| Endometrial cancer | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-endometrial-cancer | is-endometrial-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Endometriosis | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-endometriosis | is-endometriosis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Fibroids | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-fibroids | is-fibroids.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Genitourinary syndrome of menopause | Gynaecological tract | missing | medium | phase-3-create-backlog |  | is-genitourinary-syndrome-of-menopause.html | no-final-file-yet | create-new | not-started |  |
| Lichen sclerosus | Gynaecological tract | missing | medium | phase-3-create-backlog |  | is-lichen-sclerosus.html | no-final-file-yet | create-new | not-started |  |
| Menopause/ perimenopause | Gynaecological tract | missing | medium | phase-3-create-backlog |  | is-menopause-perimenopause.html | no-final-file-yet | create-new | not-started |  |
| Ovarian cancer | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-ovarian-cancer | is-ovarian-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Ovarian cysts | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-ovarian-cyst | is-ovarian-cysts.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Ovarian torsion | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-ovarian-torsion | is-ovarian-torsion.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Pelvic inflammatory disease | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-pelvic-inflammatory-disease | is-pelvic-inflammatory-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Polycystic ovary syndrome (PCOS) | Gynaecological tract | covered-needs-refresh | medium | phase-2-refresh | is-pcos | is-polycystic-ovary-syndrome-pcos.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Termination of pregnancy | Gynaecological tract | missing | medium | phase-3-create-backlog |  | is-termination-of-pregnancy.html | no-final-file-yet | create-new | not-started |  |
| Vaginal prolapse | Gynaecological tract | missing | medium | phase-3-create-backlog |  | is-vaginal-prolapse.html | no-final-file-yet | create-new | not-started |  |
| Vulval cancer | Gynaecological tract | missing | medium | phase-3-create-backlog |  | is-vulval-cancer.html | no-final-file-yet | create-new | not-started |  |

## Pregnancy and the puerperium

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Antepartum haemorrhage | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-antepartum-haemorrhage.html | no-final-file-yet | create-new | not-started |  |
| Blood group incompatibility in pregnancy | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-blood-group-incompatibility-in-pregnancy.html | no-final-file-yet | create-new | not-started |  |
| Chorioamnionitis | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-chorioamnionitis.html | no-final-file-yet | create-new | not-started |  |
| Complications of labour (including malpresentation, shoulder-dystocia, preterm labour, cord prolapse) | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-complications-of-labour-including-malpresentation-shoulder-dystocia-preterm-labour-cord-prolapse.html | no-final-file-yet | create-new | not-started |  |
| Diabetes in pregnancy (gestational and pre-existing) | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-diabetes-in-pregnancy-gestational-and-pre-existing.html | no-final-file-yet | create-new | not-started |  |
| Ectopic pregnancy | Pregnancy and the puerperium | covered-needs-refresh | high | phase-1-pilot | is-ectopic-pregnancy | is-ectopic-pregnancy.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Hyperemesis gravidarum | Pregnancy and the puerperium | covered-needs-refresh | high | phase-1-pilot | is-hyperemesis-gravidarum | is-hyperemesis-gravidarum.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hypertension in pregnancy (including gestational hypertension, pre-eclampsia, eclampsia) | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-hypertension-in-pregnancy-including-gestational-hypertension-pre-eclampsia-eclampsia.html | no-final-file-yet | create-new | not-started |  |
| Jaundice in pregnancy | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-jaundice-in-pregnancy.html | no-final-file-yet | create-new | not-started |  |
| Miscarriage and intrauterine death | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-miscarriage-and-intrauterine-death.html | no-final-file-yet | create-new | not-started |  |
| Multiple pregnancy | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-multiple-pregnancy.html | no-final-file-yet | create-new | not-started |  |
| Obesity in pregnancy | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-obesity-in-pregnancy.html | no-final-file-yet | create-new | not-started |  |
| Placenta praevia | Pregnancy and the puerperium | covered-needs-refresh | high | phase-1-pilot | is-placenta-praevia | is-placenta-praevia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Placental abruption | Pregnancy and the puerperium | covered-needs-refresh | high | phase-1-pilot | is-placental-abruption | is-placental-abruption.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Polyhydramnios/ oligohydramnios | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-polyhydramnios-oligohydramnios.html | no-final-file-yet | create-new | not-started |  |
| Postpartum haemorrhage | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-postpartum-haemorrhage.html | no-final-file-yet | create-new | not-started |  |
| Vasa praevia | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-vasa-praevia.html | no-final-file-yet | create-new | not-started |  |
| Venous thromboembolism (VTE) in pregnancy and puerperium | Pregnancy and the puerperium | missing | high | phase-3-create-priority |  | is-venous-thromboembolism-vte-in-pregnancy-and-puerperium.html | no-final-file-yet | create-new | not-started |  |

## Male genitourinary tract

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Benign prostatic hyperplasia | Male genitourinary tract | covered-needs-refresh | medium | phase-2-refresh | is-benign-prostatic-hypertrophy | is-benign-prostatic-hyperplasia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hydrocoele/ varicocoele/ epididymal cyst | Male genitourinary tract | missing | medium | phase-3-create-backlog |  | is-hydrocoele-varicocoele-epididymal-cyst.html | no-final-file-yet | create-new | not-started |  |
| Penile cancer | Male genitourinary tract | missing | medium | phase-3-create-backlog |  | is-penile-cancer.html | no-final-file-yet | create-new | not-started |  |
| Phimosis/ paraphimosis | Male genitourinary tract | missing | medium | phase-3-create-backlog |  | is-phimosis-paraphimosis.html | no-final-file-yet | create-new | not-started |  |
| Prostate cancer | Male genitourinary tract | covered-needs-refresh | medium | phase-2-refresh | is-metastatic-cancer-prostate-cancer; is-prostate-cancer | is-prostate-cancer.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Prostatitis, epididymitis and orchitis | Male genitourinary tract | missing | medium | phase-3-create-backlog |  | is-prostatitis-epididymitis-and-orchitis.html | no-final-file-yet | create-new | not-started |  |
| Testicular cancer | Male genitourinary tract | missing | medium | phase-3-create-backlog |  | is-testicular-cancer.html | no-final-file-yet | create-new | not-started |  |
| Testicular torsion | Male genitourinary tract | covered-needs-refresh | medium | phase-2-refresh | is-testicular-torsion | is-testicular-torsion.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Brain and spinal cord

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Brain abscess | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-brain-abscess | is-brain-abscess.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Brain tumours (primary and secondary) | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-brain-tumour | is-brain-tumours-primary-and-secondary.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Cerebral palsy and hypoxic-ischaemic encephalopathy | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-cerebral-palsy-and-hypoxic-ischaemic-encephalopathy.html | no-final-file-yet | create-new | not-started |  |
| Cerebral venous sinus thrombosis (CVST) | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-cvst.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. Canonical final filename intentionally shortened to is-cvst.html. |
| Delirium | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-delirium; is-medication-induced-delirium | is-delirium.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Dementias (including Alzheimer dementia, Lewy-Body dementia, frontotemporal dementia, vascular dementia) | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-dementias-including-alzheimer-dementia-lewy-body-dementia-frontotemporal-dementia-vascular-dementia.html | no-final-file-yet | create-new | not-started |  |
| Encephalitis | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-encephalitis | is-encephalitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Epilepsy | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-epilepsy | is-epilepsy.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Essential tremor | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-essential-tremor | is-essential-tremor.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Extradural haemorrhage | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-extradural-haemorrhage.html | no-final-file-yet | create-new | not-started |  |
| Idiopathic intracranial hypertension | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-idiopathic-intracranial-hypertension | is-idiopathic-intracranial-hypertension.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Meningitis | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-meningitis | is-meningitis.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Motor neurone disease | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-motor-neurone-disease | is-motor-neurone-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Multiple sclerosis (MS) | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-multiple-sclerosis | is-multiple-sclerosis-ms.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Parkinsonism (including Parkinson disease) | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-parkinsonism-including-parkinson-disease.html | no-final-file-yet | create-new | not-started |  |
| Primary headache disorders (including migraine, cluster headache, tension headache) | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-primary-headache-disorders-including-migraine-cluster-headache-tension-headache.html | no-final-file-yet | create-new | not-started |  |
| Raised intracranial pressure | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-raised-intracranial-pressure | is-raised-intracranial-pressure.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Spinal cord compression | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-cervical-cord-compression; is-spinal-cord-compression | is-spinal-cord-compression.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Spinal cord injury | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-spinal-cord-injury.html | no-final-file-yet | create-new | not-started |  |
| Status epilepticus | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-status-epilepticus.html | no-final-file-yet | create-new | not-started |  |
| Stroke | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-stroke.html | no-final-file-yet | create-new | not-started |  |
| Subarachnoid haemorrhage | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-subarachnoid-haemorrhage | is-subarachnoid-haemorrhage.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Subdural haemorrhage | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-subdural-haemorrhage.html | no-final-file-yet | create-new | not-started |  |
| Transient ischaemic attacks (TIA) | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-transient-ischaemic-attack | is-transient-ischaemic-attacks-tia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Vestibular schwannoma (acoustic neuroma) | Brain and spinal cord | covered-needs-refresh | high | phase-1-pilot | is-acoustic-neuroma | is-vestibular-schwannoma-acoustic-neuroma.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Wernicke encephalopathy/ Wernicke-Korsakoff syndrome | Brain and spinal cord | missing | high | phase-3-create-priority |  | is-wernicke-encephalopathy-wernicke-korsakoff-syndrome.html | no-final-file-yet | create-new | not-started |  |

## Peripheral nervous system and neuromuscular junction

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Autonomic neuropathy | Peripheral nervous system and neuromuscular junction | covered-needs-refresh | medium | phase-2-refresh | is-autonomic-neuropathy; is-diabetic-autonomic-neuropathy | is-autonomic-neuropathy.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Bell palsy | Peripheral nervous system and neuromuscular junction | covered-needs-refresh | medium | phase-2-refresh | is-bells-palsy | is-bell-palsy.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Guillain- Barré/ inflammatory demyelinating polyneuropathy | Peripheral nervous system and neuromuscular junction | missing | medium | phase-3-create-backlog |  | is-guillain-barr-inflammatory-demyelinating-polyneuropathy.html | no-final-file-yet | create-new | not-started |  |
| Muscular dystrophies | Peripheral nervous system and neuromuscular junction | missing | medium | phase-3-create-backlog |  | is-muscular-dystrophies.html | no-final-file-yet | create-new | not-started |  |
| Myasthenia gravis | Peripheral nervous system and neuromuscular junction | covered-needs-refresh | medium | phase-2-refresh | is-myasthenia-gravis | is-myasthenia-gravis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Peripheral nerve injuries/ palsies | Peripheral nervous system and neuromuscular junction | missing | medium | phase-3-create-backlog |  | is-peripheral-nerve-injuries-palsies.html | no-final-file-yet | create-new | not-started |  |
| Peripheral neuropathy | Peripheral nervous system and neuromuscular junction | covered-needs-refresh | medium | phase-2-refresh | is-painful-peripheral-neuropathy; is-peripheral-neuropathy | is-peripheral-neuropathy.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Radiculopathies | Peripheral nervous system and neuromuscular junction | missing | medium | phase-3-create-backlog |  | is-radiculopathies.html | no-final-file-yet | create-new | not-started |  |
| Trigeminal neuralgia | Peripheral nervous system and neuromuscular junction | covered-needs-refresh | medium | phase-2-refresh | is-trigeminal-neuralgia | is-trigeminal-neuralgia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Mental health

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Acute stress reaction | Mental health | missing | medium | phase-3-create-backlog |  | is-acute-stress-reaction.html | no-final-file-yet | create-new | not-started |  |
| Alcohol withdrawal and opioid withdrawal | Mental health | missing | medium | phase-3-create-backlog |  | is-alcohol-withdrawal-and-opioid-withdrawal.html | no-final-file-yet | create-new | not-started |  |
| Attention deficit hyperactivity disorder (ADHD) | Mental health | missing | medium | phase-3-create-backlog |  | is-attention-deficit-hyperactivity-disorder-adhd.html | no-final-file-yet | create-new | not-started |  |
| Autism spectrum disorder (ASD) | Mental health | missing | medium | phase-3-create-backlog |  | is-autism-spectrum-disorder-asd.html | no-final-file-yet | create-new | not-started |  |
| Bipolar affective disorder (including mania/ hypomania) | Mental health | missing | medium | phase-3-create-backlog |  | is-bipolar-affective-disorder-including-mania-hypomania.html | no-final-file-yet | create-new | not-started |  |
| Delusional disorder | Mental health | missing | medium | phase-3-create-backlog |  | is-delusional-disorder.html | no-final-file-yet | create-new | not-started |  |
| Depression | Mental health | covered-needs-refresh | medium | phase-2-refresh | is-depression | is-depression.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Eating disorders | Mental health | covered-needs-refresh | medium | phase-2-refresh | is-eating-disorder | is-eating-disorders.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Gambling disorder | Mental health | missing | medium | phase-3-create-backlog |  | is-gambling-disorder.html | no-final-file-yet | create-new | not-started |  |
| Gender dysphoria and/ or incongruence | Mental health | missing | medium | phase-3-create-backlog |  | is-gender-dysphoria-and-or-incongruence.html | no-final-file-yet | create-new | not-started |  |
| Generalised anxiety disorder | Mental health | covered-needs-refresh | medium | phase-2-refresh | is-generalised-anxiety-disorder | is-generalised-anxiety-disorder.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Obsessive-compulsive disorder (OCD) | Mental health | missing | medium | phase-3-create-backlog |  | is-obsessive-compulsive-disorder-ocd.html | no-final-file-yet | create-new | not-started |  |
| Panic disorder | Mental health | covered-needs-refresh | medium | phase-2-refresh | is-panic-disorder | is-panic-disorder.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Personality disorder | Mental health | missing | medium | phase-3-create-backlog |  | is-personality-disorder.html | no-final-file-yet | create-new | not-started |  |
| Phobias (including agoraphobia) | Mental health | missing | medium | phase-3-create-backlog |  | is-phobias-including-agoraphobia.html | no-final-file-yet | create-new | not-started |  |
| Post traumatic stress disorder | Mental health | missing | medium | phase-3-create-backlog |  | is-post-traumatic-stress-disorder.html | no-final-file-yet | create-new | not-started |  |
| Postpartum depression | Mental health | missing | medium | phase-3-create-backlog |  | is-postpartum-depression.html | no-final-file-yet | create-new | not-started |  |
| Postpartum psychosis | Mental health | missing | medium | phase-3-create-backlog |  | is-postpartum-psychosis.html | no-final-file-yet | create-new | not-started |  |
| Psychotic disorder | Mental health | missing | medium | phase-3-create-backlog |  | is-psychotic-disorder.html | no-final-file-yet | create-new | not-started |  |
| Schizoaffective disorder | Mental health | missing | medium | phase-3-create-backlog |  | is-schizoaffective-disorder.html | no-final-file-yet | create-new | not-started |  |
| Schizophrenia | Mental health | covered-needs-refresh | medium | phase-2-refresh | is-psychosis-and-schizophrenia | is-schizophrenia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Self-harm | Mental health | missing | medium | phase-3-create-backlog |  | is-self-harm.html | no-final-file-yet | create-new | not-started |  |
| Somatic symptom disorder | Mental health | missing | medium | phase-3-create-backlog |  | is-somatic-symptom-disorder.html | no-final-file-yet | create-new | not-started |  |
| Substance use disorder | Mental health | missing | medium | phase-3-create-backlog |  | is-substance-use-disorder.html | no-final-file-yet | create-new | not-started |  |

## Ear, nose and throat

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Airway compromise/ management | Ear, nose and throat | missing | medium | phase-3-create-backlog |  | is-airway-compromise-management.html | no-final-file-yet | create-new | not-started |  |
| Benign paroxysmal positional vertigo (BPPV) | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-bppv | is-benign-paroxysmal-positional-vertigo-bppv.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Cholesteatoma | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-cholesteatoma | is-cholesteatoma.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Epiglottitis | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-epiglottitis | is-epiglottitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Epistaxis | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-epistaxis | is-epistaxis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Head and neck cancer (including oral, laryngeal and salivary gland) | Ear, nose and throat | missing | medium | phase-3-create-backlog |  | is-head-and-neck-cancer-including-oral-laryngeal-and-salivary-gland.html | no-final-file-yet | create-new | not-started |  |
| Labyrinthitis / vestibular neuritis | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-vestibular-neuritis | is-labyrinthitis-vestibular-neuritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Mastoiditis | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-mastoiditis | is-mastoiditis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Ménière disease | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-menieres-disease | is-mnire-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Nasal polyps | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-nasal-polyps | is-nasal-polyps.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Otitis externa | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-malignant-otitis-externa; is-otitis-externa | is-otitis-externa.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Otitis media | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-otitis-media | is-otitis-media.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Perforated eardrum | Ear, nose and throat | missing | medium | phase-3-create-backlog |  | is-perforated-eardrum.html | no-final-file-yet | create-new | not-started |  |
| Pharyngitis/ tonsillitis | Ear, nose and throat | missing | medium | phase-3-create-backlog |  | is-pharyngitis-tonsillitis.html | no-final-file-yet | create-new | not-started |  |
| Quinsy/ peritonsillar abscess | Ear, nose and throat | missing | medium | phase-3-create-backlog |  | is-quinsy-peritonsillar-abscess.html | no-final-file-yet | create-new | not-started |  |
| Rhinosinusitis | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-rhinosinusitis | is-rhinosinusitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Thyroid cancer | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-thyroid-cancer | is-thyroid-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Thyroid nodules | Ear, nose and throat | missing | medium | phase-3-create-backlog |  | is-thyroid-nodules.html | no-final-file-yet | create-new | not-started |  |
| Upper respiratory tract infection | Ear, nose and throat | covered-needs-refresh | medium | phase-2-refresh | is-urti | is-upper-respiratory-tract-infection.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Child health

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Biliary atresia | Child health | missing | high | phase-3-create-priority |  | is-biliary-atresia.html | no-final-file-yet | create-new | not-started |  |
| Bronchiolitis | Child health | covered-needs-refresh | high | phase-1-pilot | is-bronchiolitis | is-bronchiolitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Bronchopulmonary dysplasia (chronic lung disease of prematurity) | Child health | missing | high | phase-3-create-priority |  | is-bronchopulmonary-dysplasia-chronic-lung-disease-of-prematurity.html | no-final-file-yet | create-new | not-started |  |
| Childhood cancer (including retinoblastoma) | Child health | missing | high | phase-3-create-priority |  | is-childhood-cancer-including-retinoblastoma.html | no-final-file-yet | create-new | not-started |  |
| Childhood hip/ leg disorders (including Perthes disease, slipped upper femoral epiphyses, developmental dysplasia of the hip) | Child health | covered-needs-refresh | high | phase-1-pilot | is-developmental-dysplasia-of-the-hip | is-childhood-hip-leg-disorders-including-perthes-disease-slipped-upper-femoral-epiphyses-developmental-dysplasia-of-the-hip.html | legacy-source-only | defer | not-started | Legacy/archive source scripts exist in gap tracker. Explicitly deferred in short priority queue. |
| Cow milk protein allergy | Child health | covered-needs-refresh | high | phase-1-pilot | is-cows-milk-allergy | is-cow-milk-protein-allergy.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Croup | Child health | covered-needs-refresh | high | phase-1-pilot | is-croup | is-croup.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Cryptorchidism | Child health | missing | high | phase-3-create-priority |  | is-cryptorchidism.html | no-final-file-yet | create-new | not-started |  |
| Faltering growth (failure to thrive) | Child health | missing | high | phase-3-create-priority |  | is-faltering-growth-failure-to-thrive.html | no-final-file-yet | create-new | not-started |  |
| Febrile convulsions | Child health | covered-needs-refresh | high | phase-1-pilot | is-febrile-convulsions-children | is-febrile-convulsions.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Kawasaki disease | Child health | missing | high | phase-3-create-priority |  | is-kawasaki-disease.html | no-final-file-yet | create-new | not-started |  |
| Mesenteric adenitis | Child health | covered-needs-refresh | high | phase-1-pilot | is-mesenteric-adenitis | is-mesenteric-adenitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Necrotising enterocolitis | Child health | missing | high | phase-3-create-priority |  | is-necrotising-enterocolitis.html | no-final-file-yet | create-new | not-started |  |
| Neonatal jaundice (including pathological and physiological jaundice) | Child health | missing | high | phase-3-create-priority |  | is-neonatal-jaundice-including-pathological-and-physiological-jaundice.html | no-final-file-yet | create-new | not-started |  |
| Neonatal surgical emergencies (including pyloric stenosis, Intussusception) | Child health | missing | high | phase-3-create-priority |  | is-neonatal-surgical-emergencies-including-pyloric-stenosis-intussusception.html | no-final-file-yet | create-new | not-started |  |
| Prematurity | Child health | missing | high | phase-3-create-priority |  | is-prematurity.html | no-final-file-yet | create-new | not-started |  |
| Scarlet fever | Child health | missing | high | phase-3-create-priority |  | is-scarlet-fever.html | no-final-file-yet | create-new | not-started |  |
| Viral exanthema (including measles, rubella, varicella) | Child health | missing | high | phase-3-create-priority |  | is-viral-exanthema-including-measles-rubella-varicella.html | no-final-file-yet | create-new | not-started |  |
| Whooping cough | Child health | covered-needs-refresh | high | phase-1-pilot | is-whooping-cough | is-whooping-cough.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Infections

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Abscess | Infections | covered-needs-refresh | high | phase-1-pilot | is-anorectal-abscess; is-breast-abscess; is-iliopsoas-abscess; is-intra-abdominal-abscess; is-pelvic-abscess; is-peritonsillar-abscess; is-retropharyngeal-abscess; is-spinal-abscess | is-abscess.html | legacy-source-only | defer | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. Explicitly deferred in short priority queue. |
| COVID-19 | Infections | covered-needs-refresh | high | phase-1-pilot | is-covid-19 | is-covid-19.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Candidiasis | Infections | covered-needs-refresh | high | phase-1-pilot | is-oral-candidiasis | is-candidiasis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Chlamydia | Infections | covered-needs-refresh | high | phase-1-pilot | is-chlamydia | is-chlamydia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Gonorrhoea | Infections | covered-needs-refresh | high | phase-1-pilot | is-gonorrhoea | is-gonorrhoea.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Helicobacter pylori | Infections | missing | high | phase-3-create-priority |  | is-helicobacter-pylori.html | no-final-file-yet | create-new | not-started |  |
| Herpes simplex virus | Infections | missing | high | phase-3-create-priority |  | is-herpes-simplex-virus.html | no-final-file-yet | create-new | not-started |  |
| Hospital acquired infections | Infections | missing | high | phase-3-create-priority |  | is-hospital-acquired-infections.html | no-final-file-yet | create-new | not-started |  |
| Human immunodeficiency virus (HIV) | Infections | covered-needs-refresh | high | phase-1-pilot | is-hiv | is-human-immunodeficiency-virus-hiv.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Human papilloma virus infection | Infections | missing | high | phase-3-create-priority |  | is-human-papilloma-virus-infection.html | no-final-file-yet | create-new | not-started |  |
| Infectious mononucleosis (including Epstein-Barr virus, cytomegalovirus) | Infections | missing | high | phase-3-create-priority |  | is-infectious-mononucleosis-including-epstein-barr-virus-cytomegalovirus.html | no-final-file-yet | create-new | not-started |  |
| Influenza | Infections | covered-needs-refresh | high | phase-1-pilot | is-influenza | is-influenza.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Malaria | Infections | missing | high | phase-3-create-priority |  | is-malaria.html | no-final-file-yet | create-new | not-started |  |
| Measles | Infections | covered-needs-refresh | high | phase-1-pilot | is-measles | is-measles.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Mumps | Infections | missing | high | phase-3-create-priority |  | is-mumps.html | no-final-file-yet | create-new | not-started |  |
| Pyrexia of unknown origin | Infections | missing | high | phase-3-create-priority |  | is-pyrexia-of-unknown-origin.html | no-final-file-yet | create-new | not-started |  |
| Rubella | Infections | covered-needs-refresh | high | phase-1-pilot | is-rubella | is-rubella.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Sepsis (including neutropenic sepsis) | Infections | missing | high | phase-3-create-priority |  | is-sepsis-including-neutropenic-sepsis.html | no-final-file-yet | create-new | not-started |  |
| Surgical site infection | Infections | missing | high | phase-3-create-priority |  | is-surgical-site-infection.html | no-final-file-yet | create-new | not-started |  |
| Syphilis | Infections | missing | high | phase-3-create-priority |  | is-syphilis.html | no-final-file-yet | create-new | not-started |  |
| Tetanus | Infections | missing | high | phase-3-create-priority |  | is-tetanus.html | no-final-file-yet | create-new | not-started |  |
| Toxic shock syndrome | Infections | missing | high | phase-3-create-priority |  | is-toxic-shock-syndrome.html | no-final-file-yet | create-new | not-started |  |
| Toxoplasmosis | Infections | missing | high | phase-3-create-priority |  | is-toxoplasmosis.html | no-final-file-yet | create-new | not-started |  |
| Trichomonas vaginalis | Infections | missing | high | phase-3-create-priority |  | is-trichomonas-vaginalis.html | no-final-file-yet | create-new | not-started |  |
| Tuberculosis | Infections | covered-needs-refresh | high | phase-1-pilot | is-spinal-tuberculosis; is-tuberculosis; is-tuberculosis-lymphadenopathy; is-urinary-tract-tuberculosis | is-tuberculosis.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Typhoid | Infections | missing | high | phase-3-create-priority |  | is-typhoid.html | no-final-file-yet | create-new | not-started |  |
| Varicella zoster virus | Infections | missing | high | phase-3-create-priority |  | is-varicella-zoster-virus.html | no-final-file-yet | create-new | not-started |  |
| Zoonotic infections (including Lyme disease) | Infections | covered-needs-refresh | high | phase-1-pilot | is-lyme-disease | is-zoonotic-infections-including-lyme-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Breast

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Breast abscess/ mastitis | Breast | missing | medium | phase-3-create-backlog |  | is-breast-abscess-mastitis.html | no-final-file-yet | create-new | not-started |  |
| Breast cancer | Breast | covered-needs-refresh | medium | phase-2-refresh | is-breast-cancer | is-breast-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Breast cysts | Breast | missing | medium | phase-3-create-backlog |  | is-breast-cysts.html | no-final-file-yet | create-new | not-started |  |
| Fibroadenoma | Breast | missing | medium | phase-3-create-backlog |  | is-fibroadenoma.html | no-final-file-yet | create-new | not-started |  |

## Kidneys and urinary tract

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Acid-base abnormality | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-acid-base-abnormality.html | no-final-file-yet | create-new | not-started |  |
| Acute kidney injury | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-acute-kidney-injury.html | no-final-file-yet | create-new | not-started |  |
| Bladder cancer | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-bladder-cancer | is-bladder-cancer.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Chronic kidney disease | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-anaemia-of-chronic-disease; is-chronic-kidney-disease | is-chronic-kidney-disease.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| End stage renal disease (including renal replacement therapy and transplantation) | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-end-stage-renal-disease-including-renal-replacement-therapy-and-transplantation.html | no-final-file-yet | create-new | not-started |  |
| Glomerulonephritis | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-glomerulonephritis | is-glomerulonephritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Hydronephrosis | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-hydronephrosis.html | no-final-file-yet | create-new | not-started |  |
| Hypercalcaemia/ hypocalcaemia | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-hypercalcaemia-hypocalcaemia.html | no-final-file-yet | create-new | not-started |  |
| Hyperkalaemia/ hypokalaemia | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-hyperkalaemia-hypokalaemia.html | no-final-file-yet | create-new | not-started |  |
| Hyponatraemia/ hypernatraemia | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-hyponatraemia-hypernatraemia.html | no-final-file-yet | create-new | not-started |  |
| IgA vasculitis | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-iga-vasculitis.html | no-final-file-yet | create-new | not-started |  |
| Nephrotic syndrome | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-nephrotic-syndrome | is-nephrotic-syndrome.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Polycystic kidney disease | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-pckd | is-polycystic-kidney-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Pyelonephritis | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-pyelonephritis | is-pyelonephritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Renal cancer | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-renal-cancer.html | no-final-file-yet | create-new | not-started |  |
| Rhabdomyolysis | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-rhabdomyolysis; is-statin-related-myopathy-inc-rhabdomyolysis | is-rhabdomyolysis.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Urinary incontinence | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-urinary-incontinence.html | no-final-file-yet | create-new | not-started |  |
| Urinary retention/ obstructive uropathy | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-acute-urinary-retention | is-urinary-retention-obstructive-uropathy.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Urinary tract calculi | Kidneys and urinary tract | missing | medium | phase-3-create-backlog |  | is-urinary-tract-calculi.html | no-final-file-yet | create-new | not-started |  |
| Urinary tract infection | Kidneys and urinary tract | covered-needs-refresh | medium | phase-2-refresh | is-genito-urinary-tract-infection; is-uti | is-urinary-tract-infection.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |

## Musculoskeletal

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Bone tumours | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-bone-tumours-primary-and-secondary-including-osteosarcoma-ewing-sarcoma.html | no-final-file-yet | create-new | not-started |  |
| Bursitis | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-bursitis; is-olecranon-bursitis; is-prepatellar-bursitis; is-trochanteric-bursitis | is-bursitis.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Cauda equina syndrome | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-cauda-equina-syndrome | is-cauda-equina-syndrome.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Complications of fractures (including compartment syndrome, non-union, malunion, avascular necrosis) | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-complications-of-fractures-including-compartment-syndrome-non-union-malunion-avascular-necrosis.html | no-final-file-yet | create-new | not-started |  |
| Crystal arthropathy | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-crystal-arthropathy.html | no-final-file-yet | create-new | not-started |  |
| Fibromyalgia | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-fibromyalgia | is-fibromyalgia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Fracture(s) (including pathological fractures) | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-fractures-including-pathological-fractures.html | no-final-file-yet | create-new | not-started |  |
| Giant cell arteritis | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-temporal-arteritis-gca | is-giant-cell-arteritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Intervertebral disc prolapse | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-lumbar-disc-prolapse | is-intervertebral-disc-prolapse.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Joint dislocation or subluxation | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-fracture-or-dislocation | is-joint-dislocation-or-subluxation.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Juvenile idiopathic arthritis | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-juvenile-idiopathic-arthritis | is-juvenile-idiopathic-arthritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Lower back pain and sciatica | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-lower-back-pain-and-sciatica.html | no-final-file-yet | create-new | not-started |  |
| Osteoarthritis | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-knee-osteoarthritis; is-osteoarthritis; is-shoulder-osteoarthritis | is-osteoarthritis.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Osteomalacia | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-osteomalacia | is-osteomalacia.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Osteomyelitis | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-osteomyelitis | is-osteomyelitis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Osteoporosis and fragility fractures | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-osteoporosis-and-fragility-fractures.html | no-final-file-yet | create-new | not-started |  |
| Polymyalgia rheumatica | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-polymyalgia-rheumatica; is-polymyalgia-rheumatica-gca | is-polymyalgia-rheumatica.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Polymyositis and dermatomyositis | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-polymyositis-and-dermatomyositis.html | no-final-file-yet | create-new | not-started |  |
| Raynaud phenomenon | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-raynaud-phenomenon.html | no-final-file-yet | create-new | not-started |  |
| Rheumatoid arthritis | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-rheumatoid-arthritis | is-rheumatoid-arthritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Scleroderma and mixed connective tissue disease | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-connective-tissue-diseases | is-scleroderma-and-mixed-connective-tissue-disease.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Septic arthritis | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-septic-arthritis | is-septic-arthritis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Seronegative spondyloarthropathies (including ankylosing spondylitis, reactive arthritis, enteropathic arthritis, psoriatic arthritis) | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-seronegative-spondyloarthropathies-including-ankylosing-spondylitis-reactive-arthritis-enteropathic-arthritis-psoriatic-arthritis.html | no-final-file-yet | create-new | not-started |  |
| Sjogren syndrome | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-sjogrens-syndrome | is-sjogren-syndrome.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Soft tissue injury | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-soft-tissue-injury | is-soft-tissue-injury.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Systemic lupus erythematosus | Musculoskeletal | covered-needs-refresh | medium | phase-2-refresh | is-systemic-lupus-erythematosus | is-systemic-lupus-erythematosus.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Vasculitis/ vasculitides | Musculoskeletal | missing | medium | phase-3-create-backlog |  | is-vasculitis-vasculitides.html | no-final-file-yet | create-new | not-started |  |

## Drugs and drug effects

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Adverse drug effects | Drugs and drug effects | missing | high | phase-3-create-priority |  | is-adverse-drug-effects.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Drug overdose | Drugs and drug effects | missing | high | phase-3-create-priority |  | is-drug-overdose.html | canonical-final-exists | refresh-existing | drafted | Canonical final file present in final folder. |
| Neuroleptic malignant syndrome | Drugs and drug effects | missing | high | phase-3-create-priority |  | is-neuroleptic-malignant-syndrome.html | no-final-file-yet | create-new | not-started |  |
| Serotonin syndrome | Drugs and drug effects | covered-needs-refresh | high | phase-1-pilot | is-serotonin-syndrome | is-serotonin-syndrome.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Multi-system diseases

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Allergic disorder (including food allergy) | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-allergic-disorder-including-food-allergy.html | no-final-file-yet | create-new | not-started |  |
| Anaphylaxis | Multi-system diseases | covered-needs-refresh | medium | phase-2-refresh | is-anaphylaxis | is-anaphylaxis.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Carbon monoxide poisoning | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-carbon-monoxide-poisoning.html | no-final-file-yet | create-new | not-started |  |
| Hyperthermia and hypothermia | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-hyperthermia-and-hypothermia.html | no-final-file-yet | create-new | not-started |  |
| Hypovolaemia/ volume depletion | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-hypovolaemia-volume-depletion.html | no-final-file-yet | create-new | not-started |  |
| Incidental finding | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-incidental-finding.html | no-final-file-yet | create-new | not-started |  |
| Infertility/ subfertility | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-infertility-subfertility.html | no-final-file-yet | create-new | not-started |  |
| Malnutrition | Multi-system diseases | covered-needs-refresh | medium | phase-2-refresh | is-malnutrition | is-malnutrition.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Medically unexplained symptoms | Multi-system diseases | covered-needs-refresh | medium | phase-2-refresh | is-medically-unexplained-symptoms | is-medically-unexplained-symptoms.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Metastatic cancer | Multi-system diseases | covered-needs-refresh | medium | phase-2-refresh | is-metastatic-cancer; is-metastatic-cancer-chest-wall | is-metastatic-cancer.html | legacy-source-only | cluster-resolution-first | not-started | Legacy/archive source scripts exist in gap tracker. Multiple matched scripts; canonicalisation needed before drafting. |
| Multi-organ dysfunction syndrome | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-multi-organ-dysfunction-syndrome.html | no-final-file-yet | create-new | not-started |  |
| Myalgic encephalomyelitis (ME)/ chronic fatigue syndrome (CFS) | Multi-system diseases | covered-needs-refresh | medium | phase-2-refresh | is-chronic-fatigue-syndrome | is-myalgic-encephalomyelitis-me-chronic-fatigue-syndrome-cfs-awareness-and-approach.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Obesity | Multi-system diseases | covered-needs-refresh | medium | phase-2-refresh | is-obesity | is-obesity.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Sarcopenia/ frailty | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-sarcopenia-frailty.html | no-final-file-yet | create-new | not-started |  |
| Transplantation (including graft rejection and immunosuppression) | Multi-system diseases | missing | medium | phase-3-create-backlog |  | is-transplantation-including-graft-rejection-and-immunosuppression.html | no-final-file-yet | create-new | not-started |  |
| Vitamin B12 and/ or folate deficiency | Multi-system diseases | covered-needs-refresh | medium | phase-2-refresh | is-vitamin-b12-deficiency | is-vitamin-b12-and-or-folate-deficiency.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |
| Vitamin D deficiency | Multi-system diseases | covered-needs-refresh | medium | phase-2-refresh | is-vitamin-d-deficiency | is-vitamin-d-deficiency.html | legacy-source-only | refresh-existing | not-started | Legacy/archive source scripts exist in gap tracker. |

## Other knowledge

| Condition | Category | Gap tracker status | Priority | Phase | Matched scripts | Canonical final target | Current final file status | Next action | Review status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Disease prevention/ screening | Other knowledge | missing | medium | phase-3-create-backlog |  | is-disease-prevention-screening.html | no-final-file-yet | create-new | not-started |  |
| Iatrogenic condition | Other knowledge | missing | medium | phase-3-create-backlog |  | is-iatrogenic-condition.html | no-final-file-yet | create-new | not-started |  |
| Non-accidental injury | Other knowledge | missing | medium | phase-3-create-backlog |  | is-non-accidental-injury.html | no-final-file-yet | create-new | not-started |  |
| Notifiable diseases | Other knowledge | missing | medium | phase-3-create-backlog |  | is-notifiable-diseases.html | no-final-file-yet | create-new | not-started |  |

## Verification Notes

- Tracker rows generated: $totalRows.
- Existing final HTML files referenced in tracker: $(is-acute-coronary-syndromes.html is-aortic-aneurysm.html is-aortic-dissection.html is-arterial-thrombosis-embolism.html is-cardiomyopathy.html is-deep-vein-thrombosis.html is-heart-failure.html is-infective-endocarditis.html is-pulmonary-embolism.html is-acute-bronchitis.html is-asthma.html is-copd.html is-empyema.html is-pneumonia.html is-pneumothorax.html is-ectopic-pregnancy.html is-cvst.html is-meningitis.html is-adverse-drug-effects.html is-drug-overdose.html.Count).
- Any mismatch between final-folder filenames and canonical tracker targets should be treated as a naming or mapping issue to resolve before broad scaling.
