# Module 325: Generic-versus-collision local-model split for the eight-slot minor row

## 1. Precise theorem / claim being advanced

Module 324 cataloged the collision and diagonal strata of the exact eight-slot
minor row from Module 323. This module turns that catalog into a status-safe
generic-versus-collision local-model split.

Define:

```text
GenericCollisionLocalModelSplit_325(P_minor^0).
```

Verdict:

```text
GenericCollisionLocalModelSplit_325(P_minor^0):
  STRUCTURAL / EXTRACTION.

GenericMinorLocalFactor_325:
  STRUCTURAL / EXTRACTION.

CollisionDefectDecomposition_325:
  STRUCTURAL / EXTRACTION.

StructuralDiagonalRows_325:
  OPEN.

FinitePrimeCollisionLoadRows_325:
  OPEN.

OverflowRows_325:
  OPEN.

DataDependentKernelSelectionRows_325:
  OPEN.

GenericNoncollisionRow_325:
  OPEN.

LocalModelInsertion_325:
  OPEN.

CurrentGenericCollisionClosure_325:
  FALSE / BLOCKED.

SignedInclusionExclusionMinorAudit_326(P_minor^0):
  OPEN next target.
```

The split records what would have to be proved after the eight-slot expansion:
a generic eight-distinct local factor, structural diagonal control, finite-prime
collision load control, overflow control, data-dependent kernel-selection
uniformity, and a same-family local-model insertion theorem. It proves none of
those estimates.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no residual eight-slot cancellation, no signed minor-kernel
gain, no admissible `Phi`, no threshold closure, no column barrier, no
`PhaseKernelBound_273^0`, no residual cube endpoint, no selector transfer, and
no statement about the original selected-average problem.

## 3. Definitions and variables

Work in the same local family as Modules 278, 323, and 324:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

The eight slots are:

```text
L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k.
```

Let:

```text
Lambda_8={1,2,3,4,5,6,7,8}.
```

For `S subset Lambda_8`, define the finite-prime residue count:

```text
r_p(S;d_1,d_2,x,y,h,k)
  =
  |{ L_i mod p : i in S }|.
```

The exact collision-sensitive local factor for the subset `S` is:

```text
Theta_{w,S}^{8,min}(d_1,d_2,x,y,h,k)
  =
  prod_{p>w}
    (1-1/p)^(-|S|)
    (1-r_p(S;d_1,d_2,x,y,h,k)/p).
```

The residual eight-slot local model is the signed subset expansion:

```text
Omega_{w,8}^{minor}(d_1,d_2,x,y,h,k)
  =
  sum_{S subset Lambda_8}
    (-1)^(8-|S|) Theta_{w,S}^{8,min}(d_1,d_2,x,y,h,k).
```

The generic size-only factor, valid only when every selected slot occupies a
distinct residue for every relevant prime, is:

```text
Theta_{w,s}^{gen}
  =
  prod_{p>w} (1-1/p)^(-s)(1-s/p),
```

and the corresponding generic residual factor is:

```text
Omega_w^{gen}
  =
  sum_{s=0}^8 binom(8,s)(-1)^(8-s)Theta_{w,s}^{gen}.
```

These are local-model objects. They are not the actual prime average and they
are not a transfer theorem for the sharp moving selector.

For labels `i<j`, keep Module 324's slot differences:

```text
Delta_{ij}=L_i-L_j.
```

Define the structural zero set:

```text
Z_struct^8
  =
  union_{i<j} { Delta_{ij}=0 in G_N }.
```

Off `Z_struct^8`, define the finite-prime collision load:

```text
B_{w,8}^{minor}(d_1,d_2,x,y,h,k)
  =
  sum_{1<=i<j<=8}
    sum_{p>w, p | Delta_{ij}} 1/p.
```

The generic region is the complement of structural diagonals with controlled
finite-prime load:

```text
G_{w,8}^{minor}(T)
  =
  { (d_1,d_2,x,y,h,k) notin Z_struct^8 :
      B_{w,8}^{minor}(d_1,d_2,x,y,h,k) <= T }.
```

The overflow region is:

```text
O_{w,8}^{minor}(T)
  =
  { (d_1,d_2,x,y,h,k) notin Z_struct^8 :
      B_{w,8}^{minor}(d_1,d_2,x,y,h,k) > T }.
```

For threshold-localized masks `U,V`, the row from Module 323 is:

```text
WOff_{U,V}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      F_8(d_1,d_2;x,y,h,k)
      K_{U,V}^0(d_1,d_2;h+k).
```

