# Prime Resonance Gap Docs

This directory contains the active proof ledger, module chain, status files,
review artifacts, and Codex continuation protocol for the Prime Gap Resonance
Project.

## Current Frontier

```text
Latest module frontier: Module 256
Active phase: Phase G, fixed-row package feasibility gates
Latest project-wide review: docs/reviews/Prime_Resonance_Gap_1000_Page_Review.md
```

The original positive existence problem, the all-alpha theorem, the
unconditional finite-type theorem, and the residual cube endpoint remain open
unless explicitly marked otherwise in `docs/status/global_status.md`.

## Main Navigation

```text
status/
  global_status.md          Global theorem/status ledger
  forbidden_upgrades.md     Claims that must not be made without proof
  long_term_plan.md         Active schedule and iteration counters

modules/
  module_178_residual_cube.md
  module_179_fourier_major_minor.md
  ...
  module_256_two_point_escalation_gate.md
  modules_156_178_summary.md

reviews/
  Prime_Resonance_Gap_1000_Page_Review.md

paper/
  Prime_Resonance_Gap_500_Page_Paper.txt

ledger/
  prime_gap_resonance_project_250_page_breakdown.txt

codex/
  continuation_protocol.md
  SHORT_CODEX_PROMPT.md
```

## Reading Order

Start with:

```text
AGENTS.md
docs/status/global_status.md
docs/status/forbidden_upgrades.md
docs/codex/continuation_protocol.md
docs/status/long_term_plan.md
docs/reviews/Prime_Resonance_Gap_1000_Page_Review.md
```

Then continue from the latest module named in `docs/status/long_term_plan.md`.

## Status Discipline

Allowed labels are:

```text
PROVEN
CONDITIONAL
STRUCTURAL / EXTRACTION
HEURISTIC
OPEN
FALSE / BLOCKED
```

Do not upgrade a decomposition to a proof. Do not upgrade model, smoothed, or
frozen selector statements to actual moving-selector statements without the
named transfer packages.
