# MSS LinkedIn Infiltration Investigation

The repository tracks open-source evidence of long-term influence operations attributed to the Chinese Ministry of State Security (MSS). It focuses on how synthetic or stolen identities exploit professional platforms, especially LinkedIn, to build trust and collect intelligence.

## Mission

- Preserve and organize artifacts of suspected MSS-run professional network campaigns.
- Analyze persona clusters, outreach tactics, and supporting infrastructure.
- Share reproducible methods so researchers and defenders can collaborate.

## Repository Overview

- **research/** – methodology notes, open questions, and guidance for contributors.
- **datasets/** – structured CSV/JSON files and summaries used in analysis. Utilities live under `scripts/`.
- **LinkedIn/** – reports and data tied to LinkedIn investigations, including cluster-specific folders such as `Sesame/`.
- **case-studies/** – narrative reports examining individual operations.
- **shell-companies/** – information on commercial services enabling large-scale persona creation.
- Additional folders contain references, draft reports, and test suites.

## Working with Data

1. Use `python scripts/update_datasets.py <file> <profile_id> <sector> <source>` to append records.
2. Run `python scripts/analyze_datasets.py` to regenerate `datasets/analysis_summary.md`.
3. Review `datasets/README.md` for schema requirements.

## Future Research Needs

- Expand persona catalogues across sectors and languages.
- Correlate LinkedIn activity with infrastructure such as shell companies or leaked credential sets.
- Develop tooling for detecting AI-generated media and automated outreach.
- Compare operations on other platforms to build cross-network intelligence.

## Usage and Attribution

Content is provided for research and education. Some material may be incomplete or unverified; corroborate with independent sources before attribution.

## Contributing

Pull requests that enhance documentation or supply verifiable evidence are welcome. Remove sensitive personal data and cite sources for all contributions.
