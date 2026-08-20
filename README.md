# pharmainteractions
open-source, explainable drug interaction rule engine
# PharmaInteractions

**An open-source, explainable drug interaction rule engine for medication and supplement safety software.**

PharmaInteractions is an open-source project designed to make drug–drug and drug–supplement interaction information easier to represent, understand, and integrate into software applications.

The project provides a structured data model and an explainable rule engine that can identify documented interactions and return information about severity, mechanism, recommended action, and evidence provenance.

> **Important:** PharmaInteractions is currently an early-stage open-source project. The included interaction rules are demonstration data and must not be used for clinical decision-making. Production use requires validation against authoritative pharmaceutical and clinical sources.

## Why PharmaInteractions?

Drug interaction information is often distributed across different databases, references, and proprietary systems. This makes it difficult for developers to build transparent and reusable medication-safety applications.

PharmaInteractions aims to provide an open and developer-friendly foundation for this type of software.

### Goals

* Create a machine-readable interaction database
* Make interaction rules transparent and explainable
* Include evidence and source provenance
* Support drug–drug interactions
* Support drug–supplement interactions
* Provide a simple developer API
* Enable community contributions
* Make the data reusable by other open-source projects

## Example

A query such as:

```bash
pharma-interactions check warfarin aspirin
```

can return structured information such as:

```text
Severity: major

Mechanism:
Additive antithrombotic effects can increase bleeding risk.

Action:
Review concomitant use and bleeding risk.

Evidence:
demo
```

The same information can be returned as JSON:

```bash
pharma-interactions check warfarin aspirin --json
```

This makes the project suitable for integration into other applications.

## Architecture

```text
Drug / Supplement
       ↓
Normalization
       ↓
Interaction Database
       ↓
Rule Engine
       ↓
Evidence & Provenance
       ↓
Severity / Mechanism / Action
       ↓
CLI / JSON / API
```

## Current Status

PharmaInteractions is currently in the early development stage.

Current features include:

* Python-based interaction rule engine
* Structured interaction data
* Explainable interaction results
* Command-line interface
* JSON output
* Automated tests
* GitHub Actions continuous integration
* Contribution guidelines

## Roadmap

### Phase 1 — Foundation

* [x] Create interaction rule engine
* [x] Create structured data model
* [x] Add CLI
* [x] Add JSON output
* [x] Add automated tests
* [x] Add CI workflow

### Phase 2 — Evidence-based dataset

* [ ] Expand the interaction database
* [ ] Add authoritative references
* [ ] Add source provenance
* [ ] Add publication/version tracking
* [ ] Add standardized drug identifiers

### Phase 3 — Expanded interactions

* [ ] Drug–drug interactions
* [ ] Drug–supplement interactions
* [ ] Drug–food interactions
* [ ] Duplicate/interaction classification
* [ ] Contraindication and precaution metadata

### Phase 4 — Developer ecosystem

* [ ] REST API
* [ ] Python API
* [ ] JavaScript/TypeScript client
* [ ] Documentation website
* [ ] Community contribution workflow
* [ ] Multilingual interaction explanations

## Contributing

Contributions are welcome.

Before submitting an interaction rule, contributors should provide:

1. The substances involved
2. The interaction mechanism
3. Severity classification
4. Recommended action
5. Evidence/source
6. Appropriate tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## Disclaimer

PharmaInteractions is an open-source software project and is not a substitute for professional clinical judgment, official prescribing information, or validated clinical decision-support systems.

Interaction data must be independently verified before being used in healthcare applications or patient care.

## License

This project is released under the MIT License.

