# Global status

This file is the first status document Codex should read.

Current frontier:

```text
Latest module frontier: Module 261
Active phase: Phase H, projected model-neutrality feasibility window
Latest project-wide review:
  docs/reviews/Prime_Resonance_Gap_1000_Page_Review.md
```

| Claim | Status |
|---|---|
| Existence of irrational `alpha` with `A_alpha(x) -> L0 > 1` | **OPEN** |
| All irrational `alpha` satisfy no positive finite limit `L0 > 1` | **OPEN** |
| Metric theorem `A_alpha(x) -> 1` for Lebesgue-a.e. irrational `alpha` | **PROVEN according to project ledger** |
| Finite-type no-positive-limit theorem | **CONDITIONAL** |
| `s=2` rational-major endpoint | **OPEN** (analytic-engine descriptor) |

## What the project has achieved

- Metric theorem recorded as proven according to the ledger.
- Structural covariance extraction.
- Clipped/tail obstruction routing.
- Finite-local covariance cancellation and spectral suppression.
- Exact local pair, rectangle, and two-rectangle models.
- Compression of the `s=2` rational-major branch to one endpoint class.
- Residual derivative cube major/minor decomposition and dependency map.
- One-point fixed-support prototype reduced to fixed-row kernel, boundary,
  short-interval, and side-row feasibility gates.
- A project-wide 1000-page-scope review through Module 252.
- A fixed-row short-interval range gate for the W one-point boundary mean.
- A side-row convention gate separating exact conventions from weighted
  defect estimates.
- A fixed-row one-point feasibility verdict: valid conditional route, no
  proved closure.
- A same-slot two-point escalation gate, diagnostic only and still
  conditional.
- A minor-arc reentry comparison showing that boundary gates and
  `NarrowMinorArc_3^B` control different objects unless a localized transfer
  row is supplied.
- A projected-major reentry comparison showing that fixed boundary gates are
  only local slices of `CycIntTransfer_3^major`, not proofs of
  `WProjectedLocalMatch_3^major` or `ProjectedMajorTarget_3^B`.
- An eighth plan update closing Phase G as a diagnostic window and redirecting
  the next branch to projected model-neutrality.
- A projected model-neutrality feasibility gate separating generic W-tail
  cancellation, kernel budget, collision defects, denominator/W-limit
  uniformity, and model-domain conventions.
- `Reflective_3.md`, a memory log reviewing Modules 221-260 and preserving
  the open endpoint statuses.

## What the project has not proved

- The original positive existence problem.
- The all-alpha no-positive-limit theorem.
- The unconditional finite-type theorem.
- `RBDH_pair_short(Hcal)`, `CPC_3^sharp(Hcal)`, or `AU^3(Hcal)`.
- `ResCube_3^sharp`, `ProjectedMajorTarget_3^B`, or the actual sharp
  moving-selector endpoint.
- `ProjectedModelNeutralityGate_260` or
  `ProjectedModelNeutrality_3^major(P_adm)`.
- `FixedRowOnePointPkg_249`, `KernelHolderGate_252`,
  `WShortRangeGate_253`, `SideConventionGate_254`,
  `FixedRowFeasGate_255`, `TwoPointEscGate_256`,
  `BoundaryMinorReentry_257`, `BoundaryMajorReentry_258`,
  `OnePointBIHL_242`, or `TwoPointBIHL_256` outside exact model conventions.

## Current endpoint class

```text
RBDH_pair_short(Hcal)
  <=> CPC_3^sharp(Hcal)
  <=> SPAC_2^sharp
  <=> SU2Pair_2^sharp
  <=> DyadicDerivativeU^2
  <=> AU^3
```

Status: **OPEN**, modulo side packages.

## Active diagnostics

The completed Phase G fixed-row diagnostic remains:

```text
FixedRowOnePointPkg_249
  = KernelAvgStrength_245^local
    + OnePointSideRows_246^local.
```

The completed Phase G gates are:

```text
Boundary mass:
  (C_mean_245+1)A_W(M)GeomModel_251+MassErr_245=o_W(1)

Holder:
  K_q(M)E_p(s0)=o_W(1)

W short-interval range:
  eps_WPNT_253 BLength_245
    + WPNTError_253
    + BadRangeMass_253=o_W(1)

Side-row convention:
  SideConventionGate_254
    => OnePointSideRows_246^local

Assembled one-point verdict:
  FixedRowFeasGate_255
    = MeanFeasGate_255 + SideConventionGate_254
    => FixedRowOnePointPkg_249

Two-point diagnostic:
  TwoPointEscGate_256
    => BoundaryIntervalHL_234({(00,0),(00,1)},(00,0))

Minor-arc reentry:
  BoundaryMinorReentry_257
    classifies boundary/minor-arc routing

Projected-major reentry:
  BoundaryMajorReentry_258
    classifies boundary/projected-major routing

Phase H next target:
  ProjectedModelNeutralityGate_260(P_adm)
    conditionally reduces NeutralErr_major^P to generic-tail, kernel,
    collision, denominator, W-limit, and model-convention rows

Next governance checkpoint:
  Module 262 fifth plan challenge
```

Status: **CONDITIONAL**.