The kernel is:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t).
```

For large-spectrum masks, `U,V` are data-dependent. This dependence is part
of the target, not an ignorable bookkeeping detail.

## 4. Assumptions

This module assumes only the active status ledger and the exact identities and
catalogs from Modules 278, 284, 297, 308-324.

It does not assume:

```text
LocalModelInsertion_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
SignedInclusionExclusionMinorAudit_326,
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

### A. Exact generic local factor

If every selected subset of slots occupies `s=|S|` distinct residues modulo
every prime `p>w`, then:

```text
r_p(S;d_1,d_2,x,y,h,k)=s,
```

and:

```text
Theta_{w,S}^{8,min}(d_1,d_2,x,y,h,k)=Theta_{w,s}^{gen}.
```

Thus the generic residual factor is:

```text
Omega_w^{gen}
  =
  sum_{s=0}^8 binom(8,s)(-1)^(8-s)Theta_{w,s}^{gen}.
```

Classification:

```text
GenericMinorLocalFactor_325:
  STRUCTURAL / EXTRACTION.
```

This is only an extraction of the local factor that would appear on a
collision-free model row. It does not show that the actual eight-slot prime
average is equal to the local factor, and it does not estimate the resulting
kernel-weighted contribution.

### B. Collision defect decomposition

For a general tuple, collisions change `r_p(S)` from `|S|`. The exact local
defect relative to the generic factor is:

```text
Def_{w,8}^{minor}
  =
  Omega_{w,8}^{minor}(d_1,d_2,x,y,h,k)
  - Omega_w^{gen}.
```

Any future use of the split must bound the contribution of:

```text
1_{Z_struct^8},
1_{G_{w,8}^{minor}(T)} Def_{w,8}^{minor},
1_{O_{w,8}^{minor}(T)} Omega_{w,8}^{minor},
```

with the same kernel, cutoff, dyadic range, W-residue convention, threshold
schedule, limiting order, and selector class as the row being proved.

Classification:

```text
CollisionDefectDecomposition_325:
  STRUCTURAL / EXTRACTION.
```

This is not collision smallness. It is the required partition of the local
model into generic, finite-prime defect, overflow, and structural-diagonal
pieces.

### C. Structural diagonal rows

The structural set `Z_struct^8` contains:

```text
h=0, h=d_1, h=-d_1,
k=0, k=d_2, k=-d_2,
```

and the sixteen cross-block equations:

```text
x-y = -a d_1 - b h + c d_2 + e k,
(a,b),(c,e) in {(1,0),(0,0),(1,1),(0,1)}.
```

A future diagonal row must prove, with the actual residual product and the
actual threshold-localized minor kernel:

```text
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k}
    1_{Z_struct^8}
    F_8(d_1,d_2;x,y,h,k)
    K_{U,V}^0(d_1,d_2;h+k)
  = acceptable error.
```

Classification:

```text
StructuralDiagonalRows_325:
  OPEN.
```

Codimension counting alone is not enough unless it is coupled to the residual
weights, the threshold masks, the minor kernel, and the declared W-limit.

### D. Finite-prime collision load rows

Off structural diagonals, collisions modulo primes `p>w` are measured by:

```text
B_{w,8}^{minor}
  =
  sum_{i<j} sum_{p>w, p | Delta_{ij}} 1/p.
```

A future finite-prime collision row must prove a kernel-weighted estimate of
the form:

```text
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k}
    1_{G_{w,8}^{minor}(T)}
    |K_{U,V}^0(d_1,d_2;h+k)|
    B_{w,8}^{minor}(d_1,d_2,x,y,h,k)
  = o_W(1),
```

or a signed analogue strong enough to replace the absolute value in the exact
row. The signed analogue must remain in the exact same projection, cutoff,
denominator, W-residue, dyadic-shell, selector, and limiting family.

Classification:

```text
FinitePrimeCollisionLoadRows_325:
  OPEN.
```

The Module 324 load definition is diagnostic only. It is not an average
estimate.

### E. Overflow rows

The finite-prime load comparison also needs the high-load region:

```text
O_{w,8}^{minor}(T).
```

A typical sufficient row would control a kernel-weighted exponential moment:

```text
D^(-1) sum_{d_1 != d_2}
  E_{x,y,h,k}
    1_{O_{w,8}^{minor}(T)}
    |K_{U,V}^0(d_1,d_2;h+k)|
    exp(C B_{w,8}^{minor})
  = o_W(1),
```

