# Module 321: Data-dependent fiber gain audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 320 formulated the conditional cross-shell `Phi` criterion. The next
question is whether the current `P_minor^0` data-dependent fibers already
force a nontrivial overlap or entropy gain that could produce an admissible
`Phi`.

Define:

```text
DataDependentFiberGainAudit_321(P_minor^0).
```

Verdict:

```text
DataDependentFiberGainAudit_321(P_minor^0):
  STRUCTURAL / EXTRACTION.

FiberOverlapIdentities_321:
  STRUCTURAL / EXTRACTION.

CompleteFiberConcentrationModel_321:
  STRUCTURAL / EXTRACTION diagnostic.

CurrentFiberCapsForcePhiGain_321:
  FALSE / BLOCKED.

SelectionRuleGivesIndependence_321:
  FALSE / BLOCKED.

FiberOverlapGainTarget_321(P_minor^0):
  OPEN.

PlanUpdate_15_Challenge_9_322:
  OPEN next target.
```

The row and column caps in `P_minor^0` do not by themselves force a
same-frequency overlap gain. They are compatible, at the deterministic
incidence level, with complete concentration on the same column fibers. A
future gain would need a genuinely new prime-specific or residual-structure
theorem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no `Phi` estimate, no weighted column-pair gain, no
threshold closure, no adaptive-shell gain, no phase-kernel bound, no residual
cube endpoint, and no selector transfer. It only audits what follows from the
current deterministic fiber restrictions.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D.
```

For a shell set:

```text
U=J_{j,k},
V=J_{j,l},
k,l>=j,
```

define:

```text
N_U(xi)=# { d:(d,xi) in U },
C_U(xi)=sum_{d:(d,xi) in U}|beta_0(d,xi)|^2,

R(U)=sup_d # { xi:(d,xi) in U },
K(U)=sup_xi N_U(xi),

Eng(U)=D^(-1) sum_{(d,xi) in U}|beta_0(d,xi)|^2.
```

The two overlap rows relevant to Module 320 are:

```text
Overlap_N(U,V)
  =
  sum_{xi in Minor_0} N_U(xi)N_V(xi),

Overlap_C(U,V)
  =
  sum_{xi in Minor_0} C_U(xi)C_V(xi).
```

For shell heights `lambda_k,lambda_l`, the weighted cross-shell row satisfies:

```text
WOff(U,V)
  <=
  D^(-1) Overlap_C(U,V).
```

Also, using only shell upper bounds:

```text
WOff(U,V)
  <=
  16 lambda_k^2 lambda_l^2 D^(-1) Overlap_N(U,V).
