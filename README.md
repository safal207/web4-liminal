# web4-liminal

[![CI](https://github.com/safal207/web4-liminal/actions/workflows/ci.yml/badge.svg)](https://github.com/safal207/web4-liminal/actions/workflows/ci.yml)
[![Security Baseline](https://github.com/safal207/web4-liminal/actions/workflows/security.yml/badge.svg)](https://github.com/safal207/web4-liminal/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-rfc%20phase-blue.svg)](docs/CARE-STACK-RFC.md)

Web4 Liminal is an architecture and protocol incubation repository for meaning-aware, causal, and human-aligned systems.

It frames a practical transition from interaction-centric systems to continuity-centric systems where memory, responsibility, and irreversible transitions are first-class design constraints.

## Fast Validation Path

```bash
python scripts/validate_repo.py
```

## What This Repository Is

- A canonical architectural RFC for the **Care Stack**
- A coordination point for normative protocol work (spec layer)
- A reference map connecting CaPU, CML, LPT, T-Trace, and RINSE trajectories

## What This Repository Is Not

- Not a monolithic implementation of all stack layers
- Not a benchmark suite (yet)
- Not a production SDK repository

## Repository Map

- `docs/CARE-STACK-RFC.md` - core conceptual RFC
- `docs/ARCHITECTURE.md` - layer-by-layer architecture walkthrough
- `docs/product/` - one-pager, pilot SOW, and landing template artifacts
- `spec/README.md` - normative spec plan and versioning policy
- `scripts/validate_repo.py` - documentation/repo hygiene validator
- `.github/workflows/` - CI and security automation

## Care Stack Summary

```text
Web4 Presence
  -> Cybernetics 2.0 (Care-First)
    -> CaPU (causal processing)
      -> CML (causal memory)
        -> LPT (liminal passage constraints)
          -> T-Trace (irreversible transition trace)
            -> RINSE (reflective integration)
```

## Adoption Guidance

1. Start with RFC alignment (`docs/CARE-STACK-RFC.md`).
2. Define boundaries and invariants for your target layer.
3. Implement validation-first artifacts (schemas, test vectors, replay checks).
4. Add trust and safety gates before performance optimization.

## Governance

- Security policy: `SECURITY.md`
- Contribution guide: `CONTRIBUTING.md`
- Code of conduct: `CODE_OF_CONDUCT.md`

## License

MIT (`LICENSE`).