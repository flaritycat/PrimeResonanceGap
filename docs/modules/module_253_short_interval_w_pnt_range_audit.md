# Module 253: Short-interval W-PNT range audit

## 1. Precise theorem / claim being advanced

This module tests the W-tricked short-interval input left open by Module 244
and scheduled by Module 252.

The active one-point W branch is:

```text
WOneBoundaryPNT_244:
  OPMeanErr_244(W,D0,rho0)=o_W(1).
```

Recall:

```text
OPMeanErr_244(W,D0,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        sum_{r in {L,R}}
          |E_n 1_{J_r}(n)(mu_W(n-t0)-1)|.
```

Define:

```text
WShortRangeGate_253(W,D0,rho0)
```

to be the fixed-row package consisting of:

```text
1. a W-uniform short-interval PNT input on every active translated interval
   whose length is in the theorem range;

2. a weighted bad-range estimate for active intervals below that range;

3. residue, cutoff, range, and limit-order compatibility with the same fixed
   row used in OPMeanErr_244.
```

The conditional claim is:

```text
WShortRangeGate_253(W,D0,rho0)
  => WOneBoundaryPNT_244.
```

The audit verdict is:

```text
The W branch is local only if the short-interval theorem is uniform for fixed
w, applies to the translated boundary intervals J_L,J_R in the same residue
convention, and survives the absolute |W_M| average. If the intervals are
below the available theorem range and the below-range weighted mass is not
separately small, the relative W-PNT route is blocked. If the theorem changes
the selector, projection, cutoff, residue family, or limit order, the route is
mixed.
```

This module does not prove a short-interval W-tricked PNT.

## 2. Status label

`CONDITIONAL`

The module derives the exact fixed-row range gate for the W branch and blocks
full-interval PNT as a shortcut. It does not prove `WOneBoundaryPNT_244`, the
one-point prototype, or any endpoint theorem.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0=W,cutoff0),
w fixed, N -> infinity, then w -> infinity.
```

The active row remains:

```text
BdPrefRow_224^P(W,D0;N,w,rho0),
Pi=P_M,
edge=cyc_W -> int_W,
D0<|d|<=2D0.
```

The active one-point form is:

```text
m0(n,t)=n-t0.
```

The boundary intervals are:

```text
J_L(d,h,k;t)={n: m0(n,t) <= L_N},
J_R(d,h,k;t)={n: m0(n,t) > N-L_N},
```

intersected with the fixed interval averaging domain and `cutoff0`.

Write:

```text
r in {L,R},
J_r=J_r(d,h,k;t),
ell_r(d,h,k;t)=E_n 1_{J_r}(n),
Y_r(d,h,k;t)=N ell_r(d,h,k;t).
```

Thus `Y_r` is the unnormalized active interval length in the `n` variable.
After the translation `m=n-t0`, the corresponding W-variable interval is:

```text
I_r(d,h,k;t)=m0(J_r(d,h,k;t)).
```

It has the same cardinality as `J_r`, except for losses assigned to:

```text
RangeOne_242,
CutOne_242.
```

The fixed weighted averaging operator is:

```text
E_K F
  = (1/D0) sum_{D0<|d|<=2D0} E_{h,k,t}|W_M(t)|F(d,h,k;t).
```

Then:

```text
OPMeanErr_244(W,D0,rho0)
  = E_K sum_{r in {L,R}} |e_r(W;d,h,k;t)|,
```

where:

```text
e_r(W;d,h,k;t)
  = E_n 1_{J_r}(n)(mu_W(m0(n,t))-1).
```

Let:

```text
Y_PNT_253(N,w,rho0)
```

be the minimum interval length for the short-interval W-PNT theorem being
used. This is a theorem-input threshold, not a proved project quantity.

Define the good-range indicator:

```text
Good_r^253(d,h,k;t)
  = 1_{Y_r=0 or Y_r >= Y_PNT_253(N,w,rho0)}.
```

Define the below-range defect:

```text
BadRangeMass_253
  = E_K sum_{r in {L,R}}
      1_{0<Y_r<Y_PNT_253}
      |E_n 1_{J_r}(n)(mu_W(m0(n,t))-1)|.
```

If one uses a mass majorant instead of direct control, it must appear as:

```text
BadRangeMass_253
  <= (C_mean_253+1)
       E_K sum_r 1_{0<Y_r<Y_PNT_253} ell_r
     + BadMassErr_253.
```

This estimate is not automatic.

## 4. Assumptions

`WShortRangeGate_253(W,D0,rho0)` consists of the following fixed-row
assumptions.

### A. W-short interval input

There are quantities:

```text
eps_WPNT_253(N,w,rho0) -> 0 after fixed w and N -> infinity,
Err_r^WPNT(d,h,k;t),
```

such that for every active interval with `Good_r^253=1` and exact W-residue
compatibility:

```text
|e_r(W;d,h,k;t)|
  <= eps_WPNT_253(N,w,rho0) ell_r(d,h,k;t)
     + |Err_r^WPNT(d,h,k;t)|.
