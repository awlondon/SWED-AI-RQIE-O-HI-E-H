# Fabrication-Suspected LinkedIn Profiles

This directory contains subfolders for personas believed to be AI-fabricated. For broader context, see the parent [LinkedIn README](../../README.md).

Each profile includes:

- `*_profile_full.png` – screenshot of the full LinkedIn profile image.
- Feature crops such as `eyes.png` or `nose.png` and their corresponding `*_AIDR.png` overlays highlighting anomalies found by the AI-image-detection pipeline (AIDR).
- Images may contain embedded text captured through OCR.

Summary statistics and probabilities derived from these AIDR outputs are tracked in `RESULTS.md`.

## Related Datasets
- [`fake_profiles.csv`](../../../datasets/fake_profiles.csv) – suspected synthetic or compromised LinkedIn profiles.

## Related Case Studies
- [Kevin Mallory](../../../case-studies/kevin-mallory/README.md) – contacted via LinkedIn and convicted of espionage.
- [Yanjun Xu](../../../case-studies/yanjun-xu/README.md) – used talent recruitment programs for technology theft.

## Related Institutions
- [Sesame](../../../institutions/sesame/README.md) – corporate background and linked personas.
- [Zinn Labs](../../../institutions/zinn-labs/README.md) – acquisition details and technology considerations.
