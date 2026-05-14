# Module 314: Minor-kernel row split inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the row split selected by Module 313.

Define:

```text
MinorKernelRowSplit_314(P_minor^0).
```

Starting from Module 312:

```text
WPair(d_1,d_2)
  =
  E_{h,k}
    A_{d_1}(h)A_{d_2}(k)K_minor^0(h+k),
```

the goal is to split the minor kernel into full-frequency, zero-mode, and
major-correction rows before making any weighted pair gain claim.

Verdict:

```text
MinorKernelRowSplit_314(P_minor^0):
  STRUCTURAL / EXTRACTION.

FullAntiDiagonalRowIdentity_314:
  STRUCTURAL / EXTRACTION.

ZeroModeProductIdentity_314:
  STRUCTURAL / EXTRACTION.

MajorKernelCorrectionIdentity_314:
  STRUCTURAL / EXTRACTION.

IndependentRowSmallnessRoute_314:
  FALSE / BLOCKED.

FullAntiDiagonalControl_314(P_minor^0):
  OPEN.

ZeroModeProductControl_314(P_minor^0):
  OPEN.

MajorKernelCorrectionControl_314(P_minor^0):
  OPEN.

SignedMinorKernelCombinationTarget_314(P_minor^0):
  OPEN.

ZeroModeProductAudit_315(P_minor^0):
  OPEN next target.
```

The exact split is useful, but it does not prove weighted column-pair
smallness. Current tools do not make any of the three rows harmless at the
needed threshold-weighted scale.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The split below is an exact algebraic decomposition inside the fixed local
model `P_minor^0`. It is not a weighted pair estimate, not column-barrier
smallness, not threshold closure, not adaptive-shell gain, not a minor-arc
endpoint, and not selector transfer.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D.
```

Use:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi)
             = E_{n in G_N} B_d^0(n)e_N(-xi n),

A_d(h)=E_n B_d^0(n)conj(B_d^0(n+h)).
```

The weighted same-frequency pair energy is:

```text
WPair(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

The off-diagonal weighted pair average is:

```text
WOff_311
  =
  D^(-1) sum_{d_1 != d_2} WPair(d_1,d_2).
```

Under the Module 278 / Module 312 nonzero-minor convention:

```text
Minor_0(R,eta)=(G_N\{0})\Major_0(R,eta),
```

with zero not included in `Major_0(R,eta)`, define:

```text
K_full(t)=sum_{xi in G_N} e_N(xi t)=N 1_{t=0},

K_major^0(t)=sum_{xi in Major_0(R,eta)} e_N(xi t),

