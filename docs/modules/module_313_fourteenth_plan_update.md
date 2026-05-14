# Module 313: Fourteenth plan update after the weighted autocorrelation split

## 1. Precise theorem / claim being advanced

This module performs the scheduled fourteenth plan update after Module 312.

Define:

```text
PlanUpdate_14_313.
```

This is not a theorem. It is a steering and status-discipline update for the
Phase K column branch after the identity:

```text
WPair(d_1,d_2)
  =
  E_{h,k}
    A_{d_1}(h)A_{d_2}(k)K_minor^0(h+k).
```

The decision is:

```text
Do not attack AntiDiagonalTwoShiftKernelGain_312(P_minor^0) directly next.
First split the minor kernel into full-frequency, zero-mode, and major
correction rows.
```

Verdict:

```text
PlanUpdate_14_313:
  STRUCTURAL / EXTRACTION.

DirectAntiDiagonalAttack_313:
  FALSE / BLOCKED as the next move under current tools.

MinorKernelRowSplit_314(P_minor^0):
  OPEN next target.

ColumnBranchContinue_313:
  CONDITIONAL.
```

The column branch may continue, but only through a narrower row split that
makes each missing estimate visible. It must not treat Module 312's
autocorrelation identity as a proof of weighted column-pair gain.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a plan update. It proves no weighted pair estimate, no column-barrier
smallness, no threshold closure, no adaptive-shell gain, no minor-arc
endpoint, and no selector transfer.

## 3. Definitions and variables

Use the Module 278 local family:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D.
```

Use the Module 312 autocorrelation notation:

```text
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi),

A_d(h)=E_n B_d^0(n)conj(B_d^0(n+h)),

K_minor^0(t)=sum_{xi in Minor_0(R,eta)} e_N(xi t).
```

Under the standard nonzero-minor convention:

```text
K_minor^0(t)=K_full(t)-1-K_major^0(t),
K_full(t)=N 1_{t=0}.
```

The open Module 312 target is:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0):
  control
    D^(-1) sum_{d_1 != d_2}
      E_{h,k} A_{d_1}(h)A_{d_2}(k)K_minor^0(h+k)
  strongly enough after threshold conversion and Module 284 weights.
```

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297, 308,
309, 310, 311, and 312.

It does not assume:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
MinorKernelRowSplit_314(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Cadence check

Before this module, the counters were:

```text
Latest completed module: 312
Post-Reflective_1 solving count: 131
Long-term-plan count: 125
```

This module is the next substantive solving iteration, so after completion:

```text
Latest completed module: 313
Post-Reflective_1 solving count: 132
Long-term-plan count: 126
```

The cadence status is:

```text
126 is divisible by 9,
so the fourteenth plan update is due and completed here.

126 is not divisible by 15,
so no plan challenge is due.

The next reflective log remains expected around Module 341.
```

### B. What Module 312 clarified

Module 312 converted the weighted pair target from a coefficient-space name
into a precise physical/Fourier object:

```text
WPair(d_1,d_2)
  =
  E_{h,k}
    A_{d_1}(h)A_{d_2}(k)K_minor^0(h+k).
```

It also exposed the standard decomposition:

```text
K_minor^0(t)=N 1_{t=0}-1-K_major^0(t).
```

This means the weighted pair problem contains at least three distinct rows:

```text
Full anti-diagonal row:
  N E_h A_{d_1}(h)A_{d_2}(-h).

Zero-mode product row:
  E_{h,k} A_{d_1}(h)A_{d_2}(k).

Major correction row:
  E_{h,k} A_{d_1}(h)A_{d_2}(k)K_major^0(h+k).
```

The identity is useful because it prevents vague language. It does not
estimate any of these rows.

### C. Option A: direct attack on the full anti-diagonal target

A direct attack would try to prove:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0)
```

without first splitting the full, zero, and major rows.

This is blocked as the next move because the bundled target simultaneously
contains:

```text
full-frequency anti-diagonal structure,
zero-mode correction,
major-arc correction,
off-diagonal shift averaging,
eight residual slots,
collision and near-collision strata,
threshold-grid losses,
W-residue and limiting-order uniformity,
and the local selector/model conventions of P_minor^0.
```

Any proof attempt at this size would be difficult to audit. Worse, it risks
using endpoint-strength cancellation under a local name.

Therefore:

```text
DirectAntiDiagonalAttack_313:
  FALSE / BLOCKED as the next move under current tools.
```

This does not say the target is false. It says the project should not attack
the bundled object before splitting its rows.

### D. Option B: pause the column branch immediately

Pausing the column branch would be defensible if Module 312 had only renamed
the missing endpoint.

However, Module 312 produced a useful exact split:

```text
minor kernel = full anti-diagonal - zero mode - major correction.
```

This is narrower than the previous column multiplicity language. It gives a
concrete next audit that can classify which row is local, which is circular,
and which is tied to major-arc inputs.

So the column branch should not be abandoned yet. It should continue only in
proof-or-blocked mode and only for the row split.

Therefore:

```text
ColumnBranchContinue_313:
  CONDITIONAL.
