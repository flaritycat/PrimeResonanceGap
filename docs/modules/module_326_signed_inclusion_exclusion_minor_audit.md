# Module 326: Signed inclusion-exclusion audit for the eight-slot minor row

## 1. Precise theorem / claim being advanced

Module 325 formulated the generic-versus-collision local-model split for the
eight-slot minor row. This module audits what the signed `f=nu-1`
inclusion-exclusion actually cancels in that split, and what survives as an
analytic row.

Define:

```text
SignedInclusionExclusionMinorAudit_326(P_minor^0).
```

Verdict:

```text
SignedInclusionExclusionMinorAudit_326(P_minor^0):
  STRUCTURAL / EXTRACTION.

SubsetMobiusIdentity_326:
  STRUCTURAL / EXTRACTION.

ProperSupportCancellation_326:
  STRUCTURAL / EXTRACTION.

FullGenericMinorZeroIdentity_326:
  STRUCTURAL / EXTRACTION.

FullCoverCollisionRows_326:
  OPEN.

StratifiedGenericRemainderRows_326:
  OPEN.

SignedLocalModelInsertion_326:
  OPEN.

SignedIECancelsAllCollisionDefects_326:
  FALSE / BLOCKED.

CurrentSignedIEClosure_326:
  FALSE / BLOCKED.

FullCoverClusterAudit_327(P_minor^0):
  OPEN next target.
```

The audit shows that signed inclusion-exclusion is a top-Mobius extractor. It
kills terms whose total label support is a proper subset of the eight labels,
provided they remain inside the exact same signed average. It does not kill
full-cover clusters, structural diagonal restrictions, finite-prime overflow,
data-dependent kernel-selection rows, or the local-model insertion problem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no collision smallness, no residual eight-slot
cancellation, no signed minor-kernel gain, no admissible `Phi`, no threshold
closure, no column barrier, no `PhaseKernelBound_273^0`, no residual cube
endpoint, no selector transfer, and no statement about the original
selected-average problem.

## 3. Definitions and variables

Work inside the same local model:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Use the eight labels and slots from Modules 323-325:

```text
Lambda_8={1,2,3,4,5,6,7,8},

L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k.
```

For `S subset Lambda_8`, let:

```text
Theta_{w,S}^{8,min}(d_1,d_2,x,y,h,k)
  =
  prod_{p>w}
    (1-1/p)^(-|S|)
    (1-r_p(S;d_1,d_2,x,y,h,k)/p),
```

where `r_p(S;...)` counts distinct residue classes occupied by
`{L_i : i in S}` modulo `p`.

Define the signed subset operator:

```text
Delta_8 H
  =
  sum_{S subset Lambda_8} (-1)^(8-|S|) H(S).
```

Then the residual local factor from Module 325 is:

```text
Omega_{w,8}^{minor}
  =
  Delta_8(Theta_{w,S}^{8,min}).
```

For threshold-localized masks `U,V`, define the model-side signed minor row:

```text
ModelSignedMinor_{U,V}^{326}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      Omega_{w,8}^{minor}(d_1,d_2,x,y,h,k).
```

Equivalently, with:

```text
A_S^{326}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      Theta_{w,S}^{8,min}(d_1,d_2,x,y,h,k),
```

one has:

```text
ModelSignedMinor_{U,V}^{326}
  =
  sum_{S subset Lambda_8} (-1)^(8-|S|) A_S^{326}(U,V).
```

This is a local-model row only. The physical row still contains the actual
residual product `F_8`; replacing that product by the local model is the open
insertion problem.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
the exact eight-slot expansion from Module 323,
the collision catalog from Module 324,
and the local-model split from Module 325.
```

It does not assume:

```text
SignedLocalModelInsertion_326,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
LocalModelInsertion_325,
ResidualEightSlotMinorCancellation_319,
AdmissiblePhiGain_320,
FiberOverlapGainTarget_321,
SignedMinorKernelGain_318,
MajorLocalModelTransfer_317,
AntiDiagonalTwoShiftKernelGain_312,
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
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

