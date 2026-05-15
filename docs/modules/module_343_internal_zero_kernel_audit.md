# Module 343: Internal exact-zero kernel audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Modules 339 and 342 left the exact-zero tail obstruction in two pieces:

```text
internal lifted-zero rows,
cross lifted-zero rows.
```

This module audits the internal rows:

```text
h=0, h=d_1, h=-d_1,
k=0, k=d_2, k=-d_2.
```

It asks whether current tools bound those rows with the same absolute
localized kernel, low-prime cover envelope, zero-tail weight, masks, dyadic
ranges, W-residue convention, cutoff order, selector class, and limiting
order.

Define:

```text
InternalZeroKernelAudit_343(P_minor^0).
```

Verdict:

```text
InternalZeroKernelAudit_343(P_minor^0):
  STRUCTURAL / EXTRACTION.

InternalZeroRowsCatalog_343:
  STRUCTURAL / EXTRACTION.

BareInternalCodimension_343:
  STRUCTURAL / EXTRACTION.

InternalZeroWeightedFunctional_343:
  STRUCTURAL / EXTRACTION.

InternalZeroKernelTransferCriterion_343:
  CONDITIONAL.

InternalZeroKernelRows_339:
  OPEN.

CurrentInternalZeroKernelClosure_343:
  FALSE / BLOCKED.

CodimensionOnlyInternalZeroClosure_343:
  FALSE / BLOCKED.

CrossZeroKernelAudit_344(P_minor^0):
  OPEN next target.
```

The useful extraction is that the six internal exact-zero families are simple
fixed-slice rows in `h` or `k`. The current ledger does not turn that bare
codimension into a weighted estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no `InternalZeroKernelRows_339`, no
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

For a declared integer lift:

```text
tilde Delta_{ij}(z)=tilde L_i(z)-tilde L_j(z).
```

Let:

```text
KAbs_{U,V}^0(d_1,d_2;t)
  =
  |K_{U,V}^0(d_1,d_2;t)|
```

for the same threshold-localized masks `U,V` as in Modules 323-342.

Let `LowEnv_Y^{343}(z)` be the positive low-prime cover envelope inherited
from Modules 338 and 342:

```text
LowEnv_Y^{343}(z)
  =
  1+
  sum_{F low full cover, maxp(F)<=Y}
    1_{E(F;z)} Weight(F).
```

Let `TailWeight_Y^{int,0}(z)` denote the exact positive high-prime zero-tail
contribution on internal lifted-zero rows. This is inherited from the
schematic `TailWeight_Y^{zero}` of Module 339. It is not replaced by the
nonzero divisor envelope.

Define the internal lifted-zero set:

```text
Z_int^{343}
  =
  {h=0} union {h=d_1} union {h=-d_1}
  union {k=0} union {k=d_2} union {k=-d_2}.
```

Define the internal exact-zero weighted functional:

```text
IZ_Y^{343}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{343}(z)
      TailWeight_Y^{int,0}(z)
      1_{Z_int^{343}}(z).
```

The desired internal row would be:

```text
lim_{w -> infinity} limsup_{N -> infinity}
  IZ_{Y(N,w)}^{343}(U,V)
  =
  0
```

for every admissible `U,V`, in the same cutoff and limiting convention as
Modules 337-342.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-342,
the lifted exact-zero catalog from Module 339,
the low-envelope definition from Modules 338 and 342,
and the declared lift/wrap convention of P_minor^0.
```

It does not assume:

```text
InternalZeroKernelRows_339,
ExactZeroWeightedRows_339,
ExactZeroTailAbsorptionCriterion_339 as a proved estimate,
StructuralDiagonalTransferCriterion_339 as a proved estimate,
StructuralDiagonalRows_325,
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

### A. Internal row catalog

Within the first block:

```text
L_1=x+d_1, L_2=x, L_3=x+h+d_1, L_4=x+h,
```

the nontrivial lifted internal zero equations are:

```text
h=0,
h=d_1,
h=-d_1.
```

The equation `d_1=0` is excluded by the active dyadic shell. Similarly, within
the second block:

```text
L_5=y+d_2, L_6=y, L_7=y+k+d_2, L_8=y+k,
```

the nontrivial lifted internal zero equations are:

```text
k=0,
k=d_2,
k=-d_2.
```

Classification:

```text
InternalZeroRowsCatalog_343:
  STRUCTURAL / EXTRACTION.
```

This is only a catalog.

### B. Kernel slices forced by the internal rows

The six rows fix one of `h,k`, and therefore evaluate the kernel at:

```text
h=0:       t=k,
h=d_1:     t=k+d_1,
h=-d_1:    t=k-d_1,
k=0:       t=h,
k=d_2:     t=h+d_2,
k=-d_2:    t=h-d_2.
```

Thus the internal exact-zero row is not the full-frequency anti-diagonal
diagnostic `h+k=0`. It is a family of shifted one-variable kernel slices.
The absolute value in `KAbs_{U,V}^0` removes any zero-mean cancellation that
might have been available in a signed kernel.

Classification:

