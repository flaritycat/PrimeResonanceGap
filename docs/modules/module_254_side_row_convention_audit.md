# Module 254: Exact side-row convention audit

## 1. Precise theorem / claim being advanced

This module tests whether the five one-point side rows from Module 246 are
actually exact conventions in the fixed row, or whether they remain separate
weighted estimates.

The active one-point package is:

```text
FixedRowOnePointPkg_249
  = KernelAvgStrength_245^local
    + OnePointSideRows_246^local.
```

Module 246 defined:

```text
OnePointSideRows_246(s0,D0,rho0)
  =
  CutOne_242=o_W(1),
  RangeOne_242=o_W(1),
  WResOne_242=o_W(1),
  PPOne_242=o_W(1),
  NormZeroOne_242=o_W(1).
```

Define:

```text
SideConventionGate_254(s0,D0,rho0)
```

to be the fixed-row convention package consisting of the five pointwise
exactness checks:

```text
CutExact_254,
RangeExact_254,
WResExact_254,
PPExact_254,
NormZeroExact_254,
```

or, where exactness fails, their corresponding fixed-row local weighted
defect estimates:

```text
CutDefect_254=o_W(1),
RangeDefect_254=o_W(1),
WResDefect_254=o_W(1),
PPDefect_254=o_W(1),
NormZeroDefect_254=o_W(1).
```

The conditional claim is:

```text
SideConventionGate_254(s0,D0,rho0)
  => OnePointSideRows_246^local(s0,D0,rho0).
```

If every exactness check holds pointwise in the same fixed row, then:

```text
OnePointSideRows_246(s0,D0,rho0)=0.
```

If any check fails, the row is not exact by convention. It remains local only
if the corresponding weighted defect is proved in the same row. It is mixed
if exactness is obtained by changing the row, and endpoint-strength if the
defect is controlled only through the residual cube endpoint.

This module does not prove the side package.

## 2. Status label

`CONDITIONAL`

The module gives a fixed-row exactness test and a conditional implication to
`OnePointSideRows_246^local`. It does not prove the one-point prototype or any
side-row estimate in a non-exact convention.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The active one-point form is:

```text
m0(n,t)=n-t0.
```

The active boundary intervals are:

```text
J_L(d,h,k;t)={n: m0(n,t) <= L_N},
J_R(d,h,k;t)={n: m0(n,t) > N-L_N},
```

intersected with the fixed interval averaging domain and `cutoff0`.

The fixed weighted averaging operator is:

```text
E_K F
  = (1/D0) sum_{D0<|d|<=2D0} E_{h,k,t}|W_M(t)|F(d,h,k;t).
```

Write:

```text
a_s0(n,t)=mu_s0(m0(n,t)).
```

The source boundary/cutoff event is:

```text
BdSrc_254(n;d,h,k;t).
```

The simplified interval event is:

```text
BdInt_254(n;d,h,k;t)
  = cutoff0(n,t)(1_{J_L}(n)+1_{J_R}(n)).
```

The source support indicator for the one-point weight is:

```text
Supp_s0(m),
```

and the fixed denominator-grid / truncation condition is:

```text
Grid_s0(m;rho0).
```

The fixed W-residue compatibility indicator is:

```text
WAdm_s0(m;w,rho0).
```

For non-W selector classes, `WAdm_s0` is interpreted only if that class still
uses a W-tail local model. If it is inactive by exact convention, the W-residue
side row is zero by definition.

If the active weight has a prime-power component, write:

```text
mu_s0 = mu_s0^prime + pp_s0.
```

If the active convention is prime-supported, then:

```text
pp_s0=0.
```

The normalization and zero-mode drift terms are:

```text
NormDrift_254(d,h,k;t),
ZeroLeak_254(d,h,k;t).
```

They compare the actual one-point normalization and projected zero-mode
convention with the model term `ell_r`.

## 4. Assumptions

The exact side convention checks are as follows.

### A. Cutoff exactness

```text
CutExact_254:
  BdSrc_254(n;d,h,k;t)=BdInt_254(n;d,h,k;t)
  pointwise in the fixed row.
```

If this fails, define:

```text
CutDefect_254
  = E_K E_n |BdSrc_254-BdInt_254|(1+|a_s0(n,t)|).
```

The local replacement is:

```text
CutDefect_254=o_W(1).
```

### B. Range exactness

```text
RangeExact_254:
  BdInt_254(n;d,h,k;t)=1
  => Supp_s0(m0(n,t))=1 and Grid_s0(m0(n,t);rho0)=1
```

pointwise in the fixed row.

If this fails, define:

```text
RangeDefect_254
  = E_K E_n BdInt_254(n;d,h,k;t)
      1_{range/grid failure for m0(n,t)}(1+|a_s0(n,t)|).
```

The local replacement is:

