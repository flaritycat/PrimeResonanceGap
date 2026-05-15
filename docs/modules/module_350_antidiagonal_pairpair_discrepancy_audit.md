# Module 350: Anti-diagonal pair-pair discrepancy audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 349 reduced each minimal fully coupled quadruple row to the
anti-diagonal Fourier coefficient of:

```text
Delta_pairpair^349(a,b)
  =
  P_nu^0(a)P_nu^0(b)-R_w^0(a,b).
```

This module audits that coefficient and the way it is paired with the
threshold-localized `d`-masks. The question is whether existing pair,
rectangle, or kernel inputs prove the needed anti-diagonal row, or whether
the project has exposed a new analytic input.

Define:

```text
AntiDiagonalPairPairDiscrepancyAudit_350(P_minor^0).
```

Verdict:

```text
AntiDiagonalPairPairDiscrepancyAudit_350(P_minor^0):
  STRUCTURAL / EXTRACTION.

AntiDiagonalCoefficientIdentity_350:
  STRUCTURAL / EXTRACTION.

TwistedMaskPairingIdentity_350:
  STRUCTURAL / EXTRACTION.

CoefficientNormCriteria_350:
  CONDITIONAL.

UnweightedCoefficientShortcut_350:
  FALSE / BLOCKED.

CurrentPairRectangleCoefficientClosure_350:
  FALSE / BLOCKED.

AntiDiagonalPairPairRows_350:
  OPEN.

PairRectangleDefectSplit_351(P_minor^0):
  OPEN next target.
```

The useful extraction is:

```text
widehat{Delta_pairpair^349}(-xi,-xi)
  =
  |widehat{nu_0}(xi)|^4 - C_w^0(xi)
```

inside the finite cyclic model, where `C_w^0(xi)` is the exact
anti-diagonal Fourier transform of the averaged four-point local factor.
This identity does not make the coefficient small.

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
D<|d_i|<=2D,
d_1 != d_2.
```

Use the Fourier convention:

```text
widehat{F}(xi)=E_{n in G_N} F(n)e_N(-xi n).
```

Recall from Module 349:

```text
P_nu^0(a)
  =
  E_{r in G_N} nu_0(r)nu_0(r+a),

Theta_w^4(a,b;q)
  =
  prod_{p>w}
    (1-1/p)^(-4)
    (1-#({0,a,q,q+b} mod p)/p),

R_w^0(a,b)
  =
  E_{q in G_N} Theta_w^4(a,b;q),

Delta_pairpair^349(a,b)
  =
  P_nu^0(a)P_nu^0(b)-R_w^0(a,b).
```

Define the physical pair-correlation Fourier coefficient:

```text
C_nu^0(xi)
  =
  E_{a in G_N} P_nu^0(a)e_N(xi a).
```

Define the exact model anti-diagonal coefficient:

```text
C_w^0(xi)
  =
  E_{a,b in G_N} R_w^0(a,b)e_N(xi(a+b))
  =
  E_{a,b,q in G_N}
    Theta_w^4(a,b;q)e_N(xi(a+b)).
```

Define:

```text
A_Delta^350(xi)
  =
  widehat{Delta_pairpair^349}(-xi,-xi)
  =
  E_{a,b in G_N}
    Delta_pairpair^349(a,b)e_N(xi(a+b)).
```

For offset type:

```text
alpha,beta in {-1,0,1},
```

and masks `U,V` supported on `Minor_0(R,eta)`, define the twisted mask
coefficient:

```text
M_{alpha,beta}^{U,V}(xi)
  =
  D^(-1) sum_{d_1 != d_2}
    U(d_1,xi)V(d_2,xi)
    e_N(-xi(alpha d_1+beta d_2)).
```

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-349,
the nonzero minor-frequency support of K_{U,V}^0,
and the convention that U(d,xi), V(d,xi) do not depend on x,y,h,k.
```

It does not assume:

```text
AntiDiagonalPairPairRows_350=o_W(1),
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

### A. The physical coefficient is a fourth Fourier power

By finite cyclic algebra:

```text
C_nu^0(xi)
  =
  E_{a,r} nu_0(r)nu_0(r+a)e_N(xi a).
```

Set `s=r+a`. Then:

```text
C_nu^0(xi)
  =
  E_{r,s} nu_0(r)nu_0(s)e_N(xi(s-r))
  =
  widehat{nu_0}(xi)widehat{nu_0}(-xi).
```

Since the local prime-only weight `nu_0` is real-valued in `P_minor^0`:

```text
C_nu^0(xi)=|widehat{nu_0}(xi)|^2.
```

Therefore:

```text
A_Delta^350(xi)
  =
  (C_nu^0(xi))^2-C_w^0(xi)
  =
  |widehat{nu_0}(xi)|^4-C_w^0(xi).
```

Classification:

```text
AntiDiagonalCoefficientIdentity_350:
  STRUCTURAL / EXTRACTION.
```

This is an identity, not a minor-arc fourth-power bound.

### B. The minimal quadruple rows are mask pairings

Module 349 gives, for each offset type `(alpha,beta)`:

```text
Err_{alpha,beta}^{350}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Minor_0(R,eta)}
      U(d_1,xi)V(d_2,xi)
      e_N(-xi(alpha d_1+beta d_2))
      A_Delta^350(xi).
```

Equivalently:

```text
Err_{alpha,beta}^{350}(U,V)
  =
  sum_{xi in Minor_0(R,eta)}
    M_{alpha,beta}^{U,V}(xi) A_Delta^350(xi).
```

Classification:

```text
TwistedMaskPairingIdentity_350:
  STRUCTURAL / EXTRACTION.
