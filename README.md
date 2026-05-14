# Prime Resonance Gap

This repository documents the **Prime Gap Resonance Project**.

This is a research ledger, proof-map, conditional theorem architecture, endpoint-reduction record, and computational/documentation workspace. It is **not** a proof of the original positive existence problem and **not** a proof of the all-alpha no-positive-limit theorem.

## Current frontier

```text
Latest module frontier: Module 278
Active phase: Phase J, minimal transverse proof-package feasibility
Latest project-wide review:
  docs/reviews/Prime_Resonance_Gap_1000_Page_Review.md
```

Module 278 defines the minimal local W-cyclic transverse family
`P_minor^0`. It fixes the model class, Fourier group, W-order, dyadic ranges,
threshold schedules, shell convention, cutoff convention, and limiting order
for the next phase-kernel test. `PhaseKernelBound_273^0` remains open.

## Global status

| Claim | Status |
|---|---|
| Existence of irrational `alpha` with `A_alpha(x) -> L0 > 1` | **OPEN** |
| All-alpha no-positive-limit theorem | **OPEN** |
| Metric theorem `A_alpha(x) -> 1` for Lebesgue-a.e. irrational `alpha` | **PROVEN according to project ledger** |
| Finite-type no-positive-limit theorem | **CONDITIONAL** |
| `s=2` rational-major endpoint | **OPEN** (analytic-engine descriptor) |

For a compact object-by-object ledger, see
`docs/status/theorem_status_index.md`. For the dependency map, see
`docs/modules/dependency_graph.md`.

## Core selected average

```text
chi_alpha(p) = 1_{||alpha p|| < 1/log p}
D_alpha(x)  = sum_{p <= x} chi_alpha(p)
N_alpha(x)  = sum_{p <= x} chi_alpha(p) g(p)
A_alpha(x)  = N_alpha(x) / D_alpha(x)
g(p)        = (p^+ - p) / log p
```

## Current endpoint target

The current compressed `s=2` endpoint class is:

```text
RBDH_pair_short(Hcal)
  <=> CPC_3^sharp(Hcal)
  <=> SPAC_2^sharp
  <=> SU2Pair_2^sharp
  <=> DyadicDerivativeU^2
  <=> AU^3
```

The endpoint itself remains **OPEN**.

## Repository layout

```text
AGENTS.md                         Codex operating rules and status discipline
README.md                         This file
CITATION.cff                      Citation metadata placeholder
LICENSE_PENDING.md                License decision placeholder

source_texts/                     Original large text artifacts
  Prime_Resonance_Gap_500_Page_Paper.txt
  prime_gap_resonance_project_250_page_breakdown.txt

docs/
  paper/                          Copy of the generated 500-page paper
  ledger/                         Copy of the 250-page project ledger
  status/                         Global status, theorem index, forbidden upgrades
  modules/                        Current modules, dependency graph, indexes
  reviews/                        Project-wide reviews and audits
  codex/                          Prompts, continuation protocol, review checklist

papers/
  paper_I_structural_obstruction/
  paper_II_conditional_finite_type/
  paper_III_s2_endpoint_compression/

experiments/                      Computational experiment stubs
scripts/                          Lightweight audit/index scripts
.github/                          Codex prompt files, workflows, issue templates
```

## How to continue

A continuation agent should begin with:

```text
Read AGENTS.md, docs/status/global_status.md, docs/status/forbidden_upgrades.md,
docs/codex/continuation_protocol.md, docs/status/long_term_plan.md, and
docs/reviews/Prime_Resonance_Gap_1000_Page_Review.md. Then continue from the
latest module.
```

The current mathematical target is the residual derivative cube:

```text
(1/D) sum_{D<|d|<=2D} sum_{xi != 0} |widehat{B_d}(xi)|^4 = o(1)
```

where:

```text
B_d(n) = f(n+d) conjugate(f(n))
f      = nu - 1
```

Do not call this solved. It is not. The endpoint has merely been reduced to a more explicit formula, with the analytic estimates still open.
