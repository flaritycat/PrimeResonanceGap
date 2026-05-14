# Module 249: One-point prototype proof-or-blocked verdict

## 1. Precise theorem / claim being advanced

This module gives the promised proof-or-blocked verdict for the one-point
prototype from Modules 242-248.

The active row is:

```text
OnePointBIHL_242(s0,D0,rho0)
  = BoundaryIntervalHL_234({(00,0)},(00,0)).
```

The active reduction is:

```text
KernelAvgStrength_245(s0,D0,rho0)
  + OnePointSideRows_246(s0,D0,rho0)
    => OnePointBIHL_242(s0,D0,rho0).
```

Define:

```text
OnePointVerdict_249(s0,D0,rho0)
```

as the following verdict ledger:

```text
conditional local:
  if KernelAvgStrength_245 and OnePointSideRows_246 are both supplied by
  exact fixed-row conventions or fixed-row one-point estimates that do not
  change selector, projection, cutoff, W-residue convention, dyadic shell, or
  limit order.

mixed:
  if the proof uses selector transfer, projection smoothing, cutoff transfer,
  W-residue-family comparison, range repair, or denominator-grid movement.

endpoint-strength:
  if the proof closes the row by assuming projected residual fourth-moment
  control or an endpoint package.

false / blocked as a shortcut:
  if the proof claims closure from ordinary first-moment Hardy-Littlewood,
  full-interval PNT, full-interval W-tricked PNT, ordinary pair-BDH, or
  rectangle-BDH alone.
```

The main conditional claim is:

```text
FixedRowOnePointPkg_249(s0,D0,rho0)
  => OnePointBIHL_242(s0,D0,rho0),
```

where:

```text
FixedRowOnePointPkg_249
  = KernelAvgStrength_245^local(s0,D0,rho0)
    + OnePointSideRows_246^local(s0,D0,rho0).
```

Here the superscript `local` means that the relevant Module 245 and Module
246 inputs are proved by exact fixed-row conventions or by fixed-row
one-point estimates, not by mixed transfer or endpoint-strength control.

This module does not prove `FixedRowOnePointPkg_249`.

## 2. Status label

`CONDITIONAL`

The module records a valid conditional local route and blocks invalid shortcut
closures. The W, smoothed, frozen, and actual selector prototype rows remain
unproved unless the named fixed-row hypotheses are supplied.

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
J_R(d,h,k;t)={n: m0(n,t) > N-L_N}.
```

The fixed weighted average is:

```text
E_K F
  = (1/D0) sum_{D0<|d|<=2D0} E_{h,k,t}|W_M(t)| F(d,h,k;t).
```

The one-point mean error is:

```text
OPMeanErr_244(s0,D0,rho0)
  = E_K sum_{r in {L,R}}
      |E_n 1_{J_r}(n)(mu_s0(m0(n,t))-1)|.
```

The strength package is local only when it is supplied by one of the
fixed-row routes from Module 245:

```text
direct weighted fixed-row control,
uniform pointwise control beating A_W(M),
boundary-length majorant with BLength_245,
relative boundary-PNT in the active range,
Holder control K_q(M)E_p(s0)=o_W(1),
```

and without changing the row.

The side package is local only when each row is exact by convention or
controlled in the same fixed weighted normalization:

```text
CutOne_242=o_W(1),
RangeOne_242=o_W(1),
WResOne_242=o_W(1),
PPOne_242=o_W(1),
NormZeroOne_242=o_W(1).
```

## 4. Assumptions

The conditional local route assumes:

```text
FixedRowOnePointPkg_249(s0,D0,rho0).
```

Expanded:

```text
KernelAvgStrength_245^local(s0,D0,rho0),
OnePointSideRows_246^local(s0,D0,rho0).
```

The assumptions must preserve:

```text
selector class s0,
projection P_M,
kernel K_M,
dyadic shell D0<|d|<=2D0,
boundary intervals J_L,J_R,
cutoff0,
W-residue convention,
prime-only / prime-power convention,
normalization and zero-mode convention,
fixed-w then N -> infinity then w -> infinity limit order.
```

The module explicitly does not assume:

```text
ordinary first-moment HL closes OPMeanErr_244,
full-interval PNT closes OPMeanErr_244,
full-interval W-tricked PNT closes OPMeanErr_244,
ordinary pair-BDH closes OPMeanErr_244,
rectangle-BDH closes OPMeanErr_244,
selector transfer is free,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
RBDH_pair_short,
CPC_3^sharp,
AU^3.
```

## 5. Proof / disproof / reduction

### A. Conditional local route

Module 244 gives:

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

Module 246 defines:

```text
OnePointSideRows_246
  = CutOne_242 + RangeOne_242 + WResOne_242
    + PPOne_242 + NormZeroOne_242
