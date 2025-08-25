# MSS LinkedIn Infiltration Investigation

The repository tracks open-source evidence of long-term influence operations attributed to the Chinese Ministry of State Security (MSS). It focuses on how synthetic or stolen identities exploit professional platforms, especially LinkedIn, to build trust and collect intelligence.

## Mission

- Preserve and organize artifacts of suspected MSS-run professional network campaigns.
- Analyze persona clusters, outreach tactics, and supporting infrastructure.
- Share reproducible methods so researchers and defenders can collaborate.

## Repository Overview

- [research/](research/) – methodology notes, open questions, and guidance for contributors.
- [datasets/](datasets/) – structured CSV/JSON files and summaries used in analysis. Utilities live under [scripts/](scripts/).
- [LinkedIn/](LinkedIn/) – reports and data tied to LinkedIn investigations, including cluster-specific folders such as `Sesame/`.
- [case-studies/](case-studies/) – narrative reports examining individual operations.
- [Intelligence-Analyst/](Intelligence-Analyst/) – planning documents and research schedules for analyst workflows.
- [institutions/](institutions/) – institution dossiers with infiltration reports; examples include the [MCF University infiltration report](MCF_University_Infiltration_Report.md).
- [shell-companies/](shell-companies/) – information on commercial services enabling large-scale persona creation.
- [MSS_LinkedIn_Infiltration_Analysis__CLAUDE.md](MSS_LinkedIn_Infiltration_Analysis__CLAUDE.md) – analysis of LinkedIn infiltration tactics.
- [mss_ai_intelligence_cycle_report.md](research/mss_ai_intelligence_cycle_report.md) – integration of AI across the MSS intelligence cycle.
- [Grok_MSS_AI_Development_Report.md](Grok_MSS_AI_Development_Report.md) – summary of MSS involvement in AI development.
- [MSS_AI_Intelligence_1995-2025__ANKAA.md](MSS_AI_Intelligence_1995-2025__ANKAA.md) – open-source and declassified intelligence on MSS AI activities.
- [dragon-fall/](dragon-fall/) – cross-cultural dragon timelines, lineages, and megalith speculation.
- Additional folders contain references, draft reports, and test suites.

## Installation

Install the project and its dependencies using either `requirements.txt` or the
`pyproject.toml` file.

### Using `requirements.txt`

```bash
pip install -r requirements.txt
```

### Using `pyproject.toml`

```bash
pip install .
```

After installation, run the test suite to verify the setup:

```bash
pytest
```

## Working with Data

1. Append records with the `update-datasets` console script:

   ```bash
   pip install -e .
   # or
   pip install -r requirements.txt

   ```

2. Regenerate `datasets/analysis_summary.md` with `analyze-datasets`:

   ```bash
   analyze-datasets
   ```

3. Review `datasets/README.md` for schema requirements.

## Future Research Needs

- Expand persona catalogues across sectors and languages; see case studies on [Kevin Mallory](case-studies/kevin-mallory/) and notes on [Chen Lai](case-studies/chen-lai/notes.md).
- Correlate LinkedIn activity with infrastructure such as shell companies or leaked credential sets; review the [shell company profiles](shell-companies/README.md) and [MSS LinkedIn infiltration analysis](MSS_LinkedIn_Infiltration_Analysis__CLAUDE.md).
- Evaluate how global cybersecurity workforce shortages could influence MSS targeting. See CSET's [Cyber Employment Report](https://cset.georgetown.edu/wp-content/uploads/t0231_cyber_employment_report_EN.pdf) and the local [summary](research/cyber_employment_report_summary.md).
- Develop tooling for detecting AI-generated media and automated outreach; consult [research notes](research/README.md) for methodological guidance.
- Compare operations on other platforms to build cross-network intelligence, aligning with insights from the [Yanjun Xu case study](case-studies/yanjun-xu/).
- Monitor export-control developments affecting VR/AR sensor firms and track misuse of advanced voice-cloning models.
- Investigate state-driven human monitoring efforts; review the [China human monitoring report](research/china_human_monitoring_report.md).

## Usage and Attribution

Content is provided for research and education. Some material may be incomplete or unverified; corroborate with independent sources before attribution.

## Contributing

Pull requests that enhance documentation or supply verifiable evidence are welcome. Remove sensitive personal data and cite sources for all contributions.

## License

This project is licensed under the [MIT License](LICENSE).