```

The weighted error satisfies:

```text
WPNTError_253
  = E_K sum_r |Err_r^WPNT(d,h,k;t)|
  = o_W(1).
```

### B. Weighted range compatibility

Intervals below the short-interval theorem range are separately negligible:

```text
BadRangeMass_253=o_W(1).
```

Equivalently, it is enough to prove the displayed mass-majorant estimate with:

```text
(C_mean_253+1)
  E_K sum_r 1_{0<Y_r<Y_PNT_253} ell_r
  + BadMassErr_253
=o_W(1).
```

### C. Residue compatibility

The translated variable:

```text
m=m0(n,t)=n-t0
```

must lie in the same admissible W-residue convention used to define
`mu_W`. If this is exact by construction, there is no extra term.

If it is not exact, the defect belongs to:

```text
WResOne_242,
```

and Module 253 does not hide it inside `WOneBoundaryPNT_244`.

### D. Fixed-row discipline

The W-short interval input must keep:

```text
same selector class W,
same projection P_M,
same kernel K_M,
same dyadic shell D0<|d|<=2D0,
same intervals J_L,J_R,
same cutoff0,
same W-residue convention,
same normalization of mu_W,
same prime-only or prime-power convention,
fixed w, then N -> infinity, then w -> infinity.
```

The module does not assume:

```text
full-interval W-tricked PNT implies WOneBoundaryPNT_244,
ordinary first-moment HL implies WOneBoundaryPNT_244,
ordinary pair-BDH implies WOneBoundaryPNT_244,
A_W(M)=O_W(1),
BLength_245=o_W(1),
WResOne_242=o_W(1),
RangeOne_242=o_W(1),
CutOne_242=o_W(1),
PPOne_242=o_W(1),
NormZeroOne_242=o_W(1),
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

## 5. Proof / disproof / reduction

### A. Good-range contribution

Split:

```text
OPMeanErr_244(W,D0,rho0)
  = E_K sum_r Good_r^253 |e_r|
    + E_K sum_r (1-Good_r^253)|e_r|.
```

For the good-range part, the W-short interval input gives:

```text
E_K sum_r Good_r^253 |e_r|
  <= eps_WPNT_253 E_K sum_r ell_r
     + WPNTError_253.
```

The length average is bounded by `BLength_245`:

```text
E_K sum_r ell_r = BLength_245(D0,rho0).
```

Therefore:

```text
E_K sum_r Good_r^253 |e_r|
  <= eps_WPNT_253 BLength_245 + WPNTError_253.
```

### B. Below-range contribution

The bad-range part is exactly:

```text
E_K sum_r (1-Good_r^253)|e_r|
  = BadRangeMass_253.
```

By assumption:

```text
BadRangeMass_253=o_W(1).
```

This is the place where the audit genuinely questions the previous branch:
if the active boundary intervals are below the available W-PNT range and no
separate weighted mass estimate is supplied, the relative W-PNT route has not
survived.

### C. Conditional implication

Combining the two pieces:

```text
OPMeanErr_244(W,D0,rho0)
  <= eps_WPNT_253 BLength_245
     + WPNTError_253
     + BadRangeMass_253.
```

Thus a sufficient condition for `WOneBoundaryPNT_244` is:

```text
eps_WPNT_253 BLength_245
  + WPNTError_253
  + BadRangeMass_253
=o_W(1).
```

This is precisely the output of `WShortRangeGate_253`.

Hence:

```text
WShortRangeGate_253(W,D0,rho0)
  => WOneBoundaryPNT_244.
```

### D. Relation to Module 245

Module 245 listed a relative boundary-PNT route:

```text
|e_r(W;d,h,k;t)|
  <= eps_rel ell_r + err_r^rel.
```

Module 253 identifies the range audit hidden inside that route. The relative
estimate is only meaningful on intervals that satisfy the theorem's length
and residue hypotheses. Otherwise one must add:

```text
BadRangeMass_253
```

or mark the relative W-PNT route blocked.

### E. Full-interval W-PNT is not enough

A full-interval W-tricked prime number theorem controls an average over a
long interval or full residue class. It does not imply:

```text
E_K sum_r |E_n 1_{J_r}(n)(mu_W(n-t0)-1)|=o_W(1),
```

because the target has:

```text
short boundary intervals,
translation by t0,
absolute value before averaging,
|W_M(t)| weighting,
fixed W-residue convention,
cutoff and range side rows.
```

Therefore:

```text
full-interval W-PNT => WOneBoundaryPNT_244
```

is `FALSE / BLOCKED` as a shortcut.

### F. Local, mixed, endpoint-strength, and blocked classifications

The route is conditional local if:

```text
eps_WPNT_253 BLength_245 + WPNTError_253 + BadRangeMass_253=o_W(1)
```

is proved in the same fixed row.

The route is mixed if the W-PNT input is proved only after:

```text
smoothing J_r,
changing P_M or K_M,
changing selector class,
changing W-residue convention,
moving the denominator grid,
altering cutoff0,
changing the fixed-w then N -> infinity then w -> infinity order.
```

The route is endpoint-strength if it is proved only by assuming:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
(1/D0)sum_d ||P_M B_{d,W}||_{U^2}^4=o_W(1),
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

The relative W-PNT route is false / blocked as a closure route if:

```text
0<Y_r<Y_PNT_253
```

on a non-negligible `|W_M|`-weighted portion of the row and no separate
`BadRangeMass_253=o_W(1)` estimate is supplied.

## 6. Edge cases

- If `Y_r=0`, the interval contributes zero to `OPMeanErr_244`; it should not
  be counted as a range failure.
- If `0<Y_r<Y_PNT_253`, a relative short-interval theorem does not apply.
  The contribution must be handled by `BadRangeMass_253` or by another Module
  245 route.
- If `J_L` or `J_R` is clipped by `cutoff0`, the theorem must apply to the
  clipped interval. Otherwise the discrepancy belongs to `CutOne_242`.
- If translating `m=n-t0` sends part of the interval outside the support of
  the W-tricked weight, the issue belongs to `RangeOne_242`.
- If the admissible residue class is not fixed after translation by `t0`, the
  issue belongs to `WResOne_242`, not to the singleton local factor.
- If a short-interval theorem is uniform for fixed residue classes but not
  uniform in the `t0` family selected by `|W_M(t)|`, it does not match the
  row.
- If a theorem gives a signed average after summing over `t`, it does not
  apply after the row takes `|W_M(t)|` and the absolute value of each interval
  error.
- If `A_W(M)` or `BLength_245` grows, the product
  `eps_WPNT_253 BLength_245` must still be `o_W(1)`.
- If the proof uses a smoothed boundary interval in place of `J_r`, it is
  mixed unless a cutoff-transfer row returns to the exact interval.
- If prime powers are active in the selected W weight, their contribution
  remains `PPOne_242`.
- If a W-branch estimate is supplied, it still does not imply the smoothed,
  frozen, or actual moving selector branches without named transfer rows.

## 7. Where it fits in the project map

The Phase G feasibility chain is now:

```text
Module 251:
  boundary length is reduced to A_W(M)GeomModel_251.

Module 252:
  kernel absolute-mass and Holder feasibility are separated.

Module 253:
  the relative W-short-interval route is reduced to a fixed-row range gate.
```

The output is:

```text
WShortRangeGate_253
  => WOneBoundaryPNT_244
  => OPMeanErr_244(W,D0,rho0)=o_W(1),
```

with the explicit bound:

```text
OPMeanErr_244(W,D0,rho0)
  <= eps_WPNT_253 BLength_245
     + WPNTError_253
     + BadRangeMass_253.
```

The next module should audit the exact side-row conventions:

```text
Module 254:
  CutOne_242, RangeOne_242, WResOne_242, PPOne_242, NormZeroOne_242.
```

## 8. What remains open

This module does not prove:

- `WShortRangeGate_253(W,D0,rho0)`;
- `WOneBoundaryPNT_244`;
- `OPMeanErr_244(W,D0,rho0)=o_W(1)`;
- any W-uniform short-interval PNT in the required range;
- `BadRangeMass_253=o_W(1)`;
- `WPNTError_253=o_W(1)`;
- `eps_WPNT_253 BLength_245=o_W(1)`;
- `BLength_245=o_W(1)`;
- `BoundaryLengthGate_251`;
- `KernelHolderGate_252`;
- `KernelAvgStrength_245^local`;
- `OnePointSideRows_246^local`;
- `FixedRowOnePointPkg_249`;
- `OnePointBIHL_242` outside the exact model convention;
- any smoothed, frozen, or actual moving selector boundary mean theorem;
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

- Do not cite full-interval W-PNT as a proof of `WOneBoundaryPNT_244`.
- Do not use ordinary first-moment HL, ordinary pair-BDH, rectangle-BDH, or
  the residual cube endpoint as a one-point boundary PNT.
- Do not ignore the interval length threshold `Y_PNT_253`.
- Do not hide below-range intervals inside `o_W(1)` without proving
  `BadRangeMass_253=o_W(1)`.
- Do not change the W-residue convention after translating by `t0`.
- Do not use cancellation in `W_M`; this row uses `|W_M|`.
- Do not replace sharp boundary intervals by smoothed intervals without
  marking the route mixed.
- Do not move from the W branch to smoothed, frozen, or actual moving
  selectors without named transfer rows.
- Do not close this gate by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
