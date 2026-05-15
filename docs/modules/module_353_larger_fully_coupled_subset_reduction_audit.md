# Module 353: Larger fully coupled subset reduction audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 352 completed the bounded mask-budget audit requested by
`PlanChallenge_11_352`. The challenge allowed one more bounded module to test
whether fully coupled subsets larger than the minimal quadruples reduce to
the same anti-diagonal coefficient and mask package.

This module performs that test.

Define:

```text
LargerFullyCoupledSubsetReductionAudit_353(P_minor^0).
```

Verdict:

```text
LargerFullyCoupledSubsetReductionAudit_353(P_minor^0):
  STRUCTURAL / EXTRACTION.

FullyCoupledBlockNormalForm_353:
  STRUCTURAL / EXTRACTION.

LargerSubsetCoefficientCatalog_353:
  STRUCTURAL / EXTRACTION.

HigherOrderBlockCoefficientRows_353:
  OPEN.

SameCoefficientMaskPackageForAllFullyCoupledRows_353:
  FALSE / BLOCKED.

EnumerationBranchContinuation_353:
  FALSE / BLOCKED.

NoTwistMaskBudgetFeasibility_354(P_minor^0):
  OPEN next target.
```

The useful extraction is that every fully coupled subset row has an exact
block-correlation normal form. However, the 65 larger fully coupled rows do
not generally reduce to the Module 349-352 pair-pair coefficient/mask
package. They introduce higher-order block coefficients depending on `d_1`,
`d_2`, or both.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no `HigherOrderBlockCoefficientRows_353`, no
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

Use the eight slots:

```text
L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k.
```

Retain:

```text
X_*={1,2},   H_*={3,4},
Y_*={5,6},   K_*={7,8}.
```

For a fully coupled subset `S`, define:

```text
A=S cap {1,2,3,4},
B=S cap {5,6,7,8}.
```

Then `A` meets both `X_*` and `H_*`, while `B` meets both `Y_*` and `K_*`.
Choose canonical anchors:

```text
i=min(A cap X_*),   j=min(A cap H_*),
m=min(B cap Y_*),   n=min(B cap K_*).
```

For the first block set:

```text
eta_l=0 for l in X_*,
eta_l=1 for l in H_*,
c_1=c_3=1,
c_2=c_4=0.
```

For the second block set:

```text
tau_l=0 for l in Y_*,
tau_l=1 for l in K_*,
c'_5=c'_7=1,
c'_6=c'_8=0.
```

Define:

```text
alpha_{ij}=c_j-c_i,
beta_{mn}=c'_n-c'_m,

r=L_i,
s=L_m,
a=L_j-L_i,
b=L_n-L_m,
q=s-r.
```

For `l in A`, define the first-block relative form:

```text
lambda_l^{i,j}(a,d_1)
  =
  eta_l a + (c_l-c_i-eta_l(c_j-c_i))d_1.
```

For `l in B`, define the second-block relative form:

```text
mu_l^{m,n}(b,d_2)
  =
  tau_l b + (c'_l-c'_m-tau_l(c'_n-c'_m))d_2.
```

Then:

```text
L_l=r+lambda_l^{i,j}(a,d_1)     for l in A,
L_l=s+mu_l^{m,n}(b,d_2)         for l in B.
```

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-352,
the nonzero minor-frequency support,
the full cyclic `P_minor^0` averaging convention,
and the convention that U(d,xi), V(d,xi) do not depend on x,y,h,k.
```

It does not assume:

```text
HigherOrderBlockCoefficientRows_353=o_W(1),
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

### A. Fully coupled block normal form

For fixed `d_1,d_2`, the map:

```text
(x,y,h,k) -> (r,s,a,b)
```

is a bijection of `G_N^4`. In these coordinates:

```text
h+k=a+b-alpha_{ij}d_1-beta_{mn}d_2.
```

Define the physical block correlations:

```text
P_A^0(a;d_1)
  =
  E_{r in G_N}
    prod_{l in A} nu_0(r+lambda_l^{i,j}(a,d_1)),

P_B^0(b;d_2)
  =
  E_{s in G_N}
    prod_{l in B} nu_0(s+mu_l^{m,n}(b,d_2)).
```

Define the exact model factor:

```text
Theta_{w,A,B}^{353}(a,b,q;d_1,d_2)
  =
  prod_{p>w}
    (1-1/p)^(-|A|-|B|)
    (1-#(Lambda_A(a,d_1) union (q+Mu_B(b,d_2)) mod p)/p),
```

where:

```text
Lambda_A(a,d_1)={lambda_l^{i,j}(a,d_1): l in A},
Mu_B(b,d_2)={mu_l^{m,n}(b,d_2): l in B}.
```

Let:

```text
R_{w,A,B}^0(a,b;d_1,d_2)
  =
  E_{q in G_N} Theta_{w,A,B}^{353}(a,b,q;d_1,d_2),

Delta_{A,B}^{353}(a,b;d_1,d_2)
  =
  P_A^0(a;d_1)P_B^0(b;d_2)-R_{w,A,B}^0(a,b;d_1,d_2).
```

Then the subset discrepancy row is exactly:

```text
Err_S^{353}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{a,b}
      K_{U,V}^0(
        d_1,d_2;
        a+b-alpha_{ij}d_1-beta_{mn}d_2
      )
      Delta_{A,B}^{353}(a,b;d_1,d_2).
```

Classification:

```text
FullyCoupledBlockNormalForm_353:
  STRUCTURAL / EXTRACTION.
```

This is exact. It is not a smallness theorem.

### B. Fourier form and comparison with the minimal package

For fixed `d_1,d_2`, define:

```text
widehat{Delta_{A,B}^{353}}_{d_1,d_2}(-xi,-xi)
  =
  E_{a,b}
    Delta_{A,B}^{353}(a,b;d_1,d_2)e_N(xi(a+b)).
```

Then:

```text
Err_S^{353}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Minor_0(R,eta)}
      U(d_1,xi)V(d_2,xi)
      e_N(-xi(alpha_{ij}d_1+beta_{mn}d_2))
      widehat{Delta_{A,B}^{353}}_{d_1,d_2}(-xi,-xi).
```

If both `A` and `B` have size `2`, this is the minimal quadruple package of
Modules 349-352: the coefficient is independent of `d_1,d_2` and reduces to
`Delta_pairpair^349`.

If `A` has size `3` or `4`, then `P_A^0(a;d_1)` and the model factor depend
on `d_1`. If `B` has size `3` or `4`, they depend on `d_2`. Thus the
coefficient is generally a `d`-dependent higher-order block coefficient, not
the same coefficient times the same mask budget.

Classification:

```text
SameCoefficientMaskPackageForAllFullyCoupledRows_353:
  FALSE / BLOCKED.
```

### C. Catalog of larger fully coupled rows

Each fully coupled first-block pattern is a nonempty choice from `X_*`
times a nonempty choice from `H_*`, hence there are:

```text
3*3=9
```

first-block patterns. Of these, `4` are minimal two-slot patterns and `5`
are enlarged patterns. The same count holds for the second block.

Therefore the `81` fully coupled subsets split into:

```text
minimal-minimal:        4*4  = 16,
minimal-enlarged:       4*5 + 5*4 = 40,
enlarged-enlarged:      5*5  = 25.
```

The first class is the Module 349-352 package. The other `65` rows are
larger fully coupled rows and require higher-order block coefficients:

```text
HigherOrderBlockCoefficientRows_353:
  OPEN.
```

Classification:

```text
LargerSubsetCoefficientCatalog_353:
  STRUCTURAL / EXTRACTION.
```

### D. Why enumeration should pause

The bounded test requested by `PlanChallenge_11_352` has a negative result:
larger fully coupled rows do not compress to the same pair-pair
coefficient/mask package. Continuing by enumerating the 65 larger rows would
create a family of higher-order coefficient rows without supplying analytic
smallness.

Classification:

```text
EnumerationBranchContinuation_353:
  FALSE / BLOCKED.
```

The next move should return to a named missing theorem. Since Module 352
isolated the no-twist mask barrier, the next target should be:

```text
NoTwistMaskBudgetFeasibility_354(P_minor^0).
```

## 6. Edge cases and exclusions

### Anchor choices

The canonical anchors above make the normal form unique. Choosing different
anchors gives equivalent coordinates but different displayed offsets. Any
future estimate must be invariant under this bookkeeping.

### Minimal quadruples

The 16 minimal-minimal rows are exactly the rows already treated by Modules
349-352. This module does not reprove or improve their estimates.

### Enlarged one-block rows

The 40 minimal-enlarged rows depend on one shift parameter through the
enlarged block. They are not controlled by the d-independent coefficient
package from Modules 349-352.

### Enlarged two-block rows

The 25 enlarged-enlarged rows depend on both `d_1` and `d_2`. They are even
farther from the minimal pair-pair package.

### Collision residues

All residue collisions inside `Lambda_A` and `q+Mu_B` remain in the exact
model factor. They are not replaced by product pair factors.

### Selector and boundary transfer

Everything remains inside the full cyclic `P_minor^0` model. This module
does not transfer to boundary-restricted sums, W-limit families, the actual
sharp moving selector, or full gap averages.

## 7. Project-map location

This module lies on the Phase K signed insertion branch:

```text
PairRectangleDefectSplit_351
  -> TwistedMaskBudgetAudit_352
  -> LargerFullyCoupledSubsetReductionAudit_353
  -> NoTwistMaskBudgetFeasibility_354.
```

It completes the bounded larger-subset test from `PlanChallenge_11_352` and
pauses the enumeration branch.

## 8. What remains open

Still open:

```text
NoTwistMaskBudgetFeasibility_354(P_minor^0),
HigherOrderBlockCoefficientRows_353,
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
NoTwistMaskBudgetFeasibility_354(P_minor^0).
```

The current cadence after completing this module is:

```text
Latest completed module: 353
Post-Reflective_1 solving count: 172
Long-term-plan count: 166

166 is not divisible by 9, so no plan update is due in this module.
166 is not divisible by 15, so no plan challenge is due in this module.
The next reflective log is expected around Module 381.
```

## 9. Forbidden upgrades

Do not cite `FullyCoupledBlockNormalForm_353` as smallness.

Do not treat larger fully coupled rows as controlled by the minimal
quadruple package.

Do not replace the exact model factor `R_{w,A,B}^0` by products of pair
factors.

Do not continue enumerating larger fully coupled rows as if enumeration were
analytic progress.

Do not use first-moment pair HL, pair-BDH, large-sieve fixed-set ceilings, or
first-moment rectangle HL as substitutes for the higher-order coefficient or
mask rows.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this cyclic normal form to the actual sharp moving selector
or to the original selected-average problem.