```text
RangeDefect_254=o_W(1).
```

### C. W-residue exactness

```text
WResExact_254:
  either the W-residue side row is inactive by exact selector convention,
  or BdInt_254(n;d,h,k;t)=1 implies WAdm_s0(m0(n,t);w,rho0)=1
  in the same W-residue convention used by mu_s0 and by the singleton
  local model.
```

If this fails, define:

```text
WResDefect_254
  = E_K E_n BdInt_254(n;d,h,k;t)
      1_{W-residue failure for m0(n,t)}(1+|a_s0(n,t)|).
```

The local replacement is:

```text
WResDefect_254=o_W(1).
```

### D. Prime-power exactness

```text
PPExact_254:
  pp_s0=0
```

as a definition of the active selector weight.

If prime powers are active, define:

```text
PPDefect_254
  = E_K sum_{r in {L,R}}
      E_n 1_{J_r}(n)|pp_s0(m0(n,t))|.
```

The local replacement is:

```text
PPDefect_254=o_W(1).
```

### E. Normalization and zero-mode exactness

```text
NormZeroExact_254:
  NormDrift_254(d,h,k;t)=0 and ZeroLeak_254(d,h,k;t)=0
  pointwise in the fixed row.
```

If this fails, define:

```text
NormZeroDefect_254
  = E_K (|NormDrift_254(d,h,k;t)|+|ZeroLeak_254(d,h,k;t)|).
```

The local replacement is:

```text
NormZeroDefect_254=o_W(1).
```

All five checks and defect estimates must keep:

```text
same selector class s0,
same projection P_M,
same kernel K_M,
same dyadic shell D0<|d|<=2D0,
same intervals J_L,J_R,
same cutoff0,
same W-residue convention,
same prime-only or prime-power convention,
same normalization and centering convention,
fixed w, then N -> infinity, then w -> infinity.
```

The module does not assume:

```text
SideConventionGate_254,
OnePointSideRows_246^local,
KernelAvgStrength_245^local,
FixedRowOnePointPkg_249,
OnePointBIHL_242,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

## 5. Proof / disproof / reduction

### A. Cutoff row

Module 246 controls the cutoff side row by:

```text
CutOne_242
  <= E_K E_n CutFail_246(n;d,h,k;t)(1+|a_s0(n,t)|).
```

With the present notation:

```text
CutFail_246 = 1_{BdSrc_254 != BdInt_254}.
```

If `CutExact_254` holds, then:

```text
CutFail_246=0
```

pointwise, and therefore:

```text
CutOne_242=0.
```

If exactness fails but `CutDefect_254=o_W(1)`, then:

```text
CutOne_242=o_W(1)
```

by the same Module 246 majorization. This is local only if the defect estimate
is fixed-row local.

### B. Range row

Module 246 controls:

```text
RangeOne_242
  <= E_K E_n RangeFail_246(n;d,h,k;t)(1+|a_s0(n,t)|).
```

If `RangeExact_254` holds, then no active interval point leaves the support,
denominator grid, dyadic shell, or truncation range, so:

```text
RangeFail_246=0,
RangeOne_242=0.
```

If exactness fails, the range row remains local only under:

```text
RangeDefect_254=o_W(1).
```

Changing the row to make the implication true is not exactness; it is a mixed
range repair.

### C. W-residue row

Module 246 controls:

```text
WResOne_242
  <= E_K E_n WFail_246(n;d,h,k;t)(1+|a_s0(n,t)|).
```

If `WResExact_254` holds, then either the row is inactive by exact selector
convention or:

```text
WFail_246=0
```

pointwise. Hence:

```text
WResOne_242=0.
```

If exactness fails, the row remains local only under:

```text
WResDefect_254=o_W(1).
```

This audit blocks a quiet mistake from earlier stages: the equality
`Theta_{w,{(00,0)}}^proj=1` accounts only for primes `p>w`. It does not by
itself synchronize the finite W-residue convention at primes `p<=w`.

### D. Prime-power row

If `PPExact_254` holds, then:

```text
pp_s0=0
```

and the Module 246 prime-power row is:

```text
PPOne_242=0.
```

If prime powers are active, then:

```text
PPOne_242=PPDefect_254.
```

Thus:

```text
PPDefect_254=o_W(1)
  => PPOne_242=o_W(1).
