# Sesame AIDR Image Analysis Results

Based on the internal AIDR summary file, there are 97 images flagged by the AI-image-recognition system (“AIDR images”) and 127 original images across 22 LinkedIn personas. The summary below was last updated on 2025-08-23 19:06 UTC. The AIDR report lists which features triggered the AI detection (ears, eyes, nose, etc.) for each persona. Research on how to spot AI-generated photos notes that generative models often mis-place facial features, producing odd eyes, noses or ears; they may also struggle with accessories like hats or glasses and generate oversaturated skin or “waxy” faces. Experts caution, however, that individual anomalies can occur naturally—people may genuinely have unusual features or extra fingers—so false positives are possible.

### AIDR AI-detection results by person

| Persona | AIDR images / total images | Features flagged by AI | Approx. probability of AI-generated profile* |
| --- | --- | --- | --- |
| **Alia-De-Jesus** | 4 / 9 (44 %) | eyes, face, mouth, nose | **Medium-high (~65%)** |
| **Angela-Gayles** | 5 / 11 (45 %) | eyes, face, head, mouth, nose | **Medium-high (~65%)** |
| **Ben-Rodrian** | 6 / 13 (46 %) | chin, eyes, face, hat, mouth, nose | **High (~70%)** |
| **Chris-Ronne** | 4 / 9 (44 %) | eyes, mouth, nose, profile_face | **Medium-high (~60%)** |
| **Chris-Yabsley** | 4 / 9 (44 %) | ear, eyes, face, nose | **Medium-high (~60%)** |
| **David-Braun** | 5 / 11 (45 %) | eyes, face, head, mouth, nose | **Medium-high (~65%)** |
| **Han-Roh** | 5 / 11 (45 %) | eyes, face, head, mouth, nose | **Medium-high (~65%)** |
| **Jacob-Van-Wingen** | 4 / 9 (44 %) | eyes, face, head, nose | **Medium-high (~60%)** |
| **Justin-Alvey** | 4 / 9 (44 %) | eyes, face, head, nose | **Medium-high (~60%)** |
| **Justin-Singer** | 3 / 8 (38 %) | eyes, face, head | **Medium (~50%)** |
| **Lee-Cooper** | 5 / 11 (45 %) | eyes, face, head, mouth, nose | **Medium-high (~65%)** |
| **Mark-Bu** | 3 / 7 (43 %) | eyes, hand_drink_glass, head | **Medium (~55%)** |
| **Natalie-Dunnege** | 2 / 6 (33 %) | eyes, mouth | **Low (~45%)** |
| **Neal-Manaktola** | 3 / 8 (38 %) | eyes, face, head | **Medium (~50%)** |
| **Paul-Stamatiou** | 6 / 16 (38 %) | beard, ear, glasses, hat, mouth, nose | **Medium (~55%)** |
| **Roduardo-Villafane** | 5 / 11 (45 %) | eyes, face, head, mouth, nose | **Medium-high (~65%)** |
| **Ryan-Brown** | 5 / 12 (42 %) | chin, eyes, face, head, mouth | **Medium-high (~60%)** |
| **Sam-Resnick** | 5 / 11 (45 %) | eyes, face, head, mouth, nose | **Medium-high (~65%)** |
| **Sean-McBeath** | 6 / 13 (46 %) | chin, eyes, face, head, mouth, nose | **High (~70%)** |
| **Sheldon-Nelson** | 5 / 11 (45 %) | eyes, face, head, mouth, nose | **Medium-high (~65%)** |
| **Xiao-Qin** | 4 / 9 (44 %) | glasses, head, mouth, nose | **Medium-high (~60%)** |
| **Zach-Little** | 4 / 10 (40 %) | eyes, face, mouth, nose | **Medium-high (~60%)** |

*Probabilities are approximate judgments derived from the proportion of AIDR-flagged images and the types of features flagged; they are not definitive labels.


### Probability derivation and limitations

The probability column applies a simple heuristic based on two factors:

1. **Flagged-image ratio** – the share of images marked by AIDR for each persona.
2. **Feature weighting** – a +5% adjustment for each distinct core facial feature flagged (eyes, nose, mouth, head/face); accessories such as glasses or hats contribute at most +2%.

The estimate is calculated as:

`p ≈ (flagged images ÷ total images) × 100% + feature adjustment`

Rounded to the nearest five percent, results are mapped to qualitative labels (e.g., “Medium”, “Medium-high”).

**Assumptions and limitations**

- Each image and feature is treated as an independent indicator, though correlations are possible.
- Weightings are analyst judgment, not statistically validated; they do not reflect AIDR confidence scores.
- Sample sizes are small, and AIDR’s false-positive/false-negative rates are not quantified here.
- Manual review and ground-truth images are required for high confidence.

Further background on methodology and detection reliability appears in the [LinkedIn Infiltration Research Plan](../../Intelligence-Analyst/LinkedIn_Infiltration_Research_Plan.md) and broader context in the [MSS LinkedIn Infiltration Analysis](../../MSS_LinkedIn_Infiltration_Analysis__CLAUDE.md) with supporting references in [MSS_LinkedIn_refs.md](../../MSS_LinkedIn_refs.md).

### Interpretation

The AI-image-recognition system flagged facial features—eyes, nose, head shape, and mouths—most often. Academic and practitioner articles on AI-generated images explain that these areas frequently contain artifacts: generative models may mis-place eyes or noses, produce mismatched ears, or create overly smooth and shiny skin. Accessories such as hats, glasses or jewelry may also appear distorted. Thus, individuals with multiple facial features flagged and a high proportion of suspect images (e.g., David-Braun, Lee-Cooper, Roduardo-Villafane, Sam-Resnick, and Sheldon-Nelson) were assessed with a medium-high probability of being AI-generated profiles.

However, AI-detection is not infallible. The research emphasises that some anomalies can occur naturally, and singular artifacts (e.g., an ear appearing odd or a missing finger) do not conclusively prove an image is synthetic. As such, the probabilities above are only indicative; manual inspection and cross-comparison with trusted photographs would be necessary for conclusive attribution.

