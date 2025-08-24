# Event-Based Gaze Tracking – Risks and Controls

## What's Real
- **Low-power event cameras:** Dynamic Vision Sensors such as Prophesee's GenX320 enable microsecond-latency eye tracking at milliwatt to microwatt power budgets, allowing "always-on" smart glasses.
- **Gaze as biometric:** Peer-reviewed studies report up to ~95–100% identification within a session and ~64–78% across sessions using eye-movement dynamics.
- **Inference attacks:** Demonstrations like 2024's "GAZEploit" on Apple Vision Pro inferred typed text from eye cues, highlighting privacy risks.
- **Corporate link:** Public records list Gordon Wetzstein as Zinn Labs co-founder; Zinn Labs announced it "joined" Sesame AI in 2025.

## Threat Model (HLSF + Event-Based Gaze)
- **Collection → Fusion → Inference → Action loop** using eye events, pupil metrics, blinks, ambient audio and device context.
- **Inferences:** biometric re-identification, gaze-to-UI mapping for secrets (e.g., PINs), and affect/attention estimates.
- **Actions:** personalization, surveillance, manipulation and targeting at scale.

## Dual-Use Pivots
- **Covert surveillance:** Small, low-power glasses can silently capture gaze and ambient data, risking bystander privacy.
- **Tracking & scoring:** Persistent gaze-based IDs could feed social-scoring or predictive-policing systems.
- **Cross-border leverage:** PRC laws (NIL, DSL, PIPL) enable state access to biometric/behavioral data.

## Mitigation Strategies
- **Technical safeguards:** on-device processing, rate-limited/obfuscated APIs, privacy filters that suppress keypad fixations, and provenance via C2PA manifests with watermarking.
- **Policy & compliance:** align with EU AI Act prohibitions on emotion inference, perform export-control and human-rights due diligence, and audit against NIST AI RMF.
- **User empowerment:** granular gaze/voice/environment toggles, sensitive-scene shielding (auto blur/muffle) and signed transparency exports.

