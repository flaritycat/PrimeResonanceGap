# Module 319: Anti-diagonal new-input inventory inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 318 records that the centered full-minus-major formulation is exactly
the original off-diagonal minor row:

```text
FullAntiDiag_circ_316
  -
MajorKernelCorrectionRow_circ_317
  =
WOff_311.
```

This module inventories what would count as a genuinely new input for that
row, and rejects inputs that merely assume an open endpoint, transfer theorem,
projected-major target, or column-barrier closure.

Define:

```text
AntiDiagonalNewInputInventory_319(P_minor^0).
```

Verdict:

```text
AntiDiagonalNewInputInventory_319(P_minor^0):
  STRUCTURAL / EXTRACTION.

EndpointAssumptionFilter_319:
  STRUCTURAL / EXTRACTION.

RejectedInputList_319:
  STRUCTURAL / EXTRACTION.

DirectSignedMinorKernelTheorem_319(P_minor^0):
  OPEN, valid but not smaller.

SizeSensitiveMinorKernelCriterion_320(P_minor^0):
  OPEN next target.

DataDependentLargeSpectrumGain_319(P_minor^0):
  OPEN.

ResidualEightSlotMinorCancellation_319(P_minor^0):
  OPEN.

CurrentInventoryClosesAntiDiagonal_319:
  FALSE / BLOCKED.
```

The inventory does not prove the anti-diagonal minor-kernel row. It selects
one smaller next target: formulate a size-sensitive criterion precise enough
to say what extra saving would actually beat the Module 311/312 ceiling after
the Module 310 threshold conversion.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module is a steering and filtering step. It proves no minor-kernel
cancellation, no weighted column-pair gain, no threshold closure, no
adaptive-shell gain, no phase-kernel bound, no residual cube endpoint, and no
selector transfer.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D.
```

Use the centered product:

```text
B_d^{0,circ}(n)=B_d^0(n)-Z_d,
gamma_0(d,xi)=widehat{B_d^{0,circ}}(xi).
```

For `xi != 0`:

```text
gamma_0(d,xi)=beta_0(d,xi).
```

Define:

```text
A_d^{circ}(h)
  =
  E_n B_d^{0,circ}(n)conj(B_d^{0,circ}(n+h)).
```

The exact centered anti-diagonal minor-kernel row is:

```text
M_minor^{circ}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{h,k}
      A_{d_1}^{circ}(h)A_{d_2}^{circ}(k)K_minor^0(h+k).
```

Equivalently:

```text
M_minor^{circ}
  =
  WOff_311
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Minor_0(R,eta)}
      |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

This is the row that any new input must control after the Module 310
threshold conversion and the Module 284 column-barrier weights.

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297, 308,
309, 310, 311, 312, 313, 314, 315, 316, 317, and 318.

It uses:

```text
the exact centered minor-kernel identity,
the threshold-conversion role of WOff_311,
and the active status labels of open endpoint and transfer objects.
```

It does not assume:

```text
SizeSensitiveMinorKernelCriterion_320(P_minor^0),
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
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

### A. Acceptance filter for a new input

A candidate input is admissible only if it satisfies all of the following.

```text
1. It is stated in the exact family P_minor^0.
2. It controls the centered objects B_d^{0,circ}, A_d^{circ}, and K_minor^0.
3. It is averaged over the same off-diagonal dyadic shell d_1 != d_2.
4. It is uniform in the declared R, eta, W-residue b, threshold grid,
   cutoff conventions, and N -> infinity then w -> infinity order.
5. It survives the Module 310 threshold conversion losses.
6. It supplies enough saving for the Module 284 column-barrier weights.
7. It does not assume any endpoint, selector transfer, projected-major target,
   column-barrier closure, or residual cube estimate.
```

Classification:

```text
EndpointAssumptionFilter_319:
  STRUCTURAL / EXTRACTION.
