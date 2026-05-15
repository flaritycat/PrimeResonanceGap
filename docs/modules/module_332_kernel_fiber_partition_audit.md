# Module 332: Kernel-fiber partition audit for one-prime compatibility rows

## 1. Precise theorem / claim being advanced

Module 331 separated one-prime partition rank into free-fiber rank and
compatibility rank in the weighted variables:

```text
b=(t,d_1,d_2),  t=h+k.
```

This module audits the kernel part of that compatibility rank.

Define:

```text
KernelFiberPartitionAudit_332(P_minor^0).
```

Verdict:

```text
KernelFiberPartitionAudit_332(P_minor^0):
  STRUCTURAL / EXTRACTION.

CompatibilityFiberSplit_332:
  STRUCTURAL / EXTRACTION.

KernelResidueMassCriterion_332:
  CONDITIONAL.

TrivialKernelResidueCeiling_332:
  STRUCTURAL / EXTRACTION.

FullKernelSpikeObstruction_332:
  STRUCTURAL / EXTRACTION.

FourierSupportImpliesResidueUniformity_332:
  FALSE / BLOCKED.

AbsoluteMinorKernelResidueUniformity_332:
  OPEN.

KernelFiberCountingClosure_332:
  FALSE / BLOCKED.

DyadicResidueUniformityAudit_333(P_minor^0):
  OPEN next target.
```

The audit shows that compatibility rank in `(t,d_1,d_2)` cannot be read as a
kernel saving by itself. At most one compatibility condition can live in the
single kernel variable `t`; the remaining base compatibility must be supplied
by dyadic residue uniformity for `d_1,d_2` and by mask uniformity.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module extracts the exact kernel-fiber bookkeeping and states the
residue-mass criterion that would be needed. It does not prove that
criterion.

It proves no kernel-weighted partition count, no dyadic residue uniformity,
no mask residue uniformity, no multi-prime CRT product estimate, no finite
prime tail removal, no signed local-model insertion, no threshold closure, no
`PhaseKernelBound_273^0`, no residual cube endpoint, no selector transfer, and
no statement about the original selected-average problem.

## 3. Definitions and variables

Work in:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

The localized minor kernel is:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t),
```

where `U,V` are threshold-localized shell masks. The exact unlocalized kernel
from Modules 312 and 314 is:

```text
K_minor^0(t)
  =
  sum_{xi in Minor_0(R,eta)} e_N(xi t).
```

Under the nonzero-minor convention:

```text
K_minor^0(t)=K_full(t)-1-K_major^0(t),

K_full(t)=N 1_{t=0}.
```

Module 331 attaches to a one-prime partition class `pi` a compatibility
subspace:

```text
C_pi subset F_p^3
```

in the base variables:

```text
b=(t,d_1,d_2).
```

This subspace is the set of residues for which:

```text
A_u(pi)u=-A_b(pi)b
```

is solvable in `u=(r,h)`.

For any compatibility subspace `C subset F_p^3`, define:

```text
pi_d(C)={ (d_1,d_2) in F_p^2 : exists t with (t,d_1,d_2) in C }.
```

For a fixed `d=(d_1,d_2)`, define the `t`-fiber:

```text
C_t(d)={ t in F_p : (t,d_1,d_2) in C }.
```

Since `t` is one-dimensional, for every admissible `d` the fiber is either:

```text
C_t(d)=F_p,
```

or:

```text
C_t(d)={a_C(d)}
```

for an affine residue function `a_C`.

Define:

```text
s_t(C)=
  0 if C_t(d)=F_p on the generic projected d-support,
  1 if C_t(d) is a single residue on the generic projected d-support.
```

The remaining compatibility codimension is a dyadic-shift condition:

```text
s_d(C)=codim pi_d(C) in F_p^2.
```

For linear subspaces in the one-prime rows:

```text
codim C = s_d(C)+s_t(C).
```

up to empty or exceptional small-prime fibers, which are not used as closure
inputs.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 312, 314, 320, and 331,
finite linear algebra over F_p,
and the exact kernel definitions above.
```

It does not assume:

```text
KernelResidueMassCriterion_332 as a proved estimate,
AbsoluteMinorKernelResidueUniformity_332,
DyadicResidueUniformityAudit_333,
DyadicResidueUniformity_331,
MaskResidueUniformity_331,
KernelWeightedPartitionClassCounting_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
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

### A. Base compatibility splits into `d` and `t` fibers

Module 331 gives a compatibility subspace:

```text
C subset F_p^3,  b=(t,d_1,d_2).
```

The weighted compatibility row has the schematic absolute form:

```text
M_C^{332}(p;U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_t |K_{U,V}^0(d_1,d_2;t)|
      1_{(t,d_1,d_2) mod p in C}.
```

Splitting through the projection to `d=(d_1,d_2)` gives:

```text
M_C^{332}(p;U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    1_{d mod p in pi_d(C)}
    E_t |K_{U,V}^0(d_1,d_2;t)|
      1_{t mod p in C_t(d)}.
```

Classification:

```text
CompatibilityFiberSplit_332:
  STRUCTURAL / EXTRACTION.
```

The split is exact bookkeeping. It does not estimate either factor.

### B. Kernel residue-mass criterion

The kernel-fiber input needed by the Module 330/331 route is:

```text
KernelResidueMassCriterion_332:

For every admissible p>w, threshold-localized U,V, and affine residue
function a(d) generated by a one-prime partition compatibility class,

D^(-1) sum_{d_1 != d_2}
  1_{d mod p in E}
  E_t |K_{U,V}^0(d_1,d_2;t)| 1_{t=a(d) mod p}

<=
(p^(-1)+err_K(p,N,w,U,V,E))
D^(-1) sum_{d_1 != d_2}
  1_{d mod p in E}
  E_t |K_{U,V}^0(d_1,d_2;t)|,
```

with an error summable or absorbable in the exact limit order:

```text
N -> infinity first at fixed w,
then w -> infinity.
```

Here `E subset F_p^2` is the projected dyadic residue condition left by the
same compatibility class. If `s_t(C)=0`, this criterion is vacuous for that
class and all remaining saving must come from the `d`-projection row.

Classification:

```text
KernelResidueMassCriterion_332:
  CONDITIONAL.

AbsoluteMinorKernelResidueUniformity_332:
  OPEN.
```

This is a criterion, not a proved residue-uniformity theorem.

### C. What current trivial bounds give

The immediate absolute estimate is only:

```text
M_C^{332}(p;U,V)
  <=
  D^(-1) sum_{d_1 != d_2}
    E_t |K_{U,V}^0(d_1,d_2;t)|.
```

If `s_t(C)=1`, this loses the expected factor `p^(-1)`. If `s_d(C)>0`, it
also ignores the dyadic residue condition on `d_1,d_2`.

Using the pointwise ceiling:

```text
|K_{U,V}^0(d_1,d_2;t)|
  <=
  #{ xi : U(d_1,xi)V(d_2,xi)=1 }
```

turns the row into a frequency-count ceiling. That ceiling is diagnostic but
does not supply the kernel-residue saving needed by the cover-moment
criterion.

Classification:

```text
TrivialKernelResidueCeiling_332:
  STRUCTURAL / EXTRACTION.
```

It is a ceiling only, not a closure row.

### D. Parseval and square-root residue losses

For fixed `d_1,d_2`, Parseval gives:

```text
E_t |K_{U,V}^0(d_1,d_2;t)|^2
  =
  #{ xi : U(d_1,xi)V(d_2,xi)=1 }.
```

On a residue class `t=a mod p`, Cauchy gives at best the schematic bound:

```text
E_t |K_{U,V}^0(d_1,d_2;t)|1_{t=a mod p}
  <=
  p^(-1/2)
  (#{ xi : U(d_1,xi)V(d_2,xi)=1 })^(1/2),
```

up to finite-cyclic residue-rounding errors. This is a square-root residue
bound for a second moment, not the relative `p^(-1)` mass distribution of the
absolute kernel.

After summing over `d_1,d_2`, this route returns to the row/column and
frequency-count ceilings already recorded in Modules 312, 320, and 321.

Classification:

```text
FourierSupportImpliesResidueUniformity_332:
  FALSE / BLOCKED.
```

Fourier support and Parseval do not imply the needed absolute L1
residue-uniformity.

### E. Full-kernel spike obstruction

The full-frequency kernel has:

```text
K_full(t)=N 1_{t=0}.
```

Thus:

```text
E_t |K_full(t)|1_{t=0 mod p}
  =
  E_t |K_full(t)|.
```

The expected residue-uniform value would be:

```text
p^(-1) E_t |K_full(t)|.
```

So the full-frequency diagnostic has a complete spike on the residue class
containing `0`. The minor kernel is:

```text
K_minor^0=K_full-1-K_major^0,
```

but the target row contains absolute values. Therefore signed cancellation in
the decomposition cannot be used as residue uniformity for `|K_minor^0|` or
for `|K_{U,V}^0|` without a new theorem.

Classification:

```text
FullKernelSpikeObstruction_332:
  STRUCTURAL / EXTRACTION.
```

This obstruction does not disprove minor-kernel residue uniformity. It blocks
the shortcut that residue uniformity is automatic from the full/zero/major
decomposition.

### F. Class examples

The Module 331 full one-prime block has compatibility:

```text
t=0, d_1=0, d_2=0 mod p.
```

Here:

```text
s_t=1,
s_d=2.
```

Only the first loss is a kernel-residue question; the other two losses are
dyadic residue questions for `d_1,d_2`.

A class imposing:

```text
t=d_1-d_2 mod p
```

has:

```text
s_t=1,
s_d=0.
```

It requires a moving residue class for `t`, depending on the active dyadic
shifts and masks.

A class imposing only:

```text
d_1=0 mod p
```

has:

```text
s_t=0,
s_d=1.
```

It is not a kernel-fiber row at all. It belongs to the dyadic residue
uniformity audit.

### G. Current closure verdict

The current ledger now has:

```text
the compatibility-fiber split,
the kernel residue-mass criterion,
trivial absolute ceilings,
the Parseval square-root diagnostic,
and the full-kernel spike obstruction.
```

It does not have:

```text
absolute L1 residue uniformity for K_{U,V}^0,
dyadic residue uniformity for d_1,d_2,
mask residue uniformity for U,V,
coarsening inclusion-exclusion estimates,
multi-prime CRT/mask compatibility,
or finite-prime tail control.
```

Therefore:

```text
KernelFiberCountingClosure_332:
  FALSE / BLOCKED.
```

The next useful target is not another rank slogan. It is the dyadic residue
row for `d_1,d_2`, because the compatibility split shows that many partition
classes spend most of their codimension outside the kernel variable.

## 6. Edge cases and exclusions

- If `s_t(C)=0`, the class has no kernel-residue saving to extract.
- If `s_t(C)=1`, the needed saving is an absolute L1 residue-mass statement,
  not a signed exponential-sum identity.
- Full-residue rank can overstate what the kernel can supply because `t` is
  only one-dimensional.
- Conditions such as `p|d_1` or `p|d_2` are dyadic shift rows, not kernel
  rows.
- The full-frequency kernel is concentrated at `t=0`; it is not residue
  uniform.
- The minor/full/major decomposition is signed. Absolute values block direct
  cancellation.
- The masks `U,V` are data-dependent and remain inside the target row.
- Finite-cyclic residue rounding is not harmless unless a row states its
  convention and error.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- A kernel-fiber criterion is not an analytic proof.

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
  -> DyadicResidueUniformityAudit_333.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. DyadicResidueUniformityAudit_333(P_minor^0):
     decide whether the dyadic ranges for d_1,d_2 provide the residue
     savings required by pi_d(C), with off-diagonal and wrap conventions.

2. AbsoluteMinorKernelResidueUniformity_332:
     prove or reject L1 residue uniformity for |K_{U,V}^0(d_1,d_2;t)| under
     data-dependent masks.

3. MaskResidueUniformity_331:
     prove or reject residue uniformity after U,V are imposed.

4. ExactPartitionCoarseningAudit_334:
     decide whether exact partition inequalities can be handled by
     coarsening inclusion-exclusion in the same row.

5. MultiPrimeCoverMomentRows_330:
     prove or reject CRT/uniformity for products of one-prime compatibility
     rows under kernel and mask weights.
```

The current cadence after completing this module is:

```text
Latest completed module: 332
Post-Reflective_1 solving count: 151
Long-term-plan count: 145

145 is not divisible by 9, so no plan update is due in this module.
145 is not divisible by 15, so no plan challenge is due in this module.
Next reflective log remains expected around Module 341.
```

## 9. Forbidden upgrades

This module does not prove:

```text
KernelResidueMassCriterion_332 as an estimate,
AbsoluteMinorKernelResidueUniformity_332,
DyadicResidueUniformityAudit_333,
DyadicResidueUniformity_331,
MaskResidueUniformity_331,
KernelWeightedPartitionClassCounting_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
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

Do not cite `KernelFiberPartitionAudit_332` as a kernel-residue estimate. It
states the row and blocks current shortcuts.
