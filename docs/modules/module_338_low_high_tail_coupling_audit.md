# Module 338: Low-high tail coupling audit

## 1. Precise theorem / claim being advanced

Module 336 showed that cutoff removal is not a standalone high-prime tail
problem:

```text
Def_Z-Def_Y=(1+Def_Y)Def_{Y,Z}.
```

Module 337 then bounded the nonzero high-prime part by an exponential in the
high-prime divisor load. This module audits the product that remains:

```text
low-prime cover envelope times high-prime divisor envelope
```

under the same absolute kernel, masks, dyadic ranges, W-residue conventions,
and cutoff order.

Define:

```text
LowHighTailCouplingAudit_338(P_minor^0).
```

Verdict:

```text
LowHighTailCouplingAudit_338(P_minor^0):
  STRUCTURAL / EXTRACTION.

CutoffProductFactorization_338:
  STRUCTURAL / EXTRACTION.

PositiveLowHighEnvelope_338:
  STRUCTURAL / EXTRACTION.

UniformLowMassAbsorptionCriterion_338:
  CONDITIONAL.

CauchyCouplingCriterion_338:
  CONDITIONAL.

DivisorDecorrelCriterion_338:
  CONDITIONAL.

WeightedLowHighCouplingRows_338:
  OPEN.

LowEnvelopeMassRows_338:
  OPEN.

LowEnvelopeSecondMomentRows_338:
  OPEN.

HighDivisorMomentRows_338:
  OPEN.

ExactZeroTailDiagonalAudit_339(P_minor^0):
  OPEN next target.

LowHighIndependenceShortcut_338:
  FALSE / BLOCKED.

CurrentLowHighTailClosure_338:
  FALSE / BLOCKED.
```

The module records the exact positive envelope for the low-high product and
three possible conditional routes. None of these routes is proved by current
ledger inputs.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The factorization and positive envelope are structural. All analytic rows
that would make the low-high product small remain open or conditional.

This module proves no `TailUniformityRows_336`, no
`KernelWeightedDivisorWindowCriterion_337`, no `FinitePrimeTailRows_330`, no
`KernelWeightedMobiusMomentCriterion_330`, no `PhaseKernelBound_273^0`, no
residual cube endpoint, no selector transfer, and no statement about the
original selected-average problem.

## 3. Definitions and variables

Work in:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Use the eight-slot variables:

```text
z=(x,y,h,k,d_1,d_2),
t=h+k,
Lambda_8={1,...,8},
Delta_{ij}=L_i-L_j.
```

Let `U,V` be an admissible threshold-localized mask pair and write:

```text
KAbs_{U,V}^0(d_1,d_2;t)
  =
  |K_{U,V}^0(d_1,d_2;t)|.
```

Let the positive low-prime cover envelope be:

```text
LowEnv_Y^{338}(z)
  =
  1+
  sum_{F low full cover, maxp(F)<=Y}
    1_{E(F;z)} Weight(F).
```

Let the nonzero high-prime divisor envelope from Module 337 be:

```text
HighEnv_Y^{338}(z)
  =
  (exp(C_8 DivTail_Y^{337}(z))-1) 1_{z notin Z_0^{337}}.
```

Define the coupled low-high tail functional:

```text
LH_{Y}^{338}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{338}(z)
      HighEnv_Y^{338}(z).
```

The target row would be:

```text
lim_{w -> infinity} limsup_{N -> infinity}
  LH_{Y(N,w)}^{338}(U,V)
  =
  0
```

for every admissible `U,V`, with `Y(N,w)` compatible with the finite-side
CRT/mask range.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-337,
the finite cutoff factorization,
the Module 337 nonzero high-prime exponential envelope,
and positive-envelope algebra.
```

It does not assume:

```text
WeightedLowHighCouplingRows_338,
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
HighDivisorMomentRows_338,
ExactZeroTailDiagonalAudit_339,
KernelWeightedDivisorWindowCriterion_337 as a proved estimate,
CutoffCompatibilityWindow_337 as a proved estimate,
WeightedDivisorWindowRows_337,
LowEnvelopeMassRows_337,
ExactZeroTailDiagonalRows_337,
TailUniformityRows_336,
LowHighCoverCouplingRows_336,
CutoffWindowCriterion_336 as a proved estimate,
FinitePrimeTailRows_330,
MultiPrimeCoverMomentRows_330,
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
MaskResidueUniformity_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
PrimeMobiusSmallness_329,
KernelWeightedMobiusCoverRows_329,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as a proved estimate,
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
ResidualEightSlotMinorCancellation_319,
AdmissiblePhiGain_320,
FiberOverlapGainTarget_321,
SignedMinorKernelGain_318,
AntiDiagonalTwoShiftKernelGain_312,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
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