```

This filter is not a theorem. It is a guardrail for future modules.

### B. Rejected inputs

The following do not count as new inputs for `M_minor^{circ}`.

| Candidate | Verdict | Reason |
|---|---|---|
| `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, `AU^3` | Rejected as assumptions | These are endpoint or endpoint-equivalent objects in the active ledger. |
| `NarrowMinorArc_3^B` or `MinorArcTransfer_3^B` | Rejected as assumptions | These are open/conditional minor-arc endpoint or transfer rows. |
| `ProjectedMajorTarget_3^B`, `WProjectedLocalMatch_3^major`, `ProjectedModelNeutralityGate_260` | Rejected as assumptions | They belong to conditional/open major-projected packages, not a proved `P_minor^0` input. |
| `CenteredFullAntiDiagonalControl_316` or `MajorKernelCorrectionControl_314` | Rejected as assumptions | These are exactly the open row controls exposed by Modules 316-317. |
| `WeightedColumnSecondMomentTarget_311` or `WeightedColumnPairEnergyTarget_310` | Rejected as assumptions | They are upstream targets that this row was meant to help prove. |
| `ColumnBarrierP0_284` or `SigmaColumnBarrierP0_284` | Rejected as assumptions | These are the column barriers, not inputs to prove them. |
| Pair-BDH, pair covariance, or first-moment Hardy-Littlewood alone | Insufficient | They do not control the fourth moment of pair products in the exact minor kernel. |
| Fixed-set large sieve or Bessel bounds alone | Insufficient | The obstruction uses data-dependent large spectra and off-diagonal shift pairs. |
| Cauchy, Parseval, cardinality bounds, or absolute kernel bounds | Insufficient | These reproduce the Module 311/312 ceilings. |
| Low-level tail or vacuous bad-frequency removal | Insufficient | Modules 297-299 show these do not close the threshold window. |
| Heuristic experiments | HEURISTIC only | They can suggest targets but cannot be cited as proof. |

Classification:

```text
RejectedInputList_319:
  STRUCTURAL / EXTRACTION.
```

### C. Candidate inputs that are genuine but open

#### 1. Direct signed minor-kernel theorem

A direct theorem could assert the needed estimate for:

```text
M_minor^{circ}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{h,k}
      A_{d_1}^{circ}(h)A_{d_2}^{circ}(k)K_minor^0(h+k).
```

This is admissible if it is proved in the exact same family and with the
required threshold losses. However, it is not a smaller target; it is the
anti-diagonal target itself.

Status:

```text
DirectSignedMinorKernelTheorem_319(P_minor^0):
  OPEN, valid but not smaller.
```

#### 2. Size-sensitive minor-kernel criterion

A potentially smaller target would not try to prove `M_minor^{circ}` directly.
Instead it would prove a criterion of the form:

```text
M_minor^{circ}
  <=
  Phi(size parameters, energy parameters, kernel parameters),
```

where `Phi` improves on the Module 311 ceiling whenever the row and column
large-spectrum fibers obey declared size or entropy bounds.

This route is admissible only if the size parameters are already available in
`P_minor^0` or are routed to separately named open estimates. It may not hide
the endpoint in `Phi`.

Status:

```text
SizeSensitiveMinorKernelCriterion_320(P_minor^0):
  OPEN next target.
```

This is selected because it is smaller than the full anti-diagonal theorem:
Module 320 can specify the exact exponents and losses needed without claiming
the size-sensitive estimate is true.

#### 3. Data-dependent large-spectrum gain

Another genuine input would control the incidence graph:

```text
(d,xi) with xi in Minor_0(R,eta) and |beta_0(d,xi)| >= lambda,
```

in a way that sees simultaneous row and column structure beyond first
incidence. It would need to beat the layer-cake and first-moment ceilings
from Modules 308-310.

Status:

```text
DataDependentLargeSpectrumGain_319(P_minor^0):
  OPEN.
```

This is a real candidate, but it should be formulated only after the
size-sensitive criterion says what gain would actually be enough.

#### 4. Residual eight-slot minor cancellation

