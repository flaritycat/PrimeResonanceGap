# Module 246: One-point side-row audit

## 1. Precise theorem / claim being advanced

This module audits the side rows left outside the one-point boundary mean
reduction of Modules 242-245.

The active prototype is still:

```text
OnePointBIHL_242(s0,D0,rho0)
  = BoundaryIntervalHL_234({(00,0)},(00,0)).
```

Module 245 isolated the main weighted one-point mean input:

```text
KernelAvgStrength_245(s0,D0,rho0)
  => OPMeanErr_244(s0,D0,rho0)=o_W(1).
```

Define:

```text
OnePointSideRows_246(s0,D0,rho0)
```

to be the package:

```text
CutOne_242(s0,D0,rho0)=o_W(1),
RangeOne_242(s0,D0,rho0)=o_W(1),
WResOne_242(s0,D0,rho0)=o_W(1),
PPOne_242(s0,D0,rho0)=o_W(1),
NormZeroOne_242(s0,D0,rho0)=o_W(1).
```

The conditional claim is:

```text
KernelAvgStrength_245(s0,D0,rho0)
  + OnePointSideRows_246(s0,D0,rho0)
    => OnePointBIHL_242(s0,D0,rho0).
```

The audit verdict is:

```text
The one-point prototype is genuinely smaller than the projected residual
endpoint only if all five side rows are zero by convention or proved by
fixed-row local estimates. If any side row is closed only by a residual
fourth-moment endpoint, then the prototype has not escaped the endpoint.
```

This module does not prove the side rows.

## 2. Status label

`CONDITIONAL`

The module gives a conditional composition and a classification ledger for the
side rows. It does not prove W-residue, prime-power, range, cutoff,
normalization, or zero-mode estimates.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The active same-vertex forms are:

```text
lambda0=sigma0=(00,0),
v_lambda0(n,t)=v_sigma0(n,t)=n-t0.
```

Write:

```text
m0(n,t)=n-t0.
```

The active boundary intervals from Module 242 are:

```text
J_L(d,h,k;t) = {n: m0(n,t) <= L_N},
J_R(d,h,k;t) = {n: m0(n,t) > N-L_N}.
```

The fixed-row weighted averaging operator is:

```text
E_K F
  = (1/D0) sum_{D0<|d|<=2D0} E_{h,k,t}|W_M(t)| F(d,h,k;t).
```

For the active selector class, write:

```text
a_s0(n,t)=mu_s0(m0(n,t)).
```

The mean term audited in Modules 244-245 is:

```text
OPMeanErr_244
  = E_K sum_{r in {L,R}}
      |E_n 1_{J_r}(n)(a_s0(n,t)-1)|.
```

The five side rows are normalized as nonnegative weighted defects. The exact
project module may realize them by equality or by an upper bound; in either
case the required output is `o_W(1)` in the same fixed-row normalization.

### A. Cutoff row

Let:

```text
CutFail_246(n;d,h,k;t)
```

be the symmetric-difference indicator between the actual boundary/cutoff event
used in the source row and the simplified interval expression:

```text
cutoff0(n,t)(1_{J_L}(n)+1_{J_R}(n)).
```

The cutoff side row is controlled by:

```text
CutOne_242
  <= E_K E_n CutFail_246(n;d,h,k;t)(1+|a_s0(n,t)|).
```

### B. Range row

Let:

```text
RangeFail_246(n;d,h,k;t)
```

be the indicator that `m0(n,t)` or the associated row parameters leave the
allowed support, denominator grid, dyadic shell, or truncation range required
for the one-point prototype.

The range side row is controlled by:

```text
RangeOne_242
  <= E_K E_n RangeFail_246(n;d,h,k;t)(1+|a_s0(n,t)|).
```

### C. W-residue row

Let:

```text
WFail_246(n;d,h,k;t)
```

be the indicator that the fixed `p <= w` residue convention for `m0(n,t)` is
not the one used by the local model or by the selected W-tricked weight.

The W-residue side row is controlled by:

```text
WResOne_242
  <= E_K E_n WFail_246(n;d,h,k;t)(1+|a_s0(n,t)|).
```

### D. Prime-power row

If the active von Mangoldt-type weight is decomposed as:

```text
mu_s0 = mu_s0^prime + pp_s0,
```

then the one-point prime-power side row is:

```text
PPOne_242
  = E_K sum_{r in {L,R}}
      E_n 1_{J_r}(n)|pp_s0(m0(n,t))|.
```

If the selector class has no prime-power component by definition, this row is
zero by convention.

### E. Normalization and zero-mode row

