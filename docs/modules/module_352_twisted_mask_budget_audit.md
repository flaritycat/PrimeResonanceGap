# Module 352: Twisted mask budget audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Modules 349-351 reduced the minimal fully coupled quadruple obstruction to
masked anti-diagonal coefficients. The remaining row has the form:

```text
sum_{xi in Minor_0(R,eta)}
  M_{alpha,beta}^{U,V}(xi) A(xi),
```

where `A(xi)` is one of the pair-residual, rectangle-defect, or combined
anti-diagonal coefficients, and:

```text
M_{alpha,beta}^{U,V}(xi)
  =
  D^(-1) sum_{d_1 != d_2}
    U(d_1,xi)V(d_2,xi)
    e_N(-xi(alpha d_1+beta d_2)).
```

This module audits the mask side. The question is whether a coefficient
estimate can be inserted directly, or whether the project needs a separate
same-family twisted-mask budget.

Define:

```text
TwistedMaskBudgetAudit_352(P_minor^0).
```

Verdict:

```text
TwistedMaskBudgetAudit_352(P_minor^0):
  STRUCTURAL / EXTRACTION.

ExactTwistedMaskTransformIdentity_352:
  STRUCTURAL / EXTRACTION.

MaskBudgetCriteria_352:
  CONDITIONAL.

NoTwistOffsetBarrier_352:
  STRUCTURAL / EXTRACTION.

CoefficientOnlyClosureShortcut_352:
  FALSE / BLOCKED.

CurrentTwistedMaskBudgetClosure_352:
  FALSE / BLOCKED.

PlanChallenge_11_352:
  STRUCTURAL / EXTRACTION.

LargerFullyCoupledSubsetReductionAudit_353(P_minor^0):
  OPEN next target.
```

The useful extraction is that `M_{alpha,beta}^{U,V}` factors into twisted
`d`-transforms of the masks, except for the excluded diagonal correction.
That factorization is not a smallness estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no `AntiDiagonalPairPairRows_350`, no
`MinimalFullyCoupledQuadrupleRows_349`, no
`FullyCoupledSubsetDiscrepancyRows_348`, no `SignedLocalModelInsertion_326`,
no `LocalModelInsertion_325`, no `PhaseKernelBound_273^0`, no residual cube
endpoint, no selector transfer, and no statement about the original
selected-average problem.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
mathcal D={d:D<|d|<=2D},
d_1 != d_2.
```

For:

```text
alpha,beta in {-1,0,1},
xi in Minor_0(R,eta),
```

and masks `U,V` on `mathcal D x Minor_0(R,eta)`, define:

```text
U_alpha(xi)
  =
  sum_{d in mathcal D}
    U(d,xi)e_N(-alpha xi d),

V_beta(xi)
  =
  sum_{d in mathcal D}
    V(d,xi)e_N(-beta xi d),

Diag_{alpha+beta}^{U,V}(xi)
  =
  sum_{d in mathcal D}
    U(d,xi)V(d,xi)e_N(-xi(alpha+beta)d).
```

The twisted mask coefficient is:

```text
M_{alpha,beta}^{U,V}(xi)
  =
  D^(-1) sum_{d_1 != d_2}
    U(d_1,xi)V(d_2,xi)
    e_N(-xi(alpha d_1+beta d_2)).
```

Let `A(xi)` denote any coefficient produced by Modules 350-351, for example:

```text
A_Delta^351(xi),
E_+^0(xi)^2,
E_+^0(xi)K_+^0(xi),
RDef_+^0(xi).
```

The active masked pairing is:

```text
Pair_{alpha,beta}^{U,V}(A)
  =
  sum_{xi in Minor_0(R,eta)}
    M_{alpha,beta}^{U,V}(xi) A(xi).
```

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-351,
the nonzero minor-frequency support,
the same `P_minor^0` dyadic shift family,
and the convention that U(d,xi), V(d,xi) do not depend on x,y,h,k.
```

It does not assume:

```text
MaskBudgetCriteria_352 as proved estimates,
PairResidualCriteria_351 as proved estimates,
RectangleDefectCoefficientCriterion_351 as a proved estimate,
AntiDiagonalPairPairRows_350=o_W(1),
CoefficientNormCriteria_350 as a proved estimate,
AntiDiagonalPairPairDiscrepancyCriterion_349 as a proved estimate,
MinimalFullyCoupledQuadrupleRows_349=o_W(1),
FullyCoupledSubsetDiscrepancyRows_348=o_W(1),
WeightedSubsetModelDiscrepancyCriterion_346 as a proved estimate,
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
KernelWeightedMobiusMomentCriterion_330,
WeightedCRTMaskCriterion_335,
KernelWeightedDivisorWindowCriterion_337,
LowEnvelopeMassRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

## 5. Proof / disproof / reduction

### A. Exact twisted transform identity

For fixed `xi`, expand the unrestricted double sum:

```text
U_alpha(xi)V_beta(xi)
  =
  sum_{d_1,d_2 in mathcal D}
    U(d_1,xi)V(d_2,xi)
    e_N(-xi(alpha d_1+beta d_2)).
```

The excluded diagonal part is:

```text
Diag_{alpha+beta}^{U,V}(xi)
  =
  sum_{d in mathcal D}
    U(d,xi)V(d,xi)e_N(-xi(alpha+beta)d).
```

Therefore:

```text
M_{alpha,beta}^{U,V}(xi)
  =
  D^(-1)
  (
    U_alpha(xi)V_beta(xi)
    - Diag_{alpha+beta}^{U,V}(xi)
  ).
```

Classification:

```text
ExactTwistedMaskTransformIdentity_352:
  STRUCTURAL / EXTRACTION.
```

This identity is exact. It gives no saving without estimates for the twisted
mask transforms or the diagonal correction.

### B. Conditional mask-budget criteria

The following are sufficient, but not proved here:

```text
sum_{xi in Minor_0(R,eta)}
  |M_{alpha,beta}^{U,V}(xi)| |A(xi)|
  =
  o_W(1)
```

for every coefficient `A` needed by Module 351 and every admissible
`U,V,alpha,beta`; or the two-norm variant:

```text
(
  sum_{xi in Minor_0(R,eta)}
    |M_{alpha,beta}^{U,V}(xi)|^2
)^(1/2)
*
(
  sum_{xi in Minor_0(R,eta)}
    |A(xi)|^2
)^(1/2)
  =
  o_W(1).
```

Equivalently, one may prove separate bounds for:

```text
U_alpha(xi)V_beta(xi)
```

and:

```text
Diag_{alpha+beta}^{U,V}(xi),
```

but the diagonal correction must be included with the same normalization and
limiting order.

Classification:

```text
MaskBudgetCriteria_352:
  CONDITIONAL.
```

### C. No-twist offset barrier

For:

```text
(alpha,beta)=(0,0),
```

the mask coefficient becomes:

```text
M_{0,0}^{U,V}(xi)
  =
  D^(-1)
  (
    (sum_d U(d,xi))(sum_d V(d,xi))
    - sum_d U(d,xi)V(d,xi)
  ).
```

There is no oscillatory `d`-phase. Thus any route relying only on twist
cancellation must fail for this offset type. This offset occurs among the
minimal quadruple rows because both `alpha=0` and `beta=0` have multiplicity
two in Module 349.

Classification:

```text
NoTwistOffsetBarrier_352:
  STRUCTURAL / EXTRACTION.
```

The barrier does not prove the row large. It only blocks a universal
twist-cancellation proof.

### D. Coefficient-only closure is blocked

Suppose one has a coefficient estimate such as:

```text
sup_{xi in Minor_0(R,eta)} |A(xi)| <= eps.
```

This gives:

```text
|Pair_{alpha,beta}^{U,V}(A)|
  <=
  eps
  sum_{xi in Minor_0(R,eta)}
    |M_{alpha,beta}^{U,V}(xi)|.
```

Without a same-family bound for the mask sum, this is not a closure. For
data-dependent threshold masks, current ledger inputs do not prevent the
masks from concentrating on frequencies where `A` is largest.

Classification:

```text
CoefficientOnlyClosureShortcut_352:
  FALSE / BLOCKED.
```

### E. Current tools do not close the mask budget

Current pair/rectangle local-model inputs concern the coefficient side. They
do not control:

```text
U_alpha(xi), V_beta(xi), Diag_{alpha+beta}^{U,V}(xi)
```

for threshold masks derived from the same large-spectrum or shell-selection
data.

Large-sieve or Bessel ceilings for fixed frequency sets also do not supply
the needed same-family estimate for these data-dependent products. At best
they give fixed-set or ceiling-scale diagnostics already recorded in earlier
Phase K modules.

Classification:

```text
CurrentTwistedMaskBudgetClosure_352:
  FALSE / BLOCKED.