```

with each term required to be `o_W(1)`.

Therefore:

```text
KernelAvgStrength_245 + OnePointSideRows_246
  => OnePointBIHL_242.
```

If both inputs are supplied by fixed-row local estimates, this becomes:

```text
FixedRowOnePointPkg_249
  => OnePointBIHL_242.
```

This proves only a conditional implication.

### B. Exact model branch

For:

```text
s0=model,
mu_model(m0(n,t))=1
```

on the active intervals, the mean error is:

```text
OPMeanErr_244(model,D0,rho0)=0.
```

If all side rows are also zero by exact convention, then:

```text
OnePointBIHL_242(model,D0,rho0)
```

is closed inside the model convention.

Classification:

```text
exact local model branch only.
```

This does not prove the W, smoothed, frozen, or actual moving-selector rows.

### C. W branch

For:

```text
s0=W,
```

the needed fixed-row input is:

```text
WOneBoundaryPNT_244:
  OPMeanErr_244(W,D0,rho0)=o_W(1)
```

or one of the exact Module 245 routes that implies it. The side rows must
also be local in the Module 246 sense.

Classification:

```text
conditional local if WOneBoundaryPNT_244 and side rows are proved in the
same fixed |W_M|-weighted row;
open otherwise.
```

It is not proved by ordinary first-moment HL, full-interval W-tricked PNT, or
ordinary pair-BDH.

### D. Smoothed branch

For:

```text
s0=sm,
```

there are two possible routes.

Direct route:

```text
OPMeanErr_244(sm,D0,rho0)=o_W(1)
```

plus local side rows in the same smoothed fixed row.

Transfer route:

```text
WtoSmOneMean_244
```

or another named selector/projection/cutoff transfer.

Classification:

```text
conditional local under a direct fixed-row smoothed boundary mean theorem;
mixed if it is obtained by transfer from the W branch;
open otherwise.
```

### E. Frozen branch

For:

```text
s0=fr,
```

the direct fixed-row route is:

```text
OPMeanErr_244(fr,D0,rho0)=o_W(1)
```

plus local side rows.

Any route through:

```text
SmToFrOneMean_244
```

or moving-threshold control is a transfer route.

Classification:

```text
conditional local under a direct fixed-row frozen boundary mean theorem;
mixed if obtained by smoothed-to-frozen or moving-threshold transfer;
open otherwise.
```

The actual sharp moving selector is still outside the row.

### F. Shortcut disproofs

The following implications are blocked:

```text
ordinary first-moment HL
  => OPMeanErr_244=o_W(1);

full-interval PNT
  => OPMeanErr_244=o_W(1);

full-interval W-tricked PNT
  => OPMeanErr_244=o_W(1);

ordinary pair-BDH
  => OPMeanErr_244=o_W(1);

ordinary pair-BDH
  => OnePointBIHL_242.
```

Reason:

```text
OPMeanErr_244 is a boundary interval one-point mean after an absolute
projected-kernel weight, with selector, W-residue, cutoff, range,
prime-power, normalization, and zero-mode side rows separated.
```

The shortcut tools control different objects or omit required normalization.

Classification:

```text
FALSE / BLOCKED as shortcuts.
```

### G. Endpoint-strength route

If the prototype is closed by assuming:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
(1/D0) sum_d ||P_M B_{d,s0}||_{U^2}^4=o_W(1),
CPC_3^sharp,
RBDH_pair_short,
AU^3,
```

then the row is not a local boundary theorem. It is endpoint-strength.

Classification:

```text
endpoint-strength, not a proof of the smaller local package.
```

## 6. Edge cases

