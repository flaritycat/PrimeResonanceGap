# Module 231: Consolidated endpoint dependency table

## 1. Precise theorem / claim being advanced

This module consolidates Modules 227-230 into one endpoint dependency table.

Define:

```text
EndpointDependencyTable_231.
```

Claim:

```text
EndpointDependencyTable_231
```

is the current allowed-status ledger for the residual derivative cube endpoint
and its surrounding equivalence arrows. It records, row by row:

```text
arrow or target,
fixed-object status,
analytic side package,
selector-transfer package,
boundary / W / prime-power / range package,
allowed status label,
and current verdict.
```

This is a dependency table, not a proof of the endpoint. No row below upgrades
`ResCube_3^sharp`, `RBDH_pair_short`, `CPC_3^sharp`, `SPAC_2^sharp`,
`SU2Pair_2^sharp`, `DyadicDerivativeU^2`, or `AU^3` to `PROVEN`.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The table is extracted from earlier modules. It adds no analytic estimate and
does not prove any transfer package.

## 3. Definitions and variables

Use the residual derivative object:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)),
c_d=E_n B_d(n),
B_d^circ(n)=B_d(n)-c_d.
```

The nonzero residual Fourier fourth moment is:

```text
ResFour_B(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} |widehat{B_d}(xi)|^4.
```

The pair product and centered pair residual are:

```text
P_d(n)=nu(n+d)conj(nu(n)),
R_d(n)=P_d(n)-kappa_w(d).
```

The linear margin is:

```text
L_d(n)=f(n+d)+conj(f(n)).
```

For nonzero frequencies:

```text
widehat{R_d}(xi)=widehat{B_d}(xi)+widehat{L_d}(xi).
```

The exact local models are:

```text
kappa_w(d),
Sigma_w(d,h),
Theta_{w,S}(d,h,k),
Omega_w(d,h,k),
Omega_w^proj(d,h,k;t).
```

Here `Sigma_w(d,h)` is the exact rectangle model. It is not pointwise
`kappa_w(d)^2`.

The selector-transfer norms from Module 230 are:

```text
Sel_B^full,
Sel_B^major,
Sel_B^minor,
Sel_R^pair,
Sel_Rect.
```

The actual target selector is:

```text
mv: chi_alpha(p)=1_{||alpha p||<1/log p}.
```

Statements first proved in:

```text
model, W, cyc, int, sm, fr, bern, fs
```

are not `mv` statements until the corresponding selector-transfer row is
proved.

## 4. Assumptions

This table assumes:

- one fixed dyadic shell `D<|d|<=2D`;
- normalized Fourier conventions;
- the zero mode is removed when `ResFour_B` or the derivative `U^2` endpoint
  is used;
- exact local models `kappa_w`, `Sigma_w`, and `Omega_w` are kept distinct;
- projected major-arc local models use `Omega_w^proj(d,h,k;t)` when kernel
  shifts are active;
- W-dependent statements use fixed `w`, then `N -> infinity`, then
  `w -> infinity`;
- selector class is declared before an estimate is cited;
- `LocalBdPkg_226` is only one fixed projected-major boundary/prefix row, not
  full boundary transfer;
- allowed status labels are only:

```text
PROVEN,
CONDITIONAL,
STRUCTURAL / EXTRACTION,
HEURISTIC,
OPEN,
FALSE / BLOCKED.
```

## 5. Consolidated endpoint dependency table

| Row | Arrow / target | Fixed-object status | Analytic side package | Selector-transfer package | Boundary / W / prime-power / range package | Allowed status label | Current verdict |
|---|---|---|---|---|---|---|---|
| 1 | `ResCube_3^sharp` as `ResFour_B(D)=o(1)` | target identity only | needs major+minor or equivalent residual fourth-moment estimate | `Sel_B^full` if not already `mv` | full boundary, W, prime-power, range, zero-mode discipline | `OPEN` | endpoint target remains open |
| 2 | `ResCube_3^sharp <-> DyadicDerivativeU^2` | exact Fourier `U^2` identity for `B_d^circ` | none at fixed object | `Sel_B^full` or major/minor composition for selector changes | zero-mode and domain compatibility | `STRUCTURAL / EXTRACTION` | identity only; no estimate |
| 3 | `DyadicDerivativeU^2 <-> AU^3` | eight-vertex reindexing of the same derivative cube | none at fixed object | `Sel_B^full`; transfer must occur after forming `B_d` | boundary and projection compatibility if model changes | `STRUCTURAL / EXTRACTION` | reindexing only; no AU^3 estimate |
| 4 | exact sharp major/minor split | exact partition of `{xi != 0}` | major and minor estimates both needed for endpoint | `Sel_B^major + Sel_B^minor + MajorMinorSelCompat_3(P_adm)` | `PartBdSel_4`, `ArcBdSel_4`, `DenMMErr`, `ZeroMMErr`, `BdMMErr`, `PPWMMErr` if not exact | `STRUCTURAL / EXTRACTION` for exact split; `CONDITIONAL` for buffered/smoothed recomposition | exact algebra only in one fixed partition |
| 5 | `ProjectedMajorTarget_3^B` | fixed projected `P_M B_d` target | `MajorAnalyticPkg_229` | `MajorSelectorTransfer_3^P` / `Sel_B^major` | `WProjectedLocalMatch_3^major`, `ProjectedModelNeutrality_3^major`, `CycIntTransfer_3^major`, `PPSPTransfer_3^major`, collision and range rows | `CONDITIONAL` | projected major target remains conditional |
| 6 | `MinorTarget_3^B` | fixed minor `Pi_minor B_d` target | `MinorAnalyticPkg_229` | `MinorArcTransfer_3^B` / `Sel_B^minor` | arc-boundary, threshold, W-growth, prime-power, dyadic range rows | `CONDITIONAL` | minor target remains conditional |
| 7 | `ResCube_3^sharp <-> CPC_3^sharp` | not structural because `B_d` and `R_d` differ by the linear margin | `PairResidualTransfer_229` and `LinearU2Margin_229` | `Sel_B^full` and `Sel_R^pair` along the same selector chain | `kappa_w` centering, zero-mode, boundary, W, prime-power, range | `CONDITIONAL` | valid only with margin and transfer packages |
| 8 | `CPC_3^sharp <-> SPAC_2^sharp` | structural only after both sides are the same centered `R_d` in one model | `CPCSPACAlign_229` and `CovCal_229` | `Sel_R^pair` | covariance, cutoff, cyclic/interval, W, prime-power, range | `CONDITIONAL` before alignment; structural after alignment | not a free endpoint arrow |
| 9 | `SPAC_2^sharp <-> SU2Pair_2^sharp` | fixed-`R_d` autocorrelation / `U^2` identity | none after same `R_d` is fixed | `Sel_R^pair` for selector changes | boundary, cutoff, centering compatibility | `STRUCTURAL / EXTRACTION` at fixed object; `CONDITIONAL` under selector/domain changes | identity only after same object is fixed |
| 10 | `CPC_3^sharp <-> RBDH_pair_short` | not structural because rectangle residuals and pair `U^2` live in different norms | `RBDHCPCBridge_229` | `Sel_Rect` and `Sel_R^pair` | exact `Sigma_w`, pair mean calibration, covariance, cutoff, W, prime-power, range | `CONDITIONAL` | endpoint-grade bridge remains open |
| 11 | `RBDH_pair_short` representative | rectangle variance target | full endpoint RBDH engine, not first-moment HL | `Sel_Rect` if not already `mv` | exact local model, W-order, boundary, prime-power, range | `OPEN` | representative endpoint object remains open |
| 12 | `CPC_3^sharp` representative | pair-residual `U^2` / covariance target | pair residual and covariance packages | `Sel_R^pair` plus any `B_d` transfer if compared to ResCube | `kappa_w`, covariance, boundary, W, prime-power, range | `OPEN` | representative endpoint object remains open |
| 13 | `AU^3` representative | derivative eight-vertex formulation | same analytic content as derivative residual cube after reindexing | `Sel_B^full` | boundary, W, prime-power, range | `OPEN` | not proved by structural reindexing |
| 14 | `LocalBdPkg_226` fixed row | one projected-major cyclic-to-interval boundary/prefix row | weighted boundary tuple and model-mass package | same selector class only; no selector edge | `AbsMajorant_225`, `KernelAbsTail_225`, `BoundaryTupleHL_225`, `BoundaryModelMass_225`, `WPPBoundary_225`, `NormRow_224^P` | `CONDITIONAL` | local row remains open and limited |
| 15 | Bernoulli / finite-stage extraction to `mv` | not an actual-selector theorem at fixed model | model estimate plus extraction | `DetExtract_3^Pi(s -> mv)` | grid, summability, coupling, stage convergence, diagonal stability, alpha-exception rows | `STRUCTURAL / EXTRACTION` as requirement; analytic extraction `OPEN` | expectation or model convergence is insufficient |
| 16 | frozen-to-moving selector edge `fr -> mv` | not a pointwise threshold drift | `MoveLayerCube_3^Pi` and side rows | `FrozenMovingObstruction_3^Pi` | moving layer, amplitude, dyadic prefix, denominator/projection, centering | `STRUCTURAL / EXTRACTION` as obstruction; analytic transfer `OPEN` | one-point layer counts are insufficient |
| 17 | ordinary pair-BDH shortcut to `CPC_3^sharp` or `ResCube_3^sharp` | controls wrong object unless upgraded | missing margin and residual transfer | missing `Sel_B` / `Sel_R` rows | missing local, boundary, W, prime-power, range rows | `FALSE / BLOCKED` | blocked as standalone implication |
| 18 | first-moment HL or mean rectangle-HL to `RBDH_pair_short` | mean is not variance | missing variance-strength residual package | missing rectangle selector transfer | missing exact local model and W-uniform variance rows | `FALSE / BLOCKED` | blocked as standalone implication |
| 19 | pointwise replacement of `Sigma_w(d,h)` by `kappa_w(d)^2` | false model identity | no analytic package supplied | not a selector issue | exact local model discipline fails | `FALSE / BLOCKED` | forbidden replacement |
| 20 | full endpoint chain to actual `mv` | composition of rows 1-16 | all conditional packages needed | full selector chain and major/minor compatibility needed | all boundary, W, prime-power, range, centering packages needed | `OPEN` | endpoint class remains open |

## 6. Reduction / proof of the table

Rows 2, 3, 4, and 9 inherit their fixed-object structural content from Module
228:

```text
Fourier U^2 identity,
eight-vertex reindexing,
exact sharp nonzero major/minor partition,
fixed-pair autocorrelation / U^2 identity.
```

These rows become conditional when the proof changes selector class, domain,
projection, denominator grid, or centering convention.

Rows 5-8 and 10 inherit their analytic side packages from Module 229:

```text
MajorAnalyticPkg_229,
MinorAnalyticPkg_229,
PairResidualTransfer_229,
CPCSPACAlign_229,
RBDHCPCBridge_229.
```

Their status is `CONDITIONAL`, because the packages are named but not proved.

Rows 11-13 record the representative endpoint objects themselves. They are
`OPEN` by the project ledger. Structural equivalence language does not change
that status.

Rows 14-16 record transfer or local-row subpackages. They are not endpoint
proofs. `LocalBdPkg_226` is conditional and local only in its fixed row.
`DetExtract_3^Pi` and `FrozenMovingObstruction_3^Pi` are structural
requirements whose analytic estimates remain open.

Rows 17-19 are blocked shortcuts from Modules 198-199 and the exact local
model discipline. Their status is `FALSE / BLOCKED` as standalone
implications.

Finally, row 20 is the full endpoint class. Since at least one open analytic
or transfer row is required in every route, the composed actual-selector
endpoint remains:

```text
OPEN.
```

## 7. Edge cases

- If a theorem is stated directly in the actual selector class `mv`, selector
  transfer may be absent, but the analytic side packages remain open.
- If a theorem is proved in `model`, `W`, `cyc`, `int`, `sm`, `fr`, `bern`,
  or `fs`, it is not an actual-selector theorem without Module 230's attached
  transfer norm.
- If a row uses a smoothed major projection and a sharp minor projection,
  row 4 is conditional on the Module 218 partition rows.
- If `LocalBdPkg_226` is cited for anything beyond its fixed
  projected-major boundary/prefix row, the citation is too strong.
- If `CPC` or `SPAC` is formed from `P_d` while `SU2Pair` is formed from
  `R_d`, the structural identity is being applied to different objects.
- If rectangle cutoffs differ, `Sel_Rect` and `RBDHCPCBridge_229` must include
  the cutoff discrepancy.
- If the zero frequency is retained on one side and removed on another,
  centering and zero-mode leakage rows are active.
- If a Bernoulli or finite-stage statement is used for a fixed alpha, the
  deterministic extraction rows must be present.
- If frozen-to-moving transfer appears, one-point estimates for the threshold
  layer do not replace the residual moving-layer cube.
- If a route uses first-moment Hardy-Littlewood only to identify local factors,
  it may be useful background, but it is not a variance-strength endpoint row.

## 8. Where it fits in the project map

The endpoint-equivalence audit now has a four-step output:

```text
Module 227
  -> inventory of arrows
