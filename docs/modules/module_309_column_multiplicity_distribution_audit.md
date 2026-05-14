# Module 309: Column-multiplicity distribution audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the distributional audit selected by Module 308.

Define:

```text
ColumnMultiplicityDistributionAudit_309(P_minor^0).
```

The question is whether rewriting the column multiplicity moment through
layer-cake tails gives a genuinely smaller target than:

```text
ColumnMultiplicityGainTarget_308(r),
```

or whether the available first-moment distribution bound simply reproduces
Module 308's first-incidence ceiling.

Verdict:

```text
ColumnMultiplicityDistributionAudit_309(P_minor^0):
  STRUCTURAL / EXTRACTION.

ColumnLayerCakeIdentity_309(lambda_j):
  STRUCTURAL / EXTRACTION.

FirstMomentColumnTailBound_309(lambda_j,T):
  STRUCTURAL / EXTRACTION.

FirstMomentLayerCakeCollapse_309(r):
  FALSE / BLOCKED as a gain route.

ColumnTailGainCriterion_309(r;U):
  STRUCTURAL / EXTRACTION.

ColumnTailGainTarget_309(r):
  OPEN.

ColumnPairMultiplicityExpansion_310(P_minor^0):
  OPEN next target.
```

The layer-cake identity is exact, but first-moment tails alone do not improve
the column barriers. A future proof must supply high-multiplicity tail decay,
or an expansion of the second column moment into a same-frequency shift-pair
object that can be audited separately.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module extracts an exact distributional formulation and classifies the
current first-moment route. It proves no column-barrier smallness, no
threshold closure, no adaptive-shell gain, no minor-arc endpoint, and no
selector transfer.

## 3. Definitions and variables

Work inside:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D,
S_D=# { d:D<|d|<=2D },
C_D=S_D/D,
m_minor^0=#Minor_0(R,eta).
```

For `lambda_j in Lambda_0`, recall:

```text
Spec_{d,0}^minor(lambda_j)
  =
  { xi in Minor_0(R,eta):
      |beta_0(d,xi)|>=lambda_j },

N_{xi,0}(lambda_j)
  =
  # { d:D<|d|<=2D,
      xi in Spec_{d,0}^minor(lambda_j) }.
```

Define the column tail-count function:

```text
ColTail_{j,0}(T)
  =
  # { xi in Minor_0(R,eta):
      N_{xi,0}(lambda_j) >= T },

1 <= T <= S_D.
```

Define the first incidence count:

```text
I_{j,0}
  =
  sum_{xi in Minor_0(R,eta)} N_{xi,0}(lambda_j)
  =
  sum_{D<|d|<=2D} #Spec_{d,0}^minor(lambda_j).
```

For fixed `r>1`, let:

```text
Delta_r(T)=T^r-(T-1)^r.
```

The Module 284 column moment is:

```text
MultMomentP0_284(r;lambda_j)
  =
  D^(-1) sum_{xi in Minor_0(R,eta)}
    N_{xi,0}(lambda_j)^r.
```

Use:

```text
theta_r=(r-1)/r.
```

The two column barriers remain:

```text
ColumnBarrierP0_284(r)
  =
  sum_j lambda_j^2
    (A_N^0)^2
    (L_j m_minor^0/D)^theta_r
    MultMomentP0_284(r;lambda_j)^(1/r),

SigmaColumnBarrierP0_284(r)
  =
  sum_j lambda_j^2
    ((A_N^0)^2 MultMomentP0_284(r;lambda_j))^(1/r)
    (m_minor^0 H_j/D)^theta_r.
```

## 4. Assumptions

This module assumes Modules 278, 284, 297, 298, 299, 300, 307, and 308, plus
the active status ledger.

It uses only:

```text
integer layer-cake identities,
the first-incidence count I_{j,0},
Module 297's local second-energy bound,
and the deterministic cap N_{xi,0}(lambda_j)<=S_D.
```

It does not assume:

```text
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
MultMomentP0_284(r;lambda_j) smallness,
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
FreqRemovalBudget_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
SizeSensitiveClosure_306,
FixedFiberRowSquareGain_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
RowSquareMomentTarget_302,
RowMomentGainTarget_300(q),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
DirectShellCrossTermGain_287,
SelectionTransfer_280,
UniformFiberBound_280,
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

### A. Exact column layer-cake identity

For an integer `n>=0`:

```text
n^r
  =
  sum_{1<=T<=n} Delta_r(T).
```

Since:

```text
0 <= N_{xi,0}(lambda_j) <= S_D,
```

we obtain:

```text
sum_{xi in Minor_0(R,eta)}
  N_{xi,0}(lambda_j)^r
  =
  sum_{T=1}^{S_D}
    Delta_r(T) ColTail_{j,0}(T).
```