Let:

```text
NormDrift_246(d,h,k;t)
```

measure the difference between the actual one-point normalization and the
normalization used in the model term `ell_r`.

Let:

```text
ZeroLeak_246(d,h,k;t)
```

measure any constant-mode contribution that reappears after interval
restriction, cutoff insertion, or projected-kernel truncation.

The combined normalization / zero-mode side row is controlled by:

```text
NormZeroOne_242
  <= E_K ( |NormDrift_246(d,h,k;t)| + |ZeroLeak_246(d,h,k;t)| ).
```

## 4. Assumptions

The side package requires all five estimates in the same fixed row:

```text
OnePointSideRows_246(s0,D0,rho0).
```

No estimate in this package may change:

```text
selector class s0,
projection P_M,
dyadic shell D0<|d|<=2D0,
boundary intervals J_L,J_R,
cutoff0,
denominator grid,
W-residue convention,
limit order w fixed, N -> infinity, then w -> infinity.
```

The permitted classifications are:

```text
zero by convention,
local,
mixed,
endpoint-strength,
open.
```

They mean the following.

`zero by convention`: the row vanishes from exact definitions in this
prototype.

`local`: the row is bounded by fixed-row one-point support, volume, residue,
or prime-power estimates that do not require residual fourth-moment endpoint
control.

`mixed`: the row needs a selector, projection, cutoff, W-residue,
denominator-grid, or model-to-actual transfer beyond the fixed one-point row.

`endpoint-strength`: the row is closed only by assuming projected residual
fourth-moment control, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, `AU^3`, or an equivalent endpoint package.

`open`: the row has not yet been estimated.

## 5. Proof / disproof / reduction

Module 244 gives the one-point reduction:

```text
OPMeanErr_244=o_W(1)
  + CutOne_242=o_W(1)
  + RangeOne_242=o_W(1)
  + WResOne_242=o_W(1)
  + PPOne_242=o_W(1)
  + NormZeroOne_242=o_W(1)
    => OnePointBIHL_242.
```

Module 245 gives:

```text
KernelAvgStrength_245
  => OPMeanErr_244=o_W(1).
```

Combining these two conditional implications gives:

```text
KernelAvgStrength_245 + OnePointSideRows_246
  => OnePointBIHL_242.
```

The rest of the module classifies what would be needed to make
`OnePointSideRows_246` credible.

### A. Cutoff row classification

`CutOne_242` is zero by convention if the source boundary event is exactly:

```text
cutoff0(n,t)(1_{J_L}(n)+1_{J_R}(n))
```

inside the active row.

It is local if the symmetric-difference set `CutFail_246` has weighted
one-point mass `o_W(1)` under the same `|W_M|` average. This may follow from a
deterministic boundary-volume estimate plus a one-point mass majorant of the
kind audited in Module 245.

It is mixed if proving the cutoff identity requires changing the interval
cutoff, smoothing the projection, moving the selector threshold, or comparing
two selector classes.

It is endpoint-strength if the only available bound is an unlocalized
projected residual cube estimate.

### B. Range row classification

`RangeOne_242` is zero by convention if the truncated row is defined so that:

```text
m0(n,t)
```

always lies in the permitted support and all denominator-grid constraints are
already built into `rho0`.

It is local if the range-failure set has fixed-row one-point mass `o_W(1)`.
The proof must include the `|W_M|` average and the active boundary intervals.

It is mixed if range repair changes `T0`, the denominator grid, the dyadic
shell, the projection, or the selector class.

It is endpoint-strength if range repair is supplied only by invoking the full
projected residual endpoint.

### C. W-residue row classification

`WResOne_242` is zero by convention if the W-tricked row restricts `m0(n,t)`
to the admissible residue class before the local model is formed and the same
restriction is used in `Theta_{w,{(00,0)}}^proj=1`.

It is local if the inadmissible residue set has one-point mass `o_W(1)` in the
fixed row.

It is mixed if the proof compares different W-residue conventions, changes
the W-family with `N`, or transfers from a W-tricked selector to a smoothed or
frozen selector.

It is endpoint-strength if W-residue synchronization is obtained only after
bounding a projected residual fourth moment.

### D. Prime-power row classification

`PPOne_242` is zero by convention when the active weight is prime-supported.

It is local if the weighted boundary prime-power mass:

```text
E_K sum_{r in {L,R}} E_n 1_{J_r}(n)|pp_s0(m0(n,t))|
```

is `o_W(1)` by a one-point prime-power sparsity estimate that survives the
absolute kernel mass.

