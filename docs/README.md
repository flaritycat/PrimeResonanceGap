# Prime Resonance Gap Docs

This directory contains the active proof ledger, module chain, status files,
review artifacts, and Codex continuation protocol for the Prime Gap Resonance
Project.

## Current Frontier

```text
Latest module frontier: Module 280
Active phase: Phase J, minimal transverse proof-package feasibility
Latest project-wide review: docs/reviews/Prime_Resonance_Gap_1000_Page_Review.md
```

The original positive existence problem, the all-alpha theorem, the
unconditional finite-type theorem, and the residual cube endpoint remain open
unless explicitly marked otherwise in `docs/status/global_status.md`.

## Main Navigation

```text
status/
  global_status.md          Global theorem/status ledger
  theorem_status_index.md   Compact object-by-object status index
  forbidden_upgrades.md     Claims that must not be made without proof
  long_term_plan.md         Active schedule and iteration counters

modules/
  dependency_graph.md       Compact dependency/status graph
  dependency_graph.mmd      Mermaid source for the dependency graph
  module_178_residual_cube.md
  module_179_fourier_major_minor.md
  ...
  module_260_projected_model_neutrality_gate.md
  module_262_fifth_plan_challenge.md
  module_263_signed_inclusion_exclusion_expansion.md
  module_264_collision_diagonal_strata.md
  module_265_kernel_absolute_vs_signed.md
  module_266_uniformity_admissible_family.md
  module_267_projected_model_neutrality_verdict.md
  module_268_ninth_plan_update.md
  module_269_transverse_incidence_object.md
  module_270_threshold_removal_audit.md
  module_271_transverse_phase_equations.md
  module_272_phase_tool_compatibility.md
  module_273_transverse_incidence_gate.md
  module_274_transverse_gate_compatibility.md
  module_275_transverse_degeneracy_classification.md
  module_276_transverse_gate_verdict.md
  module_277_tenth_plan_update_sixth_challenge.md
  module_278_minimal_transverse_family.md
  module_279_xi_dual_phase_expansion.md
  module_280_fixed_set_shell_transfer.md
  modules_156_178_summary.md

reviews/
  Prime_Resonance_Gap_1000_Page_Review.md

root/
  Reflective_3.md

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
