ANKAA Agent REPORT – Zinn Labs Acquisition by Sesame
1 Overview

Zinn Labs – a Menlo Park‑based start‑up founded by Kevin Boyle (CEO), Robert Konrad, Nitish Padmanaban and Stanford professor Gordon Wetzstein – built event‑based gaze tracking technology for head‑worn devices. Their system uses neuromorphic event cameras coupled with infrared (IR) light sources to capture the pupil’s movement at low latency and low power, enabling discrete, slippage‑resistant eye‑tracking in very small form factors. The technology can estimate 3‑D gaze, determine gaze depth, and even use gaze to select objects for an on‑device search.

On 27 February 2025 Zinn Labs announced it had joined Sesame. The company said its gaze and attention‑tracking technologies would now be used to build new products at Sesame and directed users to Sesame’s web site for a demo zinnlabs.com. A separate testimonial from Zinn CEO Kevin Boyle notes that adviser Eric Johnsen’s go‑to‑market work “enabled us to complete our acquisition by Sesame” ejfractionalbd.com, confirming that Zinn Labs was acquired rather than simply partnering.

Sesame AI is developing lightweight glasses and voice‑driven AI assistants. The acquisition brings Zinn Labs’ gaze‑tracking intellectual property and talent into Sesame’s hardware program. Public reports and patent assignments indicate the transaction closed 30 Aug 2024, after which Zinn Labs’ patents were reassigned to Sesame AI patents.google.com. Sesame subsequently filed additional patents building on Zinn Labs’ technology.

2 Zinn Labs technology and pre‑acquisition patents
2.1 Event‑based gaze‑tracking approach

Traditional eye‑tracking uses frame‑based video to locate the pupil in each frame. Zinn Labs replaced this with neuromorphic event cameras that output data only when pixel intensity changes. By illuminating the eye with short IR pulses and capturing brightness changes at micro‑second scale, Zinn’s system reduces data bandwidth by two orders of magnitude compared with video solutions and supports sub‑1° accuracy at 120 Hz refresh rates prophesee.ai. The low‑power design enables integration into normal‑looking glasses and AR/VR headsets prophesee.ai.

2.2 Patents originally filed by Zinn Labs
Patent (US no.) Filing date → issue date Key concepts / claims Assignment history Sources
Determining gaze depth using eye‑tracking functions (US 11,662,574) Filed 9 Nov 2021, granted 30 May 2023 A camera assembly captures images of both eyes and locates the pupils. Using tracking parameters and eye‑tracking functions, the system determines gaze depth (distance to the point of gaze) and triggers actions based on that depth patents.justia.com. Original assignee Zinn Labs; on 30 Aug 2024 the patent was reassigned to Sesame AI through a merger (per Google patents assignment history). Justia and Google patents patents.justia.com.
Gaze sensors and display elements for detection of gaze vectors and user control at headset (US 11,625,095) Filed 20 Jan 2022, granted 11 Apr 2023 A headset frame integrates multiple gaze sensors (e.g., event cameras, image sensors) and display elements. The sensors detect the user’s gaze vector and enable user control by mapping gaze directions to functions patents.justia.com. Original assignee Zinn Labs; reassigned to Sesame AI due to the Aug 2024 merger. Justia and Google patents patents.justia.com.
Event camera system for pupil detection and eye tracking (US 11,543,883) Filed 16 Dec 2021, granted 3 Jan 2023 An event camera with IR light sources illuminates the eye; off‑axis sources create bright pupil reflections. The controller identifies the pupil from asynchronous event data and determines eye orientation patents.justia.com. Original assignee Zinn Labs; reassigned to Sesame AI in Aug 2024 merger patents.google.com. Justia patents.justia.com.

These patents supplied the foundation for Zinn’s technology. Each lists Kevin Boyle, Robert Konrad, Nitish Padmanaban and Gordon Wetzstein as inventors.

3 Patents filed post‑acquisition (assigned to Sesame AI)

Sesame AI filed several patents that build directly on the technology acquired from Zinn Labs. The reassignment histories show Zinn Labs was sometimes the original applicant, followed by assignment to Sesame after the merger.