### A. Signed subset sum as a top-Mobius extractor

For any set function `H` on subsets of `Lambda_8`, define its Mobius
coefficient:

```text
m_T(H)
  =
  sum_{R subset T} (-1)^(|T|-|R|) H(R).
```

The finite Mobius inversion identity gives:

```text
H(S)=sum_{T subset S} m_T(H).
```

Applying `Delta_8` gives:

```text
Delta_8 H
  =
  m_{Lambda_8}(H).
```

Classification:

```text
SubsetMobiusIdentity_326:
  STRUCTURAL / EXTRACTION.
```

Thus signed inclusion-exclusion extracts the top eight-label interaction
coefficient of the chosen local factor. It is not, by itself, a smallness
estimate.

### B. Proper-support cancellation

If a term has total label support contained in a proper subset
`T subsetneq Lambda_8`, meaning:

```text
H(S)=H(S cap T)
```

for every `S subset Lambda_8`, then:

```text
Delta_8 H
  =
  sum_{R subset T} (-1)^(|T|-|R|)H(R)
    sum_{Q subset Lambda_8\T} (-1)^(|Lambda_8|-|T|-|Q|)
  =
  0.
```

Classification:

```text
ProperSupportCancellation_326:
  STRUCTURAL / EXTRACTION.
```

This is the exact formal cancellation that can remove lower-support local
terms. The word "support" here means total support after multiplying all
local pieces in the expansion. Products of several proper-support pieces may
survive if their union of labels is all of `Lambda_8`.

### C. Generic size-only terms

For the size-only generic factors:

```text
Theta_{w,s}^{gen}
  =
  prod_{p>w}(1-1/p)^(-s)(1-s/p),

Omega_w^{gen}
  =
  sum_{s=0}^8 binom(8,s)(-1)^(8-s)Theta_{w,s}^{gen}.
```

The signed operator is the eighth finite difference in the size variable:

```text
Delta_8 P(|S|)
  =
  sum_{s=0}^8 binom(8,s)(-1)^(8-s)P(s).
```

It annihilates all polynomials in `s` of degree `<8`. Therefore generic
tail estimates may try to exploit the fact that only degree-eight and higher
terms survive in a size expansion. This module does not prove such a tail
estimate.

In the unrestricted cyclic minor row, there is a separate exact zero-mode
identity. Since `K_{U,V}^0` is supported on nonzero minor frequencies and
`U,V` depend on `(d,xi)` rather than on `h,k`, the full cyclic average obeys:

```text
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k} K_{U,V}^0(d_1,d_2;h+k)
  =
  0.
```

Consequently the full unrestricted size-only generic contribution is zero
inside `P_minor^0`:

```text
Omega_w^{gen}
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k} K_{U,V}^0(d_1,d_2;h+k)
=0.
```

Classification:

```text
FullGenericMinorZeroIdentity_326:
  STRUCTURAL / EXTRACTION.
```

This identity is not a generic-tail theorem and it is not a transfer theorem.
It can fail as a usable cancellation after restricting to structural
diagonals, finite-prime load strata, overflow sets, boundary/cutoff regions,
or selector-transfer errors, because those indicators depend on the same
variables as the kernel.

### D. Collision defects after signed inclusion-exclusion

Write:

```text
Theta_{w,S}^{8,min}
  =
  Theta_{w,|S|}^{gen} + Def_S^{326}.
```

Then:

```text
Omega_{w,8}^{minor}
  =
  Omega_w^{gen}
  +
  Delta_8(Def_S^{326}).
```

The operator `Delta_8` kills any component of `Def_S^{326}` whose total label
support is a proper subset of `Lambda_8`. What remains is the full-cover
Mobius coefficient:

```text
m_{Lambda_8}(Def^{326}).
```

The surviving coefficient may be produced by:

```text
one full eight-label collision cluster,
several smaller finite-prime collisions whose union covers all eight labels,
structural diagonal restrictions coupled to the kernel,
or high-load/overflow interactions.
```

Classification:

```text
FullCoverCollisionRows_326:
  OPEN.
```

