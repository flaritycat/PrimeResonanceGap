# Module 344: Cross exact-zero kernel audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 343 audited the internal lifted-zero rows. This module audits the
remaining cross lifted-zero rows from Module 339:

```text
x-y = -a d_1 - b h + c d_2 + e k,

(a,b),(c,e) in {(1,0),(0,0),(1,1),(0,1)}.
```

There are sixteen such rows. The question is whether their bare codimension
can be promoted into a weighted estimate with the same absolute localized
kernel, low-prime cover envelope, zero-tail weight, threshold masks, dyadic
ranges, W-residue convention, cutoff order, selector class, and limiting
order.

Define:

```text
CrossZeroKernelAudit_344(P_minor^0).
```

Verdict:

```text
CrossZeroKernelAudit_344(P_minor^0):
  STRUCTURAL / EXTRACTION.

CrossZeroRowsCatalog_344:
  STRUCTURAL / EXTRACTION.

BareCrossCodimension_344:
  STRUCTURAL / EXTRACTION.

CrossZeroWeightedFunctional_344:
  STRUCTURAL / EXTRACTION.

CrossZeroKernelTransferCriterion_344:
  CONDITIONAL.

CrossZeroKernelRows_339:
  OPEN.

CurrentCrossZeroKernelClosure_344:
  FALSE / BLOCKED.

CodimensionOnlyCrossZeroClosure_344:
  FALSE / BLOCKED.

PhaseKPostCoverBranchDecision_345:
  OPEN next target.
```

The useful extraction is that cross lifted-zero rows are affine slices in
`x-y`. The current ledger does not control the same weighted row on those
slices.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no `CrossZeroKernelRows_339`, no
`ExactZeroWeightedRows_339`, no `StructuralDiagonalRows_325`, no
`LowEnvelopeMassRows_338`, no `KernelWeightedMobiusMomentCriterion_330`, no
`SignedLocalModelInsertion_326`, no `PhaseKernelBound_273^0`, no residual cube
endpoint, no selector transfer, and no statement about the original
selected-average problem.

## 3. Definitions and variables

Work in:

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
t=h+k.
```

Let:

```text
S_0={(1,0),(0,0),(1,1),(0,1)}.
```

For `(a,b),(c,e) in S_0`, define the cross affine form:

```text
Phi_{a,b,c,e}(z)
  =
  x-y+a d_1+b h-c d_2-e k.
```

The cross lifted-zero set is:

```text
Z_cross^{344}
  =
  union_{(a,b),(c,e) in S_0}
    { Phi_{a,b,c,e}(z)=0 }.
```

Let:

```text
KAbs_{U,V}^0(d_1,d_2;t)
  =
  |K_{U,V}^0(d_1,d_2;t)|.
```

Let `LowEnv_Y^{344}(z)` be the positive low-prime cover envelope inherited
from Modules 338 and 342, and let `TailWeight_Y^{cross,0}(z)` be the exact
positive zero-tail contribution on cross lifted-zero rows. As in Module 339,
this zero-tail weight is not replaced by the nonzero divisor envelope.

Define the cross exact-zero weighted functional:

```text
CZ_Y^{344}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{344}(z)
      TailWeight_Y^{cross,0}(z)
      1_{Z_cross^{344}}(z).
```

The desired cross row would be:

```text
lim_{w -> infinity} limsup_{N -> infinity}
  CZ_{Y(N,w)}^{344}(U,V)
  =
  0
```

for every admissible threshold-localized mask pair `U,V`, in the same cutoff
and limiting convention as Modules 337-343.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-343,
the lifted exact-zero catalog from Module 339,
the low-envelope definition from Modules 338 and 342,
and the declared lift/wrap convention of P_minor^0.
```

It does not assume:

```text
CrossZeroKernelRows_339,
ExactZeroWeightedRows_339,
ExactZeroTailAbsorptionCriterion_339 as a proved estimate,
StructuralDiagonalTransferCriterion_339 as a proved estimate,
StructuralDiagonalRows_325,
InternalZeroKernelRows_339,
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
WeightedLowHighCouplingRows_338,
HighDivisorMomentRows_338,
UniformLowMassAbsorptionCriterion_338 as a proved estimate,
CauchyCouplingCriterion_338 as a proved estimate,
DivisorDecorrelCriterion_338 as a proved estimate,
KernelWeightedDivisorWindowCriterion_337 as a proved estimate,
WeightedDivisorWindowRows_337,
ExactZeroTailDiagonalRows_337,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
WeightedCRTMaskCriterion_335 as a proved estimate,
KernelResidueMassCriterion_332 as a proved estimate,
AbsoluteMinorKernelResidueUniformity_332,
KernelWeightedPartitionClassCounting_331,
SharpCoverSmallness_328,
SignedLocalModelInsertion_326,
ResidualEightSlotMinorCancellation_319,
AntiDiagonalTwoShiftKernelGain_312,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

## 5. Proof / disproof / reduction

### A. Cross row catalog

The first block slot offsets relative to `x` are:

```text
(1,0), (0,0), (1,1), (0,1)
```

for `d_1` and `h`. The second block slot offsets relative to `y` are the same
four pairs for `d_2` and `k`. Thus each cross collision between a first-block
slot and a second-block slot has equation:

```text
x-y = -a d_1-b h+c d_2+e k,
```

with `(a,b),(c,e) in S_0`.

Classification:

```text
CrossZeroRowsCatalog_344:
  STRUCTURAL / EXTRACTION.
```

This is the Module 339 cross catalog rewritten as an explicit affine family.
It is not a weighted estimate.

### B. Kernel geometry

The cross rows fix `x-y`; they do not fix the kernel variable:

```text
t=h+k.
```

Therefore the cross rows are different from:

```text
h+k=0
```

and different from the internal rows of Module 343. On a cross slice, the
absolute localized kernel remains:

```text
KAbs_{U,V}^0(d_1,d_2;h+k),
```

with `h,k` still varying. Any future estimate must control the kernel on
those affine `x-y` slices with the low-prime envelope and zero-tail weight
present.

Classification:

```text
CrossZeroWeightedFunctional_344:
  STRUCTURAL / EXTRACTION.
```

The functional is exact as a target, not an estimate.

### C. Bare codimension

For fixed `d_1,d_2,h,k`, each cross equation fixes one value of `x-y`. In an
unweighted cyclic average over `x,y`:

```text
E_{x,y} 1_{Phi_{a,b,c,e}=0}
  =
  1/N.
```

By the union bound over sixteen rows:

```text
E_{x,y} 1_{Z_cross^{344}}
  <=
  16/N.
```

Classification:

```text
BareCrossCodimension_344:
  STRUCTURAL / EXTRACTION.
```

This is only a counting diagnostic. The actual row includes:

```text
KAbs_{U,V}^0,
LowEnv_Y^{344},
TailWeight_Y^{cross,0},
threshold masks,
dyadic shell restrictions,
and the cutoff order.
```

### D. Conditional transfer criterion

A valid transfer from bare codimension to the desired row would require
same-family estimates of the form:

```text
For every (a,b),(c,e) in S_0,

lim_{w -> infinity} limsup_{N -> infinity}
  D^(-1) sum_{d_1 != d_2}
    E_{y,h,k}
      N^(-1)
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{344}(y-a d_1-b h+c d_2+e k,
                     y,h,k,d_1,d_2)
      TailWeight_Y^{cross,0}(y-a d_1-b h+c d_2+e k,
                             y,h,k,d_1,d_2)
  =
  0.
```

The displayed expression uses `x=y-a d_1-b h+c d_2+e k` on the lifted cross
slice. A precise future theorem would also have to include the declared lift
and wrap convention.

Classification:

```text
CrossZeroKernelTransferCriterion_344:
  CONDITIONAL.
```

No such estimate is currently proved.

### E. Current closure is blocked

Current inputs do not close `CZ_Y^{344}`:

```text
BareCrossCodimension_344
```

does not control weight concentration on the sixteen affine slices.

```text
InternalZeroKernelAudit_343
```

does not transfer to cross rows because it fixed `h` or `k`, while cross rows
fix `x-y`.

```text
LowEnvelopeMassPrototype_342
```

does not prove a low-envelope mass row; it supplies only a trivial
total-weight ceiling.

```text
StructuralDiagonalRows_325
```

remain open and were not proved with the low-prime envelope, zero-tail weight,
absolute localized kernel, masks, cutoff, and limit order.

Therefore:

```text
CurrentCrossZeroKernelClosure_344:
  FALSE / BLOCKED.