It is mixed if prime-power removal is coupled to selector transfer,
W-residue repair, projection smoothing, or cutoff replacement.

It is endpoint-strength if prime-power removal is closed only by the projected
cube endpoint or by a cube-level prime-power transfer theorem.

### E. Normalization and zero-mode classification

`NormZeroOne_242` is zero by convention if the one-point weight is exactly
normalized on the active row and the projection/interval/cutoff operations do
not reintroduce any constant mode.

It is local if:

```text
E_K |NormDrift_246|=o_W(1),
E_K |ZeroLeak_246|=o_W(1),
```

by fixed-row normalization control and a truncated zero-mode estimate.

It is mixed if the proof changes centering convention, projection, interval
normalization, or selector class.

It is endpoint-strength if zero-mode leakage is bounded only by an endpoint
fourth-moment theorem.

## 6. Edge cases

- If the model selector has `a_model(n,t)=1` on the active row, then the main
  mean term is zero, but cutoff, range, W-residue, and normalization rows still
  must be exact or separately zero.
- If `cutoff0` already contains `J_L union J_R`, double-counting can occur
  unless the convention states whether `J_L` and `J_R` are inserted before or
  after cutoff restriction.
- If `J_L` and `J_R` overlap at very small `N` or under an oversized boundary
  length, the intervals must be interpreted with the fixed-row truncation
  convention before summing their contributions.
- If `m0(n,t)` crosses `0`, `N`, or the support of the W-tricked weight near a
  boundary endpoint, the range and cutoff rows are not interchangeable.
- If the W-residue convention is exact only for interior points, boundary
  residue failures must be assigned to `WResOne_242`, not hidden in the local
  factor `Theta_{w,{(00,0)}}^proj`.
- If prime powers are sparse only on full intervals, the estimate does not
  automatically control the boundary row after multiplication by `|W_M|`.
- If the projected kernel has a large absolute mass, every side row with a
  pointwise error must beat that mass, as in Module 245.
- If zero-mode removal is exact in the cyclic model but not after interval
  restriction, the leakage belongs to `NormZeroOne_242`.
- If any side row uses cancellation in `W_M`, it does not apply after the
  absolute value in the fixed-row average.

## 7. Where it fits in the project map

The Phase F2 chain is now:

```text
Module 242
  -> fixed OnePointBIHL_242.

Module 243
  -> exact singleton local model, Theta=1 and main term ell_r.

Module 244
  -> reduction to OPMeanErr_244 plus side rows.

Module 245
  -> strength audit for OPMeanErr_244 after the |W_M| average.

Module 246
  -> side-row audit for cutoff, range, W-residue, prime powers,
     normalization, and zero-mode leakage.
```

Thus the one-point prototype is reduced to:

```text
KernelAvgStrength_245(s0,D0,rho0)
  + OnePointSideRows_246(s0,D0,rho0).
```

The next scheduled iteration is the fourth 15-iteration plan challenge. It
should ask whether Phase F2 has exposed a genuinely smaller target or whether
the required boundary mean and side rows are already too close to endpoint
strength.

## 8. What remains open

This module does not prove:

- `OnePointSideRows_246(s0,D0,rho0)`;
- `CutOne_242=o_W(1)`;
- `RangeOne_242=o_W(1)`;
- `WResOne_242=o_W(1)`;
- `PPOne_242=o_W(1)`;
- `NormZeroOne_242=o_W(1)`;
- `KernelAvgStrength_245(s0,D0,rho0)`;
- `OPMeanErr_244(s0,D0,rho0)=o_W(1)`;
- `OnePointBIHL_242(s0,D0,rho0)` except conditionally;
- any off-vertex one-point row;
- any two-point or higher `BoundaryIntervalHL_234(S,lambda)` row;
- `FixedSupportTupleHL_238`;
- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)`;
- selector transfer to the actual sharp moving selector;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not hide cutoff, range, W-residue, prime-power, normalization, or
  zero-mode defects inside `KernelAvgStrength_245`.
- Do not treat a full-interval prime-power sparsity estimate as a boundary
  estimate after the `|W_M|` average unless the weighted boundary version is
  proved.
- Do not treat W-admissibility of the local factor as W-residue
  synchronization for the actual source row.
- Do not replace a range-failure estimate by a change of dyadic shell without
  recording a mixed transfer row.
- Do not assume cyclic zero-mode cancellation survives interval truncation.
- Do not use cancellation in `W_M` after the fixed row has taken `|W_M|`.
- Do not use selector transfer to close a side row without naming the
  transfer norm and class.
- Do not close any side row by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
