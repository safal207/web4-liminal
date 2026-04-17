# Pilot SOW Template (4 Weeks)

## 1. Engagement Summary

**Project:** web4-liminal Incident Replay & Audit Pack Pilot  
**Duration:** 4 weeks  
**Customer:** <Organization Name>  
**Owner:** <Buyer + Technical Champion>

## 2. Pilot Goal

Demonstrate measurable improvements in incident reproducibility and triage quality for one selected AI workflow.

## 3. Scope

### In scope

- One target workflow/pipeline
- Up to <N> incident traces (recommended: 10 seeded or historical)
- Baseline vs pilot comparison
- Standardized reproducibility report outputs

### Out of scope

- Full platform migration
- Multi-team rollout
- Custom enterprise auth/compliance controls beyond pilot needs

## 4. Deliverables

1. Integration setup checklist and data boundary map
2. Trace validation + replay runbook
3. Incident report pack for pilot set
4. Metrics summary:
   - TTRI baseline vs pilot
   - replay success rate
   - false-positive / false-negative observations (if policy checks enabled)
5. Final recommendation memo (adopt / iterate / defer)

## 5. Success Criteria

Pilot is considered successful if all are met:

- TTRI reduction >= <target %> (recommended 30-40%)
- Replay success >= <target %> (recommended 85%)
- At least <X> incident classes produce reproducible report artifacts
- Technical champion confirms workflow is usable without bespoke one-off scripts

## 6. Responsibilities

### Customer

- Provide incident inputs and test environment access
- Assign one technical champion and one decision owner
- Attend weekly sync and validation review

### web4-liminal team

- Configure validation/replay path for selected workflow
- Run analysis and prepare report artifacts
- Provide weekly status and risk log

## 7. Timeline

### Week 1
- Kickoff, workflow selection, data boundary confirmation
- Baseline metric capture

### Week 2
- Integration and first replay runs
- Early report iteration

### Week 3
- Full pilot run on selected incident set
- Intervention/policy comparisons (if in scope)

### Week 4
- Final metrics and recommendation memo
- Stakeholder readout

## 8. Data & Security

- Customer data remains customer-owned
- Pilot data handling constraints: <list>
- Security contact and disclosure process: see `SECURITY.md`

## 9. Commercials

- Pilot fee: <amount / fixed>
- Payment terms: <terms>
- Optional next phase: <retainer / implementation package>

## 10. Acceptance

Accepted by:

- Customer representative: <Name / Title / Date>
- Provider representative: <Name / Title / Date>