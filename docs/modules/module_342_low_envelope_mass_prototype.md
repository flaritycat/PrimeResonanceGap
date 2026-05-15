# Module 342: Low-envelope mass prototype inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Modules 337 and 338 isolated a concrete obstruction in the finite-prime tail
route: the high-prime divisor ceiling is multiplied by a positive low-prime
cover envelope under the same absolute kernel and threshold masks. Module 340
then selected the narrow diagnostic row:

```text
LowEnvelopeMassPrototype_342(P_minor^0).
```

This module tests that row directly. It asks whether the current ledger proves
an absolute-kernel mass estimate for the low-prime cover envelope strong
enough to feed the absorption route in Module 338.

Verdict:

```text
LowEnvelopeMassPrototype_342(P_minor^0):
  STRUCTURAL / EXTRACTION.

LowEnvelopeMassFunctional_342:
  STRUCTURAL / EXTRACTION.

TrivialLowEnvelopeMassCeiling_342:
  STRUCTURAL / EXTRACTION.

LowEnvelopeAbsorptionImplication_342:
  CONDITIONAL.

LowEnvelopeMassRows_338:
  OPEN.

UniformLowMassAbsorptionCriterion_338:
  CONDITIONAL, not proved here.

CurrentLowEnvelopeMassClosure_342:
  FALSE / BLOCKED.

MassOnlyCoverRouteClosure_342:
  FALSE / BLOCKED.

InternalZeroKernelAudit_343(P_minor^0):
  OPEN next target.
```

The useful extraction is an exact functional and a trivial ceiling. The
ceiling is not small enough, by itself, to prove the absorption row.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module defines and tests a prototype row. It does not prove
`LowEnvelopeMassRows_338`, `UniformLowMassAbsorptionCriterion_338`,
`KernelWeightedDivisorWindowCriterion_337`, `KernelWeightedMobiusMomentCriterion_330`,
`SharpCoverSmallness_328`, `SignedLocalModelInsertion_326`,
`PhaseKernelBound_273^0`, any residual cube endpoint, any selector transfer,
or any statement about the original selected-average problem.

## 3. Definitions and variables

Work in the same local family as Modules 337-340:

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

Let `U,V` be the same admissible threshold-localized shell masks used in the
minor-kernel row, and set:

```text
KAbs_{U,V}^0(d_1,d_2;t)
  =
  |K_{U,V}^0(d_1,d_2;t)|.
```

For a finite cutoff `Y>w`, inherit the positive low-prime envelope from
Module 338:

```text
LowEnv_Y^{342}(z)
  =
  1+
  sum_{F low full cover, maxp(F)<=Y}
    1_{E(F;z)} Weight(F).
```

Here `E(F;z)` and `Weight(F)` are the finite cover events and Mobius-degree
weights of Modules 328-330. The word `low` means all primes in `F` are at
most `Y`; it does not mean the envelope is small.

Define the absolute kernel mass:

```text
KMass_{U,V}^{342}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k).
```

Define the low-envelope mass functional:

```text
LMass_Y^{342}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{342}(z).
```

The absorption row asked for by Module 338 is:

```text
lim_{w -> infinity} limsup_{N -> infinity}
  (log N)/(Y(N,w) log Y(N,w))
  LMass_{Y(N,w)}^{342}(U,V)
  =
  0
```

