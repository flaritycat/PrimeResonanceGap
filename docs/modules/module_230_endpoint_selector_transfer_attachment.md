# Module 230: Endpoint selector-transfer attachment ledger

## 1. Precise theorem / claim being advanced

This module attaches selector-transfer requirements to every endpoint arrow
inventoried in Modules 227-229.

Define:

```text
EndpointSelectorAttach_230.
```

Claim:

```text
EndpointSelectorAttach_230
```

is the current ledger that records, for each endpoint arrow:

```text
source selector class,
target selector class,
selector edge or chain,
required residual fourth-moment norm,
active selector-transfer rows,
classification of the row,
and remaining open transfer input.
```

The purpose is not to prove selector transfer. The purpose is to remove the
ambiguity left by phrases such as "plus selector transfer" in earlier modules.
Those phrases now mean a specific norm after forming the relevant residual
object.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module is an attachment ledger. It does not estimate any selector-transfer
row and does not upgrade any endpoint theorem.

## 3. Definitions and variables

Selector classes:

```text
fs      finite-stage / reference / survivor / core-floor model selector
bern    hidden Bernoulli lift
sm      smoothed finite-band frozen selector
fr      sharp frozen dyadic selector
mv      actual sharp moving selector
W       W-tricked prime or von-Mangoldt model
cyc     finite cyclic Fourier model
int     interval model
model   abstract projected or local model
```

The actual selector is:

```text
mv: chi_alpha(p)=1_{||alpha p||<1/log p}.
```

For each selector or model class `s`, define:

```text
nu_s,
f_s=nu_s-1,
B_{d,s}(n)=f_s(n+d)conj(f_s(n)),
c_{d,s}=E_n B_{d,s}(n),
B_{d,s}^circ(n)=B_{d,s}(n)-c_{d,s}.
```

The pair objects are:

```text
P_{d,s}(n)=nu_s(n+d)conj(nu_s(n)),
R_{d,s}(n)=P_{d,s}(n)-kappa_w(d).
```

When a selector step changes W-normalization or the local pair model, the
centering row must also compare the two versions of `kappa_w(d)`. That
comparison is not absorbed into the notation above.

For an adjacent edge:

```text
a -> b
```

let:

```text
T_{a->b}
```

be the declared transport map when the two classes do not live on the same
space. Define:

```text
Delta B_d(a->b)=B_{d,b}-T_{a->b}B_{d,a},
Delta R_d(a->b)=R_{d,b}-T_{a->b}R_{d,a}.
```

The unprojected nonzero residual transfer norm is:

```text
Sel_B^full(a->b;D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} |widehat{Delta B_d(a->b)}(xi)|^4.
```

The projected major transfer norm is:

```text
Sel_B^major(a->b;N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      ||P_M^b B_{d,b}
          - T_{a->b}(P_M^a B_{d,a})||_{U^2}^4.
```

The minor transfer norm is:

```text
Sel_B^minor(a->b;D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      ||Pi_minor^b B_{d,b}
          - T_{a->b}(Pi_minor^a B_{d,a})||_{U^2}^4.
```

The pair-residual transfer norm is:

```text
Sel_R^pair(a->b;D)
  = (1/D) sum_{D<|d|<=2D}
      ||Delta R_d(a->b)||_{U^2}^4.
```

For rectangle statements, use the weighted variance transfer norm:

```text
Sel_Rect(a->b;D)
  = (1/D) sum_{D<|d|<=2D}
      E_h | Rect_{d,b}(h)-T_{a->b}Rect_{d,a}(h) |^2,
```

where:

```text
Rect_{d,s}(h)
  = E_n Phi(n/N,h/N) P_{d,s}(n+h)conj(P_{d,s}(n))
      - Sigma_w(d,h) E_n Phi(n/N,h/N).
```

If cutoffs, smoothing, W-normalization, or local models differ across the
selector step, `Sel_Rect` must include those differences explicitly.

## 4. Assumptions

This attachment ledger assumes:

- all dyadic averages use the same shift shell `D<|d|<=2D`;
- the target endpoint selector is `mv` unless another target class is
  explicitly declared;
- every selector step uses fixed `w`, then `N -> infinity`, then
  `w -> infinity`;
- major and minor projections have declared denominator ranges and zero-mode
  conventions;
- pair residuals are centered by the exact `kappa_w(d)`;
- rectangle residuals use the exact `Sigma_w(d,h)`;
- projected residual cubes use `Omega_w^proj(d,h,k;t)` when kernel shifts are
  active;
- Bernoulli or finite-stage statements require deterministic extraction before
  they can become actual `mv` statements;
- a row classified as endpoint-strength cannot be used as a harmless side
  package.

## 5. Selector attachment table

The table below attaches selector requirements to the endpoint arrows.