No estimate for the full-cover coefficient is supplied here.

### E. Stratified generic remainders

Module 325 split the local model by regions such as:

```text
Z_struct^8,
G_{w,8}^{minor}(T),
O_{w,8}^{minor}(T).
```

The full generic row is killed by the nonzero minor kernel only before such
variable-dependent indicators are inserted. After restriction, one must
control rows of the form:

```text
Omega_w^{gen}
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k}
    1_E(d_1,d_2,x,y,h,k)
    K_{U,V}^0(d_1,d_2;h+k),
```

where `E` is a structural, collision-load, overflow, boundary, or transfer
region.

Classification:

```text
StratifiedGenericRemainderRows_326:
  OPEN.
```

The zero-mode identity cannot be applied after the row has been cut by a
variable-dependent stratum unless a same-family remainder estimate is proved.

### F. Signed local-model insertion

The actual Module 323 physical row is:

```text
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k}
    F_8(d_1,d_2;x,y,h,k)
    K_{U,V}^0(d_1,d_2;h+k).
```

The signed local-model row replaces `F_8` by:

```text
Omega_{w,8}^{minor}(d_1,d_2,x,y,h,k).
```

That replacement requires a theorem in the exact same family, with the same
cutoff, W-residue class, dyadic shell, denominator/minor-arc convention,
threshold masks, and limiting order.

Classification:

```text
SignedLocalModelInsertion_326:
  OPEN.
```

The signed subset algebra is internal to the model. It does not insert the
model into the physical residual row.

### G. Blocked shortcuts

The following shortcut is invalid:

```text
Signed inclusion-exclusion kills proper-support terms
  therefore all collision defects are gone.
```

It fails because full-cover Mobius coefficients can survive. It also fails
after structural restrictions, overflow cuts, data-dependent kernel selection,
and local-model insertion.

Therefore:

```text
SignedIECancelsAllCollisionDefects_326:
  FALSE / BLOCKED.
```

The current ledger still lacks:

```text
full-cover collision estimates,
stratified generic remainder estimates,
signed local-model insertion,
data-dependent kernel-selection uniformity,
and transfer out of P_minor^0.
```

Hence:

```text
CurrentSignedIEClosure_326:
  FALSE / BLOCKED.
```

## 6. Edge cases and exclusions

- Proper-support cancellation applies only before absolute values are inserted.
- The cancellation applies only inside the exact same signed average. Changing
  cutoff, projection, W-residue convention, threshold masks, or limiting order
  creates a transfer row.
- Products of lower-support collision terms can survive if their union covers
  all eight labels.
- The full generic size-only row is killed in the unrestricted cyclic
  nonzero-frequency minor row, but not automatically on structural,
  collision-load, overflow, boundary, or selector-transfer subregions.
- The data-dependent masks `U,V` remain part of the row. Signed
  inclusion-exclusion does not make them fixed external kernels.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- The full gap is not a clipped gap, a tail row, or a model gap.
- A structural reduction is not an analytic proof.
- A conditional theorem is not a theorem.
- No endpoint object may be used as an assumption in a module meant to prove
  that endpoint.

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
  -> FullCoverClusterAudit_327.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. FullCoverClusterAudit_327(P_minor^0):
     classify the full-cover Mobius coefficients that survive signed
     inclusion-exclusion and identify their minimal collision/load structure.

2. StratifiedGenericRemainderRows_326:
     decide whether generic zero-mode cancellation survives the structural,
     collision-load, overflow, and boundary restrictions.

3. SignedLocalModelInsertion_326:
     prove or reject the exact local-model insertion theorem for the signed
     eight-slot minor row with data-dependent masks.

4. DataDependentKernelSelectionRows_325:
     decide whether fixed-kernel local estimates can be made uniform over the
     large-spectrum-selected kernels.
```

## 9. Forbidden upgrades

This module does not prove:

```text
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
LocalModelInsertion_325,
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

Do not cite `SignedInclusionExclusionMinorAudit_326` as proof that collision
defects vanish. It is an exact support audit and a proof-blocker map only.