A stronger candidate would expand the centered minor-kernel row into the
eight residual slots and prove cancellation across non-collision and
collision strata with the exact minor kernel. This would need the same-family
residual inclusion-exclusion discipline emphasized in Modules 179 and 317.

Status:

```text
ResidualEightSlotMinorCancellation_319(P_minor^0):
  OPEN.
```

This candidate is high-risk because it may be as hard as an endpoint theorem
unless it is carefully localized and shown not to assume `ResCube_3^sharp`.

### D. Why the inventory does not close the row

The inventory has found no proved estimate that can be inserted into:

```text
M_minor^{circ}=WOff_311.
```

The current valid-but-open candidates are:

```text
DirectSignedMinorKernelTheorem_319(P_minor^0),
SizeSensitiveMinorKernelCriterion_320(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0).
```

None is proved. Therefore:

```text
CurrentInventoryClosesAntiDiagonal_319:
  FALSE / BLOCKED.
```

### E. Selected next target

The smallest next move is not to attack the full anti-diagonal theorem
directly. It is to ask what size-sensitive estimate would be sufficient.

Define:

```text
SizeSensitiveMinorKernelCriterion_320(P_minor^0):
  formulate a criterion bounding M_minor^{circ} by row/column fiber sizes,
  coefficient energies, and minor-kernel parameters, with explicit losses
  checked against the Module 310 threshold conversion and Module 284
  column-barrier weights.
```

Status:

```text
SizeSensitiveMinorKernelCriterion_320(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If a candidate estimate is proved only for fixed frequency sets, it does not
handle the data-dependent large spectra unless a selection theorem is also
supplied.

If a candidate estimate controls only the full nonzero-frequency row, it does
not prove the minor row unless the major correction is also controlled or the
minor kernel is treated directly.

If a candidate estimate is averaged over W-residues, denominator ranges, or
dyadic shells differently from `P_minor^0`, it is a transfer statement, not a
same-family input.

If a candidate estimate proves only a first moment or pair covariance, it
does not control the same-frequency pair energy required here.

If a candidate theorem is strong enough to imply an endpoint object directly,
that is not forbidden, but the proof must be supplied. The endpoint cannot be
used as the input.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The Phase K column branch now reads:

```text
Module 312:
  weighted pair energy expands to the minor-kernel anti-diagonal row.

Modules 314-318:
  row splitting is audited; zero is centered away, full and major rows remain
  open, and the signed full-minus-major row is exactly WOff_311.

Module 319:
  candidate inputs are filtered; endpoint assumptions and current-tool
  ceilings are rejected; the next smaller task is a size-sensitive criterion.
```

The selected next target is:

```text
SizeSensitiveMinorKernelCriterion_320(P_minor^0).
```

## 8. What remains open

Still open:

```text
SizeSensitiveMinorKernelCriterion_320(P_minor^0),
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
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

Do not cite `AntiDiagonalNewInputInventory_319(P_minor^0)` as an
anti-diagonal estimate.

Do not claim any candidate in this inventory is proved.

Do not use endpoint objects, transfer theorems, projected-major targets,
column-barrier closure, or residual-cube estimates as inputs to prove the
same-family minor-kernel row.

Do not use pair-BDH, first-moment Hardy-Littlewood, fixed-set large sieve,
Cauchy, Parseval, cardinality-kernel, low-level-tail, or vacuous-removal
estimates as a substitute for the needed signed minor-kernel theorem.

Do not hide the endpoint inside a size-sensitive function `Phi`.

Do not move this local `P_minor^0` inventory to the actual sharp moving
selector without transfer rows.

## 10. Next target

The next target is:

```text
Module 320:
  SizeSensitiveMinorKernelCriterion_320(P_minor^0).
```

It should define an exact criterion for bounding `M_minor^{circ}` in terms of
row/column fiber sizes, coefficient energies, and kernel parameters, and then
check which exponents would actually survive the Module 310 threshold
conversion and Module 284 column-barrier weights.
