# Sesame AIDR Image Analysis Results

Based on the internal AIDR summary file, there are 49 images flagged by the AI-image-recognition system (“AIDR images”) and 64 original images across 11 LinkedIn personas. The AIDR report lists which features triggered the AI detection (ears, eyes, nose, etc.) for each persona. Research on how to spot AI-generated photos notes that generative models often mis-place facial features, producing odd eyes, noses or ears; they may also struggle with accessories like hats or glasses and generate oversaturated skin or “waxy” faces. Experts caution, however, that individual anomalies can occur naturally—people may genuinely have unusual features or extra fingers—so false positives are possible.

### AIDR AI-detection results by person

| Persona                | AIDR images / total images | Features flagged by AI                | Approx. probability of AI-generated profile*                                                                                              |
| ---------------------- | -------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Chris-Yabsley**      | 4 / 9 (44 %)               | ear, eyes, face, nose                 | **Medium (~60 %)** – multiple facial features flagged and four of nine images are suspect, suggesting possible AI artifacts.              |
| **David-Braun**        | 5 / 11 (45 %)              | eyes, face, head, mouth, nose         | **Medium-high (~65 %)** – eyes, head shape and nose are common AI trouble-spots, and nearly half of images are flagged.                   |
| **Jacob-Van-Wingen**   | 4 / 9 (44 %)               | eyes, face, head, nose                | **Medium (~60 %)** – similar pattern of facial-feature anomalies.                                                                         |
| **Justin-Alvey**       | 4 / 9 (44 %)               | eyes, face, head, nose                | **Medium (~60 %)** – ratio and features mirror Jacob-Van-Wingen.                                                                          |
| **Justin-Singer**      | 3 / 8 (38 %)               | eyes, face, head                      | **Medium (~55 %)** – fewer images flagged; no nose or mouth anomalies.                                                                    |
| **Lee-Cooper**         | 5 / 11 (45 %)              | eyes, face, head, mouth, nose         | **Medium-high (~65 %)** – multiple key facial features flagged.                                                                           |
| **Neal-Manaktola**     | 3 / 8 (38 %)               | eyes, face, head                      | **Medium (~55 %)** – ratio is lower; flagged features limited to eyes/face/head.                                                          |
| **Paul-Stamatiou**     | 6 / 15 (40 %)              | beard, ear, glasses, hat, mouth, nose | **Medium (~60 %)** – ratio moderate; some flags (glasses, hat, beard) could be accessories, but nose and mouth anomalies raise suspicion. |
| **Roduardo-Villafane** | 5 / 11 (45 %)              | eyes, face, head, mouth, nose         | **Medium-high (~65 %)** – multiple facial features flagged.                                                                               |
| **Sam-Resnick**        | 5 / 11 (45 %)              | eyes, face, head, mouth, nose         | **Medium-high (~65 %)** – similar to Roduardo.                                                                                            |
| **Sheldon-Nelson**     | 5 / 11 (45 %)              | eyes, face, head, mouth, nose         | **Medium-high (~65 %)** – similar to Roduardo and Sam.                                                                                    |

*Probabilities are approximate judgments derived from the proportion of AIDR-flagged images and the types of features flagged; they are not definitive labels.

### Interpretation

The AI-image-recognition system flagged facial features—eyes, nose, head shape, and mouths—most often. Academic and practitioner articles on AI-generated images explain that these areas frequently contain artifacts: generative models may mis-place eyes or noses, produce mismatched ears, or create overly smooth and shiny skin. Accessories such as hats, glasses or jewelry may also appear distorted. Thus, individuals with multiple facial features flagged and a high proportion of suspect images (e.g., David-Braun, Lee-Cooper, Roduardo-Villafane, Sam-Resnick, and Sheldon-Nelson) were assessed with a medium-high probability of being AI-generated profiles.

However, AI-detection is not infallible. The research emphasises that some anomalies can occur naturally, and singular artifacts (e.g., an ear appearing odd or a missing finger) do not conclusively prove an image is synthetic. As such, the probabilities above are only indicative; manual inspection and cross-comparison with trusted photographs would be necessary for conclusive attribution.

