# Module 256: Two-point escalation gate

## 1. Precise theorem / claim being advanced

This module decides how to treat a two-point fixed-support row after the
one-point feasibility verdict of Module 255.

Module 255 showed that:

```text
FixedRowFeasGate_255
  => FixedRowOnePointPkg_249
  => OnePointBIHL_242,
```

but did not prove `FixedRowFeasGate_255`. Therefore a two-point row cannot be
used as if the one-point gates were already closed.

The diagnostic two-point row chosen here is the same-slot derivative pair:

```text
lambda0=(00,0),
S2^pair={(00,0),(00,1)}.
```

Thus the boundary-marked vertex is:

```text
v_{00,0}=n-t0,
```

and the second weighted vertex is:

```text
v_{00,1}=n-t0+d.
```

Define:

```text
TwoPointBIHL_256(s0,D0,rho0)
  = BoundaryIntervalHL_234(S2^pair,lambda0).
```

The exact W-tail local model for this same-slot two-point row is:

```text
Theta_{w,S2^pair}^proj(d,h,k;t)=kappa_w(d)
```

in the normalized shifted-pair convention, with W-residue and small-prime
compatibility separated into side rows.

Define:

```text
TwoPointEscGate_256(s0,D0,rho0)
```

to be the fixed-row diagnostic package consisting of:

```text
PairBoundaryMean_256(s0,D0,rho0),
PairSideRows_256(s0,D0,rho0),
KernelTransfer_256(s0,D0,rho0),
OnePointInheritance_256(s0,D0,rho0).
```

The conditional implication is:

```text
TwoPointEscGate_256(s0,D0,rho0)
  => TwoPointBIHL_256(s0,D0,rho0).
```

The escalation verdict is:

```text
Two-point escalation is allowed only as a diagnostic. It is not a proof route
unless the pair boundary mean, pair side rows, inherited one-point gates, and
kernel constraints are supplied in the same fixed row. If the two-point row
merely duplicates unresolved one-point gates plus a harder pair boundary
theorem, the boundary branch should pause after this diagnostic rather than
expand to larger tuple rows.
```

This module does not prove the two-point row.

## 2. Status label

`CONDITIONAL`

The module defines the first two-point diagnostic and reduces it to exact
fixed-row gates. It does not prove `TwoPointBIHL_256`, `FixedSupportTupleHL_238`,
or any endpoint theorem.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The row remains:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

The selected labels are:

```text
lambda0=(00,0),
sigma0=(00,0),
sigma1=(00,1),
S2^pair={sigma0,sigma1}.
```

The two active affine forms are:

```text
m0(n,t)=n-t0,
m1(n,d,t)=n-t0+d.
```

The boundary intervals are the same as in the one-point row:

```text
J_L(d,h,k;t)={n: m0(n,t) <= L_N},
J_R(d,h,k;t)={n: m0(n,t) > N-L_N},
```

intersected with the fixed averaging domain and `cutoff0`.

Write:

```text
r in {L,R},
J_r=J_r(d,h,k;t),
ell_r(d,h,k;t)=E_n 1_{J_r}(n).
```

The fixed weighted averaging operator is:

```text
E_K F
  = (1/D0) sum_{D0<|d|<=2D0} E_{h,k,t}|W_M(t)|F(d,h,k;t).
```

The pointwise two-point boundary error is:

```text
PairErr_256(s0;r,d,h,k;t)
  =
  E_n 1_{J_r}(n)
    mu_s0(m0(n,t)) mu_s0(m1(n,d,t))
  - ell_r(d,h,k;t) |kappa_w(d)|.
```

The averaged pair boundary error is:

```text
PairBIHLErr_256(s0,D0,rho0)
  = E_K sum_{r in {L,R}}
      |PairErr_256(s0;r,d,h,k;t)|.
```

Define:

```text
PairBoundaryMean_256(s0,D0,rho0):
  PairBIHLErr_256(s0,D0,rho0)=o_W(1)
```

with the exact same fixed row.

The pair side rows are:

```text
PairDiag_256,
PairWRes_256,
PairRange_256,
PairPP_256,
PairNormZero_256,
PairCut_256.
```

They are the two-point analogues of the Module 254 side rows, with additional
diagonal and pair-residue synchronization.

## 4. Assumptions

`TwoPointEscGate_256(s0,D0,rho0)` consists of the following assumptions.

### A. Pair boundary mean

The fixed-row pair boundary mean holds:

```text
PairBoundaryMean_256(s0,D0,rho0).
```

No full-interval pair theorem may replace it unless converted to the exact
boundary, W-admissible, `|W_M|`-weighted estimate above.

### B. Pair side rows

The pair side package is:

```text
PairSideRows_256:
  PairDiag_256=o_W(1),
  PairWRes_256=o_W(1),
  PairRange_256=o_W(1),
  PairPP_256=o_W(1),
  PairNormZero_256=o_W(1),
  PairCut_256=o_W(1).
```

The side rows mean:

```text
PairDiag_256:
  structural coincidences, repeated forms, or excluded d=0 / collision cases;

PairWRes_256:
  W-residue compatibility for both m0 and m1;

PairRange_256:
  support, denominator-grid, dyadic-shell, and endpoint support compatibility
  for both forms;

PairPP_256:
  prime-power artifacts in either of the two weights;

PairNormZero_256:
  normalization, centering, and zero-mode leakage after interval restriction;

PairCut_256:
  mismatch between the source boundary event and the declared J_L,J_R
  decomposition.
```

Each side row must be exact by convention or bounded in the same fixed-row
weighted normalization.

### C. Kernel transfer

The same absolute kernel constraints from Modules 251-252 are inherited:

```text
A_W(M),
K_q(M),
P_M,
|W_M(t)|.
```

Any proof of the pair boundary mean that changes the projection, replaces the
kernel, or uses signed cancellation in `W_M` is mixed.

### D. One-point inheritance

The two-point diagnostic must explicitly carry, rather than silently assume,
the unresolved one-point gates:

```text
FixedRowFeasGate_255
```

whenever the two-point proof uses one-point estimates as inputs.

This does not mean `FixedRowFeasGate_255` is proved. It means that a two-point
row cannot erase the one-point debt.

### E. Fixed-row discipline

All assumptions must preserve:

```text
same selector class s0,
same projection P_M,
same kernel K_M,
same boundary label lambda0,
same dyadic shell D0<|d|<=2D0,
same boundary intervals J_L,J_R,
same cutoff0,
same W-residue convention,
same prime-only or prime-power convention,
fixed w, then N -> infinity, then w -> infinity.
```

The module does not assume:

```text
TwoPointEscGate_256,
TwoPointBIHL_256,
FixedRowFeasGate_255,
FixedRowOnePointPkg_249,
FixedSupportTupleHL_238,
ordinary pair-BDH,
full-interval pair HL,
selector transfer,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

## 5. Proof / disproof / reduction

### A. Exact local model for the same-slot pair

For:

```text
S2^pair={(00,0),(00,1)},
```

the two active forms are:

```text
n-t0,
n-t0+d.
```

Their difference is `d`. In the normalized W-tail shifted-pair convention, the
local factor for primes `p>w` is:

```text
kappa_w(d)
  = prod_{p>w} (1-1/p)^(-2)
      (1 - #{0,-d mod p}/p).
```

Therefore:

```text
Theta_{w,S2^pair}^proj(d,h,k;t)=kappa_w(d)
```

for this same-slot pair, modulo the W-residue, diagonal, range, prime-power,
and normalization side rows.

This is the first genuine local-model change from the one-point row:

```text
one point: Theta=1,
same-slot two point: Theta=kappa_w(d).
```

It is not the rectangle model `Sigma_w(d,h)`, not the two-rectangle model
`Theta_w(d,h,k)`, and not a pointwise replacement by a squared pair factor.

### B. Reduction to `BoundaryIntervalHL_234`

Module 234 says that for nonempty `S`, a boundary interval weighted HL row
with the exact projected local factor implies:

```text
BoundaryTupleHL_225(S,lambda).
```

For `S=S2^pair` and `lambda=lambda0`, the required row is exactly:

```text
TwoPointBIHL_256(s0,D0,rho0)
  = BoundaryIntervalHL_234(S2^pair,lambda0).
```

The pair boundary mean plus pair side rows give the Module 234 input:

```text
PairBoundaryMean_256
  + PairSideRows_256
    => BoundaryIntervalHL_234(S2^pair,lambda0).
```

Therefore:

```text
PairBoundaryMean_256
  + PairSideRows_256
    => TwoPointBIHL_256.
```

Adding kernel and one-point inheritance bookkeeping yields:

```text
TwoPointEscGate_256
  => TwoPointBIHL_256.
```

This is a conditional reduction only.

### C. What is genuinely new

The two-point row introduces:

```text
1. pair local factor kappa_w(d);
2. pair diagonal / collision accounting;
3. simultaneous W-residue compatibility for m0 and m1;
4. boundary mean for a product of two weights;
5. pair-specific prime-power and range side rows.
```

These are genuine new obstructions relative to the one-point row.

### D. What is inherited

The two-point row does not remove:

```text
|W_M|-weighted boundary averaging,
absolute kernel mass,
cutoff and range synchronization,
same selector class discipline,
fixed dyadic shell discipline,
fixed-w then N -> infinity then w -> infinity limit order.
```

If the proof uses one-point estimates as inputs, then:

```text
FixedRowFeasGate_255
```

must be carried as an explicit assumption.

Thus the two-point row may be harder than the one-point row, not a bypass of
it.

### E. Shortcut disproofs

The following are false / blocked as closure routes:

```text
ordinary pair-BDH
  => TwoPointBIHL_256;

full-interval pair Hardy-Littlewood
  => TwoPointBIHL_256;

Theta_{w,S2^pair}^proj=kappa_w(d)
  => TwoPointBIHL_256;

FixedRowFeasGate_255
  => TwoPointBIHL_256.
```

Reasons:

```text
ordinary pair-BDH controls a different variance object;
full-interval pair HL lacks boundary localization and |W_M| weighting;
the local factor is only the model main term;
the one-point gate does not estimate a product of two weights.
```

### F. Local, mixed, endpoint-strength, and blocked verdict

The two-point row is conditional local if:

```text
PairBoundaryMean_256,
PairSideRows_256,
KernelTransfer_256,
OnePointInheritance_256 when used
```

are all supplied in the same fixed row.

It is mixed if it uses:

```text
selector transfer,
projection smoothing or replacement,
cutoff replacement,
W-residue-family comparison,
denominator-grid movement,
moving-threshold control,
changed dyadic shell,
changed limit order.
```

It is endpoint-strength if it is proved only by assuming:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
(1/D0)sum_d ||P_M B_{d,s0}||_{U^2}^4=o_W(1),
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

It is false / blocked as a shortcut if it is claimed from:

```text
ordinary pair-BDH,
first-moment HL,
full-interval pair HL,
the exact pair local factor alone,
the one-point package alone.
```

### G. Escalation decision

The two-point row is worth recording because it exposes the next local model:

```text
Theta_{w,S2^pair}^proj=kappa_w(d).
```

But escalation should continue only as a diagnostic. The project should not
expand into all two-point rows or all `FixedSupportTupleHL_238` rows until the
diagnostic row is classified as:

```text
local,
mixed,
endpoint-strength,
or false / blocked as a shortcut.
```

The present module gives the classification framework:

```text
TwoPointBIHL_256 remains CONDITIONAL.
```

## 6. Edge cases

- The dyadic shell excludes `d=0`, but pair diagonal and small-prime
  collisions still require `PairDiag_256`.
- If `p>w` divides `d`, the exact `kappa_w(d)` factor changes; do not replace
  it by a generic constant.
- W-residue compatibility must hold for both `m0` and `m1`. One-point
  W-residue synchronization is not enough.
- If `m1=n-t0+d` leaves the finite support near a boundary endpoint, the
  defect belongs to `PairRange_256`.
- If prime powers are absent by convention, `PairPP_256` may be exact zero;
  if they are merely sparse, a weighted boundary pair estimate is still
  required.
- If a pair theorem applies only to long intervals, the boundary interval
  range issue persists.
- If a theorem is proved after smoothing the boundary interval, it is mixed
  unless a cutoff-transfer row returns to `J_L,J_R`.
- If the proof uses signed cancellation in `W_M`, it does not apply after the
  fixed row takes `|W_M|`.
- If the proof invokes rectangle or cube endpoint estimates, the row is not a
  local two-point theorem.
- Off-slot two-point rows, such as `{(00,0),(10,0)}`, have different shifts
  involving `h,t0,t1` and are not proved by this same-slot diagnostic.

## 7. Where it fits in the project map

The fixed-support boundary chain now has:

```text
Modules 242-255:
  one-point prototype and feasibility verdict.

Module 256:
  same-slot two-point escalation gate.
```

The selected row is:

```text
BoundaryIntervalHL_234({(00,0),(00,1)},(00,0)).
```

It sits inside:

```text
FixedSupportTupleHL_238,
```

but it does not prove that family.

The next project step should be a reentry decision, not blind expansion:

```text
Module 257:
  minor-arc reentry gate, comparing this boundary obstruction with
  NarrowMinorArc_3^B and MinorArcTransfer_3^B.
```

## 8. What remains open

This module does not prove:

- `TwoPointEscGate_256(s0,D0,rho0)`;
- `TwoPointBIHL_256(s0,D0,rho0)`;
- `PairBoundaryMean_256`;
- `PairSideRows_256`;
- `PairDiag_256`;
- `PairWRes_256`;
- `PairRange_256`;
- `PairPP_256`;
- `PairNormZero_256`;
- `PairCut_256`;
- any off-slot two-point boundary row;
- any all-two-point fixed-support package;
- `FixedSupportTupleHL_238`;
- `FixedRowFeasGate_255`;
- `FixedRowOnePointPkg_249`;
- `OnePointBIHL_242`;
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

- Do not cite the one-point feasibility verdict as proof of a two-point row.
- Do not cite `Theta_{w,S2^pair}^proj=kappa_w(d)` as a pair boundary theorem.
- Do not replace the pair local factor by `1`, by `Sigma_w(d,h)`, by
  `kappa_w(d)^2`, or by a generic collision-free constant.
- Do not cite ordinary pair-BDH or full-interval pair HL as proof of the
  boundary-marked pair row.
- Do not use cancellation in `W_M`; the fixed row uses `|W_M|`.
- Do not change selector class, projection, cutoff, W-residue convention,
  dyadic shell, or limit order inside the diagnostic.
- Do not expand to all fixed-support tuple rows while pretending this
  diagnostic is proved.
- Do not close this row by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