### A. Cutoff product factorization

For `w<Y<Z`, Module 336 gives:

```text
Def_Z(S)-Def_Y(S)
  =
  (1+Def_Y(S))Def_{Y,Z}(S).
```

After taking the top cover coefficient and applying the positive Mobius-cover
envelope, every term in the cutoff difference has:

```text
at least one high prime p>Y,
and an arbitrary finite low-prime factor from primes <=Y.
```

Thus cutoff removal is not a pure tail estimate. It is a low-high product
estimate.

Classification:

```text
CutoffProductFactorization_338:
  STRUCTURAL / EXTRACTION.
```

This is finite algebra only.

### B. Positive low-high envelope

On the nonzero lifted-difference complement `z notin Z_0^{337}`, Module 337
gives:

```text
HighEnv_{Y,Z}^{337}(z)
  <=
  exp(C_8 DivTail_Y^{337}(z))-1.
```

Therefore the nonzero part of the cutoff-difference contribution is bounded
by:

```text
LH_Y^{338}(U,V).
```

Classification:

```text
PositiveLowHighEnvelope_338:
  STRUCTURAL / EXTRACTION.
```

This is an upper envelope for the nonzero high-prime part. It is not an
estimate for the weighted row.

### C. Uniform low-mass absorption route

Using Module 337's pointwise window:

```text
DivTail_Y^{337}(z)
  <=
  C_8 log N/(Y log Y)
```

on nonzero lifted differences, a sufficient route is:

```text
UniformLowMassAbsorptionCriterion_338:

Choose Y=Y(N,w) so that

lim_{w -> infinity} limsup_{N -> infinity}
  (log N)/(Y log Y)
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{338}(z)
  =
  0.
```

Classification:

```text
UniformLowMassAbsorptionCriterion_338:
  CONDITIONAL.

LowEnvelopeMassRows_338:
  OPEN.
```

The obstruction is that the low-prime envelope mass is itself a growing
finite-side cover object. Current finite-side rows do not bound it under the
same absolute kernel and masks.

### D. Cauchy coupling route

A second possible route is Cauchy-Schwarz in the weighted average:

```text
LH_Y^{338}(U,V)
  <=
  Low2_Y^{338}(U,V)^(1/2)
  High2_Y^{338}(U,V)^(1/2),
```

where:

```text
Low2_Y^{338}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{338}(z)^2,

High2_Y^{338}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      HighEnv_Y^{338}(z)^2.
```

Classification:

```text
CauchyCouplingCriterion_338:
  CONDITIONAL.

LowEnvelopeSecondMomentRows_338:
  OPEN.

HighDivisorMomentRows_338:
  OPEN.
```

This route is currently unavailable. Squaring `LowEnv_Y` introduces pairs of
low-prime cover families and therefore stronger finite-side CRT/mask rows,
not weaker ones.

### E. Decorrelation route

A third possible route would prove that, after conditioning on the low-prime
cover envelope and masks, the high-prime divisor load still has its expected
smallness:

```text
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k}
    KAbs_{U,V}^0(d_1,d_2;h+k)
    LowEnv_Y^{338}(z)
    DivTail_Y^{337}(z)

  <=
  small(Y,N,w)
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{338}(z),
```

with a summable error after the cutoff is chosen.

Classification:

```text
DivisorDecorrelCriterion_338:
  CONDITIONAL.

WeightedLowHighCouplingRows_338:
  OPEN.
```

No such decorrelation row exists in the current ledger. It would need to be
proved in the same localized family, not inferred from pointwise divisor
counting.

### F. Independence shortcut is blocked

The tempting shortcut is:

```text
low-prime cover rows are finite-side,
high-prime divisor tails are pointwise small,
therefore their product is small.
```

This is invalid because:

```text
LowEnv_Y^{338}, HighEnv_Y^{338}, KAbs_{U,V}^0, U, V, d_1, d_2, and t=h+k
are all evaluated on the same tuple z.
```

The low-prime envelope may concentrate exactly on tuples where the high-prime
load is large, and the absolute kernel may further amplify those tuples.

Classification:

```text
LowHighIndependenceShortcut_338:
  FALSE / BLOCKED.
```

### G. Current closure verdict

The current ledger now has:

```text
the exact cutoff product factorization,
a positive low-high envelope,
and three conditional analytic routes.
```

It does not have:

```text
low-envelope mass bounds,
low-envelope second moments,
high-divisor second moments,
divisor decorrelation after low-prime conditioning,
exact-zero diagonal control,
or a compatible cutoff window.
```

Therefore:

```text
CurrentLowHighTailClosure_338:
  FALSE / BLOCKED.
```

The next target remains the exact-zero tail diagonal audit. Even a successful
nonzero low-high row would still miss tuples with exact lifted differences
`tilde Delta_{ij}=0`.

## 6. Edge cases and exclusions

- The low-high envelope controls only the nonzero high-prime part; exact-zero
  lifted differences are excluded and remain open.
- `LowEnv_Y` is positive and growing with the cutoff; it is not a bounded
  harmless multiplier.
- Cauchy-Schwarz creates second moments of the low-prime cover envelope,
  which require stronger multi-prime CRT/mask rows.
- Decorrelation between low and high primes is not supplied by CRT alone,
  because the kernel and masks are shared.
- Choosing `Y` to help the high tail may worsen finite-side product moduli.
- Absolute values remove signed cancellation between low and high factors.
- Pointwise divisor bounds are not weighted estimates.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- A product envelope is not an analytic proof.

## 7. Project-map location

This module lies on the Phase K minor-arc branch:

```text
WeightedPairAutocorrelationExpansion_312
  -> MinorKernelRowSplit_314
  -> SignedMinorKernelCombinationVerdict_318
  -> AntiDiagonalNewInputInventory_319
  -> SizeSensitiveMinorKernelCriterion_320
  -> DataDependentFiberGainAudit_321
  -> PlanUpdate_15_Challenge_9_322
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
  -> ExactZeroTailDiagonalAudit_339.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. ExactZeroTailDiagonalAudit_339(P_minor^0):
     classify exact lifted zero differences in the high-prime tail row and
     decide whether current structural diagonal rows actually bound them.

2. LowEnvelopeMassRows_338:
     prove or reject absolute-kernel mass bounds for LowEnv_Y under the same
     masks and cutoff.

3. LowEnvelopeSecondMomentRows_338:
     prove or reject the squared low-envelope row required by the Cauchy
     route.

4. DivisorDecorrelCriterion_338:
     prove or reject high-prime divisor decorrelation after conditioning on
     the low-prime cover envelope.

5. CutoffCompatibilityWindow_337:
     find or reject a cutoff Y(N,w) compatible with finite CRT/mask rows and
     high-prime tail rows.
```

The current cadence after completing this module is:

```text
Latest completed module: 338
Post-Reflective_1 solving count: 157
Long-term-plan count: 151

151 is not divisible by 9, so no plan update is due in this module.
151 is not divisible by 15, so no plan challenge is due in this module.
Next reflective log remains expected around Module 341.
```

## 9. Forbidden upgrades

This module does not prove:

```text
WeightedLowHighCouplingRows_338,
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
HighDivisorMomentRows_338,
UniformLowMassAbsorptionCriterion_338 as an estimate,
CauchyCouplingCriterion_338 as an estimate,
DivisorDecorrelCriterion_338 as an estimate,
ExactZeroTailDiagonalAudit_339,
KernelWeightedDivisorWindowCriterion_337 as an estimate,
CutoffCompatibilityWindow_337 as an estimate,
WeightedDivisorWindowRows_337,
LowEnvelopeMassRows_337,
ExactZeroTailDiagonalRows_337,
TailUniformityRows_336,
LowHighCoverCouplingRows_336,
CutoffWindowCriterion_336 as an estimate,
FinitePrimeTailRows_330,
MultiPrimeCoverMomentRows_330,
WeightedCRTMaskCriterion_335 as an estimate,
MaskCRTUniformityRows_335,
KernelCRTUniformityRows_335,
CompositeModulusRangeCriterion_335 as an estimate,
ExactWeightedPartitionRows_334,
CoarseningWeightedUniformityRows_334,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
KernelResidueMassCriterion_332 as an estimate,
AbsoluteMinorKernelResidueUniformity_332,
KernelWeightedPartitionClassCounting_331,
MaskResidueUniformity_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
KernelWeightedMobiusMomentCriterion_330 as an estimate,
PrimeMobiusSmallness_329,
KernelWeightedMobiusCoverRows_329,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as an estimate,
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
ResidualEightSlotMinorCancellation_319,
AdmissiblePhiGain_320,
FiberOverlapGainTarget_321,
SignedMinorKernelGain_318,
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

Do not cite `PositiveLowHighEnvelope_338` as a finite-prime tail theorem. It
is only a positive envelope for the coupled product.
