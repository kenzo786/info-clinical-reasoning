# Primary-Care Minor-Illness Tracker

This tracker now covers the full `33`-topic `pcmi` editorial programme.

Status flow:
- `queued`
- `in polish`
- `polished awaiting batch QA`
- `published`
- `needs later editorial revisit`

Current state:
- the full corpus has been structurally uplifted to the richer DRx-style `pcmi` model
- the tracker below reflects the current editorial state before a final batch-by-batch human QA sign-off
- scores are working internal editorial scores, not external clinical accreditation scores

| Canonical slug | Baseline score | Polished reference score | Polished markmap score | Combined editorial score | Batch | Status | Residual issues |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pcmi-acute-cough` | `8.0/10` | `9.4/10` | `9.4/10` | `9.4/10` | `0` | `polished awaiting batch QA` | Could still add even finer antimicrobial-stewardship prompts for borderline pneumonia decisions. |
| `pcmi-back-pain` | `7.9/10` | `9.4/10` | `9.4/10` | `9.4/10` | `0` | `polished awaiting batch QA` | Could still deepen occupational advice and radicular follow-up nuance. |
| `pcmi-emergency-hormonal-contraception` | `8.3/10` | `9.4/10` | `9.4/10` | `9.4/10` | `0` | `polished awaiting batch QA` | Could still refine a few wording points around repeat UPSI and ongoing contraception timing. |
| `pcmi-headache` | `8.2/10` | `9.4/10` | `9.4/10` | `9.4/10` | `0` | `polished awaiting batch QA` | Could still tighten the migraine-vs-secondary-headache decision teaching in a few subsections. |
| `pcmi-vaginal-thrush` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `0` | `polished awaiting batch QA` | Could still make recurrent-disease long-term planning more explicit. |
| `pcmi-cystitis-uti` | `8.1/10` | `9.4/10` | `9.3/10` | `9.4/10` | `1` | `polished awaiting batch QA` | Could still add slightly sharper stewardship wording around delayed scripts and cultures. |
| `pcmi-earache` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `1` | `polished awaiting batch QA` | Could still sharpen referred-pain teaching and TMJ/dental discrimination. |
| `pcmi-acute-otitis-media` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `1` | `polished awaiting batch QA` | Could still add one more novice prompt around bilateral disease in children under 2. |
| `pcmi-otitis-externa` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `1` | `polished awaiting batch QA` | Could still deepen wick / canal-swelling escalation nuance. |
| `pcmi-shingles` | `8.1/10` | `9.3/10` | `9.3/10` | `9.3/10` | `1` | `polished awaiting batch QA` | Could still expand post-herpetic neuralgia follow-up prompts. |
| `pcmi-acute-sore-throat` | `8.1/10` | `9.3/10` | `9.3/10` | `9.3/10` | `2` | `polished awaiting batch QA` | Could still sharpen FeverPAIN stewardship wording and quinsy escalation prompts. |
| `pcmi-acute-sinusitis` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `2` | `polished awaiting batch QA` | Could still make orbital-complication teaching even more prominent. |
| `pcmi-fever` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `2` | `polished awaiting batch QA` | Could still add a little more age-stratified wording for adults vs children. |
| `pcmi-bacterial-conjunctivitis` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `2` | `polished awaiting batch QA` | Could still increase the contrast with painful red-eye emergencies. |
| `pcmi-allergic-conjunctivitis` | `8.0/10` | `9.2/10` | `9.3/10` | `9.3/10` | `2` | `polished awaiting batch QA` | Could still add more explicit counselling on contact lenses and eye red flags. |
| `pcmi-contact-dermatitis` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `3` | `polished awaiting batch QA` | Could still make allergic-vs-irritant trigger differentiation more teachy. |
| `pcmi-scabies` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `3` | `polished awaiting batch QA` | Could still make malathion fallback and outbreak logistics more explicit. |
| `pcmi-impetigo` | `8.1/10` | `9.3/10` | `9.3/10` | `9.3/10` | `3` | `polished awaiting batch QA` | Could still sharpen local-vs-widespread treatment thresholds. |
| `pcmi-insect-bites-and-stings` | `8.0/10` | `9.2/10` | `9.3/10` | `9.3/10` | `3` | `polished awaiting batch QA` | Could still make large-local-reaction vs cellulitis discrimination even clearer. |
| `pcmi-chickenpox` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `3` | `polished awaiting batch QA` | Could still deepen pregnancy and immunosuppression counselling. |
| `pcmi-acute-diarrhoea` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `4` | `polished awaiting batch QA` | Could still expand travel / C. difficile decision prompts. |
| `pcmi-constipation` | `8.0/10` | `9.2/10` | `9.2/10` | `9.2/10` | `4` | `polished awaiting batch QA` | Could still make named laxative examples more explicit in the map and source. |
| `pcmi-dyspepsia-indigestion` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `4` | `polished awaiting batch QA` | Could still refine ulcer-risk / cardiac-mimic prompts. |
| `pcmi-common-cold-and-nasal-congestion` | `8.0/10` | `9.2/10` | `9.2/10` | `9.2/10` | `4` | `polished awaiting batch QA` | Could still make rebound-congestion and decongestant cautions more explicit. |
| `pcmi-hay-fever-allergic-rhinitis` | `8.0/10` | `9.2/10` | `9.2/10` | `9.2/10` | `4` | `polished awaiting batch QA` | Could still convert more generic treatment classes into named medicine examples. |
| `pcmi-oral-thrush-in-adults` | `8.0/10` | `9.3/10` | `9.2/10` | `9.3/10` | `5` | `polished awaiting batch QA` | Could still make nystatin-vs-miconazole choice more explicit in management. |
| `pcmi-haemorrhoids` | `8.0/10` | `9.3/10` | `9.3/10` | `9.3/10` | `5` | `polished awaiting batch QA` | Could still sharpen the bleeding differential and cancer-safe prompts. |
| `pcmi-cold-sores` | `8.0/10` | `9.2/10` | `9.3/10` | `9.3/10` | `5` | `polished awaiting batch QA` | Could still make oral antiviral thresholds more explicit. |
| `pcmi-athletes-foot` | `7.9/10` | `9.2/10` | `9.2/10` | `9.2/10` | `5` | `polished awaiting batch QA` | Could still deepen footwear / nail-involvement counselling. |
| `pcmi-mild-acne` | `8.0/10` | `9.2/10` | `9.2/10` | `9.2/10` | `5` | `polished awaiting batch QA` | Could still name benzoyl-peroxide-first pathways more explicitly in management. |
| `pcmi-head-lice` | `8.0/10` | `9.2/10` | `9.2/10` | `9.2/10` | `6` | `polished awaiting batch QA` | Could still add clearer wet-combing vs product-choice teaching. |
| `pcmi-threadworms` | `8.0/10` | `9.2/10` | `9.2/10` | `9.2/10` | `6` | `polished awaiting batch QA` | Could still deepen household-treatment logistics and pregnancy nuance. |
| `pcmi-warts-and-verrucas` | `7.9/10` | `9.2/10` | `9.2/10` | `9.2/10` | `6` | `polished awaiting batch QA` | Could still strengthen watchful-waiting vs destructive-treatment counselling. |

## Batch notes

- `Batch 0` is the richest exemplar batch and remains the closest to the chest-pain benchmark.
- `Batches 1-6` now share the same DRx-style structure, tighter deep-link alignment, and heavier JITL coverage.
- A final human QA pass should still close the remaining residual issues before calling every topic truly `published` at the new standard.