```

The anti-diagonal coefficient is only half of the target. The other half is
the same-family threshold-mask functional `M_{alpha,beta}^{U,V}`.

### C. Conditional norm criteria

The following are sufficient, but not proved here:

```text
sup_{xi in Minor_0(R,eta)} |A_Delta^350(xi)|
  *
sum_{xi in Minor_0(R,eta)}
  |M_{alpha,beta}^{U,V}(xi)|
  =
  o_W(1),
```

uniformly for all admissible `U,V,alpha,beta`; or:

```text
(
  sum_{xi in Minor_0(R,eta)} |A_Delta^350(xi)|^2
)^(1/2)
*
(
  sum_{xi in Minor_0(R,eta)} |M_{alpha,beta}^{U,V}(xi)|^2
)^(1/2)
  =
  o_W(1).
```

Classification:

```text
CoefficientNormCriteria_350:
  CONDITIONAL.
```

These criteria make explicit the missing inputs. One needs both a coefficient
theorem for:

```text
|widehat{nu_0}(xi)|^4-C_w^0(xi)
```

and a compatible same-family budget for the twisted masks.

### D. Why unweighted coefficient information is not enough

Even if one proved:

```text
E_{xi in Minor_0(R,eta)} A_Delta^350(xi)=o_W(1),
```

that would not imply:

```text
sum_{xi} M_{alpha,beta}^{U,V}(xi)A_Delta^350(xi)=o_W(1)
```

for data-dependent threshold masks. The masks may concentrate exactly where
the coefficient is largest. The case `(alpha,beta)=(0,0)` has no oscillatory
`d`-twist at all, so it is especially sensitive to mask concentration.

Classification:

```text
UnweightedCoefficientShortcut_350:
  FALSE / BLOCKED.
```

### E. Why current pair and rectangle inputs do not close the coefficient

First-moment pair Hardy-Littlewood controls the mean size of a pair local
factor. It does not control the minor-frequency fourth coefficient:

```text
|widehat{nu_0}(xi)|^4-C_w^0(xi).
```

Pair-BDH type input concerns pair residual variance in shift variables. It
does not provide the model-side anti-diagonal coefficient `C_w^0(xi)` and
does not provide the twisted threshold-mask budget.

First-moment rectangle Hardy-Littlewood controls an averaged four-point local
density. It does not control the Fourier anti-diagonal:

```text
E_{a,b,q} Theta_w^4(a,b;q)e_N(xi(a+b)),
```

nor does it justify replacing:

```text
C_w^0(xi)
```

by a product of pair factors.

Classification:

```text
CurrentPairRectangleCoefficientClosure_350:
  FALSE / BLOCKED.

AntiDiagonalPairPairRows_350:
  OPEN.
```

## 6. Edge cases and exclusions

### Zero frequency

The row is only for:

```text
xi in Minor_0(R,eta).
```

This module does not analyze `xi=0`, and no zero-frequency mean statement is
exported.

### The no-twist offset

For `(alpha,beta)=(0,0)`, the mask coefficient is:

```text
M_{0,0}^{U,V}(xi)
  =
  D^(-1) sum_{d_1 != d_2} U(d_1,xi)V(d_2,xi).
```

There is no shift oscillation. Any proof relying on `d`-cancellation must
handle this offset separately.

### Oscillatory offsets

For nonzero `alpha` or `beta`, there is an additional additive phase in
`d_1` or `d_2`. This is only potentially helpful. Data-dependent masks may
destroy usable cancellation.

### Pair diagonals

The coefficient includes all `a,b in G_N`, including `a=0` or `b=0`. No
diagonal removal is performed here.

### Model-side factor

The exact model coefficient is `C_w^0(xi)`, formed from the averaged
four-point factor `Theta_w^4`. It is not pointwise
`kappa_w(a)kappa_w(b)`.

### Selector and boundary transfer

Everything is internal to the full cyclic `P_minor^0` model. There is no
transfer to boundary-restricted sums, W-limit families, the actual sharp
moving selector, or full gap averages.

## 7. Project-map location

This module lies on the Phase K signed insertion branch:

```text
SignedLocalModelInsertionFeasibility_346
  -> SubsetModelDiscrepancyAudit_347
  -> MinimalActivePairDiscrepancyAudit_348
  -> MinimalFullyCoupledQuadrupleAudit_349
  -> AntiDiagonalPairPairDiscrepancyAudit_350
  -> PairRectangleDefectSplit_351.
```

It refines the minimal quadruple obstruction into a coefficient theorem plus
a twisted-mask budget. It does not prove either input.

## 8. What remains open

Still open:

```text
PairRectangleDefectSplit_351(P_minor^0),
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
PairRectangleDefectSplit_351(P_minor^0).
```

The current cadence after completing this module is:

```text
Latest completed module: 350
Post-Reflective_1 solving count: 169
Long-term-plan count: 163

163 is not divisible by 9, so no plan update is due in this module.
163 is not divisible by 15, so no plan challenge is due in this module.
The next reflective log is expected around Module 381.
```

## 9. Forbidden upgrades

Do not cite `AntiDiagonalCoefficientIdentity_350` as smallness.

Do not cite `CoefficientNormCriteria_350` unless both the coefficient norm
and the twisted-mask norm are proved in the same family.

Do not treat unweighted coefficient cancellation as sufficient for
data-dependent masked rows.

Do not replace `C_w^0(xi)` or `R_w^0(a,b)` by a product of pair factors.

Do not use first-moment pair HL, pair-BDH, or first-moment rectangle HL as a
substitute for the anti-diagonal coefficient theorem.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this cyclic coefficient identity to the actual sharp moving
selector or to the original selected-average problem.
