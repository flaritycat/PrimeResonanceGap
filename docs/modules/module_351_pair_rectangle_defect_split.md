# Module 351: Pair-rectangle defect split inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 350 identified the anti-diagonal coefficient:

```text
A_Delta^350(xi)
  =
  widehat{Delta_pairpair^349}(-xi,-xi)
  =
  |widehat{nu_0}(xi)|^4-C_w^0(xi).
```

This module splits the underlying pair-pair discrepancy into exact pair
residual and rectangle-defect pieces. The goal is to decide whether the
Module 350 obstruction is only a pair residual problem, or whether an exact
four-point rectangle defect remains even after the pair model is inserted.

Define:

```text
PairRectangleDefectSplit_351(P_minor^0).
```

Verdict:

```text
PairRectangleDefectSplit_351(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairResidualProductIdentity_351:
  STRUCTURAL / EXTRACTION.

AntiDiagonalDefectDecomposition_351:
  STRUCTURAL / EXTRACTION.

PairResidualCriteria_351:
  CONDITIONAL.

RectangleDefectCoefficientCriterion_351:
  CONDITIONAL.

PairOnlyClosureShortcut_351:
  FALSE / BLOCKED.

CurrentDefectSplitClosesRows_351:
  FALSE / BLOCKED.

TwistedMaskBudgetAudit_352(P_minor^0):
  OPEN next target.
```

The useful extraction is:

```text
Delta_pairpair^349(a,b)
  =
  E_pair^0(a)E_pair^0(b)
  + E_pair^0(a)kappa_w^0(b)
  + kappa_w^0(a)E_pair^0(b)
  + RectDef_w^0(a,b).
```

The final term is the exact product-vs-rectangle defect:

```text
RectDef_w^0(a,b)=kappa_w^0(a)kappa_w^0(b)-R_w^0(a,b).
```

It is not discarded and not assumed small.

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
G_N=Z/NZ.
```

Use:

```text
widehat{F}(xi)=E_{n in G_N} F(n)e_N(-xi n),
F_+(xi)=E_{n in G_N} F(n)e_N(xi n)=widehat{F}(-xi).
```

Recall:

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

Define the exact pair local factor:

```text
kappa_w^0(a)
  =
  prod_{p>w}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p).
```

Define the pair residual:

```text
E_pair^0(a)
  =
  P_nu^0(a)-kappa_w^0(a).
```

Define the rectangle product defect:

```text
RectDef_w^0(a,b)
  =
  kappa_w^0(a)kappa_w^0(b)-R_w^0(a,b).
```

For the anti-diagonal coefficient, write:

```text
A_Delta^351(xi)
  =
  E_{a,b}
    Delta_pairpair^349(a,b)e_N(xi(a+b)).
```

This is the same coefficient as `A_Delta^350(xi)`.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-350,
the exact definitions of P_nu^0, kappa_w^0, R_w^0, and Delta_pairpair^349,
and finite cyclic Fourier algebra.
```

It does not assume:

```text
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

### A. Exact defect split in physical variables

By definition:

```text
P_nu^0(a)=kappa_w^0(a)+E_pair^0(a).
```

Therefore:

```text
Delta_pairpair^349(a,b)
  =
  P_nu^0(a)P_nu^0(b)-R_w^0(a,b)
```

equals:

```text
E_pair^0(a)E_pair^0(b)
+ E_pair^0(a)kappa_w^0(b)
+ kappa_w^0(a)E_pair^0(b)
+ kappa_w^0(a)kappa_w^0(b)-R_w^0(a,b).
```

Thus:

```text
Delta_pairpair^349(a,b)
  =
  E_pair^0(a)E_pair^0(b)
  + E_pair^0(a)kappa_w^0(b)
  + kappa_w^0(a)E_pair^0(b)
  + RectDef_w^0(a,b).
```

Classification:

```text
PairResidualProductIdentity_351:
  STRUCTURAL / EXTRACTION.
```

This is exact algebra. It is not an estimate for any row.

### B. Anti-diagonal coefficient split

Define:

```text
E_+^0(xi)
  =
  E_{a in G_N} E_pair^0(a)e_N(xi a),

K_+^0(xi)
  =
  E_{a in G_N} kappa_w^0(a)e_N(xi a),

RDef_+^0(xi)
  =
  E_{a,b in G_N}
    RectDef_w^0(a,b)e_N(xi(a+b)).
```

Then:

```text
A_Delta^351(xi)
  =
  E_+^0(xi)^2
  + E_+^0(xi)K_+^0(xi)
  + K_+^0(xi)E_+^0(xi)
  + RDef_+^0(xi).
```

Equivalently:

```text
A_Delta^351(xi)
  =
  E_+^0(xi)^2
  + 2E_+^0(xi)K_+^0(xi)
  + RDef_+^0(xi),
```

but the unsymmetrized form is better for tracing the two pair slots.

Also:

```text
RDef_+^0(xi)
  =
  K_+^0(xi)^2-C_w^0(xi).
```

Classification:

```text
AntiDiagonalDefectDecomposition_351:
  STRUCTURAL / EXTRACTION.