- If `BLength_245=o_W(1)` and the one-point mass majorant is fixed-row local,
  the prototype may close without cancellation. This is still conditional on
  proving the weighted boundary length and side rows.
- If `A_W(M)=O_W(1)`, pointwise error estimates need only be `o_W(1)`. If
  `A_W(M)` grows, they must beat that growth.
- If `K_q(M)E_p(s0)=o_W(1)` is proved directly in the fixed row, the Holder
  route is local. If `K_q(M)` is obtained by changing `P_M`, the route is
  mixed.
- If `s0=model`, exact closure is only a model convention; it does not
  transfer to W, smoothed, frozen, or actual selectors.
- If `WResOne_242` is zero only after changing residue convention, the row is
  mixed rather than local.
- If `NormZeroOne_242` is zero in the cyclic model but not after interval
  restriction, zero-mode leakage remains open.
- If prime-power sparsity is known only without `|W_M|`, it does not close
  `PPOne_242` without a kernel-correlation bound.
- If a proof uses cancellation in the signed kernel `W_M`, it does not apply
  after the fixed row takes `|W_M|`.
- If the intervals are shorter than available W-tricked PNT ranges, the W
  branch is open or blocked by range, not proved by the local factor
  `Theta=1`.

## 7. Where it fits in the project map

The Phase F2 one-point branch now has a verdict:

```text
Modules 242-243:
  fixed the prototype and computed the exact singleton local model.

Module 244:
  reduced the row to OPMeanErr_244 plus side rows.

Module 245:
  audited the strength needed after |W_M|.

Module 246:
  audited cutoff, range, W-residue, prime-power, normalization, and zero-mode
  side rows.

Module 247:
  challenged the branch and demanded proof-or-blocked mode.

Module 248:
  compared available tools and blocked standard shortcuts.

Module 249:
  records the final one-point prototype verdict:
  conditional local only under FixedRowOnePointPkg_249;
  false / blocked as a shortcut from ordinary tools;
  mixed under transfer routes;
  endpoint-strength if closed by residual endpoint assumptions.
```

The next module is the seventh plan update:

```text
Module 250.
```

It should decide whether Phase F2 should:

```text
attempt a two-point fixed-support row,
redirect to minor arcs,
return to projected major-arc local matching,
or stop the boundary branch for now.
```

## 8. What remains open

This module does not prove:

- `FixedRowOnePointPkg_249(s0,D0,rho0)`;
- `KernelAvgStrength_245^local(s0,D0,rho0)`;
- `OnePointSideRows_246^local(s0,D0,rho0)`;
- `OPMeanErr_244(W,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(sm,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(fr,D0,rho0)=o_W(1)`;
- `WOneBoundaryPNT_244`;
- `SmOneBoundaryMean_244`;
- `FrOneBoundaryMean_244`;
- any relative short-interval W-tricked PNT in the required range;
- `BLength_245=o_W(1)`;
- `K_q(M)E_p(s0)=o_W(1)`;
- `CutOne_242=o_W(1)`;
- `RangeOne_242=o_W(1)`;
- `WResOne_242=o_W(1)`;
- `PPOne_242=o_W(1)`;
- `NormZeroOne_242=o_W(1)`;
- `OnePointBIHL_242(W,D0,rho0)`;
- `OnePointBIHL_242(sm,D0,rho0)`;
- `OnePointBIHL_242(fr,D0,rho0)`;
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

- Do not cite this verdict as a proof of the W, smoothed, frozen, or actual
  selector one-point rows.
- Do not use the exact model branch as evidence for the W branch.
- Do not treat `Theta_{w,{(00,0)}}^proj=1` as a boundary prime theorem.
- Do not replace `OPMeanErr_244` by ordinary first-moment HL, full-interval
  PNT, full-interval W-tricked PNT, ordinary pair-BDH, or rectangle-BDH.
- Do not hide side rows inside `KernelAvgStrength_245`.
- Do not use cancellation in `W_M` after the fixed row takes `|W_M|`.
- Do not call a route local if it changes selector class, projection, cutoff,
  W-residue convention, denominator grid, dyadic shell, or limit order.
- Do not call a route local if it assumes `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not upgrade model, W, smoothed, or frozen selector statements to the
  actual sharp moving selector.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
