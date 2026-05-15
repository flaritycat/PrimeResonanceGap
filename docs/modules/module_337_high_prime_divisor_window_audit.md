# Module 337: High-prime divisor window audit

## 1. Precise theorem / claim being advanced

Module 336 isolated the finite-prime tail obstruction and recorded a
tuple-level divisor ceiling for nonzero lifted differences. This module tests
whether that ceiling can be promoted into the weighted tail row needed by the
cover-moment route.

Define:

```text
HighPrimeDivisorWindowAudit_337(P_minor^0).
```

Verdict:

```text
HighPrimeDivisorWindowAudit_337(P_minor^0):
  STRUCTURAL / EXTRACTION.

NonzeroHighPrimeExponentialEnvelope_337:
  STRUCTURAL / EXTRACTION.

LiftSizeWindowBound_337:
  STRUCTURAL / EXTRACTION.

KernelWeightedDivisorWindowCriterion_337:
  CONDITIONAL.

CutoffCompatibilityWindow_337:
  CONDITIONAL.

WeightedDivisorWindowRows_337:
  OPEN.

LowEnvelopeMassRows_337:
  OPEN.

ExactZeroTailDiagonalRows_337:
  OPEN.

DivisorWindowOnlyClosure_337:
  FALSE / BLOCKED.

CurrentHighPrimeDivisorClosure_337:
  FALSE / BLOCKED.

PlanChallenge_10_337:
  STRUCTURAL / EXTRACTION.

LowHighTailCouplingAudit_338(P_minor^0):
  OPEN next target.
```

The useful extraction is that, away from exact-zero diagonals, the high-prime
part of a positive cover envelope can be bounded by an exponential in the
high-prime divisor load. This does not prove the weighted tail row, because
the same absolute kernel, masks, low-prime envelope, dyadic ranges, and cutoff
window remain in the average.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The envelope and lift-size bound are structural. The weighted divisor-window
criterion and cutoff window remain conditional or open.

This module proves no `TailUniformityRows_336`, no
`LowHighCoverCouplingRows_336`, no `FinitePrimeTailRows_330`, no
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

Use the Module 323-324 eight slots:

```text
Lambda_8={1,...,8},
L_1=x+d_1, L_2=x, L_3=x+h+d_1, L_4=x+h,
L_5=y+d_2, L_6=y, L_7=y+k+d_2, L_8=y+k,
Delta_{ij}=L_i-L_j.
```

Let:

```text
z=(x,y,h,k,d_1,d_2).
```

Choose a declared integer lift of the cyclic variables, for example least
absolute representatives, and write:

```text
tilde Delta_{ij}(z)
```

for the corresponding lifted slot difference. Define the exact-zero set for
the chosen lift:

```text
Z_0^{337}
  =
  { z : tilde Delta_{ij}(z)=0 for at least one i<j }.
```

Define the nonzero high-prime divisor load:

```text
DivTail_Y^{337}(z)
  =
  sum_{1<=i<j<=8}
    sum_{p>Y, p | tilde Delta_{ij}(z),
              tilde Delta_{ij}(z) != 0}
      1/p.
```

Let `LowEnv_Y^{337}(z)` be the positive low-prime cover envelope:

```text
LowEnv_Y^{337}(z)
  =
  1 +
  sum_{F full cover, maxp(F)<=Y}
    1_{E(F;z)} Weight(F),
```

with `E(F;z)` and `Weight(F)` inherited from Module 330.

For a threshold-localized mask pair `U,V`, define:

```text
KAbs_{U,V}^0(d_1,d_2;t)
  =
  |K_{U,V}^0(d_1,d_2;t)|.
```

The weighted divisor-window quantity is:

```text
HDiv_Y^{337}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_Y^{337}(z)
      (exp(C_8 DivTail_Y^{337}(z))-1)
      1_{z notin Z_0^{337}}.
```

Here `C_8` is an absolute constant large enough to absorb the eight-slot
prime-local Mobius envelope constants.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-336,
the Module 329 pointwise prime-local Mobius-degree bound,
the Module 336 nonzero divisor ceiling,
and finite product algebra.
```

It does not assume:

```text
WeightedDivisorWindowRows_337,
LowEnvelopeMassRows_337,
ExactZeroTailDiagonalRows_337,
KernelWeightedDivisorWindowCriterion_337 as a proved estimate,
CutoffCompatibilityWindow_337 as a proved estimate,
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

### A. Nonzero high-prime exponential envelope

For a fixed high prime `p>Y` and a nonempty set `T subset Lambda_8`, the
Module 329 pointwise bound gives:

```text
mu_p(T) <= C_8 p^(-a_p(T)).
```

If `mu_p(T) != 0`, then at least two labels of `T` collide modulo `p`.
Away from exact-zero lifted differences, this implies that for some
`i<j in T`,

```text
p | tilde Delta_{ij}(z),  tilde Delta_{ij}(z) != 0.
```

Thus one high-prime local factor is bounded by:

```text
sum_{empty != T subset Lambda_8}
  1_{E_p(T;z)} mu_p(T)
  <=
  C_8 sum_{i<j}
        1_{p | tilde Delta_{ij}(z),
          tilde Delta_{ij}(z) != 0} / p.
```

Multiplying over all high primes and expanding the positive envelope gives:

```text
HighEnv_{Y,Z}^{337}(z)
  <=
  exp(C_8 DivTail_Y^{337}(z))-1
```

for the part with at least one prime in `(Y,Z]`, after excluding
`Z_0^{337}`.

Classification:

```text
NonzeroHighPrimeExponentialEnvelope_337:
  STRUCTURAL / EXTRACTION.
```

This is an envelope. It is not a weighted estimate and it does not handle
exact-zero diagonal tuples.

### B. Lift-size window bound

If the chosen representatives give:

```text
M_{337}(z)
  =
  2+max_{i<j} |tilde Delta_{ij}(z)|,
```

then Module 336 gives:

```text
DivTail_Y^{337}(z)
  <=
  C_8 log M_{337}(z)/(Y log Y).
```

For the standard representatives of the cyclic variables, the affine slot
forms have:

```text
M_{337}(z) <= C N
```

inside the local model, up to the declared lift/wrap convention. Therefore,
on nonzero lifted differences,

```text
DivTail_Y^{337}(z)
  <=
  C_8 log N/(Y log Y).
```

Classification:

```text
LiftSizeWindowBound_337:
  STRUCTURAL / EXTRACTION.
```

This is only a pointwise window bound. It depends on the chosen lift and does
not turn cyclic congruence bookkeeping into an interval theorem.

### C. Kernel-weighted divisor-window criterion

A sufficient same-family row for the nonzero high-prime part is:

```text
KernelWeightedDivisorWindowCriterion_337:

For every admissible threshold-localized U,V, choose Y=Y(N,w) so that

lim_{w -> infinity} limsup_{N -> infinity}
  HDiv_{Y(N,w)}^{337}(U,V)
  =
  0.
```

Equivalently, after using the pointwise lift-size bound, it would be enough
to prove a low-envelope mass row strong enough that:

```text
lim_{w -> infinity} limsup_{N -> infinity}
  (log N)/(Y(N,w) log Y(N,w))
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      KAbs_{U,V}^0(d_1,d_2;h+k)
      LowEnv_{Y(N,w)}^{337}(z)
  =
  0.
```

Classification:

```text
KernelWeightedDivisorWindowCriterion_337:
  CONDITIONAL.

WeightedDivisorWindowRows_337:
  OPEN.

LowEnvelopeMassRows_337:
  OPEN.
```

The criterion is not proved. The current ledger has no bound for the absolute
kernel weighted by the low-prime cover envelope over a growing cutoff.

### D. Cutoff compatibility window

The divisor tail prefers a large cutoff:

```text
Y(N,w) log Y(N,w) >> log N
```

after accounting for the low-envelope mass scale.

The finite CRT/mask side from Module 335 prefers a cutoff small enough that
the product moduli of the low-prime cover families remain inside the available
dyadic and kernel-uniformity ranges, schematically:

```text
Q(F)/D -> 0
```

or an explicitly proved weighted summability substitute.

Thus an admissible cutoff window must satisfy both:

```text
tail side:        high-prime divisor load is negligible,
finite side:      low-prime CRT/mask products remain controllable.
```

Classification:

```text
CutoffCompatibilityWindow_337:
  CONDITIONAL.
```

No such window is proved here. In particular, choosing `Y` large enough to
make the divisor ceiling small may destroy the finite-side CRT/mask range.

### E. Exact-zero obstruction

If:

```text
tilde Delta_{ij}(z)=0,
```

then every prime divides that lifted difference. The nonzero divisor load and
the exponential envelope above deliberately exclude this case.

The exact-zero tuples include the internal diagonals from Module 324:

```text
h=0, h=d_1, h=-d_1,
k=0, k=d_2, k=-d_2,
```

and the sixteen cross-block affine diagonals:

```text
x-y=-a d_1-b h+c d_2+e k.
```

Classification:

```text
ExactZeroTailDiagonalRows_337:
  OPEN.
```

These rows must be controlled by structural diagonal/collision estimates in
the same weighted average. The high-prime divisor window gives no help on
exact-zero differences.

### F. Current closure verdict

The current ledger now has:

```text
a nonzero high-prime exponential envelope,
a pointwise lift-size divisor window,
and a conditional weighted divisor-window criterion.
```

It does not have:

```text
weighted divisor-window estimates,
low-envelope absolute kernel mass,
exact-zero diagonal control,
or a cutoff window compatible with both tail and finite CRT/mask constraints.
```

Therefore:

```text
DivisorWindowOnlyClosure_337:
  FALSE / BLOCKED.

CurrentHighPrimeDivisorClosure_337:
  FALSE / BLOCKED.
```

The next target should not be a broad cover-moment route verdict yet. The
next smaller obstruction is the low-high product itself: can the low-prime
cover envelope be multiplied by the high-prime divisor load under the same
absolute kernel without reproducing the endpoint row?

### G. Plan challenge 10

The Module 336 ledger recorded count `155`. Completing Module 337 adds one
substantive solving iteration:

```text
Post-Reflective_1 solving count: 156.
Long-term-plan count: 150.
```

Since `150` is divisible by `15`, the tenth plan challenge is due.

Challenge result:

```text
PlanChallenge_10_337:
  STRUCTURAL / EXTRACTION.
```

The earlier plan expected a quick move toward signed local-model insertion or
a cover-moment route verdict after Module 337. Modules 335-337 show that this
is premature: finite-side CRT/mask control, high-prime divisor tails,
low-high coupling, and exact-zero diagonal rows are still separate open
objects. The plan is therefore questioned and narrowed.

Revised next window:

```text
Module 338:
  LowHighTailCouplingAudit_338(P_minor^0).

Module 339:
  ExactZeroTailDiagonalAudit_339(P_minor^0).

Module 340:
  CoverMomentRouteVerdict_340(P_minor^0), only if Modules 338-339 do not
  expose a sharper blocker.

Module 341:
  next reflective log boundary, if the cadence remains one module per
  solving iteration.
```

No theorem status is upgraded by this challenge.

## 6. Edge cases and exclusions

- The high-prime exponential envelope excludes exact-zero lifted differences.
- A cyclic zero and an integer lifted zero must not be interchanged without a
  declared lift/wrap convention.
- The pointwise bound `DivTail_Y <= C log N/(Y log Y)` is not a weighted row.
- The low-prime envelope may concentrate exactly where the high-prime load is
  large.
- The absolute kernel may concentrate on the same rows or `t=h+k` fibers.
- Increasing `Y` helps the high-prime divisor ceiling but worsens the
  finite-side CRT/mask product range.
- Products over high primes are controlled only as a positive envelope; this
  does not recover signed cancellation.
- Exact-zero structural diagonals survive every high-prime cutoff.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- A divisor-window envelope is not an analytic proof.

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
  -> LowHighTailCouplingAudit_338.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. LowHighTailCouplingAudit_338(P_minor^0):
     decide whether LowEnv_Y^{337} times the high-prime divisor envelope can
     be controlled under the same absolute kernel and masks.

2. ExactZeroTailDiagonalAudit_339(P_minor^0):
     classify exact lifted zero differences in the high-prime tail row and
     determine whether existing structural diagonal rows actually bound them.

3. CutoffCompatibilityWindow_337:
     find or reject a cutoff Y(N,w) compatible with both finite CRT/mask rows
     and high-prime divisor-tail rows.

4. WeightedDivisorWindowRows_337:
     prove or reject the kernel-weighted exponential divisor window.

5. FinitePrimeTailRows_330:
     prove or reject tail control above the cutoff in the Module 330 cover
     moment.
```

The current cadence after completing this module is:

```text
Latest completed module: 337
Post-Reflective_1 solving count: 156
Long-term-plan count: 150

150 is not divisible by 9, so no plan update is due in this module.
150 is divisible by 15, so PlanChallenge_10_337 is due and completed here.
Next reflective log remains expected around Module 341.
```

## 9. Forbidden upgrades

This module does not prove:

```text
WeightedDivisorWindowRows_337,
LowEnvelopeMassRows_337,
ExactZeroTailDiagonalRows_337,
KernelWeightedDivisorWindowCriterion_337 as an estimate,
CutoffCompatibilityWindow_337 as an estimate,
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

Do not cite `NonzeroHighPrimeExponentialEnvelope_337` or
`LiftSizeWindowBound_337` as a weighted finite-prime tail theorem.
