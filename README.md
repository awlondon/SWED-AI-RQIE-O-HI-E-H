# MSS LinkedIn Infiltration Investigation

This repository collects open-source intelligence on suspected operations run by China's Ministry of State Security (MSS). It documents long-term infiltration of professional networks—particularly LinkedIn—using fake or stolen identities and AI-generated content. The repo serves as a hub for analytic reports, evidence sets, and research plans that help investigators and defenders understand these campaigns.

## Mission

- Preserve and organize evidence of MSS-linked professional network operations.
- Analyze AI-generated personas, outreach patterns, and supporting infrastructure.
- Share methods and findings to encourage collaboration across the security community.

## Contents

- [research/](research/) – central hub for analytic notes and methodology. Start here and read `research/README.md` before contributing elsewhere.
- [case-studies/](case-studies/) – in-depth examinations of individual infiltration campaigns.
- [shell-companies/](shell-companies/) – information on front or shell entities linked to MSS activities.
- [datasets/](datasets/) – raw data used in this project. Run the `update.sh` script to fetch the latest files into this directory.

## Potential Activities

- Catalog suspicious LinkedIn accounts and associated artifacts.
- Perform image and text analysis to detect synthetic media or stolen credentials.
- Map relationships between accounts and track outreach behavior over time.
- Correlate findings with public records and breach data.
- Share research methods and evidence for peer review.

## Objectives

- Understand how MSS-directed campaigns leverage professional platforms.
- Identify tactics used to build credibility and manipulate targets.
- Provide resources for defenders to recognize and counter infiltration.
- Encourage transparency and information sharing across research communities.

## Repository Structure

 - `LinkedIn/` – data and reports related to LinkedIn persona investigations.
  - `AIDR_results_summary.json` – structured summary of AI detection results for 49 images across 11 accounts (parsed from `AIDR_results_summary.txt`).
  - `Ankaa_Intel_Report__08.20.25.txt` – background dossier describing MSS integration of AI into surveillance, cyber operations, and influence campaigns.
  - `Sesame/` – image fragments, facial-analysis outputs, and other evidence tied to a set of suspicious LinkedIn personas associated with the company "Sesame".
- `Intelligence-Analyst/LinkedIn_Infiltration_Research_Plan.md` – 10-hour research plan outlining steps for conducting the investigation.
- `MSS_LinkedIn_Infiltration_Analysis__CLAUDE.md` – comprehensive analysis of MSS LinkedIn operations.
- `Grok_MSS_AI_Development_Report.md` – summary of a Grok report on MSS strategies for acquiring and applying AI.
- `MSS_AI_Intelligence_1995-2025.md` – open-source and declassified intelligence on MSS use of AI over three decades.
- Additional folders will cover other targets under review, including technology firms such as Auger.

## Goals

1. Document patterns of synthetic or stolen identities used to build trust over long periods.
2. Track potential corporate targeting and network infiltration.
3. Support wider research into state-sponsored information operations and counter-intelligence.

## Usage

All material is provided for research and educational purposes. The data may contain false positives or unverified claims; exercise caution and seek independent confirmation before attribution.

Run the included `update.sh` script to refresh data stored under `datasets/`.

## Contributing

Contributions that refine documentation or add verifiable evidence are welcome. Please remove sensitive personal information and note sources for any submissions.

