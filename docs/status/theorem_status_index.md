# Theorem Status Index

This is the compact live status index for the active proof ledger. It is a
navigation aid, not a proof. When this file conflicts with
`docs/status/global_status.md`, treat `global_status.md` and the latest
module as authoritative and update this index.

Allowed statuses remain:

```text
PROVEN
CONDITIONAL
STRUCTURAL / EXTRACTION
HEURISTIC
OPEN
FALSE / BLOCKED
```

| Object | Status | Dependencies / blockers | Last relevant module | Can be used as input? |
|---|---|---|---|---|
| Original selected-average problem: existence of irrational `alpha` with `A_alpha(x)->L0>1` | OPEN | Actual sharp selector, full gap object, endpoint/obstruction branches | `global_status.md` | No |
| Metric theorem `A_alpha(x)->1` a.e. | PROVEN according to project ledger | Lebesgue-a.e. only; does not imply all-alpha theorem | `global_status.md` | Yes, only in metric/a.e. contexts |
| Finite-type theorem | CONDITIONAL | Finite-type hypotheses and side packages | `global_status.md`, Paper II | Only under stated hypotheses |
| `s=2` rational-major endpoint | OPEN | Exact local models, side packages, transfer, endpoint estimates | `module_178_residual_cube.md` onward | No |
| Residual derivative cube target `ResCube_3^sharp` | OPEN | Major target, minor target, selector, boundary/W/prime-power transfer | `module_178_residual_cube.md`, `module_179_fourier_major_minor.md` | No |
| `RBDH_pair_short(Hcal)` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `CPC_3^sharp(Hcal)` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `SPAC_2^sharp` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `SU2Pair_2^sharp` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `DyadicDerivativeU^2` | OPEN | Structurally equivalent target; analytic estimate still missing | `module_228_structural_arrow_audit.md` | Only as structural target label |
| `AU^3` | OPEN | Endpoint class plus side packages | `module_227_endpoint_arrow_inventory.md` | No |
| `WProjectedLocalMatch_3^major` | CONDITIONAL | Residual subset-HL, boundary, W-residue, prime-power, projection, denominator, selector rows | `module_209_w_admissible_projected_local_model.md` | Only as a conditional schema |
| `ProjectedMajorTarget_3^B` | OPEN | `WProjectedLocalMatch_3^major` plus projected model neutrality | `module_206_exact_projected_major_arc_target.md` | No |
| `ProjectedModelNeutralityGate_260(P_adm)` | CONDITIONAL | Exact model discipline, generic tail, kernel route, collision route, uniformity, model-domain conventions | `module_260_projected_model_neutrality_gate.md`, `module_267_projected_model_neutrality_verdict.md` | Only if every row is supplied |
| `CollNeutral_260(P_adm)` | OPEN | Absolute collision-defect control with `|W_M|` and same-family uniformity | `module_264_collision_diagonal_strata.md` | No |
| `AbsCollStrataGate_264` | OPEN | Structural strata, nonstructural load, overflow, finite-prime-set CRT, absolute kernel weight | `module_264_collision_diagonal_strata.md` | No |
| `SignedCoverGate_264` | OPEN | Exact signed averaging, structural signed rows, proper-support cancellation, full-cover clusters | `module_264_collision_diagonal_strata.md` | No; not an absolute row |
| `KernelAbsBudget_265` | OPEN | `A_W(M)eps_gen`, structural/collision load, overflow, tail and range budgets | `module_265_kernel_absolute_vs_signed.md` | No |
| `KernelSignedBudget_265` | OPEN | Exact signed `W_M`, generic signed row, signed structural/full-cover cluster rows | `module_265_kernel_absolute_vs_signed.md` | No; not an absolute row |
| `UniformityLedger_266` | OPEN | W-limit, denominator/CRT, projection, kernel tail, cutoff, W-residue, dyadic, selector, supremum closure rows | `module_266_uniformity_admissible_family.md` | No |

## Guardrail Notes

- Equivalence classes and structural decompositions are not proofs.
- A conditional gate is not an established theorem.
- Model, smoothed, frozen, or cyclic estimates do not reach the actual sharp
  moving selector without named transfer rows.
- `Sigma_w(d,h)` is not pointwise `kappa_w(d)^2`.
- No endpoint-strength object may be assumed in a module whose purpose is to
  prove or reduce that endpoint.