CodimensionOnlyCrossZeroClosure_344:
  FALSE / BLOCKED.

CrossZeroKernelRows_339:
  OPEN.
```

### F. Phase K route status after internal and cross audits

Modules 342-344 now show:

```text
low-envelope first moment: exact functional, only trivial ceiling;
internal exact-zero rows: bare codimension, no weighted closure;
cross exact-zero rows: bare codimension, no weighted closure.
```

This does not prove the cover route. It suggests that the next useful module
should not add another exact-zero catalog. It should decide whether Phase K
continues through a sharper weighted theorem, returns to signed insertion, or
pauses the cover route.

Hence:

```text
PhaseKPostCoverBranchDecision_345:
  OPEN next target.
```

## 6. Edge cases and exclusions

### Overlaps among cross rows

Two cross equations may overlap for special parameter values. The union-bound
codimension estimate remains valid. Overlaps do not remove the need for a
weighted estimate.

### Lift and wrap boundary

The equations are lifted equations. A cyclic equality in `G_N` is not
automatically the same as the chosen lifted equality near wrap boundaries.
Any proof must preserve the declared lift convention.

### Kernel anti-diagonal

The cross rows do not impose `h+k=0`. Replacing the localized minor kernel by
the full-frequency anti-diagonal would repeat a forbidden shortcut from the
earlier anti-diagonal audits.

### Nonzero divisor envelope

On lifted zero differences, the nonzero high-prime divisor envelope from
Module 337 is not available. The exact zero-tail weight must be handled
directly.

### Selector and gap object

This module is internal to `P_minor^0`. It does not transfer to the actual
sharp moving selector and says nothing about the full gap average
`A_alpha(x)`.

## 7. Where it fits in the project map

```text
Phase K
  -> ResidualEightSlotMinorExpansion_323
  -> CollisionDiagonalStrataAudit_324
  -> GenericCollisionLocalModelSplit_325
  -> SignedInclusionExclusionMinorAudit_326
  -> FullCoverClusterAudit_327
  -> FullCoverLoadCriterion_328
  -> PrimePartitionMobiusAudit_329
  -> PrimePartitionCoverMomentCriterion_330
  -> PartitionClassCountingAudit_331
  -> KernelFiberPartitionAudit_332
  -> DyadicResidueUniformityAudit_333
  -> ExactPartitionCoarseningAudit_334
  -> MultiPrimeCRTMaskAudit_335
  -> FinitePrimeTailCoverAudit_336
  -> HighPrimeDivisorWindowAudit_337
  -> LowHighTailCouplingAudit_338
  -> ExactZeroTailDiagonalAudit_339
  -> CoverMomentRouteVerdict_340
  -> Reflective_5
  -> LowEnvelopeMassPrototype_342
  -> InternalZeroKernelAudit_343
  -> CrossZeroKernelAudit_344.
```

The module is the cross half of the exact-zero tail audit. It is not an
endpoint equivalence and not a proof of finite-prime tail removal.

## 8. What remains open

Still open:

```text
CrossZeroKernelRows_339,
InternalZeroKernelRows_339,
ExactZeroWeightedRows_339,
ExactZeroTailAbsorptionCriterion_339 as an estimate,
StructuralDiagonalTransferCriterion_339 as an estimate,
StructuralDiagonalRows_325,
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
WeightedLowHighCouplingRows_338,
KernelWeightedDivisorWindowCriterion_337 as an estimate,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330,
SignedLocalModelInsertion_326,
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
PhaseKPostCoverBranchDecision_345.
```

## Red flags / forbidden upgrades

Do not cite `BareCrossCodimension_344` as a weighted exact-zero estimate.

Do not cite `CrossZeroKernelAudit_344` as proving `CrossZeroKernelRows_339`
or `ExactZeroWeightedRows_339`.

Do not transfer internal zero-slice estimates to cross rows without a named
same-family theorem.

Do not replace lifted exact-zero rows by nonzero divisor-tail bounds.

Do not use `StructuralDiagonalRows_325`, `LowEnvelopeMassRows_338`,
`KernelWeightedMobiusMomentCriterion_330`, `SignedLocalModelInsertion_326`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this local model statement to the actual sharp moving
selector or to the original selected-average problem.