```

## 6. Edge cases and exclusions

### Zero frequency

The active sum is over `Minor_0(R,eta)` and uses the nonzero minor convention.
No zero-frequency mask budget is exported.

### Excluded diagonal

The term `Diag_{alpha+beta}^{U,V}` is part of the exact identity because the
rows retain `d_1 != d_2`. Dropping it changes the object.

### No-twist offsets

The offset `(0,0)` has no oscillatory `d` saving. Any proof of the full
minimal quadruple package must handle it directly.

### Oscillatory offsets

If `alpha` or `beta` is nonzero, the additive phase may help only under a
same-family decorrelation theorem for the masks. Such a theorem is not
currently in the ledger.

### Mask dependence

The audit applies to masks `U(d,xi),V(d,xi)`. If future masks depend on
`x,y,h,k,a,b`, the reductions in Modules 349-352 must be rechecked.

### Selector and boundary transfer

Everything remains inside the full cyclic `P_minor^0` model. This module
does not transfer to boundary-restricted sums, W-limit families, the actual
sharp moving selector, or full gap averages.

## 7. Project-map location

This module lies on the Phase K signed insertion branch:

```text
AntiDiagonalPairPairDiscrepancyAudit_350
  -> PairRectangleDefectSplit_351
  -> TwistedMaskBudgetAudit_352
  -> LargerFullyCoupledSubsetReductionAudit_353.
```

It separates the missing mask theorem from the missing coefficient theorem.
It does not prove either theorem.

## 8. What remains open

Still open:

```text
LargerFullyCoupledSubsetReductionAudit_353(P_minor^0),
MaskBudgetCriteria_352,
PairResidualCriteria_351,
RectangleDefectCoefficientCriterion_351,
AntiDiagonalPairPairRows_350,
AntiDiagonalPairPairDiscrepancyCriterion_349,
MinimalFullyCoupledQuadrupleRows_349,
FullyCoupledSubsetDiscrepancyRows_348,
WeightedSubsetModelDiscrepancyCriterion_346,
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
KernelWeightedMobiusMomentCriterion_330,
WeightedCRTMaskCriterion_335,
KernelWeightedDivisorWindowCriterion_337,
LowEnvelopeMassRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the all-alpha theorem,
the finite-type theorem unconditionally,
and the original selected-average problem.
```

Next target:

```text
LargerFullyCoupledSubsetReductionAudit_353(P_minor^0).
```

### Plan challenge 11

The Module 351 ledger recorded:

```text
Post-Reflective_1 solving count: 170.
Long-term-plan count: 164.
```

Completing Module 352 adds one substantive solving iteration:

```text
Post-Reflective_1 solving count: 171.
Long-term-plan count: 165.
```

Since `165` is divisible by `15`, the eleventh plan challenge is due.

Classification:

```text
PlanChallenge_11_352:
  STRUCTURAL / EXTRACTION.
```

Challenge verdict:

```text
The Phase K signed-insertion branch has extracted the minimal fully coupled
row into coefficient and mask budgets, but it has not proved analytic
smallness. Continue for one bounded module to test whether larger fully
coupled subsets reduce to the same coefficient/mask package. If Module 353
only creates higher-order open rows without compression, pause this
enumeration branch and return to a named coefficient or mask theorem.
```

The current cadence after completing this module is:

```text
Latest completed module: 352
Post-Reflective_1 solving count: 171
Long-term-plan count: 165

165 is not divisible by 9, so no plan update is due in this module.
165 is divisible by 15, so PlanChallenge_11_352 is due and completed here.
The next reflective log is expected around Module 381.
```

## 9. Forbidden upgrades

Do not cite `ExactTwistedMaskTransformIdentity_352` as smallness.

Do not cite `MaskBudgetCriteria_352` unless the required mask budget is
proved in the same data-dependent threshold family.

Do not treat oscillatory offsets as controlling the no-twist offset.

Do not drop the excluded diagonal correction.

Do not use a coefficient theorem alone as a masked row theorem.

Do not use first-moment pair HL, pair-BDH, large-sieve fixed-set ceilings, or
first-moment rectangle HL as substitutes for `MaskBudgetCriteria_352`.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this cyclic mask identity to the actual sharp moving selector
or to the original selected-average problem.
