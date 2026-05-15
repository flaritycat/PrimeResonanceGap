# Module 345: Phase K post-cover branch decision

## 1. Precise theorem / claim being advanced

Modules 342-344 tested the narrow post-verdict rows selected after the
cover-moment route verdict:

```text
low-prime envelope mass,
internal exact-zero kernel rows,
cross exact-zero kernel rows.
```

Each test produced an exact functional and a useful obstruction, but no
weighted closure. This module decides what the project should do next:

```text
PhaseKPostCoverBranchDecision_345(P_minor^0).
```

Verdict:

```text
PhaseKPostCoverBranchDecision_345(P_minor^0):
  STRUCTURAL / EXTRACTION.

PostCoverInputInventory_345:
  STRUCTURAL / EXTRACTION.

AbsoluteCoverContinuationAsNextMove_345:
  FALSE / BLOCKED.

UnqualifiedSignedInsertionClosure_345:
  FALSE / BLOCKED.

CoverRoutePause_345:
  STRUCTURAL / EXTRACTION.

SignedLocalModelInsertionFeasibility_346(P_minor^0):
  OPEN next target.
```

The decision is:

```text
Pause the absolute cover-moment route as the primary next closure route.
Do not claim signed insertion closes anything.
Next test the signed local-model insertion row itself.
```

This is a steering result, not an analytic estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no `SignedLocalModelInsertion_326`, no
`LocalModelInsertion_325`, no `KernelWeightedMobiusMomentCriterion_330`, no
`WeightedCRTMaskCriterion_335`, no `KernelWeightedDivisorWindowCriterion_337`,
no `LowEnvelopeMassRows_338`, no `ExactZeroWeightedRows_339`, no
`PhaseKernelBound_273^0`, no residual cube endpoint, no selector transfer,
and no statement about the original selected-average problem.

The words "pause" and "select" are project-map instructions. They do not mean
that the paused route is mathematically impossible.

## 3. Definitions and variables

Work inside the same local family:

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

Recall from Module 323:

```text
f_0(n)=nu_0(n)-1,

F_8(d_1,d_2;x,y,h,k)
  =
  f_0(L_1)conj(f_0(L_2))
  conj(f_0(L_3))f_0(L_4)
  f_0(L_5)conj(f_0(L_6))
  conj(f_0(L_7))f_0(L_8).
```

For threshold-localized masks `U,V`, keep the same localized minor kernel:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t).
```

The exact physical signed row is:

```text
WOff_{U,V}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      F_8(d_1,d_2;x,y,h,k)
      K_{U,V}^0(d_1,d_2;h+k).
```

For `S subset {1,...,8}`, recall the local model factor:

```text
Theta_{w,S}^{8,min}(z)
  =
  prod_{p>w}
    (1-1/p)^(-|S|)
    (1-r_p(S;z)/p),
```

where `r_p(S;z)` counts distinct residues occupied by `{L_i(z): i in S}`
modulo `p`. The signed residual local factor is:

```text
Omega_{w,8}^{minor}(z)
  =
  sum_{S subset {1,...,8}}
    (-1)^(8-|S|) Theta_{w,S}^{8,min}(z).
```

The model-side signed minor row is:

```text
ModelSignedMinor_{U,V}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      Omega_{w,8}^{minor}(z).
```

The signed local-model insertion error is the formal target:

```text
SLMIError_{U,V}^{345}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      (F_8(d_1,d_2;x,y,h,k)-Omega_{w,8}^{minor}(z)).
```

A future insertion theorem would have to prove, in the same family and with
the same mask class:

```text
lim_{w -> infinity} limsup_{N -> infinity}
  |SLMIError_{U,V}^{345}|
  =
  0.
```

This display is a target, not a theorem.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-344,
the exact eight-slot physical identity from Module 323,
the local-model split from Module 325,
the signed Mobius audit from Module 326,
and the cover-route audits from Modules 327-344.
```

It does not assume:

```text
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
FullCoverLoadSmallness_327,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as a proved estimate,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
KernelWeightedPartitionClassCounting_331,
AbsoluteMinorKernelResidueUniformity_332,
WeightedDyadicProjectionRow_333,
ExactWeightedPartitionRows_334,
WeightedCRTMaskCriterion_335 as a proved estimate,
CutoffWindowCriterion_336 as a proved estimate,
KernelWeightedDivisorWindowCriterion_337 as a proved estimate,
WeightedLowHighCouplingRows_338,
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
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

### A. Post-cover input inventory

The cover route now has the following status:

```text
Module 330:
  KernelWeightedMobiusMomentCriterion_330 is conditional.

Modules 331-335:
  finite-side partition, residue, coarsening, and CRT/mask rows are structural
  or conditional, not proved.

Modules 336-339:
  cutoff, divisor-window, low-high, and exact-zero tail rows are structural or
  conditional, not proved.

Module 340:
  finite-side, tail, exact-zero, and total cover closure are FALSE / BLOCKED
  with current inputs.

Modules 342-344:
  the post-verdict low-envelope, internal-zero, and cross-zero tests define
  exact functionals and block the available crude/codimension closures.
```

Classification:

```text
PostCoverInputInventory_345:
  STRUCTURAL / EXTRACTION.
```

This inventory is not a proof of the cover route.

### B. Absolute cover continuation is not the best next move

Continuing the absolute cover route would require at least one genuinely new
same-family weighted theorem. In the current ledger it would have to control
several of the following at once:

```text
finite-side CRT/mask uniformity,
kernel residue mass,
weighted partition-class counting,
cutoff compatibility,
high-prime divisor-window tails,
low-prime envelope mass or second moments,
internal exact-zero kernel slices,
cross exact-zero affine slices,
and structural diagonal transfer.
```

Modules 342-344 show that the most tempting narrow shortcuts are not enough:

```text
trivial low-envelope mass ceiling:
  not small enough;