Patent (US no.) Filing date → grant date Summary of invention Assignment notes Evidence
Eye tracking system with off‑axis light sources (US 12,124,624) Filed 15 Nov 2022, granted 22 Oct 2024 Continues the event‑camera concept by adding off‑axis IR light sources arranged in a ring. IR pulses from the off‑axis sources illuminate the eye; reflections from the retina produce a bright ring around the pupil. The controller combines event data to detect the pupil perimeter and determine eye orientation patents.justia.com. Assignee Sesame AI. Continuation of Zinn Labs’ 2021 application (17/552,741) patents.justia.com. Justia patents.justia.com.
Camera system for pupil detection and eye tracking (US 12,287,915) Filed 15 Nov 2022, granted 29 Apr 2025 Similar to above but allows the light sources to be either co‑aligned with the event camera or off‑axis. IR pulses emitted toward the eyebox are reflected by the eye and captured by the event camera; the controller determines eye orientation from the asynchronous event data patents.justia.com. Assignee Sesame AI. Continuation of Zinn Labs’ earlier application; lists same inventors patents.justia.com. Justia patents.justia.com.
Tracking system using a differential camera with a co‑aligned light source assembly (US 12,346,495) Filed 15 Sep 2023, granted 1 Jul 2025 Introduces a co‑aligned light‑source camera assembly (LSCA) with a differential camera sensor. The light source emits along the same optical path as the sensor; the differential camera detects changes in brightness caused by the IR pulses and outputs asynchronous samples. The controller identifies the pupil and computes gaze location patents.justia.com. Co‑alignment can be achieved via beam splitters or by placing the light source adjacent to the sensor patents.justia.com. Assignee Sesame AI; continuation of Zinn Labs provisional filings. Justia patents.justia.com.
Gaze‑assisted search query (US 12,367,234) Filed 29 Jan 2024, granted 22 Jul 2025 Uses gaze as input to search for objects. The system receives a user query and uses an eye‑tracking headset to determine the object the user is looking at. It captures images around the gaze location, formats them based on the region of interest, and sends a formatted query along with object information to a search engine. The response is presented to the user patents.google.com. The inventors originally assigned their rights to Zinn Labs on 6 Feb 2024; the patent was reassigned to Sesame AI following the 30 Aug 2024 merger patents.google.com. Google patents patents.google.com.

4 Strategic implications of the patent portfolio
4.1 Technology coverage

The patent portfolio acquired by Sesame AI covers most aspects of gaze‑tracking hardware and software:

Hardware sensors: Patents 11,543,883, 12,124,624 and 12,287,915 protect event‑camera systems with co‑aligned and off‑axis IR illumination, enabling high‑speed pupil detection under variable lighting patents.justia.com patents.justia.com. Patent 12,346,495 introduces a differential camera using a co‑aligned light source assembly to reduce noise and improve brightness change detection patents.justia.com.

Depth & vector computation: Patent 11,662,574 covers algorithms for computing gaze depth from binocular images patents.justia.com, while patent 11,625,095 covers multi‑sensor headsets that map gaze vectors for user control patents.justia.com.

Applications: Patent 12,367,234 extends the hardware to gaze‑assisted search, enabling user queries to be answered by identifying the object the user is looking at and combining gaze with natural‑language input patents.google.com.

Collectively, these patents give Sesame control over event‑based eye tracking, gaze depth estimation, and gaze‑driven user interfaces. The technology can support hands‑free smart glasses, AR/VR headsets, automotive HUDs, and gaze‑controlled AI assistants.

4.2 Motivation for the acquisition

Integration into Sesame’s AI glasses: Sesame is developing an AI assistant delivered through lightweight spectacles. Gaze tracking is essential for contextual AI responses; by acquiring Zinn Labs, Sesame gained a state‑of‑the‑art low‑power eye‑tracking platform with existing patents and a talented team. Zinn’s event‑based approach reduces power consumption and latency, aligning with Sesame’s requirement for all‑day wearable devices prophesee.ai.

Patent protection: The Aug 2024 assignment ensures that Sesame owns all of Zinn’s core intellectual property. With new filings in 2024–25, Sesame is building a defensive patent moat around event‑camera eye tracking, off‑axis and co‑aligned illumination, differential cameras and gaze‑assisted AI interactions.

