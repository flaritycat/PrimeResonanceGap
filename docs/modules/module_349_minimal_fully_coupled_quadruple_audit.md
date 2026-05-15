# Module 349: Minimal fully coupled quadruple audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 348 proved that every non-fully-coupled subset discrepancy vanishes
inside the full cyclic nonzero-frequency `P_minor^0` model. The first
surviving subset discrepancies are the minimal fully coupled quadruples:

```text
S={i,j,m,n}
with
i in X_*={1,2},
j in H_*={3,4},
m in Y_*={5,6},
n in K_*={7,8}.
```

There are `16` such quadruples. This module audits them. The question is
whether they reduce to an existing pair or rectangle local-model row, or
whether they expose a new same-family weighted pair-pair discrepancy.

Define:

```text
MinimalFullyCoupledQuadrupleAudit_349(P_minor^0).
```

Verdict:

```text
MinimalFullyCoupledQuadrupleAudit_349(P_minor^0):
  STRUCTURAL / EXTRACTION.

MinimalQuadruplePairPairIdentity_349:
  STRUCTURAL / EXTRACTION.

MinimalQuadrupleOffsetCollapse_349:
  STRUCTURAL / EXTRACTION.

AntiDiagonalPairPairDiscrepancyCriterion_349:
  CONDITIONAL.

MinimalFullyCoupledQuadrupleRows_349:
  OPEN.

CurrentPairRectangleToolsClose_349:
  FALSE / BLOCKED.

PlanUpdate_18_349:
  STRUCTURAL / EXTRACTION.

AntiDiagonalPairPairDiscrepancyAudit_350(P_minor^0):
  OPEN next target.
```

The useful extraction is that every minimal fully coupled quadruple row is
exactly a threshold-kernel average of one common pair-pair discrepancy
function along the Fourier anti-diagonal.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no `MinimalFullyCoupledQuadrupleRows_349`, no
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
L_7=y+k+d_2,    L_8=y+k,
z=(x,y,h,k,d_1,d_2),
t=h+k,
Lambda_8={1,2,3,4,5,6,7,8}.
```

Retain the four slot groups:

```text
X_*={1,2},   H_*={3,4},
Y_*={5,6},   K_*={7,8}.
```

For a minimal fully coupled quadruple:

```text
S(i,j,m,n)={i,j,m,n},
i in X_*,
j in H_*,
m in Y_*,
n in K_*,
```

define the first and second pair offsets:

```text
alpha_{ij}=1_{j=3}-1_{i=1},
beta_{mn}=1_{n=7}-1_{m=5}.
```

Then:

```text
L_j-L_i = h + alpha_{ij} d_1,
L_n-L_m = k + beta_{mn} d_2.
```

Thus `alpha_{ij}` and `beta_{mn}` take values in `{-1,0,1}`:

```text
alpha_{13}=0,   alpha_{14}=-1,
alpha_{23}=1,   alpha_{24}=0,

beta_{57}=0,    beta_{58}=-1,
beta_{67}=1,    beta_{68}=0.
```

For threshold-localized masks:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t).
```

For `S=S(i,j,m,n)`, the discrepancy row is:

```text
Err_S^{349}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      (Nu_S^{349}(z)-Theta_{w,S}^{8,min}(z)).
```

Define the local physical pair-correlation function:

```text
P_nu^0(a)
  =
  E_{r in G_N} nu_0(r)nu_0(r+a).
```

For the four selected positions `0,a,q,q+b`, define the averaged rectangle
local factor:

```text
Theta_w^4(a,b;q)
  =
  prod_{p>w}
    (1-1/p)^(-4)
    (1-#({0,a,q,q+b} mod p)/p),

R_w^0(a,b)
  =
  E_{q in G_N} Theta_w^4(a,b;q).
```

Finally define the pair-pair discrepancy:

```text
Delta_pairpair^349(a,b)
  =
  P_nu^0(a)P_nu^0(b)-R_w^0(a,b).
```

With the Fourier convention:

```text
widehat{Delta_pairpair^349}(xi_1,xi_2)
  =
  E_{a,b in G_N}
    Delta_pairpair^349(a,b)e_N(-xi_1 a-xi_2 b).
```

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-348,
the nonzero minor-frequency support of K_{U,V}^0,
and the convention that U(d,xi), V(d,xi) do not depend on x,y,h,k.
```

It does not assume:

```text
MinimalFullyCoupledQuadrupleRows_349=o_W(1),
FullyCoupledSubsetDiscrepancyRows_348=o_W(1),
TwoSidedActiveSubsetDiscrepancyRows_347=o_W(1),
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

### A. Coordinate normal form for a minimal quadruple

Fix:

```text
S=S(i,j,m,n),
i in X_*,
j in H_*,
m in Y_*,
n in K_*.
```