K_minor^0(t)=K_full(t)-1-K_major^0(t).
```

If a future convention places zero inside the major arcs, the decomposition
must be rewritten with that zero-mode convention. The direct minor kernel
definition remains the invariant object.

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297, 308,
309, 310, 311, 312, and 313.

It uses only:

```text
the finite cyclic Fourier normalization,
the Module 312 autocorrelation identity,
the Module 278 Major_0/Minor_0 partition,
and finite algebra.
```

It does not assume:

```text
FullAntiDiagonalControl_314(P_minor^0),
ZeroModeProductControl_314(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
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
selector transfer,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Starting identity

Module 312 gives:

```text
WPair(d_1,d_2)
  =
  E_{h,k}
    A_{d_1}(h)A_{d_2}(k)K_minor^0(h+k).
```

Using:

```text
K_minor^0(t)=K_full(t)-1-K_major^0(t),
```

we obtain:

```text
WPair(d_1,d_2)
  =
  FullPair_314(d_1,d_2)
  -
  ZeroPair_314(d_1,d_2)
  -
  MajorPair_314(d_1,d_2),
```

where the three rows are defined below.

### B. Full anti-diagonal row

Define:

```text
FullPair_314(d_1,d_2)
  =
  E_{h,k}
    A_{d_1}(h)A_{d_2}(k)K_full(h+k).
```

Since:

```text
K_full(h+k)=N 1_{h+k=0},
```

we have:

```text
FullPair_314(d_1,d_2)
  =
  N E_h A_{d_1}(h)A_{d_2}(-h).
```

Equivalently:

```text
FullPair_314(d_1,d_2)
  =
  sum_{xi in G_N}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

The off-diagonal row is:

```text
FullAntiDiagonalRow_314
  =
  D^(-1) sum_{d_1 != d_2}
    FullPair_314(d_1,d_2).
```

Classification:

```text
FullAntiDiagonalRowIdentity_314:
  STRUCTURAL / EXTRACTION.

FullAntiDiagonalControl_314(P_minor^0):
  OPEN.
```

The identity exposes the anti-diagonal geometry. It does not control the
row. Replacing the minor kernel by this full-frequency row loses the zero and
major corrections.

### C. Zero-mode product row

Define:

```text
ZeroPair_314(d_1,d_2)
  =
  E_{h,k} A_{d_1}(h)A_{d_2}(k).
```

Because:

```text
E_h A_d(h)=|beta_0(d,0)|^2,
```

the zero row has the exact coefficient-space form:

```text
ZeroPair_314(d_1,d_2)
  =
  |beta_0(d_1,0)|^2 |beta_0(d_2,0)|^2.
```

The off-diagonal row is:

```text
ZeroModeProductRow_314
  =
  D^(-1) sum_{d_1 != d_2}
    |beta_0(d_1,0)|^2 |beta_0(d_2,0)|^2.
```

Classification:

```text
ZeroModeProductIdentity_314:
  STRUCTURAL / EXTRACTION.

ZeroModeProductControl_314(P_minor^0):
  OPEN.
```

This row is lower-dimensional, but it is not automatically zero. The local
object here is `B_d^0`, not a declared centered object `B_d^circ`. A future
module must decide whether `beta_0(d,0)` is controlled by an exact centering
convention, a pair-covariance estimate, or an open zero-mode row.

### D. Major-kernel correction row

Define:

```text
MajorPair_314(d_1,d_2)
  =
  E_{h,k}
    A_{d_1}(h)A_{d_2}(k)K_major^0(h+k).
```

Expanding the major kernel gives:

```text
MajorPair_314(d_1,d_2)
  =
  sum_{xi in Major_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

The off-diagonal row is:

```text
MajorKernelCorrectionRow_314
  =
  D^(-1) sum_{d_1 != d_2}
    MajorPair_314(d_1,d_2).
```

Classification:

```text
MajorKernelCorrectionIdentity_314:
  STRUCTURAL / EXTRACTION.

MajorKernelCorrectionControl_314(P_minor^0):
  OPEN.
```

This row is tied to the major-frequency side of the same weighted
coefficient-pair problem. It cannot be treated as small merely because it is
called a correction. Any control would need a same-family major-frequency
weighted pair estimate, with the exact W-residue, cutoff, denominator,
threshold, and limiting-order conventions restored.

### E. Off-diagonal row identity

Combining the three rows gives the exact off-diagonal identity:

```text
WOff_311
  =
  FullAntiDiagonalRow_314
  -
  ZeroModeProductRow_314
  -
  MajorKernelCorrectionRow_314.
```

Equivalently:

```text
D^(-1) sum_{d_1 != d_2}
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2

=

D^(-1) sum_{d_1 != d_2}
  sum_{xi in G_N}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2

-
D^(-1) sum_{d_1 != d_2}
  |beta_0(d_1,0)|^2 |beta_0(d_2,0)|^2

-
D^(-1) sum_{d_1 != d_2}
  sum_{xi in Major_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

Classification:

```text
MinorKernelRowSplit_314(P_minor^0):
  STRUCTURAL / EXTRACTION.
```

This is an exact partition of frequencies. It supplies no smallness.

### F. Why independent row smallness is not available

A tempting route is:

```text
bound FullAntiDiagonalRow_314,
bound ZeroModeProductRow_314,
bound MajorKernelCorrectionRow_314,
then infer WOff_311 is small.
```

The current ledger does not provide such bounds.

For the full row, current Cauchy/Parseval estimates recover the same
energy-square or fourth-power ceilings already recorded in Module 311.

For the zero row, no active local theorem says:

```text
beta_0(d,0)=0
```

or gives a sufficiently strong average bound for the off-diagonal product of
`|beta_0(d,0)|^2`.

For the major row, control would require a major-frequency weighted pair
estimate. The existing major-arc model ledgers are conditional and do not
automatically apply to this `P_minor^0` row.

Therefore:

```text
IndependentRowSmallnessRoute_314:
  FALSE / BLOCKED.
```

This blocks only the current independent-row route. It does not block a
future signed or jointly controlled minor-kernel estimate.

### G. Extracted combined target

The honest next analytic target is not any one row by name. It is the signed
combination:

```text
FullAntiDiagonalRow_314
  -
ZeroModeProductRow_314
  -
MajorKernelCorrectionRow_314.
```

Define:

```text
SignedMinorKernelCombinationTarget_314(P_minor^0):
  prove a same-family estimate for the signed row combination above,
  strong enough after Module 310 threshold conversion and Module 284
  column-barrier weights to beat the first-incidence ceiling.
```

Status:

```text
SignedMinorKernelCombinationTarget_314(P_minor^0):
  OPEN.
```

Before attempting that combined estimate, the smallest useful next step is
to audit the zero-mode row, because it has the exact form:

```text
ZeroModeProductRow_314
  =
  D^(-1) sum_{d_1 != d_2}
    |beta_0(d_1,0)|^2 |beta_0(d_2,0)|^2.
```

Define:

```text
ZeroModeProductAudit_315(P_minor^0):
  decide whether the zero-mode row is killed by convention, controlled by
  a local pair-covariance estimate, or remains an open obstruction.
```

Status:

```text
ZeroModeProductAudit_315(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If zero is included in `Major_0(R,eta)` by a future convention, the split must
not subtract the zero mode twice. The direct definition of `K_minor^0` should
be used to rederive the row identity.

If `Major_0(R,eta)` is empty, the major correction row is zero locally, but
the full anti-diagonal and zero-mode rows still require classification.

If `Minor_0(R,eta)` is empty, `WOff_311=0` locally. This is local vacuity, not
column-barrier smallness.

If `beta_0(d,0)=0` for a particular shift by convention or accident, that
shift contributes nothing to the zero-mode product row. A row theorem must be
uniform over the declared dyadic shift shell.

If `d_1=d_2`, the row is diagonal and returns to the fourth-power mass
already routed in Modules 310 and 311. The live column-pair obstruction is
the off-diagonal row.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The column branch now reads:

```text
Module 308:
  first-incidence column estimates give only barrier ceilings.

Module 309:
  layer-cake with first-moment tails collapses back to first incidence.

Module 310:
  r=2 column multiplicity becomes same-frequency shift-pair incidence.

Module 311:
  weighted coefficient-pair energy still gives only current-tool ceilings.

Module 312:
  weighted pair energy expands to an anti-diagonal two-shift autocorrelation
  kernel with the minor cutoff K_minor^0.

Module 313:
  direct attack on the bundled anti-diagonal target is blocked as the next
  move.

Module 314:
  the minor kernel is split into full-frequency, zero-mode, and major rows.
```

The selected next target is:

```text
ZeroModeProductAudit_315(P_minor^0).
```

## 8. What remains open

Still open:

```text
ZeroModeProductAudit_315(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
FullAntiDiagonalControl_314(P_minor^0),
ZeroModeProductControl_314(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
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

Do not cite `MinorKernelRowSplit_314(P_minor^0)` as a weighted pair estimate.
It is an exact partition.

Do not cite `FullAntiDiagonalRowIdentity_314`,
`ZeroModeProductIdentity_314`, or `MajorKernelCorrectionIdentity_314` as
smallness.

Do not discard the zero-mode row unless a future module proves the exact
centering or pair-covariance control needed for `beta_0(d,0)`.

Do not discard the major correction row unless a future module proves the
same-family major-frequency weighted pair estimate.

Do not replace the minor kernel by the full anti-diagonal row.

Do not cite `SignedMinorKernelCombinationTarget_314(P_minor^0)` or
`ZeroModeProductAudit_315(P_minor^0)` as proved.

Do not prove the column barriers by assuming:

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

Do not move this local `P_minor^0` split to the actual sharp moving selector
without transfer rows.

## 10. Next target

The next target is:

```text
Module 315:
  ZeroModeProductAudit_315(P_minor^0).
```

It should decide whether the zero-mode product row is killed by the exact
local convention, controlled by a local pair-covariance estimate, or remains
an open obstruction requiring its own input before the signed minor-kernel
combination can be attempted.
