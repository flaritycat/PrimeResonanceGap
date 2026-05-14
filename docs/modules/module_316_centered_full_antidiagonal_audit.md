# Module 316: Centered full anti-diagonal audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 315 replaced the uncentered residual-pair product:

```text
B_d^0(n)=f_0(n+d)conj(f_0(n))
```

by the centered product:

```text
B_d^{0,circ}(n)=B_d^0(n)-Z_d,
Z_d=beta_0(d,0)=E_n B_d^0(n).
```

This removes the explicit zero-frequency product row from the minor-kernel
split because the minor arcs exclude `xi=0`. The present module audits the
new full-frequency row that replaces it.

Define:

```text
CenteredFullAntiDiagonalAudit_316(P_minor^0).
```

Verdict:

```text
CenteredFullAntiDiagonalAudit_316(P_minor^0):
  STRUCTURAL / EXTRACTION.

CenteredFullAntiDiagonalIdentity_316:
  STRUCTURAL / EXTRACTION.

CenteredFullColumnSecondMomentIdentity_316:
  STRUCTURAL / EXTRACTION.

CurrentCenteredFullToolsClose_316:
  FALSE / BLOCKED.

CenteredFullAntiDiagonalControl_316(P_minor^0):
  OPEN.

CenteredFullColumnSecondMomentTarget_316(P_minor^0):
  OPEN.

MajorKernelCorrectionAudit_317(P_minor^0):
  OPEN next target.
```

The centered rewrite is exact and useful, but it does not prove the centered
full anti-diagonal row small. Current Cauchy, Parseval, and energy-square
inputs still return ceiling-scale estimates or require an unavailable
same-family full-column second-moment theorem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module supplies exact identities and a route verdict. It proves no
weighted pair gain, no minor-kernel gain, no threshold closure, no adaptive
shell gain, no phase-kernel bound, no residual cube endpoint, and no selector
transfer.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D.
```

Use the Module 315 centered product:

```text
B_d^{0,circ}(n)=B_d^0(n)-Z_d,
Z_d=beta_0(d,0).
```

Define:

```text
gamma_0(d,xi)
  =
  widehat{B_d^{0,circ}}(xi).
```

Then:

```text
gamma_0(d,0)=0,
gamma_0(d,xi)=beta_0(d,xi) for xi != 0.
```

Define the centered autocorrelation:

```text
A_d^{circ}(h)
  =
  E_{n in G_N}
    B_d^{0,circ}(n)conj(B_d^{0,circ}(n+h)).
```

The centered full pair kernel is:

```text
FullPair_circ_316(d_1,d_2)
  =
  sum_{xi in G_N}
    |gamma_0(d_1,xi)|^2 |gamma_0(d_2,xi)|^2.
```

By cyclic Parseval:

```text
FullPair_circ_316(d_1,d_2)
  =
  N E_{h in G_N}
    A_{d_1}^{circ}(h) A_{d_2}^{circ}(-h).
```

The centered full anti-diagonal row is:

```text
FullAntiDiag_circ_316
  =
  D^(-1) sum_{d_1 != d_2}
    FullPair_circ_316(d_1,d_2).
```

Because `gamma_0(d,0)=0`, this is equivalently:

```text
FullAntiDiag_circ_316
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi != 0}
      |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

## 4. Assumptions

This module assumes only the active status ledger and Modules 278, 284, 297,
308, 309, 310, 311, 312, 313, 314, and 315.

It uses:

```text
finite cyclic Fourier inversion,
the Module 315 centering identity,
the fact that gamma_0(d,0)=0,
and algebraic separation of diagonal and off-diagonal d-pairs.
```

It does not assume:

```text
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
FullAntiDiagonalControl_314(P_minor^0),
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

### A. Exact centered full-row identity

By definition:

```text
FullAntiDiag_circ_316
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in G_N}
      |gamma_0(d_1,xi)|^2 |gamma_0(d_2,xi)|^2.
```

Since `gamma_0(d,0)=0`, the zero frequency contributes nothing. Therefore:

```text
FullAntiDiag_circ_316
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi != 0}
      |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

Classification:

```text
CenteredFullAntiDiagonalIdentity_316:
  STRUCTURAL / EXTRACTION.
```

This identity is the correct replacement for the uncentered full/zero split
from Module 314. It is not a smallness estimate.

### B. Column second-moment form

For each nonzero frequency define the full nonzero column mass:

```text
M_full^{circ}(xi)
  =
  sum_{D<|d|<=2D}
    |gamma_0(d,xi)|^2
  =
  sum_{D<|d|<=2D}
    |beta_0(d,xi)|^2,
  xi != 0.
```

Then:

```text
FullAntiDiag_circ_316
  =
  D^(-1)
  [
    sum_{xi != 0} (M_full^{circ}(xi))^2
    -
    sum_{D<|d|<=2D}
      sum_{xi != 0} |beta_0(d,xi)|^4
  ].
```

Thus a positive route would need same-family control of:

```text
sum_{xi != 0} (M_full^{circ}(xi))^2
```

at the scale required by the Module 310 threshold conversion and the Module
284 column-barrier weights.

Classification:

```text
CenteredFullColumnSecondMomentIdentity_316:
  STRUCTURAL / EXTRACTION.

CenteredFullColumnSecondMomentTarget_316(P_minor^0):
  OPEN.
```