Set:

```text
a=L_j-L_i,
b=L_n-L_m,
r=L_i,
s=L_m,
q=s-r.
```

For fixed `d_1,d_2`, the map:

```text
(x,y,h,k) -> (r,s,a,b)
```

is a bijection of `G_N^4`. In these coordinates:

```text
h+k = a+b-alpha_{ij}d_1-beta_{mn}d_2,
```

and the four physical selected slots are:

```text
r, r+a, s, s+b.
```

Therefore:

```text
E_{r,s} Nu_S^{349}(z)
  =
  P_nu^0(a)P_nu^0(b).
```

The local model for the same four slots is:

```text
Theta_w^4(a,b;q)
```

with `q=s-r`, hence:

```text
E_{r,s} Theta_{w,S}^{8,min}(z)
  =
  R_w^0(a,b).
```

Thus:

```text
Err_S^{349}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{a,b}
      K_{U,V}^0(
        d_1,d_2;
        a+b-alpha_{ij}d_1-beta_{mn}d_2
      )
      Delta_pairpair^349(a,b).
```

Classification:

```text
MinimalQuadruplePairPairIdentity_349:
  STRUCTURAL / EXTRACTION.
```

This is an exact identity, not an estimate.

### B. Fourier anti-diagonal form

Expanding the kernel gives:

```text
Err_S^{349}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Minor_0(R,eta)}
      U(d_1,xi)V(d_2,xi)
      e_N(-xi(alpha_{ij}d_1+beta_{mn}d_2))
      widehat{Delta_pairpair^349}(-xi,-xi).
```

So the minimal fully coupled quadruples do not require a general two-variable
Fourier theorem for every `(xi_1,xi_2)`. They require control on the
anti-diagonal:

```text
(xi_1,xi_2)=(-xi,-xi),
xi in Minor_0(R,eta),
```

with the same data-dependent masks and the same `d_1,d_2` averaging.

Classification:

```text
AntiDiagonalPairPairDiscrepancyCriterion_349:
  CONDITIONAL.
```

A sufficient future criterion is:

```text
D^(-1) sum_{d_1 != d_2}
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)
    e_N(-xi(alpha d_1+beta d_2))
    widehat{Delta_pairpair^349}(-xi,-xi)
  =
  o_W(1)
```

for every same-family admissible `U,V` and every:

```text
alpha,beta in {-1,0,1}.
```

This criterion is not proved here.

### C. Offset collapse of the 16 quadruples

The `16` slot choices collapse to `9` offset types:

```text
(alpha,beta) in {-1,0,1}^2.
```

The multiplicity of an offset value is:

```text
mult(0)=2,
mult(-1)=mult(1)=1.
```

Hence the type `(alpha,beta)` has multiplicity:

```text
mult(alpha)mult(beta).
```

The only difference between two quadruples with the same `(alpha,beta)` is
the naming of coordinates before the bijection. The extracted discrepancy
function `Delta_pairpair^349` is common to all minimal quadruples; the offset
type only twists the kernel by:

```text
e_N(-xi(alpha d_1+beta d_2)).
```

Classification:

```text
MinimalQuadrupleOffsetCollapse_349:
  STRUCTURAL / EXTRACTION.
```

### D. Why current pair and rectangle tools do not close the rows

The row is not killed by the nonzero minor-kernel average. In the coordinates
above, `Delta_pairpair^349(a,b)` depends on both `a` and `b`, and the kernel
sees the combination `a+b`.

Ordinary first-moment pair Hardy-Littlewood would at best control an
unweighted mean of:

```text
P_nu^0(a)-kappa_w(a).
```

It does not control the anti-diagonal Fourier coefficient of:

```text
P_nu^0(a)P_nu^0(b)-R_w^0(a,b)
```

under threshold-localized masks.

Pair-BDH type input controls pair residual variance in one shift variable.
It does not by itself control the pair-pair discrepancy along the
anti-diagonal, and it does not replace the averaged four-point local factor
`R_w^0(a,b)` by `kappa_w(a)kappa_w(b)`.

A first-moment rectangle local model is also insufficient unless it is
upgraded to the exact same Fourier-weighted, mask-weighted, W-cyclic,
dyadic-shell, and limiting family. The local factor:

```text
R_w^0(a,b)=E_q Theta_w^4(a,b;q)
```

is the required model-side object for these rows. It is not an averaged
substitute that can be replaced pointwise by a product of pair factors.

Classification:

```text
CurrentPairRectangleToolsClose_349:
  FALSE / BLOCKED.

MinimalFullyCoupledQuadrupleRows_349:
  OPEN.
```

## 6. Edge cases and exclusions

### Zero frequency

The extracted anti-diagonal is used only for:

```text
xi in Minor_0(R,eta).
```