```

This identity explains why the Module 350 coefficient is not only a pair
residual coefficient. The rectangle product defect remains as a separate
model-side term.

### C. Conditional pair residual criteria

A future pair residual input could control the first three terms if it proves
compatible bounds such as:

```text
sup_{xi in Minor_0(R,eta)} |E_+^0(xi)|
```

small enough against the same twisted-mask budget and the size of:

```text
K_+^0(xi).
```

For example, one sufficient row is:

```text
sum_{xi in Minor_0(R,eta)}
  |M_{alpha,beta}^{U,V}(xi)|
  (
    |E_+^0(xi)|^2
    + |E_+^0(xi)K_+^0(xi)|
  )
  =
  o_W(1)
```

uniformly in the same admissible `U,V,alpha,beta`.

Classification:

```text
PairResidualCriteria_351:
  CONDITIONAL.
```

No such pair residual estimate is proved here.

### D. Conditional rectangle-defect criterion

Even if:

```text
E_pair^0(a)=0
```

for every `a`, the remaining coefficient would be:

```text
RDef_+^0(xi)
  =
  K_+^0(xi)^2-C_w^0(xi).
```

Thus a separate sufficient future row is:

```text
sum_{xi in Minor_0(R,eta)}
  M_{alpha,beta}^{U,V}(xi) RDef_+^0(xi)
  =
  o_W(1)
```

uniformly in the same threshold-mask family.

Classification:

```text
RectangleDefectCoefficientCriterion_351:
  CONDITIONAL.
```

This is an exact rectangle-model compatibility row, not a pair theorem.

### E. Why the pair-only shortcut is blocked

The tempting shortcut is:

```text
P_nu^0(a) approx kappa_w^0(a)
```

and therefore:

```text
Delta_pairpair^349(a,b) approx 0.
```

That is wrong unless the rectangle product defect is also controlled. The
exact model side in Module 349 is:

```text
R_w^0(a,b)=E_q Theta_w^4(a,b;q),
```

not:

```text
kappa_w^0(a)kappa_w^0(b).
```

The row can remain nonzero through:

```text
RectDef_w^0(a,b).
```

Classification:

```text
PairOnlyClosureShortcut_351:
  FALSE / BLOCKED.

CurrentDefectSplitClosesRows_351:
  FALSE / BLOCKED.
```

The split identifies smaller rows, but proves none of them.

## 6. Edge cases and exclusions

### Zero frequency

The decomposition is algebraic for all `xi`, but the active row uses only:

```text
xi in Minor_0(R,eta).
```

No zero-frequency theorem is exported.

### Pair diagonals

The functions `P_nu^0(a)`, `kappa_w^0(a)`, and `E_pair^0(a)` include
`a=0`. This module does not remove diagonal pair offsets.

### Rectangle collisions

When the residues `0,a,q,q+b` collide modulo primes `p>w`, those collisions
are part of `Theta_w^4(a,b;q)` and hence part of `R_w^0(a,b)`. They are not
ignored or averaged away.

### Product model

The product `kappa_w^0(a)kappa_w^0(b)` is introduced only as an algebraic
intermediate. It is not the exact four-point local model.

### Mask dependence

The conditional criteria must hold with the same data-dependent threshold
masks `U,V` and the same offset twists from Modules 349-350. Unweighted
coefficient information is insufficient.

### Selector and boundary transfer

Everything remains inside the full cyclic `P_minor^0` model. This module
does not transfer to boundary-restricted sums, W-limit families, the actual
sharp moving selector, or full gap averages.

## 7. Project-map location

This module lies on the Phase K signed insertion branch:

```text
MinimalFullyCoupledQuadrupleAudit_349
  -> AntiDiagonalPairPairDiscrepancyAudit_350
  -> PairRectangleDefectSplit_351
  -> TwistedMaskBudgetAudit_352.
```

It splits the anti-diagonal coefficient into pair-residual and exact
rectangle-defect pieces. It does not prove either piece small in the masked
family.

## 8. What remains open

Still open:

```text
TwistedMaskBudgetAudit_352(P_minor^0),
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
TwistedMaskBudgetAudit_352(P_minor^0).
```

The current cadence after completing this module is:

```text
Latest completed module: 351
Post-Reflective_1 solving count: 170
Long-term-plan count: 164

164 is not divisible by 9, so no plan update is due in this module.
164 is not divisible by 15, so no plan challenge is due in this module.
The next reflective log is expected around Module 381.
```

## 9. Forbidden upgrades

Do not cite `PairResidualProductIdentity_351` or
`AntiDiagonalDefectDecomposition_351` as smallness.

Do not use the product `kappa_w^0(a)kappa_w^0(b)` as a replacement for the
exact rectangle local factor `R_w^0(a,b)`.

Do not treat pair residual control as enough unless the rectangle-defect row
and twisted-mask budget are also proved in the same family.

Do not use first-moment pair HL, pair-BDH, or first-moment rectangle HL as a
substitute for the conditional rows named here.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this cyclic defect split to the actual sharp moving selector
or to the original selected-average problem.