| Arrow or target | Residual object | Same-selector status | If source is `s_0` and target is `mv` | Active rows | Classification |
|---|---|---|---|---|---|
| `ResCube_3^sharp <-> DyadicDerivativeU^2` | `B_d^circ` / nonzero `B_d` | structural identity | require `Sel_B^full(s_0->mv)=o(1)` or a major/minor composition proving it | boundary, prefix, denominator, W-residue, prime-power, centering; if split, Module 218 rows | endpoint-strength unless localized |
| `DyadicDerivativeU^2 <-> AU^3` | eight-vertex cube of `B_d` | structural reindexing | same as `Sel_B^full`, with the eight-vertex transfer expanded after forming `B_d` | same rows as full residual cube; no projection move from `B_d` to `f` | endpoint-strength unless localized |
| exact major/minor split | `B_d` Fourier fourth moment | structural only for one exact sharp partition | require `Sel_B^major + Sel_B^minor + MajorMinorSelCompat_3(P_adm)` | `PartBdSel_4`, `ArcBdSel_4`, `DenMMErr`, `ZeroMMErr`, `ChainMMErr`, `BdMMErr`, `PPWMMErr` | mixed to endpoint-strength |
| `ProjectedMajorTarget_3^B` | `P_M B_d` | selector-fixed major target | require `MajorSelectorTransfer_3^P(P_adm;s_0->mv)` | `SelErr_major^P`, boundary, transition, moving-window, prefix, denominator, tail, projection, W-residue, prime-power, centering | mixed; local only for fixed boundary/prefix rows |
| `MinorTarget_3^B` | `Pi_minor B_d` | selector-fixed minor target | require `MinorArcTransfer_3^B(s_0->mv)` | `Sel_B^minor`, threshold stability, arc-boundary, W-limit, prime-power, dyadic range, selector chain | mixed; transverse rows can be endpoint-strength |
| `ResCube_3^sharp <-> CPC_3^sharp` | `B_d` and `R_d` | conditional even at fixed selector | require `Sel_B^full` and `Sel_R^pair` along the same selector chain, plus `PairResidualTransfer_229` | linear margin, `kappa_w` centering, zero-mode, boundary, W, prime-power, range | mixed to endpoint-strength |
| `CPC_3^sharp <-> SPAC_2^sharp` | `R_d` | structural only after same centered `R_d` is fixed | require `Sel_R^pair(s_0->mv)` plus `CPCSPACAlign_229` | covariance calibration, cutoffs, interval/cyclic transfer, W, prime-power, range | mixed |
| `SPAC_2^sharp <-> SU2Pair_2^sharp` | `R_d` autocorrelation / `U^2` | structural at fixed `R_d` | require `Sel_R^pair(s_0->mv)` before using in `mv` | centering, pair residual transfer, boundary/cutoff alignment | mixed |
| `CPC_3^sharp <-> RBDH_pair_short` | `P_d`, `R_d`, rectangle residual | conditional even at fixed selector | require `Sel_Rect(s_0->mv)` and `Sel_R^pair(s_0->mv)` plus `RBDHCPCBridge_229` | exact `Sigma_w`, pair mean calibration, covariance calibration, cutoffs, W, prime-power, range | mixed to endpoint-strength |
| Bernoulli or finite-stage endpoint estimate | `Pi B_d`, `Pi in {Id_nonzero,P_M,Pi_minor}` | not an actual-selector theorem | require `DetExtract_3^Pi(s_0->mv)` | `BernSum`, `BernCouple`, `StageConv`, `DiagStable`, `ExtractCompat`, `AlphaExc` | mixed to endpoint-strength; metric only if alpha-exception is metric |
| frozen to moving selector edge | `Pi B_d` | not automatic | require `FrozenMovingObstruction_3^Pi` and `MoveLayerCube_3^Pi` rows | moving layer, amplitude, dyadic prefix, denominator/projection, centering | mixed to endpoint-strength |

## 6. Reduction / attachment proof

The reduction is a repeated triangle inequality in the correct residual norm.

For the unprojected residual cube, write:

```text
B_{d,mv}=T_{s_0->mv}B_{d,s_0}+Delta B_d(s_0->mv).
```

Then:

```text
sum_{xi != 0} |widehat{B_{d,mv}}(xi)|^4
  <= C sum_{xi != 0}
        |widehat{T_{s_0->mv}B_{d,s_0}}(xi)|^4
     + C sum_{xi != 0}
        |widehat{Delta B_d(s_0->mv)}(xi)|^4.
```

Averaging over `d` gives:

```text
ResFour_B^{mv}(D)
  <= C ResFour_B^{s_0}(D)
     + C Sel_B^full(s_0->mv;D)
     + side rows.
```

The side rows are exactly the active rows listed in the table: boundary,
prefix, transition, moving-window, denominator, tail, projection, W-residue,
prime-power, centering, and extraction rows.

The same argument gives:

```text
M_major^{mv}
  <= C M_major^{s_0} + C Sel_B^major(s_0->mv) + side rows,
```

and:

```text
M_minor^{mv}
  <= C M_minor^{s_0} + C Sel_B^minor(s_0->mv) + side rows.
```

For pair-residual arrows, replace `B_d` by `R_d` and use:

```text
Sel_R^pair(s_0->mv).
```