```

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297, 308,
309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, and 320.

It uses:

```text
the current row caps E_{d,0}(lambda_j)<=mu_0(lambda_j),
the current column caps N_{xi,0}(lambda_j)<=K_0(lambda_j),
the shell height bounds lambda_k<=|beta_0|<2lambda_k,
finite incidence identities,
and no randomness or independence assumption.
```

It does not assume:

```text
FiberOverlapGainTarget_321(P_minor^0),
AdmissiblePhiGain_320(P_minor^0),
DataDependentFiberGainAudit_321 as a gain,
SizeSensitiveMinorKernelCriterion_320 as an estimate,
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
SignedMinorKernelGain_318(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
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

### A. Exact overlap identities

The unweighted overlap is exactly:

```text
Overlap_N(U,V)
  =
  # { (d_1,d_2,xi):
        (d_1,xi) in U,
        (d_2,xi) in V }.
```

The off-diagonal version subtracts only the pairs with `d_1=d_2`; this
subtraction is nonnegative and cannot create a gain by itself:

```text
sum_{d_1 != d_2,xi}1_U(d_1,xi)1_V(d_2,xi)
  <=
  Overlap_N(U,V).
```

Similarly:

```text
Overlap_C(U,V)
  =
  sum_{xi}
    (
      sum_{d:(d,xi) in U}|beta_0(d,xi)|^2
    )
    (
      sum_{d:(d,xi) in V}|beta_0(d,xi)|^2
    ).
```

Classification:

```text
FiberOverlapIdentities_321:
  STRUCTURAL / EXTRACTION.
```

These identities locate the obstruction. They do not bound it.

### B. What the current caps imply

The active row and column caps give:

```text
R(U) <= mu_0(lambda_j)/lambda_k^2,
K(U) <= K_0(lambda_j),
```

up to harmless shell constants, and similarly for `V`. They also give:

```text
#U <= D R(U),
#U <= m_minor^0 K(U).
```

Consequently:

```text
Overlap_N(U,V)
  <=
  min(
    K(U)#V,
    K(V)#U,
    m_minor^0 K(U)K(V),
    (#U)(#V)
  ).
```

For weighted fibers:

```text
C_U(xi) <= 4 lambda_k^2 N_U(xi),
C_V(xi) <= 4 lambda_l^2 N_V(xi),
```

and hence:

```text
Overlap_C(U,V)
  <=
  16 lambda_k^2 lambda_l^2 Overlap_N(U,V).
```

These are deterministic ceilings. They are not gains over first incidence
unless a stronger estimate forces `Overlap_N(U,V)` below the displayed caps.

### C. Complete concentration is still allowed by the caps

At the deterministic incidence level, the current caps allow the following
configuration.

Choose a set `X` of minor frequencies and place both `U` and `V` on the same
columns `X`. For each `xi in X`, use the maximum allowed number of shifts:

```text
N_U(xi)=K(U),
N_V(xi)=K(V),
```

subject only to the row caps and total shell energies.

Then:

```text
Overlap_N(U,V)=#X K(U)K(V),
```

which saturates the column-overlap ceiling. With shell-size coefficients,
the weighted overlap also saturates:

```text
Overlap_C(U,V)
  approx
  lambda_k^2 lambda_l^2 #X K(U)K(V),
```

up to the fixed shell constants already paid in Module 320.

Classification:

```text
CompleteFiberConcentrationModel_321:
  STRUCTURAL / EXTRACTION diagnostic.
```

This is not claimed to be a prime model. It shows only that the currently
recorded deterministic constraints do not logically imply an overlap gain.

### D. Selection rules do not provide independence

The `P_minor^0` selection rules remove shifts with large row energy and
frequencies with large column multiplicity. After removal, the surviving set
still may have:

```text
many shifts sharing the same surviving frequency,
many frequencies sharing the same surviving shift,
and the same columns reused across shell pairs U,V.
```

The rules impose caps; they do not randomize the fibers, decorrelate shell
pairs, or force expansion of the bipartite graph.

Therefore:

```text
SelectionRuleGivesIndependence_321:
  FALSE / BLOCKED.
```

### E. Current-fiber-gain verdict

Combining the preceding sections:

```text
CurrentFiberCapsForcePhiGain_321:
  FALSE / BLOCKED.
```

The current row caps, column caps, shell-height restrictions, energy tails,
and selection rules do not imply a nontrivial `Phi` beyond the deterministic
ceilings already recorded in Module 320.

This is not a theorem that no gain exists. It says a future gain must use
information not presently encoded in the deterministic caps.

### F. Extracted open target

Define:

```text
FiberOverlapGainTarget_321(P_minor^0):
  prove a same-family estimate for Overlap_N(U,V) or Overlap_C(U,V) that
  beats the complete-concentration ceilings uniformly over all active
  cross-shell pairs J_{j,k},J_{j,l}, and whose induced Phi passes at least one
  of the Module 320 column-barrier sums.
```

Status:

```text
FiberOverlapGainTarget_321(P_minor^0):
  OPEN.
```

Possible future sources include:

```text
prime-specific residual cancellation,
same-frequency phase variation across shifts,
entropy or expansion of the large-spectrum graph,
or a localized eight-slot minor-kernel theorem.
```

None is proved here.

### G. Cadence consequence

The long-term cadence reaches its next combined checkpoint after this
iteration. The next module should be both a plan update and a plan challenge,
because the next count is divisible by both 9 and 15.

Define:

```text
PlanUpdate_15_Challenge_9_322:
  review the Phase K column branch after Modules 313-321, decide whether to
  continue through FiberOverlapGainTarget_321, switch to residual eight-slot
  minor cancellation, pause the branch, or return to a higher-level endpoint
  map.
```

Status:

```text
PlanUpdate_15_Challenge_9_322:
  OPEN next target.
```

## 6. Edge cases

If `U` or `V` is empty, the overlap vanishes. This is local vacuity, not a
uniform gain.

If row caps force `R(U)=1` or column caps force `K(U)=1`, the overlap may be
small in that special regime. A usable theorem must prove that the resulting
`Phi` survives all active `j,k,l` and the Module 320 barrier sums.

If `U=V`, the diagonal `d_1=d_2` contributes a fourth-power row. Removing it
does not control the off-diagonal concentration unless a separate
off-diagonal gain is proved.

If shell heights differ greatly, the weighted overlap changes by the visible
`lambda_k^2 lambda_l^2` factors, but common-column concentration remains
possible.

If a future argument treats the fibers as random or independent, it must
prove that independence in `P_minor^0`; it cannot be inferred from the caps.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The Phase K column branch now reads:

```text
Module 320:
  formulates the Phi criterion and shows deterministic size bounds recover
  current ceilings.

Module 321:
  audits the current data-dependent fibers and finds that the caps still
  allow complete same-frequency concentration.
```

The selected next target is:

```text
PlanUpdate_15_Challenge_9_322.
```

## 8. What remains open

Still open:

```text
PlanUpdate_15_Challenge_9_322,
FiberOverlapGainTarget_321(P_minor^0),
AdmissiblePhiGain_320(P_minor^0),
SizeSensitiveMinorKernelCriterion_320 as an estimate,
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
SignedMinorKernelGain_318(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `DataDependentFiberGainAudit_321(P_minor^0)` as a fiber-overlap
gain.

Do not cite `CompleteFiberConcentrationModel_321` as a prime counterexample.
It is only a deterministic compatibility diagnostic.

Do not claim the row/column caps, shell-height restrictions, energy tails, or
selection rules imply independence, expansion, entropy, or decorrelation.

Do not cite `FiberOverlapGainTarget_321(P_minor^0)` or
`AdmissiblePhiGain_320(P_minor^0)` as proved.

Do not use endpoint objects, projected-major targets, column-barrier closure,
selector transfer, or residual cube estimates as inputs to prove this local
fiber gain.

## 10. Next target

The next target is:

```text
Module 322:
  PlanUpdate_15_Challenge_9_322.
```

It should perform the scheduled combined plan update and plan challenge,
because the next long-term count is divisible by both 9 and 15. It should
decide whether the Phase K column branch should continue toward
`FiberOverlapGainTarget_321`, pivot to residual eight-slot minor
cancellation, or pause pending a genuinely new input.