with constants and ranges compatible with the local factor expansion.

Classification:

```text
OverflowRows_325:
  OPEN.
```

No overflow estimate is supplied by the structural split.

### F. Data-dependent kernel selection rows

For raw rows, `K_{U,V}^0` can be treated as a fixed minor kernel. For
threshold-localized rows, however:

```text
U=J_{j,k},  V=J_{j,l}
```

or related masks depend on the large Fourier coefficients of the same
residual data. Therefore a fixed-kernel local model does not automatically
apply.

A future kernel-selection row must prove one of:

```text
uniform local-model and collision estimates for every admissible selected
  kernel K_{U,V}^0,

a selection-transfer theorem from fixed masks to data-dependent masks,

or a direct estimate of the exact data-dependent kernel-weighted row.
```

Classification:

```text
DataDependentKernelSelectionRows_325:
  OPEN.
```

This is the same obstruction that prevented fixed-set estimates from closing
the shell functional earlier in Phase J/K.

### G. Generic noncollision row

Even after collision defects are removed, the generic piece remains:

```text
Omega_w^{gen}
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k),
```

or the signed residual/local-model counterpart required by the exact
inclusion-exclusion expansion.

A future row must prove that this generic contribution is acceptable after the
actual kernel budget, threshold conversion, dyadic summation, and W-limit.

Classification:

```text
GenericNoncollisionRow_325:
  OPEN.
```

The formal cancellation in the signed eight-fold generic factor is promising
only as a target. It is not a proved minor-kernel estimate.

### H. Local-model insertion row

The exact physical row contains:

```text
F_8(d_1,d_2;x,y,h,k)
```

inside a W-cyclic prime-only model. Replacing its average by
`Omega_{w,8}^{minor}` is itself a theorem-sized input:

```text
LocalModelInsertion_325(P_minor^0).
```

It must be proved for the same cutoff, W-residue class, dyadic shell,
denominator/minor-arc convention, threshold masks, and limiting order.

Classification:

```text
LocalModelInsertion_325:
  OPEN.
```

First-moment Hardy-Littlewood, pair-BDH, or a projected-major conditional
schema does not supply this eight-slot threshold-localized minor row.

### I. Current closure verdict

The current ledger has:

```text
an exact eight-slot expansion,
a collision and diagonal catalog,
a local low-level fourth-moment tail inside P_minor^0,
and many ceiling-scale audits for row/column/weighted-pair routes.
```

It does not have:

```text
structural diagonal smallness,
finite-prime collision-load estimates,
overflow control,
data-dependent kernel-selection uniformity,
generic noncollision cancellation with kernel budget,
or local-model insertion for the exact eight-slot residual row.
```

Therefore:

```text
CurrentGenericCollisionClosure_325:
  FALSE / BLOCKED.
```

The generic-versus-collision split is a better map of the obstruction, not a
proof that the obstruction is small.

## 6. Edge cases and exclusions

- `d_1 != d_2` removes only the integer shift diagonal. It does not remove
  congruences such as `d_1=d_2 mod p` for primes `p>w`.
- Internal diagonals `h=0`, `h=+-d_1`, `k=0`, and `k=+-d_2` remain separate
  rows.
- The full-frequency anti-diagonal `h+k=0` remains a diagnostic from Module
  324. The actual minor kernel does not impose that stratum by itself.
- The generic factor `Omega_w^{gen}` is not a substitute for the exact local
  factor when finite-prime collisions occur.
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
  -> SignedInclusionExclusionMinorAudit_326.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. SignedInclusionExclusionMinorAudit_326(P_minor^0):
     decide which collision-defect and generic terms are formally killed by
     the exact signed eight-slot inclusion-exclusion, and which survive as
     same-family estimates.

2. StructuralDiagonalRows_325:
     control or reject the structural diagonal contribution with the actual
     threshold-localized minor kernel.

3. FinitePrimeCollisionLoadRows_325 and OverflowRows_325:
     prove or reject collision-load and high-load estimates after kernel
     weighting.

4. DataDependentKernelSelectionRows_325:
     decide whether fixed-kernel local models can be upgraded to the actual
     data-dependent large-spectrum masks.

5. GenericNoncollisionRow_325:
     prove or reject the generic signed residual contribution after the
     kernel budget and W-limit order.
```

## 9. Forbidden upgrades

This module does not prove:

```text
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
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

Do not cite `GenericCollisionLocalModelSplit_325` as a proof of smallness. It
is a routing and local-model bookkeeping module only.
