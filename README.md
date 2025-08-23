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
- `datasets/` – structured CSVs on profiles and indictments. Run `python scripts/analyze_datasets.py` to refresh `datasets/analysis_summary.md`.
- `scripts/` – utilities for updating datasets and generating analytic summaries.
- Additional folders provide research notes, case studies, and references.

## Full Spectrum Dataset Analysis

The current datasets combine both newly added and pre-existing records:

- Fake profiles: 2 entries spanning the energy and technology sectors.
- Indictments: 2 entries covering finance and government sectors.

See `datasets/analysis_summary.md` for a detailed breakdown.

## Goals

1. Document patterns of synthetic or stolen identities used to build trust over long periods.
2. Track potential corporate targeting and network infiltration.
3. Support wider research into state-sponsored information operations and counter-intelligence.

## Usage

All material is provided for research and educational purposes. The data may contain false positives or unverified claims; exercise caution and seek independent confirmation before attribution.

Run the included `update.sh` script to refresh data stored under `datasets/`.

## Contributing

Contributions that refine documentation or add verifiable evidence are welcome. Please remove sensitive personal information and note sources for any submissions.