```

The condition is that the next module must be a status-preserving row split,
not an endpoint-strength estimate in disguise.

### E. Option C: split the minor kernel rows

The selected next target is:

```text
MinorKernelRowSplit_314(P_minor^0).
```

It should define and classify at least:

```text
FullAntiDiagonalRow_314
  =
  D^(-1) sum_{d_1 != d_2}
    N E_h A_{d_1}(h)A_{d_2}(-h).

ZeroModeProductRow_314
  =
  D^(-1) sum_{d_1 != d_2}
    E_{h,k} A_{d_1}(h)A_{d_2}(k).

MajorKernelCorrectionRow_314
  =
  D^(-1) sum_{d_1 != d_2}
    E_{h,k}
      A_{d_1}(h)A_{d_2}(k)K_major^0(h+k).
```

The module should also record the exact relation:

```text
AntiDiagonalTwoShiftKernelGain_312
  requires a signed or jointly controlled combination of these rows,
  not merely independent large upper bounds.
```

Classification:

```text
MinorKernelRowSplit_314(P_minor^0):
  OPEN next target.
```

### F. Next 9-iteration window

The next window should remain narrow and diagnostic:

```text
Module 314:
  split the full, zero, and major rows of the minor-kernel identity.

Module 315:
  audit the zero-mode product row, including whether it is exactly expressible
  through beta_0(d,0) and whether existing centering conventions control it.

Module 316:
  audit the full anti-diagonal row and decide whether it reduces to known
  two-shift local correlation rows or is endpoint-strength.

Module 317:
  audit the major-kernel correction row and its dependence on major-arc local
  model inputs.

Module 318:
  stratify collision and near-collision rows in the two-shift eight-slot
  kernel.

Module 319:
  restore threshold conversion and Module 284 column-barrier weights to see
  which row would need genuine saving.

Module 320:
  compare the row-split target with the existing PhaseKernelBound_273^0,
  row-square, and fixed-fiber branches to avoid duplicate endpoints.

Module 321:
  give a proof-or-blocked verdict for the column branch after the row split.

Module 322:
  perform the fifteenth plan update and ninth plan challenge if the cadence
  remains one substantive module per iteration.
```

This window is allowed to stop early if a row is clearly endpoint-strength or
if the row split reveals a cleaner non-column branch.

## 6. Edge cases

If the local convention puts zero inside the major arcs, Module 314 must
adjust the displayed decomposition and state the zero-mode convention
explicitly.

If `Minor_0(R,eta)` is empty, the weighted pair row is locally zero. This is
not a threshold-window theorem.

If `Major_0(R,eta)` is empty, the major correction row vanishes locally, but
the full and zero rows still require classification.

If `d_1=d_2`, the row is diagonal and returns to the fourth-power mass
already separated in Modules 310 and 311. The live column obstruction remains
`d_1 != d_2`.

If any future module proves only a fixed-shift-pair estimate, it still must
survive off-diagonal summation, threshold conversion, W-limit order, dyadic
uniformity, and selector discipline.

Nothing in this plan update transfers from `P_minor^0` to the actual sharp
moving selector.

## 7. Project-map location

The Phase K threshold branch now has this local shape:

```text
row side:
  Modules 300-307 block current row-square/fixed-fiber routes.

column side:
  Module 308 blocks first-incidence column ceilings;
  Module 309 blocks first-moment layer-cake tails;
  Module 310 expands the r=2 same-frequency shift-pair row;
  Module 311 blocks current weighted Cauchy/Parseval routes;
  Module 312 expands the weighted pair into a minor-kernel autocorrelation.

current steering:
  Module 313 selects the minor-kernel row split before any direct
  anti-diagonal proof attempt.
```

The selected next target is:

```text
MinorKernelRowSplit_314(P_minor^0).
```

## 8. What remains open

Still open:

```text
MinorKernelRowSplit_314(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `PlanUpdate_14_313` as an estimate.

Do not cite `ColumnBranchContinue_313` as evidence that the column branch
will close. It is only permission to perform the row split.

Do not cite `MinorKernelRowSplit_314(P_minor^0)` as proved.

Do not use the full-frequency anti-diagonal row as a substitute for the minor
kernel row.

Do not discard the zero-mode or major correction rows without proof.

Do not prove `AntiDiagonalTwoShiftKernelGain_312(P_minor^0)` by assuming:

```text
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
PhaseKernelBound_273^0,
selector transfer,
or the original selected-average problem.
```

Do not move this local `P_minor^0` plan update to the actual sharp moving
selector without transfer rows.

## 10. Next target

The next target is:

```text
Module 314:
  MinorKernelRowSplit_314(P_minor^0).
```

It should split the Module 312 minor-kernel identity into full-frequency,
zero-mode, and major-correction rows, classify each row as local, structural,
blocked, or open, and avoid claiming any weighted pair gain unless an actual
same-family estimate is supplied.
