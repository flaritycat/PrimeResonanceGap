# Module 318: Signed minor-kernel combination verdict inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Modules 314-317 split the weighted minor row into full, zero, and major
pieces, then rewrote the full/zero part using centered products:

```text
WOff_311
  =
  FullAntiDiag_circ_316
  -
  MajorKernelCorrectionRow_circ_317.
```

This module decides whether that signed full-minus-major formulation is a
genuinely smaller route, or whether it is merely the original minor-kernel
target in another notation.

Define:

```text
SignedMinorKernelCombinationVerdict_318(P_minor^0).
```

Verdict:

```text
SignedMinorKernelCombinationVerdict_318(P_minor^0):
  STRUCTURAL / EXTRACTION.

SignedFullMajorIdentity_318:
  STRUCTURAL / EXTRACTION.

SignedCombinationAsSmallerRoute_318:
  FALSE / BLOCKED under current inputs.

IndependentFullMajorClosure_318:
  FALSE / BLOCKED under current inputs.

SignedMinorKernelGain_318(P_minor^0):
  OPEN.

AntiDiagonalNewInputInventory_319(P_minor^0):
  OPEN next target.
```

The centered full-minus-major expression is exactly the same off-diagonal
minor row `WOff_311`. It can become a useful route only if a new signed
minor-kernel theorem is supplied. Current row splitting alone does not reduce
the analytic difficulty.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module gives a verdict about the row split. It proves no minor-kernel
cancellation, no weighted pair gain, no threshold closure, no adaptive-shell
gain, no phase-kernel bound, no residual cube endpoint, and no selector
transfer.

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
beta_0(d,xi)=widehat{B_d^0}(xi).
```

The centered product is:

```text
B_d^{0,circ}(n)=B_d^0(n)-Z_d,
Z_d=beta_0(d,0),
gamma_0(d,xi)=widehat{B_d^{0,circ}}(xi).
```

Thus:

```text
gamma_0(d,0)=0,
gamma_0(d,xi)=beta_0(d,xi) for xi != 0.
```

The active partition is:

```text
{xi != 0}
  =
  Minor_0(R,eta) disjoint union Major_0(R,eta).
```

Define:

```text
WPair(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2,

WOff_311
  =
  D^(-1) sum_{d_1 != d_2} WPair(d_1,d_2).
```

The centered full row is:

```text
FullAntiDiag_circ_316
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi != 0}
      |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

The centered major row is:

```text
MajorKernelCorrectionRow_circ_317
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Major_0(R,eta)}
      |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297, 308,
309, 310, 311, 312, 313, 314, 315, 316, and 317.

It uses:

```text
the exact nonzero-frequency partition,
the Module 315 centered rewrite,
the Module 316 centered full-row identity,
the Module 317 major-row identity,
and finite algebra.
```

It does not assume:

```text
SignedMinorKernelGain_318(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
MajorLocalModelTransfer_317(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
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
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutralityGate_260,
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

### A. The signed full-minus-major identity

Because:

```text
{xi != 0}
  =
  Minor_0(R,eta) disjoint union Major_0(R,eta),
```

we have:

```text
sum_{xi != 0}
  |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2

-

sum_{xi in Major_0(R,eta)}
  |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2

=

sum_{xi in Minor_0(R,eta)}
  |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

After summing over `d_1 != d_2`:

```text
FullAntiDiag_circ_316
  -
MajorKernelCorrectionRow_circ_317
  =
WOff_311.
```

Classification:

```text
SignedFullMajorIdentity_318:
  STRUCTURAL / EXTRACTION.
```

This identity is exact. It is not cancellation and not a gain.

### B. Centered autocorrelation form

Let:

```text
A_d^{circ}(h)
  =
  E_n B_d^{0,circ}(n)conj(B_d^{0,circ}(n+h)).
```

Since `K_minor^0` contains only nonzero frequencies:

```text
E_{h,k}
  A_{d_1}^{circ}(h)A_{d_2}^{circ}(k)K_minor^0(h+k)

=

sum_{xi in Minor_0(R,eta)}
  |gamma_0(d_1,xi)|^2 |gamma_0(d_2,xi)|^2

=

WPair(d_1,d_2).
```

Equivalently:

```text
WOff_311
  =
  D^(-1) sum_{d_1 != d_2}
    E_{h,k}
      A_{d_1}^{circ}(h)A_{d_2}^{circ}(k)K_minor^0(h+k).
```

This is the same minor-kernel object from Module 312, with the zero mode
removed by centering.

### C. Why the signed formulation is not a smaller route yet

There are two possible ways the row split could have helped.

First, the positive rows could be bounded independently:

```text
FullAntiDiag_circ_316=o(1),
MajorKernelCorrectionRow_circ_317=o(1).
```

Modules 316 and 317 record that current tools do not provide these estimates.
Thus:

```text
IndependentFullMajorClosure_318:
  FALSE / BLOCKED under current inputs.
```

Second, the signed difference could have cancellation invisible in the two
positive rows. That is possible in principle, but the only exact signed
difference is:

```text
WOff_311.
```

Therefore a useful signed route must prove a new estimate for the exact
minor-kernel row. It cannot be credited merely from the full/major split.

Classification:

```text
SignedCombinationAsSmallerRoute_318:
  FALSE / BLOCKED under current inputs.

SignedMinorKernelGain_318(P_minor^0):
  OPEN.
```

The open gain is not different from the Module 312 analytic target unless it
adds a specific new input, such as a signed anti-diagonal theorem, a residual
eight-slot cancellation theorem, or a size-sensitive kernel estimate in the
same local family.

### D. Relation to earlier targets

Module 312 defined:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0):
  prove a same-family estimate for the off-diagonal minor-kernel
  anti-diagonal row after threshold weights.
```

Module 318's signed target is:

```text
SignedMinorKernelGain_318(P_minor^0):
  prove a same-family estimate for

    D^(-1) sum_{d_1 != d_2}
      E_{h,k}
        A_{d_1}^{circ}(h)A_{d_2}^{circ}(k)K_minor^0(h+k),

  strong enough after Module 310 threshold conversion and Module 284
  column-barrier weights.
```

These are the same obstruction, with the centered convention made explicit.
So the project should not pretend Module 318 has created a new theorem. It
has clarified the exact theorem still missing.

### E. Verdict for the row-split branch

The row-split branch has served a useful purpose:

```text
Module 314:
  exposed the full, zero, and major rows.

Module 315:
  removed the explicit zero row by exact centering.

Module 316:
  showed the centered full row is still an open full nonzero-frequency
  column second moment.

Module 317:
  showed the major correction row is still an open positive major-frequency
  pair-energy row.

Module 318:
  shows the signed full-minus-major row is exactly the original minor row.
```

Thus the split does not close the weighted column-pair route under the
current toolkit. The next useful step is not another relabeling of `WOff_311`
but an inventory of genuinely new inputs that could attack the minor-kernel
target without endpoint assumptions.

Define:

```text
AntiDiagonalNewInputInventory_319(P_minor^0):
  inventory candidate non-endpoint inputs for AntiDiagonalTwoShiftKernelGain_312
  and reject any candidate that merely assumes the endpoint, projected major
  target, selector transfer, or column-barrier closure.
```

Status:

```text
AntiDiagonalNewInputInventory_319(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If `Major_0(R,eta)` is empty, then:

```text
WOff_311=FullAntiDiag_circ_316.
```

The signed split collapses to the centered full-row obstruction.

If `Minor_0(R,eta)` is empty, then `WOff_311=0` locally. This is local
vacuity, not a theorem over the active major/minor parameter regime.

If zero is included in a future major convention, the centered identity must
be rederived with that convention. The current convention removes zero before
the major/minor split.

If full and major rows are both large but nearly equal, then useful
cancellation is possible only through a theorem that sees the exact minor
kernel. Bounding the two positive rows separately will miss that cancellation.

If a future signed theorem is proved only for fixed shifts, fixed frequency
sets, or a different W-residue/limiting convention, it does not prove the
present `P_minor^0` row.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The Phase K column branch now reads:

```text
Module 312:
  weighted pair energy expands to the minor-kernel anti-diagonal row.

Module 314:
  the minor kernel is split into full, zero, and major rows.

Module 315:
  the zero row is removed only by exact centering.

Module 316:
  the centered full row remains open.

Module 317:
  the major correction row remains open.

Module 318:
  the signed full-minus-major row is exactly WOff_311, so the split is
  diagnostic unless a new signed minor-kernel theorem is supplied.
```

The selected next target is:

```text
AntiDiagonalNewInputInventory_319(P_minor^0).
```

## 8. What remains open

Still open:

```text
AntiDiagonalNewInputInventory_319(P_minor^0),
SignedMinorKernelGain_318(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
MajorLocalModelTransfer_317(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
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
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutralityGate_260,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `SignedMinorKernelCombinationVerdict_318(P_minor^0)` as a
minor-kernel estimate.

Do not cite `SignedFullMajorIdentity_318` as cancellation.

Do not claim the full-minus-major split is a smaller theorem unless a named
new signed estimate is supplied.

Do not claim `SignedMinorKernelGain_318(P_minor^0)` or
`AntiDiagonalTwoShiftKernelGain_312(P_minor^0)` is proved.

Do not use `CenteredFullAntiDiagonalControl_316`,
`MajorKernelCorrectionControl_314`, `WProjectedLocalMatch_3^major`,
`ProjectedMajorTarget_3^B`, `ProjectedModelNeutralityGate_260`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`,
`AU^3`, selector transfer, or the original selected-average problem as an
input to prove this local row.

Do not move this local `P_minor^0` verdict to the actual sharp moving
selector without transfer rows.

## 10. Next target

The next target is:

```text
Module 319:
  AntiDiagonalNewInputInventory_319(P_minor^0).
```

It should list only genuinely new non-endpoint inputs that could attack the
same-family minor-kernel anti-diagonal row, and should reject any candidate
that just renames the endpoint or assumes one of the open column-barrier,
major, minor, transfer, or residual-cube targets.