Therefore:

```text
MultMomentP0_284(r;lambda_j)
  =
  D^(-1) sum_{T=1}^{S_D}
    Delta_r(T) ColTail_{j,0}(T).
```

Classification:

```text
ColumnLayerCakeIdentity_309(lambda_j):
  STRUCTURAL / EXTRACTION.
```

This is an exact identity. It is not a decay estimate.

### B. First-moment column tail bound

The first incidence count gives:

```text
T ColTail_{j,0}(T)
  <=
  sum_{xi in Minor_0(R,eta)} N_{xi,0}(lambda_j)
  =
  I_{j,0}.
```

Thus:

```text
ColTail_{j,0}(T)
  <=
  min(m_minor^0, I_{j,0}/T).
```

Module 308 already extracted:

```text
I_{j,0}
  <=
  D lambda_j^(-2) E2_minor^0(D;R,eta).
```

Classification:

```text
FirstMomentColumnTailBound_309(lambda_j,T):
  STRUCTURAL / EXTRACTION.
```

This is Markov on the column multiplicity distribution. It is useful as a
diagnostic but has no high-multiplicity repulsion beyond the first moment.

### C. Layer-cake with first-moment tails collapses to Module 308

Using the cap:

```text
N_{xi,0}(lambda_j) <= S_D,
```

one has pointwise:

```text
N_{xi,0}(lambda_j)^r
  <=
  S_D^(r-1) N_{xi,0}(lambda_j).
```

Summing over `xi` gives immediately:

```text
MultMomentP0_284(r;lambda_j)
  <=
  D^(-1) S_D^(r-1) I_{j,0}.
```

Using the first-incidence energy bound:

```text
MultMomentP0_284(r;lambda_j)
  <=
  S_D^(r-1) lambda_j^(-2) E2_minor^0(D;R,eta).
```

This is exactly the Module 308 incidence ceiling, up to harmless constants.

Equivalently, using layer-cake:

```text
Delta_r(T) <= C_r T^(r-1)
```

and:

```text
ColTail_{j,0}(T) <= I_{j,0}/T
```

gives:

```text
D^(-1) sum_{T=1}^{S_D}
  Delta_r(T) ColTail_{j,0}(T)
  <=
  C_r D^(-1) I_{j,0}
    sum_{T=1}^{S_D} T^(r-2)
  <=
  C_r D^(-1) I_{j,0} S_D^(r-1).
```

The layer-cake form therefore does not beat first incidence unless the tail
bound improves on:

```text
ColTail_{j,0}(T) <= I_{j,0}/T
```

for the multiplicity range carrying the weighted sum.

Classification:

```text
FirstMomentLayerCakeCollapse_309(r):
  FALSE / BLOCKED as a gain route.
```

### D. Why the `min(m_minor^0,I/T)` refinement is not enough

The bound:

```text
ColTail_{j,0}(T)
  <=
  min(m_minor^0,I_{j,0}/T)
```

is sharper than `I/T` at very small `T`. But the `r`-moment layer cake weights
large multiplicities by approximately:

```text
T^(r-1).
```

Without extra decay for large `T`, the high end of the range up to `S_D`
still permits:

```text
sum_T Delta_r(T) ColTail_{j,0}(T)
  ~
  I_{j,0} S_D^(r-1)
```

at the scale allowed by first incidence. Thus the `min` refinement can improve
presentation but does not remove the `S_D^(r-1)` loss that feeds the Module
308 ceilings.

This is the column analogue of the row-side lesson from Module 302:
first-moment Markov distribution estimates reproduce the earlier ceiling.

### E. Distributional criterion for a real gain

Let `U_j(T)` be a proposed tail majorant satisfying:

```text
ColTail_{j,0}(T) <= U_j(T)
```

for every:

```text
lambda_j in Lambda_0,
1<=T<=S_D.
```

Define:

```text
TailMoment_U(r;lambda_j)
  =
  D^(-1) sum_{T=1}^{S_D} Delta_r(T) U_j(T).
```

The proposed tail majorant closes a column route only if at least one of:

```text
ColBarrier_U(r)
  =
  sum_j lambda_j^2
    (A_N^0)^2
    (L_j m_minor^0/D)^theta_r
    TailMoment_U(r;lambda_j)^(1/r)
  =
  o_W(1),
```

or:

```text
SigmaColBarrier_U(r)
  =
  sum_j lambda_j^2
    ((A_N^0)^2 TailMoment_U(r;lambda_j))^(1/r)
    (m_minor^0 H_j/D)^theta_r
  =
  o_W(1)
```

holds in the same `P_minor^0` family and limiting order.

Classification:

```text
ColumnTailGainCriterion_309(r;U):
  STRUCTURAL / EXTRACTION.
```

It is only a criterion. It becomes useful only after a concrete same-family
tail theorem supplies `U_j(T)` with losses compatible with the lambda sum,
dyadic ranges, W-limit order, and threshold schedules.

### F. Open tail target

Define:

```text
ColumnTailGainTarget_309(r):
  prove a same-family tail estimate for ColTail_{j,0}(T), beyond
  first-incidence Markov, strong enough to make
  min(ColBarrier_U(r), SigmaColBarrier_U(r))=o_W(1).
```

Classification:

```text
ColumnTailGainTarget_309(r):
  OPEN.
```

This is not weaker than `ColumnMultiplicityGainTarget_308(r)` unless a future
module supplies a specific structural tail mechanism. At present it is a
repackaging of the same missing high-multiplicity information.

### G. Why the next audit should use the second moment

A natural smaller test is the concrete case:

```text
r=2.
```

Then:

```text
MultMomentP0_284(2;lambda_j)
  =
  D^(-1) sum_xi N_{xi,0}(lambda_j)^2
```

counts same-frequency shift pairs:

```text
(d_1,d_2,xi)
```

such that:

```text
xi in Spec_{d_1,0}^minor(lambda_j)
and
xi in Spec_{d_2,0}^minor(lambda_j).
```

This object is still not a proof, but it is more concrete than an arbitrary
tail majorant. It can be expanded and routed into diagonal shift-pairs,
off-diagonal same-frequency shift-pairs, and possible threshold-weighted
coefficient versions.

Define the next target:

```text
ColumnPairMultiplicityExpansion_310(P_minor^0):
  expand the r=2 column multiplicity moment into exact same-frequency
  shift-pair incidence terms and audit whether any current tool gives a gain
  beyond first incidence.
```

Classification:

```text
ColumnPairMultiplicityExpansion_310(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If `A_N^0=0` or `Lambda_0=emptyset`, the relevant lambda sums are empty. This
is local vacuity, not useful threshold-window closure.

If `S_D=0`, the shift shell is empty. The active dyadic range assumes a
nonempty shell for meaningful estimates.

If `T=1`, the tail `ColTail_{j,0}(1)` counts frequencies that appear at least
once. First incidence controls it, but this says little about the large `T`
range that dominates the `r`-moment.

If `T=S_D`, the tail counts frequencies that persist across all shifts in the
dyadic shell. First incidence allows such concentrations unless a new
same-family multiplicity theorem forbids them.

If `r` varies with `N`, this module's constants and layer-cake estimates must
be re-audited. Here `r>1` is fixed.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The column branch now reads:

```text
Module 308:
  first-incidence column estimates give only barrier ceilings.

Module 309:
  layer-cake distributional rewriting is exact, but first-moment tails
  collapse back to the Module 308 ceiling.
```

The missing input can be viewed either as:

```text
ColumnMultiplicityGainTarget_308(r)
```

or as:

```text
ColumnTailGainTarget_309(r).
```

At present the second is not genuinely smaller than the first. The next
smaller concrete test is the `r=2` same-frequency shift-pair expansion.

## 8. What remains open

Still open:

```text
ColumnPairMultiplicityExpansion_310(P_minor^0),
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
MultMomentP0_284(r;lambda_j) smallness,
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
FreqRemovalBudget_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
SizeSensitiveClosure_306,
FixedFiberRowSquareGain_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
RowSquareMomentTarget_302,
RowMomentGainTarget_300(q),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `ColumnLayerCakeIdentity_309(lambda_j)` as a multiplicity gain. It
is an identity.

Do not cite `FirstMomentColumnTailBound_309(lambda_j,T)` as an `r`-moment
gain. It is Markov from first incidence.

Do not cite `FirstMomentLayerCakeCollapse_309(r)` as a theorem that no column
tail theorem can exist. It blocks only the current first-moment tail route.

Do not cite `ColumnTailGainCriterion_309(r;U)` as a verified tail theorem.

Do not cite `ColumnPairMultiplicityExpansion_310(P_minor^0)` before it is
actually written and classified.

Do not prove the column barriers by assuming:

```text
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
PhaseKernelBound_273^0,
selector transfer,
or the original selected-average problem.
```

Do not move this local `P_minor^0` audit to the actual sharp moving selector
without transfer rows.

## 10. Next target

The next target is:

```text
Module 310:
  ColumnPairMultiplicityExpansion_310(P_minor^0).
```

It should expand the concrete `r=2` column moment, classify diagonal and
off-diagonal same-frequency shift-pair terms, and decide whether the object is
smaller than the general high-multiplicity target or simply another
endpoint-strength obstruction.
