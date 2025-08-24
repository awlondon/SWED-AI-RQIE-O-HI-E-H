# Zinn Labs – Event-Based Gaze Tracking Risks

## What's Real
- **Prophesee integration:** Zinn Labs publicly used Prophesee's GenX320 event sensor (~3×4 mm, μW power modes) in its gaze stack for smart eyewear.
- **Biometric potential:** Studies show eye-movement dynamics can re-identify individuals with up to ~95–100% accuracy within sessions and ~64–78% across sessions.
- **Inference attacks:** "GAZEploit" demonstrated PIN/text inference on Apple Vision Pro via eye cues, illustrating risks once gaze data leaves the device.
- **Corporate linkage:** Zinn Labs announced it "joined" Sesame AI in 2025, bringing its low-power gaze technology under Sesame's AI-glasses program.

## Threat Model Highlights
- Event-based sensors enable **silent, persistent capture** with low bandwidth and power.
- Gaze signals fused with audio/video context can yield **identity persistence**, **secret inference** and **attention/affect estimates**.

## Dual-Use Concerns
- Covert surveillance and bystander capture via inconspicuous glasses.
- Persistent gaze IDs feeding social-scoring or predictive-policing systems.
- Data subject to PRC jurisdiction could be compelled under NIL, DSL or PIPL.

## Mitigation Notes
- Keep raw eye events on-device and expose only quantized intent signals.
- Apply privacy filters that block keypad fixations and cap temporal resolution.
- Attach C2PA provenance and watermarks to any exported summaries.
- Align with EU AI Act bans on emotion inference and conduct NIST AI RMF audits.