The diagonal fourth-power subtraction helps algebraically, but it is
nonnegative and cannot by itself prove cancellation in the off-diagonal row.

### C. Current Cauchy and Parseval ceilings

Let:

```text
E_full^{circ}(d)
  =
  sum_{xi != 0} |beta_0(d,xi)|^2.
```

Then:

```text
FullPair_circ_316(d_1,d_2)
  <=
  E_full^{circ}(d_1) E_full^{circ}(d_2).
```

Consequently:

```text
FullAntiDiag_circ_316
  <=
  D^(-1)
  (
    sum_d E_full^{circ}(d)
  )^2,
```

up to the same harmless two-sided shell-count convention already tracked in
Modules 308-315.

This is a ceiling. It does not provide the needed smallness unless one has a
strong same-family average for `E_full^{circ}(d)`. Module 297 controls only a
minor-energy tail in the declared local family, not the full nonzero
frequency mass. The full row includes major frequencies, and those are exactly
the frequencies that have repeatedly required separate local-model and
transfer control in the project ledger.

The fourth-power route has the same problem. It asks for a same-family full
fourth-power row:

```text
D^(-1) sum_d sum_{xi != 0}|beta_0(d,xi)|^4,
```

or for an even stronger full-column second-moment estimate. The current
ledger has neither at the needed scale.

Therefore:

```text
CurrentCenteredFullToolsClose_316:
  FALSE / BLOCKED.
```

### D. Why centering does not close the row

Centering removes:

```text
beta_0(d,0).
```

It does not alter the nonzero coefficients:

```text
beta_0(d,xi), xi != 0.
```

Thus the centered full row is precisely the full nonzero-frequency row. It is
not a minor-arc row, and it is not protected by the minor cutoff. Any proof
that this full nonzero row is small enough would be a new same-family
Fourier-distribution theorem over the shift shell, not a consequence of
centering.

This is the main correction to the optimistic reading of Module 315. The
centered rewrite improves the decomposition, but the missing analytic input
has merely moved from an explicit zero row to a centered full-column
second-moment target.

### E. Relation to the minor row

Module 315 gives:

```text
WPair(d_1,d_2)
  =
  FullPair_circ_316(d_1,d_2)
  -
  MajorPair_circ_316(d_1,d_2),
```

where:

```text
MajorPair_circ_316(d_1,d_2)
  =
  sum_{xi in Major_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

Thus the weighted minor row can be written as a signed difference:

```text
WOff_311
  =
  FullAntiDiag_circ_316
  -
  MajorKernelCorrectionRow_circ_316.
```

The project should not prove the minor row by declaring each signed component
small independently unless those row estimates are actually supplied. The
next smaller audit is the major-kernel correction row, because only after the
full and major rows have both been classified can the project decide whether
the signed combination target is a genuine route or another endpoint-strength
repackaging.

## 6. Edge cases

If every nonzero coefficient `beta_0(d,xi)` vanishes, then the centered full
row is zero. This is a degenerate local model, not a theorem about the
prime-residual family.

If the major set is empty, then the centered full row equals the minor row.
In that convention, proving centered full-row smallness is just proving the
minor row.

If the major set contains every nonzero frequency, then the minor row is empty
and the centered full/major difference is vacuous. This is not the active
major/minor regime.

The diagonal `d_1=d_2` is excluded from the anti-diagonal row. Adding it back
produces the full column second moment, but the diagonal subtraction does not
create the missing cancellation.

A fixed-frequency estimate for each `xi` is not enough unless it is summable
with the exact same shift shell, W-residue convention, cutoff, denominator
range, and limiting order used in `P_minor^0`.

Nothing here transfers from the local cyclic model to the actual sharp moving
selector.

## 7. Project-map location

The Phase K column branch now reads:

```text
Module 312:
  weighted pair energy expands to a minor-kernel anti-diagonal form.

Module 314:
  the minor kernel splits into full-frequency, zero-mode, and major rows.

Module 315:
  the zero row is not killed by convention, but an exact centered rewrite
  removes it as an explicit correction.

Module 316:
  the centered full row is the full nonzero-frequency column second moment.
  Current tools do not control it at the required scale.
```

The selected next target is:

```text
MajorKernelCorrectionAudit_317(P_minor^0).
```

## 8. What remains open

Still open:

```text
MajorKernelCorrectionAudit_317(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
ZeroModeProductControl_314(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
FullAntiDiagonalControl_314(P_minor^0),
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

Do not cite `CenteredFullAntiDiagonalAudit_316(P_minor^0)` as a full-row
estimate.

Do not cite `CenteredFullAntiDiagonalIdentity_316` or
`CenteredFullColumnSecondMomentIdentity_316` as smallness.

Do not claim centering gives cancellation in nonzero frequencies. It only
removes the zero coefficient.

Do not replace the centered full row by the minor row unless the major set is
empty by convention, and then the resulting statement is the minor-row target
itself.

Do not claim current Cauchy, Parseval, energy-square, or fourth-power
estimates close the row.

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

Do not move this local `P_minor^0` audit to the actual sharp moving selector
without transfer rows.

## 10. Next target

The next target is:

```text
Module 317:
  MajorKernelCorrectionAudit_317(P_minor^0).
```

It should audit whether the major-kernel correction row has an exact local
model strong enough to pair with the centered full row, or whether the signed
full-minus-major formulation is itself endpoint-strength under current
inputs.
