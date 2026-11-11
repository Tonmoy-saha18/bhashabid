# Bhashabid Agent Ecosystem

This repository coordinates 15 specialized personas operating under the Autonomous AI Development Lifecycle (AIDLC):

| Agent ID | Persona Name | Primary Role |
|---|---|---|
| A1 | Orchestrator | Manages backlog, enforces gates, tracks state/STATUS.md |
| A2 | Product & Spec Analyst | Author of EARS specs and traceability matrix |
| A3 | Architect | Component designer, schema author, ADR custodian |
| A4 | Source Curator | Ingestion, license auditing, clean corpus curation |
| A5 | Literature & Grammar Learner | Syntactic pattern extractor, register analyst |
| A6 | Developer | Test-first tool implementer (Python / Rust / MCP) |
| A7 | Tester | Unit, property, mutation, and regression test author |
| A8 | Memory Curator | Mistake ledger deduplication and lesson indexing |
| A9 | Knowledge Distiller | Author of atomic knowledge cards (knowledge/cards/) |
| A10 | Skill Engineer | Author of skills/bangla-expert/SKILL.md |
| A11 | QA Agent | E2E scenario validator and defect reporter |
| A12 | Evaluator / Benchmarker | Multi-model matrix evaluation and metrics reporter |
| A13 | Mistake Analyst | Root cause analysis and regression test authoring |
| A14 | Quality & Goal Reviewer | Independent auditor for constitution and release gates |
| A15 | Human Review Liaison | Native speaker packet preparation and approval logger |

Each agent contract is defined in `agents/<name>.md` and mirrored in `.claude/agents/<name>.md`.
