# ADR 001: Progressive Disclosure Architecture for Agent Skills

## Status
Accepted (2026-11-11)

## Context
Large Language Models exhibit severe context degradation and high token inference costs when provided with monolithic system prompts containing extensive grammar dictionaries and inflection tables.

## Decision
We enforce a strict two-tier progressive disclosure model:
1. The root skill entrypoint (`skills/bangla-expert/SKILL.md`) is constrained to < 600 tokens. It contains only core invariants and a dynamic routing table.
2. Comprehensive lexicographic and syntactic references reside in modular files under `references/` (`numerals.md`, `orthography.md`, `grammar_registers.md`) that are retrieved strictly on demand.

## Consequences
- Preserves LLM context window (> 90% token savings on non-Bengali turns).
- Modular reference files can be updated independently without breaking prompt cache.