The exact one-variable cancellations from Modules 347-348 relied on
`xi != 0`. This module does not analyze a zero-frequency row.

### Pair diagonals

The variables `a` or `b` may be zero in `G_N`. Those diagonal cases are not
discarded. They are included in `P_nu^0(a)`, `P_nu^0(b)`, and `R_w^0(a,b)`.
Any future estimate must handle them with the same local conventions.

### `d_1=d_2`

The working family keeps `d_1 != d_2`, as in Modules 323-348. This module
does not supply a diagonal-shift transfer row.

### Mask dependence

The identity allows `U(d,xi)` and `V(d,xi)`. If a future mask depends on
`x,y,h,k,a,b`, the coordinate averaging and Fourier identity must be
rechecked.

### Boundary and selector transfer

The proof is a full cyclic average inside `P_minor^0`. It does not survive
boundary cuts, lift-window restrictions, W-limit transfer, or actual sharp
moving selector transfer without explicit transfer rows.

### Local model discipline

The exact model-side object is `R_w^0(a,b)`, the `q`-averaged four-point
factor. Replacing it by `kappa_w(a)kappa_w(b)` pointwise is forbidden.

## 7. Project-map location

This module lies on the Phase K signed local-model insertion branch:

```text
ResidualEightSlotMinorExpansion_323
  -> CollisionDiagonalStrataAudit_324
  -> GenericCollisionLocalModelSplit_325
  -> SignedInclusionExclusionMinorAudit_326
  -> SignedLocalModelInsertionFeasibility_346
  -> SubsetModelDiscrepancyAudit_347
  -> MinimalActivePairDiscrepancyAudit_348
  -> MinimalFullyCoupledQuadrupleAudit_349
  -> AntiDiagonalPairPairDiscrepancyAudit_350.
```

The module narrows the first surviving fully coupled subset rows to an
anti-diagonal pair-pair discrepancy. It does not prove the discrepancy small.

## 8. What remains open

Still open:

```text
AntiDiagonalPairPairDiscrepancyAudit_350(P_minor^0),
MinimalFullyCoupledQuadrupleRows_349,
FullyCoupledSubsetDiscrepancyRows_348,
TwoSidedActiveSubsetDiscrepancyRows_347 beyond the local zeros,
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
AntiDiagonalPairPairDiscrepancyAudit_350(P_minor^0).
```

### Plan update 18

The Module 348 ledger recorded:

```text
Post-Reflective_1 solving count: 167.
Long-term-plan count: 161.
```

Completing Module 349 adds one substantive solving iteration:

```text
Post-Reflective_1 solving count: 168.
Long-term-plan count: 162.
```

Since `162` is divisible by `9`, the eighteenth plan update is due.

Classification:

```text
PlanUpdate_18_349:
  STRUCTURAL / EXTRACTION.
```

Updated plan:

```text
Module 350:
  AntiDiagonalPairPairDiscrepancyAudit_350(P_minor^0), testing whether
  widehat{Delta_pairpair^349}(-xi,-xi) can be controlled by existing pair,
  rectangle, and same-family kernel inputs, or whether it is a new analytic
  row.

Module 351:
  if Module 350 is blocked, split Delta_pairpair^349 into pair-residual,
  pair-model product, and rectangle-collision defect pieces without replacing
  the exact rectangle factor by kappa_w(a)kappa_w(b).

Module 352:
  audit the d-dependent twist and threshold masks to decide whether a
  coefficient bound for widehat{Delta_pairpair^349} is enough, or whether a
  stronger weighted same-family theorem is required.

Module 353:
  only after the minimal quadruple row is classified, decide whether larger
  fully coupled subsets can be reduced by the same pair-pair mechanism or
  require separate high-order local-model insertion rows.
```

No theorem status is upgraded by this plan update.

The current cadence after completing this module is:

```text
Latest completed module: 349
Post-Reflective_1 solving count: 168
Long-term-plan count: 162

162 is divisible by 9, so PlanUpdate_18_349 is due and completed here.
162 is not divisible by 15, so no plan challenge is due in this module.
The next reflective log is expected around Module 381.
```

## 9. Forbidden upgrades

Do not cite `MinimalQuadruplePairPairIdentity_349` as smallness.

Do not cite `AntiDiagonalPairPairDiscrepancyCriterion_349` unless its
same-family hypotheses are proved.

Do not replace:

```text
R_w^0(a,b)
```

by:

```text
kappa_w(a)kappa_w(b)
```

pointwise.

Do not treat ordinary pair-BDH, first-moment pair Hardy-Littlewood, or
first-moment rectangle Hardy-Littlewood as proving the weighted anti-diagonal
criterion.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this cyclic local identity to the actual sharp moving
selector or to the original selected-average problem.
