# UrjaVaani: Hear. Schedule. Prove.

A wiring-free energy and carbon platform starter for Indian SME manufacturers.

Built for **Yuva Yoddha Hackathon Challenge 04 (Smart Manufacturing: Industrial Energy & Process Efficiency)**.

| Module | Purpose |
|---|---|
| Hear | Estimate per-machine kW/kWh and detect leaks/fault cues from sound and vibration. |
| Schedule | Shift flexible loads to lower-tariff windows without missing deadlines. |
| Prove | Compute per-batch Scope 1 + 2 emissions and produce Carbon Passport outputs. |

> Config values in `config/` are illustrative only and must be replaced with plant/state-approved current values before use.

India's industry uses roughly 35-40% of national energy demand, energy can be 15-30% of production cost for many SMEs, many plants still lack real-time machine-level monitoring, and exporters increasingly need to prove product-linked emissions in a verifiable way.

```mermaid
flowchart LR
    A[Machines] --> B[Edge node (ESP32 + mic or phone)] --> C[Plant gateway (offline-first)] --> D[Cloud services (acoustic energy model, tariff-aware scheduler, carbon engine)] --> E[Outputs (WhatsApp/SMS/voice, web dashboard, Carbon Passport PDF + QR, Tally/ERP export)]
```

## Repository structure

```text
urjavaani/
├── README.md                         # Project overview and phased plan
├── requirements.txt                  # Python dependencies
├── pytest.ini                        # Pytest configuration
├── .gitignore                        # Ignore rules for local artifacts and data dumps
├── config/                           # Illustrative tariff and emission factor inputs
│   ├── tariff_example.csv            # Example ToD tariff slab table
│   └── emission_factors_example.csv  # Example hourly grid emission factor table
├── data/                             # Data folders
│   ├── raw/.gitkeep                  # Placeholder for raw files (not committed)
│   ├── processed/.gitkeep            # Placeholder for processed files (not committed)
│   └── external/README.md            # Notes for third-party datasets/tables
├── docs/                             # Architecture, assumptions, baseline and data docs
│   ├── architecture.md               # Layered design and data flow
│   ├── assumptions.md                # Assumptions register
│   ├── baseline-methodology.md       # Baseline and guardrail definitions
│   ├── data-sources.md               # Data need register
│   ├── diagrams/.gitkeep             # Placeholder for diagrams
│   └── design/.gitkeep               # Placeholder for design notes
├── edge/firmware/README.md           # Firmware scope note
├── notebooks/.gitkeep                # Placeholder for notebooks
├── pitch/.gitkeep                    # Placeholder for pitch assets
├── scripts/.gitkeep                  # Placeholder for helper scripts
├── src/urjavaani/                    # Python package source
│   ├── __init__.py                   # Package marker
│   ├── sensing/                      # Hear module stubs
│   ├── scheduler/                    # Schedule baseline planner
│   ├── carbon/                       # Prove footprint engine/passport stub
│   ├── notify/                       # WhatsApp formatter/mock sender
│   ├── api/                          # FastAPI app
│   └── simulation/                   # Synthetic data generation
├── dashboard/app.py                  # Streamlit dashboard scaffold
└── tests/                            # Baseline tests for scheduler/carbon
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
uvicorn urjavaani.api.main:app --reload
streamlit run dashboard/app.py
```

## Work phases

### Phase 0: Foundations and research
- **Goal:** Define scope, success metrics, and reference architecture.
- **Tasks:** Confirm use-cases, map stakeholders, and lock assumptions.
- **Deliverables:** Problem framing, architecture draft, assumptions register.
- **Exit criteria:** Team agrees on scope and measurable targets.

### Phase 1: Data and simulation
- **Goal:** Stand up reproducible data inputs for development.
- **Tasks:** Collect sample schemas and generate synthetic baselines.
- **Deliverables:** Data folders, synthetic generator, illustrative configs.
- **Exit criteria:** Baseline runs are reproducible and documented.

### Phase 2: Hear (acoustic energy model)
- **Goal:** Build machine-level kW estimation from sound/vibration features.
- **Tasks:** Extract features, calibrate to clamp-meter readings, train regressor.
- **Deliverables:** Feature extraction pipeline and calibrated model.
- **Exit criteria:** Held-out error is near the +/-10-15% target after calibration.

### Phase 3: Schedule (tariff-aware planner)
- **Goal:** Shift flexible jobs to lower-cost windows within deadlines.
- **Tasks:** Implement greedy baseline, then upgrade to constrained optimization.
- **Deliverables:** Daily plan output and estimated savings.
- **Exit criteria:** Planner respects earliest start/latest end constraints.

### Phase 4: Prove (Carbon Passport)
- **Goal:** Compute per-batch Scope 1 + 2 and generate passport output.
- **Tasks:** Aggregate energy by hour, apply emission factors, build PDF + QR.
- **Deliverables:** Batch footprint dictionary and passport artifact.
- **Exit criteria:** Footprint outputs are traceable and reproducible.

### Phase 5: Integration and UI
- **Goal:** Connect APIs, notifications, and dashboard views.
- **Tasks:** Wire scheduler/carbon outputs into FastAPI and Streamlit.
- **Deliverables:** End-to-end demo flow.
- **Exit criteria:** Operator can run one daily planning and reporting cycle.

### Phase 6: Evaluation and quantified impact
- **Goal:** Measure improvements against baseline.
- **Tasks:** Compare before/after SEC, cost, emissions, and peak demand.
- **Deliverables:** Quantified impact summary with guardrail checks.
- **Exit criteria:** Throughput/rejection guardrails remain acceptable.

### Phase 7: Submission artefacts
- **Goal:** Prepare hackathon-ready submission package.
- **Tasks:** Finalize deck, demo script, architecture visuals, and metrics.
- **Deliverables:** Complete submission artefacts.
- **Exit criteria:** Submission checklist is fully complete.

### Phase 8: Pilot and scale
- **Goal:** Plan rollout beyond prototype.
- **Tasks:** Define deployment, support, and scale roadmap.
- **Deliverables:** Stage-wise rollout plan.
- **Exit criteria:** Pilot and scale milestones are approved.

| Stage | Timeline |
|---|---|
| Prototype | 0-2 months |
| Pilot | 2-6 months |
| Launch | 6-12 months |
| Scale | 12-24 months |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Acoustic accuracy may drift across machines. | Re-calibrate with periodic clamp-meter checks and retraining windows. |
| No real factory data early in development. | Start with synthetic data and document assumptions until pilot data arrives. |
| Prior art exists in energy analytics space. | Differentiate with wiring-free deployment and per-batch carbon proof. |
| Tariffs and emission factors change over time. | Treat config tables as versioned inputs and refresh on schedule. |
| Scope creep across modules. | Phase-gate features and enforce exit criteria before expansion. |

## Contributing workflow

1. Create one branch per phase or scoped task.
2. Open a pull request and complete review before merge.
3. Keep raw/processed data out of git.
4. Add or update tests when changing `carbon/` or `scheduler/`.

Not yet chosen. Add a LICENSE file before making the repository public.