```

A full-interval prime-power sparsity statement is not enough unless it is
converted to this `|W_M|`-weighted boundary estimate.

### E. Normalization and zero-mode row

If `NormZeroExact_254` holds, then:

```text
NormDrift_254=0,
ZeroLeak_254=0,
```

and therefore:

```text
NormZeroOne_242=0.
```

If exactness fails, the row remains local only if:

```text
NormZeroDefect_254=o_W(1).
```

This is another place where the project must question a tempting shortcut:
zero-mode removal in a cyclic or full-interval model does not automatically
survive interval restriction and cutoff insertion.

### F. Composition

If every exactness check holds, then:

```text
CutOne_242=RangeOne_242=WResOne_242=PPOne_242=NormZeroOne_242=0,
```

so:

```text
OnePointSideRows_246(s0,D0,rho0)=0.
```

If some exactness checks fail but every corresponding defect is proved
`o_W(1)` in the same fixed row, then each Module 246 side row is `o_W(1)`.
Thus:

```text
SideConventionGate_254(s0,D0,rho0)
  => OnePointSideRows_246^local(s0,D0,rho0).
```

Combining with Module 249 gives only the conditional implication:

```text
KernelAvgStrength_245^local
  + SideConventionGate_254
    => OnePointBIHL_242.
```

This module does not supply `KernelAvgStrength_245^local`.

### G. Classification verdict

The side package is exact local only when the five exactness checks are
pointwise true in `rho0`.

It is conditional local when nonzero defects are bounded by fixed-row
weighted estimates.

It is mixed if any zero claim is made only after changing:

```text
selector class,
projection,
kernel,
cutoff,
W-residue convention,
denominator grid,
support range,
normalization,
limit order.
```

It is endpoint-strength if any defect is controlled only by assuming:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
```

or an equivalent residual fourth-moment estimate.

It is false / blocked as an exact-convention claim if any of the five
pointwise equalities fails and no defect estimate is supplied.

## 6. Edge cases

- If `J_L` and `J_R` overlap, exactness must use the same counting convention
  as `BdInt_254`; replacing the sum by a union is a change of row.
- If `cutoff0` is applied before rather than after boundary decomposition,
  `CutExact_254` must be checked with that order.
- If `m0(n,t)` crosses the finite support boundary after translation by
  `t0`, the defect is range, not cutoff.
- If the W-residue convention is exact only for interior points, boundary
  residue failures remain in `WResDefect_254`.
- If `s0=model`, the mean error may be zero while cutoff, range,
  normalization, and zero-mode conventions still require exactness checks.
- If `s0=sm` or `s0=fr`, a W-residue row may be inactive by convention, but
  any transfer from W to smoothed or frozen is mixed unless explicitly named.
- If prime powers are absent by definition, `PPExact_254` is exact. If they
  are merely sparse, the row is conditional local only after a weighted
  boundary sparsity estimate.
- If zero-mode removal is exact for the cyclic projector but interval
  restriction reintroduces a constant term, `NormZeroExact_254` fails.
- If any defect estimate uses cancellation in `W_M`, it does not apply after
  the fixed row takes `|W_M|`.
- If exactness is obtained by assuming endpoint estimates, it is not a
  convention.

## 7. Where it fits in the project map

The Phase G feasibility chain is now:

```text
Module 251:
  boundary length feasibility.

Module 252:
  kernel absolute-mass and Holder feasibility.

Module 253:
  W-short-interval range feasibility.

Module 254:
  exact side-row convention feasibility.
```

The output is:

```text
SideConventionGate_254
  => OnePointSideRows_246^local.
```

Together with previous gates, the one-point package now has the explicit
conditional shape:

```text
FixedRowOnePointPkg_249
  follows from
    KernelAvgStrength_245^local
    + SideConventionGate_254.
```

The next module should assemble a feasibility verdict:

```text
Module 255:
  FixedRowOnePointPkg_249 feasibility verdict.
```

## 8. What remains open

This module does not prove:

- `SideConventionGate_254(s0,D0,rho0)`;
- `OnePointSideRows_246^local`;
- `CutExact_254`;
- `RangeExact_254`;
- `WResExact_254`;
- `PPExact_254`;
- `NormZeroExact_254`;
- any non-exact side defect estimate;
- `KernelAvgStrength_245^local`;
- `BoundaryLengthGate_251`;
- `KernelHolderGate_252`;
- `WShortRangeGate_253`;
- `FixedRowOnePointPkg_249`;
- `OnePointBIHL_242`;
- any off-vertex one-point row;
- any two-point fixed-support row;
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

- Do not call a side row exact unless the corresponding pointwise convention
  holds in the fixed row.
- Do not hide cutoff, range, W-residue, prime-power, normalization, or
  zero-mode defects inside `KernelAvgStrength_245`.
- Do not use `Theta_{w,{(00,0)}}^proj=1` as W-residue synchronization.
- Do not replace a weighted boundary defect by an unweighted full-interval
  estimate.
- Do not use cancellation in `W_M`; the side rows use `|W_M|`.
- Do not make an exactness claim after changing selector class, projection,
  cutoff, residue convention, denominator grid, or limit order.
- Do not upgrade W, smoothed, frozen, or model side-row conventions to the
  actual moving selector.
- Do not close side rows by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
