# Bhashabid Autonomous Learning Curve & Saturation Audit

- **Execution Timestamp**: `2026-11-12 12:50:48`
- **Approved Knowledge Invariants**: `28` production cards
- **Quarantined Candidate Drafts**: `2` (Principle P2 review queue)
- **External Corpora Ingested**: `14` source files (`94` total sentences)
- **Clean Native Benchmarks**: `87`
- **Canary Flaws Trapped**: `7`
- **Active Anomaly Candidates**: `0`

## 1. Domain & Sector Saturation Index

| Domain / Sector | Sentences | Clean Benchmark | Trapped Canaries | Saturation Index | Status & Recommendation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Academic Research & Methodology | 7 | 85.7% | 1 | `100%` | SATURATED (Needs New Data) |
| Administrative Governance & Memos | 6 | 100.0% | 0 | `100%` | SATURATED (Needs New Data) |
| Agronomy & Disaster Management | 7 | 100.0% | 0 | `100%` | SATURATED (Needs New Data) |
| Banking & Macroeconomics | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Administrative Governance | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Tax & Customs | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Official Administrative | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Land Conveyancing & Deeds | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Macroeconomic & Finance | 2 | 50.0% | 1 | `100%` | LEARNING (Active Anomaly Discovery) |
| Judicial & High Court | 2 | 50.0% | 1 | `100%` | LEARNING (Active Anomaly Discovery) |
| Sports Vernacular | 2 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Corporate & Tech | 2 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Disaster Early Warning | 2 | 50.0% | 1 | `100%` | LEARNING (Active Anomaly Discovery) |
| Classical Poetry & Prosody | 5 | 100.0% | 0 | `100%` | SATURATED (Needs New Data) |
| Creative Fiction & Dialogue | 7 | 71.4% | 2 | `100%` | SATURATED (Needs New Data) |
| Education & NCTB Pedagogy | 7 | 85.7% | 1 | `100%` | SATURATED (Needs New Data) |
| Healthcare & Epidemiology | 7 | 100.0% | 0 | `100%` | SATURATED (Needs New Data) |
| ICT & Software Engineering | 7 | 100.0% | 0 | `100%` | SATURATED (Needs New Data) |
| Land Registry & Deeds | 7 | 100.0% | 0 | `100%` | SATURATED (Needs New Data) |
| Constitutional Law & Writs | 7 | 100.0% | 0 | `100%` | SATURATED (Needs New Data) |
| Macroeconomics & Banking | 7 | 100.0% | 0 | `100%` | SATURATED (Needs New Data) |
| Education & Pedagogy | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Science & Encyclopedic | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Poetic Prosody | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Agronomy & Crop Protection | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |
| Healthcare & Medicine | 1 | 100.0% | 0 | `100%` | LEARNING (Active Anomaly Discovery) |

**Average System-Wide Saturation on Current Batch**: `100.0%`

## 2. Autonomous Ingestion & Convergence Criteria

1. **When does practice on the same batch stop?**
   - **Threshold**: When a domain reaches $\ge 95\%$ saturation and $\le 0$ novel anomalies discovered over 3 consecutive rounds.
   - **Result**: Practicing beyond 3-5 rounds on a static batch yields diminishing returns. Compute must shift to new data ingestion.

2. **When is new data ingested?**
   - **Immediate Ingestion Trigger**: As soon as saturation index exceeds `0.90` or when new anomalies $\Delta A = 0$.
   - **Ingestion Channels**:
     - Unharvested files in `eval/corpora/sources/` or `eval/corpora/inbox/`.
     - Dynamic Adversarial Perturbation with elevated entropy.
     - Live RSS feeds / open government circulars.

3. **Autonomous Learning Pipeline Role Separation**:
   - **Autonomous (Machine)**: Data fetching, tokenization, multi-domain linting, canary trapping, duplicate guarding, draft card synthesis, and post-approval distillation.
   - **Human Gate (Principle P2)**: Reviewing and approving candidate cards in `knowledge/cards/drafts/` via GitHub PR.
