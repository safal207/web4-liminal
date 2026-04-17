# web4-liminal One-Pager (CTO / Investor)

## What it is

**web4-liminal** is a causal accountability foundation for long-running AI systems.

It helps teams move from "we have logs" to "we can reproduce incidents, explain decisions, and prove fixes" using structured traces, transition invariants, and validation-first evidence workflows.

## Problem

Most AI operations stacks can tell you **what happened**, but not reliably **why** it happened under continuity and policy constraints.

As systems become persistent and agentic, this creates high-cost failure loops:

- incident triage takes too long
- postmortems are hard to reproduce
- interventions are hard to compare empirically
- audit evidence is ad-hoc and non-portable

## Product wedge (v1)

### Incident Replay & Audit Pack

A focused workflow that converts incident traces into reproducible causal reports.

Core user flow:

1. Ingest trace artifacts from a target pipeline
2. Validate structural + causal invariants
3. Replay key transition windows
4. Generate an audit-ready report (findings + policy flags + reproducibility status)

## Who it serves

- AI Platform / Safety teams operating long-lived agent workflows
- Reliability and red-team engineers who need reproducible incident analysis
- Regulated domain teams (fintech, health, govtech) needing defensible evidence trails

## Why now

Agentic systems are scaling faster than trust infrastructure.

Without causal memory and reproducible transition evidence, organizations accumulate operational risk and compliance exposure as default behavior.

## Why this is different

Traditional observability tooling is event-centric.

web4-liminal is **continuity-centric**:

- reasons over raw events
- transitions over snapshots
- reproducibility over narrative post-hoc explanation

## Measurable outcomes (pilot targets)

- **TTRI** (time-to-root-incident): target reduction >= 40%
- **Replay success rate**: >= 85% for seeded incidents
- **Evidence quality**: standardized report artifacts for each incident class
- **Onboarding time**: first valid report in <= 30 minutes

## Business model (initial)

- Open-source core protocol and validation tooling
- Paid pilot + integration + hardening services
- Optional enterprise support for custom policy packs and audit workflows

## Ask / Next step

Run a 4-week pilot on one production-like incident stream.

Deliverables: baseline metrics, reproducible reports, intervention comparison, and adoption recommendation memo.