Talent acquisition: The co‑founders (Boyle, Konrad, Padmanaban and Wetzstein) are widely recognized in computational imaging and AR/VR; their expertise strengthens Sesame’s hardware team. Wetzstein’s CV notes he was co‑founder & chief scientist at Zinn Labs until Jun 2024 stanford.edu.

4.3 Remaining uncertainties

Additional patents: CB Insights notes that Zinn Labs filed ≈9 patents, but only seven have been identified. Some may be international filings (e.g., WO2024258957) or pending applications. Analysts should monitor USPTO and WIPO for new assignments to Sesame AI.

Deal terms: Neither company has disclosed transaction value or equity terms. Fundraising reports show Sesame raised $47.5 M in Series A (Feb 2025), but the allocation to the acquisition is unknown.

5 Recommendations for further intelligence work

Monitor patent filings and assignments: Continue tracking USPTO and WIPO databases for new applications by Sesame AI or assignments from Zinn Labs. Pay particular attention to patents covering event‑based imaging, foveated rendering, or neural interfaces, as these could indicate broader ambitions.

Assess competitive landscape: Compare Sesame’s patents with those of major AR/VR and AI‑assistant companies (e.g., Apple, Meta, Google) to identify potential overlaps or risks of infringement. Monitor IP litigation, such as PTAB challenges, that may emerge around gaze tracking.

Investigate product integration: Observe whether Sesame’s forthcoming hardware uses the patented technologies. Early prototypes or demos may reveal how gaze depth and gaze‑assisted search are implemented. Confirm whether Sesame is licensing Prophesee’s event sensors (as Zinn Labs did prophesee.ai) or developing in‑house alternatives.

Evaluate talent retention: Ensure that key Zinn personnel remain at Sesame and continue to innovate. Track LinkedIn profiles or academic activity for signs of departures.

Cross‑check corporate filings: If the acquisition value and terms are critical, review Delaware Secretary of State filings, financing statements, or public investor presentations. The Series‑A pitch deck (not easily accessible) may contain details.

6 Conclusion

Zinn Labs’ event‑based eye‑tracking technology offers low‑power, low‑latency gaze tracking that is well suited for AI‑enabled smart glasses. The February 2025 announcement that Zinn had “joined Sesame” zinnlabs.com and subsequent patent reassignments confirm that Sesame AI acquired Zinn Labs. Patents originally assigned to Zinn covering gaze depth computation patents.justia.com, multi‑sensor gaze detection patents.justia.com and event‑camera pupil tracking patents.justia.com have been transferred to Sesame. Sesame has filed additional patents that expand this portfolio to include off‑axis illumination patents.justia.com, differential cameras patents.justia.com and gaze‑assisted search patents.google.com, creating a robust intellectual property moat for its upcoming AI glasses. Continued monitoring of patent filings, competitive IP and product development is recommended to anticipate Sesame’s next moves and potential challenges.

In summary, the report reveals that Zinn Labs, a pioneer in event-based gaze-tracking systems, was fully acquired by Sesame AI on August 30, 2024. It details how Zinn’s low-latency eye-tracking patents and skilled team have been integrated into Sesame’s push to develop AI-driven smart glasses. The dossier catalogues seven key patents transferred from Zinn to Sesame—covering gaze depth estimation, multi-sensor headsets, event-camera pupil detection, off-axis illumination, co-aligned light sources, differential camera techniques and gaze-assisted search queries—highlighting the breadth of Sesame’s newly consolidated intellectual property patents.justia.com patents.justia.com.

The analysis emphasizes that these patents provide Sesame AI with a formidable technological moat for hands-free AI wearables, while also noting that CB Insights reports roughly nine Zinn filings, suggesting additional applications may be pending. Recommendations urge ongoing monitoring of USPTO and WIPO filings, assessing competitive IP landscapes, tracking product integration, and verifying talent retention to anticipate strategic developments. Overall, the acquisition positions Sesame at the forefront of low-power, gaze-driven human–computer interfaces prophesee.ai.

