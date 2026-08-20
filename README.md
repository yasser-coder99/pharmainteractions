# PharmaInteractions

Open-source rule engine for documenting and checking drug–drug and drug–supplement interactions.

## Why this exists

Interaction information is often fragmented across references and difficult to represent in a reusable, machine-readable format. PharmaInteractions provides a small, transparent data model and rule engine that developers can integrate into pharmacy, medication-review, and educational software.

**Important:** This project is a software/data demonstration, not a clinical decision-support system. The included examples are synthetic/demo rules and must not be used to make patient-care decisions.

## Features

- Machine-readable interaction rules
- Severity and evidence fields
- Explainable rule evaluation
- CLI interface
- JSON output for integration
- Automated tests
- GitHub Actions CI
- Contribution template for community expansion

## Quick start

```bash
pip install -e .
pharma-interactions check warfarin aspirin
pharma-interactions check simvastatin clarithromycin --json
```

## Roadmap

- Expand the open interaction dataset using authoritative public sources
- Add normalization through RxNorm/ATC identifiers
- Add drug–food and drug–supplement rules
- Add multilingual explanations
- Add provenance and source-version tracking
- Build a web API

## License

MIT