Module 228
  -> fixed-object structural identities
Module 229
  -> analytic side-package audit
Module 230
  -> selector-transfer attachment ledger
Module 231
  -> consolidated dependency table.
```

The next scheduled step is:

```text
Module 232
  -> fifth plan update and third plan challenge.
```

Module 232 should question whether this endpoint-equivalence audit has become
useful enough to guide the next analytic attack or whether the project should
stop adding dependency names and choose a smaller row to attempt.

## 9. What remains open

This module does not prove:

- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `SPAC_2^sharp`;
- `SU2Pair_2^sharp`;
- `DyadicDerivativeU^2=o(1)`;
- `AU^3`;
- `ProjectedMajorTarget_3^B`;
- `MinorTarget_3^B`;
- `MajorAnalyticPkg_229`;
- `MinorAnalyticPkg_229`;
- `PairResidualTransfer_229`;
- `CPCSPACAlign_229`;
- `RBDHCPCBridge_229`;
- `MajorSelectorTransfer_3^P`;
- `MinorArcTransfer_3^B`;
- `MajorMinorSelCompat_3(P_adm)`;
- `Sel_B^full=o(1)`;
- `Sel_B^major=o(1)`;
- `Sel_B^minor=o(1)`;
- `Sel_R^pair=o(1)`;
- `Sel_Rect=o(1)`;
- `LocalBdPkg_226`;
- `DetExtract_3^Pi(s -> mv)`;
- `MoveLayerCube_3^Pi`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not read a structural row as an analytic estimate.
- Do not read a conditional row as proved.
- Do not collapse `B_d`, `R_d`, and `P_d` into one object.
- Do not use one selector-transfer norm for pair, rectangle, major, minor,
  and unprojected residual rows.
- Do not cite `LocalBdPkg_226` as full boundary transfer.
- Do not cite ordinary pair-BDH as `PairResidualTransfer_229`.
- Do not cite first-moment Hardy-Littlewood as `RBDH_pair_short`.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not transfer model, cyclic, W-tricked, smoothed, frozen, Bernoulli, or
  finite-stage estimates to the actual sharp moving selector without the
  attached residual fourth-moment transfer rows.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