for every admissible `U,V`, with the cutoff `Y(N,w)` compatible with the
finite-side CRT/mask range and the declared limiting order.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-340,
the finite cover definitions from Modules 328-330,
the low-prime envelope definition from Module 338,
and positivity of the absolute kernel and envelope.
```

It does not assume:

```text
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
WeightedLowHighCouplingRows_338,
HighDivisorMomentRows_338,
UniformLowMassAbsorptionCriterion_338 as a proved estimate,
CauchyCouplingCriterion_338 as a proved estimate,
DivisorDecorrelCriterion_338 as a proved estimate,
KernelWeightedDivisorWindowCriterion_337 as a proved estimate,
WeightedDivisorWindowRows_337,
LowEnvelopeMassRows_337,
ExactZeroTailDiagonalRows_337,
TailUniformityRows_336,
LowHighCoverCouplingRows_336,
CutoffWindowCriterion_336 as a proved estimate,
FinitePrimeTailRows_330,
MultiPrimeCoverMomentRows_330,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
WeightedCRTMaskCriterion_335 as a proved estimate,
MaskCRTUniformityRows_335,
KernelCRTUniformityRows_335,
CompositeModulusRangeCriterion_335 as a proved estimate,
ExactWeightedPartitionRows_334,
CoarseningWeightedUniformityRows_334,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
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

### A. Exact functional

The definition of `LowEnv_Y^{342}` is positive term-by-term. Therefore
`LMass_Y^{342}(U,V)` is the exact absolute-kernel first moment of the
low-prime cover envelope in the same family used by Module 338.

Classification:

```text
LowEnvelopeMassFunctional_342:
  STRUCTURAL / EXTRACTION.
```

This is not yet an estimate. It is the target whose smallness would have to
be proved.

### B. Trivial total-weight ceiling

Define the unconditioned finite low-cover weight:

```text
A_low^{342}(Y)
  =
  1+
  sum_{F low full cover, maxp(F)<=Y}
    Weight(F),
```

where the sum is over the same declared finite-cutoff cover family used in
`LowEnv_Y^{342}`.

Since `0<=1_{E(F;z)}<=1`, pointwise:

```text
LowEnv_Y^{342}(z)
  <=
  A_low^{342}(Y).
```

Thus:

```text
LMass_Y^{342}(U,V)
  <=
  A_low^{342}(Y) KMass_{U,V}^{342}.
```

Classification:

```text
TrivialLowEnvelopeMassCeiling_342:
  STRUCTURAL / EXTRACTION.
```

This ceiling is valid but loses every finite-side event restriction. It does
not use CRT structure, mask distribution, dyadic ranges, or kernel residue
uniformity. It is therefore a ceiling, not a low-envelope mass theorem.

### C. Conditional absorption implication

The Module 338 absorption route would follow from the displayed mass row if
one can choose a cutoff `Y=Y(N,w)` such that:

```text
(log N)/(Y log Y)
  LMass_Y^{342}(U,V)
  =
  o_W(1)
```

uniformly for all admissible `U,V`, with the same finite-side and limiting
conventions.

Using the trivial ceiling, a sufficient but not proved condition is:

```text
(log N)/(Y log Y)
  A_low^{342}(Y) KMass_{U,V}^{342}
  =
  o_W(1).
```

Classification:

```text
LowEnvelopeAbsorptionImplication_342:
  CONDITIONAL.
```

This implication is not a proof of `UniformLowMassAbsorptionCriterion_338`,
because the current ledger supplies neither a small enough same-family
absolute kernel mass nor a cutoff range controlling the low-cover total
weight while preserving finite-side CRT/mask estimates.

### D. Why current inputs do not close the row

Current inputs fail to prove the mass row for five separate reasons.

First, the total-weight ceiling discards the event structure:

```text
1_{E(F;z)}.
```

Using only `A_low^{342}(Y)` replaces a kernel-weighted finite-side counting
problem by an unconditioned sum over all cover families. That is generally
too crude for a growing cutoff.

Second, retaining the event structure would require the same finite-side rows
that remain open:

```text
PartitionClassCountingRows_330,
KernelWeightedPartitionClassCounting_331,
AbsoluteMinorKernelResidueUniformity_332,
WeightedDyadicProjectionRow_333,
CoarseningWeightedUniformityRows_334,
WeightedCRTMaskCriterion_335.
```

Third, the cutoff has incompatible pressures:

```text
large Y helps (log N)/(Y log Y),
large Y enlarges the finite-side cover family and product moduli.
```