bare internal codimension:
  no weighted fixed-slice control;

bare cross codimension:
  no weighted affine-slice control.
```

Thus the proposition

```text
current Phase K should continue by adding another absolute cover-row
diagnostic before testing model insertion
```

is blocked as the immediate next move.

Classification:

```text
AbsoluteCoverContinuationAsNextMove_345:
  FALSE / BLOCKED.
```

This does not disprove any future absolute cover theorem. It only rejects
another same-shape diagnostic as the next project step.

### C. Unqualified signed insertion is also not a closure

The signed route is attractive because Module 326 records exact top-Mobius
cancellation:

```text
proper-support terms vanish inside the signed subset operator.
```

However, the physical row contains:

```text
F_8(d_1,d_2;x,y,h,k),
```

while the signed model row contains:

```text
Omega_{w,8}^{minor}(z).
```

Replacing the first object by the second under the threshold-localized kernel
is exactly the missing insertion theorem. It is not supplied by the signed
Mobius algebra itself.

Therefore:

```text
UnqualifiedSignedInsertionClosure_345:
  FALSE / BLOCKED.
```

The signed branch can only be continued as a feasibility test for the
insertion error, not as a claimed proof.

### D. Branch decision

The smallest useful next question is no longer:

```text
Can another absolute cover envelope be cataloged?
```

The smaller question is:

```text
Is the signed local-model insertion error itself decomposable into already
named rows, or is it endpoint-strength in disguise?
```

Thus the branch decision is:

```text
CoverRoutePause_345:
  STRUCTURAL / EXTRACTION.

SignedLocalModelInsertionFeasibility_346(P_minor^0):
  OPEN next target.
```

The next module should test the target:

```text
SLMIError_{U,V}^{345}=o_W(1)
```

only as a feasibility or proof-or-blocked verdict. It must not assume the
insertion theorem while trying to prove it.

### E. What Module 346 should decide

Module 346 should classify the signed insertion row by separating:

```text
1. local-model approximation error for F_8;
2. data-dependent threshold-mask interaction;
3. structural diagonal and collision defects;
4. finite-prime tail and W-limit order;
5. whether the signed cancellation remains in the same average;
6. whether any step requires PhaseKernelBound_273^0 or another endpoint.
```

Possible outcomes are:

```text
SignedLocalModelInsertionFeasibility_346:
  STRUCTURAL / EXTRACTION,
  CONDITIONAL,
  or FALSE / BLOCKED.
```

It must not be labeled `PROVEN` unless a complete same-family insertion proof
is supplied.

## 6. Edge cases and exclusions

### Cover pause is not a no-go theorem

`CoverRoutePause_345` says the current proof ledger should not spend the next
step on another absolute cover diagnostic. It does not say that an absolute
cover theorem cannot exist.

### Signed cancellation must stay signed

The top-Mobius cancellation from Module 326 holds inside the exact signed
subset sum. Passing to absolute values, envelopes, or cover loads can destroy
the cancellation.

### Model insertion is not selector transfer

Everything here remains inside `P_minor^0`. Even a future local insertion
theorem would still require transfer rows before it could speak about the
actual sharp moving selector.

### Data-dependent masks are part of the target

The masks `U,V` may be threshold-localized and data-dependent. Treating
`K_{U,V}^0` as a fixed external kernel repeats a blocked shortcut from Module
323.

### Exact local factor is not the generic factor

`Omega_{w,8}^{minor}` is collision-sensitive. Replacing it by the generic
size-only factor `Omega_w^{gen}` is another theorem-sized step unless the
collision and finite-prime load rows are proved.

### Endpoint circularity

No proof of Module 346 may assume `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3`.

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
  -> CrossZeroKernelAudit_344
  -> PhaseKPostCoverBranchDecision_345.
```

The next map node is:

```text
SignedLocalModelInsertionFeasibility_346(P_minor^0).
```

This branch returns to the signed physical-versus-model question opened by
Modules 325-326. It does not close the anti-diagonal, minor-kernel, residual
cube, or original selected-average problem.

## 8. What remains open

Still open:

```text
SignedLocalModelInsertionFeasibility_346(P_minor^0),
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
FullCoverLoadSmallness_327,
SharpCoverSmallness_328,
KernelWeightedMobiusMomentCriterion_330,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
WeightedCRTMaskCriterion_335,
CutoffWindowCriterion_336,
KernelWeightedDivisorWindowCriterion_337,
LowEnvelopeMassRows_338,
LowEnvelopeSecondMomentRows_338,
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
SignedLocalModelInsertionFeasibility_346(P_minor^0).
```

## Red flags / forbidden upgrades

Do not cite `PhaseKPostCoverBranchDecision_345` as proving any analytic
estimate.

Do not cite `CoverRoutePause_345` as disproving the absolute cover route.

Do not cite `UnqualifiedSignedInsertionClosure_345` as a signed insertion
theorem; it is the opposite, a blocked shortcut.

Do not replace `F_8` by `Omega_{w,8}^{minor}` without a named same-family
insertion theorem.

Do not replace `Omega_{w,8}^{minor}` by `Omega_w^{gen}` without collision,
finite-prime load, and overflow control.

Do not treat threshold-localized data-dependent masks as fixed kernels.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this local model steering decision to the actual sharp moving
selector or to the original selected-average problem.