```text
InternalZeroWeightedFunctional_343:
  STRUCTURAL / EXTRACTION.
```

The functional is exact as a target. It is not smallness.

### C. Bare codimension

For fixed `d_1,d_2`, each internal row fixes one value of `h` or one value of
`k`. Therefore, with unweighted cyclic averages:

```text
E_{h,k} 1_{Z_int^{343}}(h,k,d_1,d_2)
  <=
  6/N
```

by the union bound, ignoring harmless overlaps between the six rows.

Classification:

```text
BareInternalCodimension_343:
  STRUCTURAL / EXTRACTION.
```

This is not the needed estimate. The actual row contains:

```text
KAbs_{U,V}^0,
LowEnv_Y^{343},
TailWeight_Y^{int,0},
threshold masks,
dyadic shell restrictions,
and the cutoff order.
```

### D. Conditional transfer criterion

A valid route from bare codimension to the desired row would require a
same-family fixed-slice estimate such as:

```text
For each a in {-1,0,1},

lim_{w -> infinity} limsup_{N -> infinity}
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,k}
      N^(-1)
      KAbs_{U,V}^0(d_1,d_2;k+a d_1)
      LowEnv_Y^{343}(x,y,a d_1,k,d_1,d_2)
      TailWeight_Y^{int,0}(x,y,a d_1,k,d_1,d_2)
  =
  0,
```

and the analogous three estimates with `k=a d_2` and averaging over `h`.

Classification:

```text
InternalZeroKernelTransferCriterion_343:
  CONDITIONAL.
```

No such fixed-slice weighted estimate is currently proved. It is stronger
than the bare codimension statement because it controls the actual absolute
localized kernel and the low-prime/zero-tail weights on the slice.

### E. Current closure is blocked

Current inputs do not close `IZ_Y^{343}`:

```text
BareInternalCodimension_343
```

does not control the weight concentration on the six slices.

```text
LowEnvelopeMassPrototype_342
```

controls no low-envelope mass row; it supplies only the trivial total-weight
ceiling.

```text
StructuralDiagonalRows_325
```

remain open and were not proved with the zero-tail weight.

```text
KAbs_{U,V}^0
```

is absolute and data-dependent through `U,V`; signed cancellation and
fixed-kernel heuristics do not apply automatically.

Therefore:

```text
CurrentInternalZeroKernelClosure_343:
  FALSE / BLOCKED.

CodimensionOnlyInternalZeroClosure_343:
  FALSE / BLOCKED.

InternalZeroKernelRows_339:
  OPEN.
```

### F. What this does and does not redirect

This module does not prove the internal zero row. It also does not prove that
the row is impossible. It identifies the missing theorem precisely: a
same-family fixed-slice weighted estimate with the exact absolute localized
kernel, low-prime envelope, zero-tail weight, masks, cutoff, and limit order.

The remaining exact-zero branch is the cross row:

```text
x-y = -a d_1 - b h + c d_2 + e k.
```

That row has different geometry because it fixes `x-y` rather than `h` or
`k`, while leaving the kernel variable `t=h+k` free. It should be audited
separately.

## 6. Edge cases and exclusions

### Overlaps among internal rows

The six rows can overlap, for example when `h=0` and `k=0`. The union-bound
codimension estimate remains valid. Overlap accounting is not the obstruction;
the obstruction is the weighted kernel/low-envelope/zero-tail mass on the
slices.

### Excluded shift zero

The equations `d_1=0` and `d_2=0` are excluded by the dyadic shift shell. This
module does not remove any separate boundary or wrap defects; those remain
part of the declared local model conventions.

### Kernel anti-diagonal

The full-frequency diagnostic `h+k=0` is not imposed by the internal zero
rows. Replacing the minor kernel by the anti-diagonal support condition would
repeat a shortcut already rejected in Modules 314-318 and 324.

### Nonzero divisor envelope

On lifted zero differences, every prime divides the difference. The nonzero
high-prime divisor envelope from Module 337 is therefore not available.

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
  -> InternalZeroKernelAudit_343.
```

The module is a local exact-zero audit. It is not an endpoint equivalence and
not a proof of finite-prime tail removal.

## 8. What remains open

Still open:

```text
InternalZeroKernelRows_339,
ExactZeroWeightedRows_339,
CrossZeroKernelRows_339,
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
CrossZeroKernelAudit_344(P_minor^0).
```

## Red flags / forbidden upgrades

Do not cite `BareInternalCodimension_343` as a weighted exact-zero estimate.

Do not cite `InternalZeroKernelAudit_343` as proving
`InternalZeroKernelRows_339` or `ExactZeroWeightedRows_339`.

Do not replace the absolute localized kernel by a signed zero-mean kernel.

Do not replace lifted exact-zero rows by nonzero divisor-tail bounds.

Do not use `StructuralDiagonalRows_325`, `LowEnvelopeMassRows_338`,
`KernelWeightedMobiusMomentCriterion_330`, `SignedLocalModelInsertion_326`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this local model statement to the actual sharp moving
selector or to the original selected-average problem.
