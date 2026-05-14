# Module 244: One-point boundary prime-mean reduction by selector class

## 1. Precise theorem / claim being advanced

This module reduces the active one-point prototype from Module 243 to the
exact one-point boundary mean input needed in each allowed fixed selector
class.

The active row is:

```text
OnePointBIHL_242(s0,D0,rho0)
  = BoundaryIntervalHL_234({(00,0)},(00,0)).
```

Module 243 reduced its local model to:

```text
Theta_{w,{(00,0)}}^proj=1,
M_r^mod(d,h,k;t)=ell_r(d,h,k;t).
```

Therefore the open analytic target is:

```text
BIHLErr_243
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        sum_{r in {L,R}}
          |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)|
  = o_W(1).
```

Define the selector-class one-point boundary mean package:

```text
OnePointMeanPkg_244(s0,D0,rho0).
```

The conditional reduction is:

```text
OnePointMeanPkg_244(s0,D0,rho0)
  + CutOne_242=o_W(1)
  + RangeOne_242=o_W(1)
  + WResOne_242=o_W(1)
  + PPOne_242=o_W(1)
  + NormZeroOne_242=o_W(1) when active

    => OnePointBIHL_242(s0,D0,rho0).
```

This module does not prove `OnePointMeanPkg_244` for the W, smoothed, or
frozen classes. It identifies the exact input that would be needed.

## 2. Status label

`CONDITIONAL`

The implication is a definition-level reduction after Module 243. The
one-point boundary mean estimates remain open outside the pure model identity
case.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The active boundary intervals are:

```text
J_L(d,h,k;t)={n: n-t0 <= L_N},
J_R(d,h,k;t)={n: n-t0 > N-L_N},
```

intersected with the fixed interval averaging domain and `cutoff0`.

Write:

```text
J_r=J_r(d,h,k;t),  r in {L,R},
ell_r(d,h,k;t)=E_n 1_{J_r}(n).
```

The one-point boundary mean error for selector class `s0` is:

```text
MeanErr_244(s0;d,h,k;t)
  = sum_{r in {L,R}}
      |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)|.
```

The W-admissible averaged error is:

```text
OPMeanErr_244(s0,D0,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        MeanErr_244(s0;d,h,k;t).
```

The normalized target is:

```text
OPMeanErr_244(s0,D0,rho0)=o_W(1).
```

This is the same expression as `BIHLErr_243`, renamed to emphasize that the
remaining input is a one-point boundary mean theorem, not an Euler-factor
calculation and not a residual cube estimate.

## 4. Assumptions

All branches of `OnePointMeanPkg_244` preserve the fixed-row discipline:

```text
same P_M,
same K_M,
same R0 and eta0,
same selector class s0,
same dyadic shell D0<|d|<=2D0,
same W-residue convention,
same prime-only or prime-power convention,
same interval cutoff convention,
same normalization and centering convention,
fixed w, then N -> infinity, then w -> infinity.
```

The package is selector-class dependent.

### A. Model branch

For:

```text
s0=model,
```

the package is:

```text
ModelOneMean_244:
  mu_model(m)=1
  on every translated interval I_r(t0)
  in the declared normalization,
```

and the side slots:

```text
CutOne_242,
RangeOne_242,
WResOne_242,
PPOne_242,
NormZeroOne_242
```

are zero or separately small.

If the model measure is not literally normalized to one on the active row,
then `ModelOneMean_244` must be replaced by an explicit model normalization
row. The module does not assume that automatically.

### B. W-tricked prime branch

For:

```text
s0=W,
```

the required input is:

```text
WOneBoundaryPNT_244:
  OPMeanErr_244(W,D0,rho0)=o_W(1),
```

with the W-residue class held fixed and all primes `p<=w` handled outside
the W-tail Euler factor.

This is a boundary interval one-point prime number theorem in the exact
`|W_M|`-averaged normalization. It is not supplied by the singleton local
factor `Theta=1`.

### C. Smoothed finite-band branch

For:

```text
s0=sm,
```

the required input is:

```text
SmOneBoundaryMean_244:
  OPMeanErr_244(sm,D0,rho0)=o_W(1),
```

for the smoothed finite-band selector actually used in the fixed row.

This may be proved by a direct smoothed mean theorem or by a named
W-to-smoothed transfer row:

```text
WtoSmOneMean_244=o_W(1).
```

If such a transfer changes projection, denominator grid, threshold, cutoff,
or W-residue convention, the row becomes mixed and must say so.

### D. Frozen dyadic branch

For:

```text
s0=fr,
```

the required input is:

```text
FrOneBoundaryMean_244:
  OPMeanErr_244(fr,D0,rho0)=o_W(1),
```

for the sharp frozen dyadic selector in the fixed row.

It is not implied by the smoothed branch unless a named smoothed-to-frozen
boundary mean transfer row is supplied:

```text
SmToFrOneMean_244=o_W(1).
```

This branch still does not touch the actual moving selector:

```text
fr -> mv
```

is outside the fixed row.

## 5. Proof / disproof / reduction

### A. Identity with Module 243

Module 243 showed:

```text
Theta_{w,{(00,0)}}^proj=1,
M_r^mod=\ell_r.
```

Thus:

```text
Err_r^243(d,h,k;t)
  = E_n 1_{J_r}(n)(mu_s0(n-t0)-1).
```

Summing over `r`, multiplying by `|W_M(t)|`, and averaging over the fixed
dyadic shell gives:

```text
BIHLErr_243
  = OPMeanErr_244(s0,D0,rho0).
```

Therefore:

```text
OPMeanErr_244(s0,D0,rho0)=o_W(1)
  => BIHLErr_243=o_W(1).
```

Adding the side slots from Module 242 gives:

```text
OnePointMeanPkg_244 + side slots
  => OnePointBIHL_242.
```

This is the claimed conditional reduction.

### B. Model branch reduction

If:

```text
mu_model(m)=1
```

on every translated active interval, then:

```text
E_n 1_{J_r}(n)(mu_model(n-t0)-1)=0
```

for both boundary pieces. Hence:

```text
OPMeanErr_244(model,D0,rho0)=0.
```

The model branch is therefore closed only in the exact normalized model
convention. It does not say anything about W, smoothed, frozen, or actual
selector classes.

### C. W branch reduction

For `s0=W`, the same identity gives:

```text
BIHLErr_243=o_W(1)
  <=> WOneBoundaryPNT_244
```

inside the fixed row and with the side slots separated.

This is not a consequence of ordinary first-moment Hardy-Littlewood over the
full interval. The intervals `J_L` and `J_R` are boundary intervals whose
length and W-residue alignment must be compatible with the W-admissible
limit order. The average is also weighted by `|W_M(t)|`, so any pointwise or
average theorem used later must survive that multiplier.

### D. Smoothed branch reduction

For `s0=sm`, the required row is exactly:

```text
OPMeanErr_244(sm,D0,rho0)=o_W(1).
```

If the smoothed selector has been constructed so that its boundary interval
mean is model-normalized, this row may be local. If the proof compares it to
the W branch, the comparison must appear as:

```text
WtoSmOneMean_244.
```

Without that named transfer, the W branch does not imply the smoothed branch.

### E. Frozen branch reduction

For `s0=fr`, the required row is exactly:

```text
OPMeanErr_244(fr,D0,rho0)=o_W(1).
```

This row may be more delicate than the smoothed row because sharp frozen
dyadic cutoffs can create boundary and transition terms. Any use of smoothed
estimates must pass through:

```text
SmToFrOneMean_244.
```

The actual sharp moving selector is not present. A proof of the frozen row
does not imply:

```text
mv
```

without the moving-threshold transfer packages from earlier modules.

### F. What is not allowed

None of the following proves `OPMeanErr_244`:

```text
Theta_{w,{(00,0)}}^proj=1,
boundary volume alone,
full-interval first-moment Hardy-Littlewood,
ordinary pair-BDH,
ordinary rectangle-BDH,
the projected residual fourth moment,
selector transfer by notation.
```

The target is a boundary interval one-point mean in the same
`|W_M|`-weighted fixed-row normalization. That exact normalization is the
point.

## 6. Edge cases

- If `ell_r=0`, the corresponding interval contributes zero to the model
  main term, but cutoff mismatch still belongs to `CutOne_242`.
- If `J_r` is too short for a W-admissible one-point prime theorem, the W
  branch may be blocked by range rather than endpoint strength.
- If `|W_M|` has large absolute mass, a boundary mean estimate that is small
  before the `t`-average may still be insufficient.
- If the W-residue class is not fixed after the translation `m=n-t0`, the
  issue is `WResOne_242`, not `OPMeanErr_244`.
- If prime powers are active, the prime-power singleton row is `PPOne_242`;
  it is not absorbed by the one-point local factor.
- If the smoothed branch changes the projection or cutoff, it becomes mixed
  with projection or boundary transfer.
- If the frozen branch is proved by invoking moving-threshold control, it has
  left the fixed row.
- If any branch proves the mean by assuming `ResCube_3^sharp` or
  `ProjectedMajorTarget_3^B`, it is endpoint-strength and does not support a
  local proof of `LocalBdPkg_226`.

## 7. Where it fits in the project map

The Phase F2 chain now has:

```text
Module 242
  -> fixed OnePointBIHL_242.

Module 243
  -> simplified the singleton W-tail local factor to 1.

Module 244
  -> reduces the prototype to OPMeanErr_244(s0,D0,rho0)=o_W(1),
     separated by selector class.
```

The next step should audit the strength of this one-point boundary mean after
the `|W_M(t)|` average: interval length, absolute kernel mass, pointwise
versus averaged errors, and whether available prime mean estimates operate
in the needed range.

## 8. What remains open

This module does not prove:

- `OPMeanErr_244(W,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(sm,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(fr,D0,rho0)=o_W(1)`;
- `WOneBoundaryPNT_244`;
- `SmOneBoundaryMean_244`;
- `FrOneBoundaryMean_244`;
- `WtoSmOneMean_244`;
- `SmToFrOneMean_244`;
- `CutOne_242=o_W(1)`;
- `RangeOne_242=o_W(1)`;
- `WResOne_242=o_W(1)`;
- `PPOne_242=o_W(1)`;
- `NormZeroOne_242=o_W(1)`;
- `OnePointBIHL_242` outside the exact normalized model branch;
- any off-vertex one-point row;
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

- Do not cite the model branch as proof of the W, smoothed, frozen, or actual
  selector branches.
- Do not treat `Theta_{w,{(00,0)}}^proj=1` as a prime number theorem.
- Do not replace `OPMeanErr_244` by boundary volume.
- Do not replace boundary interval mean estimates by full-interval
  first-moment Hardy-Littlewood.
- Do not cite ordinary pair-BDH or rectangle-BDH as a one-point boundary mean
  theorem.
- Do not use cancellation from `W_M` after the row has taken `|W_M|`.
- Do not change selector class, projection, cutoff, W-residue convention,
  denominator grid, or dyadic shell inside the proof of a branch.
- Do not transfer smoothed estimates to frozen estimates, or frozen estimates
  to actual moving-selector estimates, without named transfer rows.
- Do not hide prime-power, W-residue, range, cutoff, normalization, or
  zero-mode terms inside `OPMeanErr_244`.
- Do not prove `OPMeanErr_244` by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