For RBDH arrows, the norm must remain the rectangle variance norm:

```text
Sel_Rect(s_0->mv).
```

A pair `U^2` transfer norm does not by itself transfer an uncentered weighted
rectangle-BDH statement with cutoff `Phi` and local model `Sigma_w(d,h)`.

Therefore every endpoint arrow is selector-ready only after both conditions
hold:

```text
the fixed-selector structural or analytic arrow is available,
the selector-transfer norm attached in the table is available.
```

No selector-transfer norm is estimated here.

## 7. Classifications and corrections

This module corrects one ambiguity in the previous endpoint map:

```text
"selector transfer" is not one package.
```

It splits into at least three different norms:

```text
Sel_B^major,
Sel_B^minor,
Sel_B^full,
```

plus pair and rectangle variants:

```text
Sel_R^pair,
Sel_Rect.
```

The correct norm is determined by the object being transferred, not by the
name of the endpoint arrow.

The most dangerous row remains:

```text
Core residual selector difference.
```

If it is unlocalized, it is endpoint-strength. The project should not accept:

```text
CoreSel_4=o(1)
```

as a small side error unless a later module supplies a genuinely smaller
localized or structured proof.

`LocalBdPkg_226` remains the smallest honest positive-looking target:

```text
one fixed projected-major boundary/prefix row,
same selector class,
same projection,
same dyadic shell,
same W-limit order.
```

It does not provide any of the mixed selector rows in the table.

## 8. Edge cases

- If an endpoint estimate is stated directly in selector class `mv`, no
  selector transfer is needed for that class, but all analytic side packages
  remain open.
- If an estimate is proved in `W`, `cyc`, `int`, `model`, `sm`, `fr`, `bern`,
  or `fs`, it is not an actual-selector estimate until the attached transfer
  row is proved.
- If major and minor pieces are transferred along different selector chains,
  `ChainMMErr` from Module 218 is active.
- If a smoothed major projection and a sharp minor projection are combined,
  `PartBdSel_4` and `ArcBdSel_4` are active.
- If the frozen-to-moving step is present, `MoveLayerCube_3^Pi` cannot be
  replaced by a one-point count of threshold-layer primes.
- If a Bernoulli estimate is used, expectation or high probability is not
  enough without summability and coupling to `mv`.
- If a finite-stage selector changes with the scale, diagonal stability must
  produce one admissible limiting selector before the estimate can be used.
- If `R_d` is transferred but `kappa_w(d)` or W-normalization changes, the
  centering row is active.
- If rectangle cutoffs or `Sigma_w(d,h)` conventions change, `Sel_Rect` must
  include that change; pair `U^2` transfer is not a substitute.
- If centering is performed before projection in one selector class and after
  interval truncation in another, zero-mode leakage must be controlled.

## 9. Where it fits in the project map

The endpoint-equivalence audit now has:

```text
Module 227
  -> endpoint arrow inventory
Module 228
  -> structural arrow audit
Module 229
  -> analytic side-package audit
Module 230
  -> selector-transfer attachment ledger.
```

The next planned module is:

```text
Module 231
  -> consolidated endpoint dependency table with each arrow labeled by
     allowed status labels.
```

This module supplies the selector columns for that table.

## 10. What remains open

This module does not prove:

- `Sel_B^full=o(1)`;
- `Sel_B^major=o(1)`;
- `Sel_B^minor=o(1)`;
- `Sel_R^pair=o(1)`;
- `Sel_Rect=o(1)`;
- `MajorSelectorTransfer_3^P`;
- `MinorArcTransfer_3^B`;
- `MajorMinorSelCompat_3(P_adm)`;
- `FrozenMovingObstruction_3^Pi`;
- `MoveLayerCube_3^Pi`;
- `DetExtract_3^Pi(s -> mv)`;
- `LocalBdPkg_226`;
- `PairResidualTransfer_229`;
- `CPCSPACAlign_229`;
- `RBDHCPCBridge_229`;
- `MajorAnalyticPkg_229`;
- `MinorAnalyticPkg_229`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `SPAC_2^sharp`;
- `SU2Pair_2^sharp`;
- `DyadicDerivativeU^2` as an estimate;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite this attachment ledger as proof of selector transfer.
- Do not use one selector norm for all endpoint arrows; `B_d`, `R_d`, and
  rectangle residuals require different transfer norms.
- Do not transfer a model, cyclic, W-tricked, smoothed, frozen, Bernoulli, or
  finite-stage estimate to `mv` without the attached residual
  fourth-moment row.
- Do not combine major and minor transferred estimates without Module 218's
  compatibility rows.
- Do not classify `fr->mv` as harmless threshold drift without
  `MoveLayerCube_3^Pi`.
- Do not turn Bernoulli or finite-stage estimates into fixed-alpha results
  without `DetExtract_3^Pi(s -> mv)`.
- Do not use metric alpha-exception accounting as an all-alpha theorem.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not use `LocalBdPkg_226` outside its fixed boundary/prefix row.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