No current module proves a window where both demands hold.

Fourth, `KMass_{U,V}^{342}` is an absolute localized minor-kernel mass. The
project has many identities and ceilings for related weighted pair and
anti-diagonal kernels, but no same-family estimate making this absolute mass
harmless after multiplication by `A_low^{342}(Y)`.

Fifth, even a proved first moment for `LowEnv_Y` would not handle:

```text
LowEnvelopeSecondMomentRows_338,
HighDivisorMomentRows_338,
DivisorDecorrelCriterion_338,
ExactZeroWeightedRows_339,
SignedLocalModelInsertion_326.
```

Therefore:

```text
CurrentLowEnvelopeMassClosure_342:
  FALSE / BLOCKED.

LowEnvelopeMassRows_338:
  OPEN.
```

### E. Mass-only cover-route shortcut is blocked

The tempting shortcut is:

```text
control the low-envelope mass,
therefore the cover route is closed.
```

This is invalid. The cover route also needs finite-side CRT/mask uniformity,
cutoff removal, high-prime divisor control under the same weights, exact-zero
tail absorption, and signed/local-model insertion.

Hence:

```text
MassOnlyCoverRouteClosure_342:
  FALSE / BLOCKED.
```

The module is still useful because it identifies the first moment one would
need before trying a Cauchy second-moment or decorrelation route.

## 6. Edge cases and exclusions

### Empty or small cover families

The constant term `1` in `LowEnv_Y^{342}` is included. It measures the bare
absolute-kernel mass. Even if all cover events vanished, the absorption row
would still require:

```text
(log N)/(Y log Y) KMass_{U,V}^{342}=o_W(1)
```

in the same cutoff window.

### Repeated primes and coarsenings

Repeated-prime consolidation and exact partition coarsening are not bypassed
by `LMass_Y^{342}`. They are exactly the finite-side structure one would need
to exploit to improve on the trivial total-weight ceiling.

### Exact-zero diagonals

This module does not treat exact lifted zero differences. The low-envelope
mass is present on those tuples too, but Module 339 showed that nonzero
high-prime divisor ceilings do not apply there.

### Cutoff order

The target must use the declared order:

```text
N -> infinity first inside fixed w and chosen cutoff convention,
then w -> infinity,
```

unless a later module explicitly proves a different uniform limiting theorem.

### Selector and gap object

This module lives inside the local finite model `P_minor^0`. It does not
transfer to the actual sharp moving selector and says nothing about the full
gap average `A_alpha(x)`.

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
  -> LowEnvelopeMassPrototype_342.
```

The module tests one narrow first-moment input after the cover-route verdict.
It is not a new endpoint equivalence and not a proof of the cover route.

## 8. What remains open

Still open:

```text
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
WeightedLowHighCouplingRows_338,
HighDivisorMomentRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
UniformLowMassAbsorptionCriterion_338 as an estimate,
CauchyCouplingCriterion_338 as an estimate,
DivisorDecorrelCriterion_338 as an estimate,
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
InternalZeroKernelAudit_343(P_minor^0).
```

The reason is that Module 342 did not supply a low-envelope mass closure, and
Module 339 left exact-zero kernel rows as the other concrete obstruction in
the tail route.

## Red flags / forbidden upgrades

Do not cite `LowEnvelopeMassPrototype_342` as proving `LowEnvelopeMassRows_338`.
It defines the mass row and proves only a trivial total-weight ceiling.

Do not cite the trivial ceiling as a cutoff theorem. It does not prove a
compatible `Y(N,w)` window.

Do not treat low-prime and high-prime factors as independent. Module 338
already blocks that shortcut.

Do not use `KernelWeightedMobiusMomentCriterion_330`,
`SharpCoverSmallness_328`, `SignedLocalModelInsertion_326`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as an assumption in this row.

Do not transfer this local model statement to the actual sharp moving
selector or to the original selected-average problem.
