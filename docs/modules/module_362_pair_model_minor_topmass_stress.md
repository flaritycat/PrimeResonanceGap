# Module 362: Pair-model minor top-mass stress test

## 1. Precise theorem / claim being advanced

Chosen attack mode:

```text
F. Counter-route with a sharper equivalent formulation.
```

Module 361 showed that the mixed pair-residual row
`|E_+^0K_+^0|` cannot be closed from pair-residual energy alone. It also needs
minor-frequency top-mass control for the exact pair-model coefficient:

```text
K_+^0(xi)
  =
  E_{a in G_N} kappa_w^0(a)e_N(xi a).
```

This module attacks:

```text
PairModelMinorTopMassTarget_361(P_minor^0).
```

Define:

```text
PairModelMinorTopMassStress_362(P_minor^0).
```

Verdict:

```text
PairModelMinorTopMassStress_362(P_minor^0):
  STRUCTURAL / EXTRACTION.

LowDenominatorMinorLeakageLemma_362:
  PROVEN.

DiagonalAtomLeakageLemma_362:
  PROVEN.

PairModelExpansionCriterion_362:
  CONDITIONAL.

CurrentPairModelMinorTopMassClosure_362:
  FALSE / BLOCKED.

PairModelRamanujanTailTarget_362:
  OPEN.

PairModelDiagonalConventionGate_362:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful extraction is that `K_+^0` is harmless on minor arcs only after an
exact denominator expansion and tail/diagonal convention are supplied. Low
denominator terms leak only weakly into the declared minor arcs, but high
denominator tails and diagonal atoms are not controlled by that observation.

## 2. Why this would advance the main theorem

The active no-twist branch now contains:

```text
PairResidualLargeValueStress_361
  -> PairModelMinorTopMassTarget_361
  -> mixed coefficient row |E_+^0K_+^0|
  -> coefficient top-mass / no-twist profile correlation
  -> SignedLocalModelInsertion_326.
```

If the exact pair-model coefficient were automatically small on minor arcs,
then Module 361's mixed row would reduce mostly to pair-residual energy.
This module shows the actual state is more delicate: minor smallness requires
a valid low-denominator expansion, a high-denominator tail estimate, and a
diagonal convention for `a=0`.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0}.
```

Use:

```text
e_N(t)=exp(2 pi i t/N),
e_q(t)=exp(2 pi i t/q).
```

The exact pair-model coefficient from Module 351 is:

```text
kappa_w^0(a)
  =
  prod_{p>w}
    (1-1/p)^(-2)
    (1-#({0,a} mod p)/p),

K_+^0(xi)
  =
  E_{a in G_N} kappa_w^0(a)e_N(xi a).
```

For a nonnegative coefficient `c(xi)`, define:

```text
A_star,c(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E} c(xi).
```

The active top-mass scale is:

```text
m_{U,V}=ceil(min(I_U/K_U,I_V/K_V)).
```

## 4. Assumptions

This module assumes:

```text
Modules 350, 351, 359, 360, and 361,
the P_minor^0 major/minor convention from Module 278,
finite cyclic Fourier algebra,
and the active status ledger.
```

It does not assume:

```text
PairModelMinorTopMassTarget_361,
PairModelRamanujanTailTarget_362,
PairModelDiagonalConventionGate_362,
PairResidualFourierEnergyTarget_361,
PairResidualLargeValueTarget_359,
CoefficientTopMassProfileCriterion_356 as a proved estimate,
NoTwistColumnProfileCorrelation_356,
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
actual sharp moving-selector transfer,
full-gap transfer,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

Forbidden shortcuts:

```text
exact pair-model coefficient is automatically minor-small,
low denominator expansion controls high denominator tail,
diagonal pair atom is harmless without a convention,
major-arc support in an infinite model transfers for free to G_N.
```

## 5. Proof / disproof / reduction

### A. Low-denominator minor leakage lemma

Let:

```text
1 <= Q <= R.
```

Let `H_Q:G_N -> C` be a finite denominator model:

```text
H_Q(a)
  =
  sum_{1<=q<=Q}
  sum_{r in (Z/qZ)^*}
    gamma_{q,r} e_q(r a).
```

Define:

```text
H_{Q,+}(xi)=E_{a in G_N} H_Q(a)e_N(xi a).
```

For every:

```text
xi in Minor_0(R,eta),
```

one has:

```text
|H_{Q,+}(xi)|
  <=
  (1/(2N eta))
  sum_{1<=q<=Q}
    q sum_{r in (Z/qZ)^*} |gamma_{q,r}|.
```

Proof:

For a fixed `(q,r)`, the finite average is:

```text
E_{a in G_N} e_q(r a)e_N(xi a)
  =
  N^(-1) sum_{a=0}^{N-1}
    exp(2 pi i a(r/q+xi/N)).
```

The standard geometric-sum bound gives:

```text
|N^(-1) sum_{a=0}^{N-1} exp(2 pi i a theta)|
  <=
  min(1, 1/(2N ||theta||_{R/Z})).
```

Since `xi` is minor and `q<=Q<=R`, the rational point `-r/q` is one of the
excluded major-arc centers. Hence:

```text
||xi/N + r/q||_{R/Z} > eta/q.
```

Therefore:

```text
|E_a e_q(r a)e_N(xi a)|
  <=
  q/(2N eta).
```

Summing with absolute values proves the bound.

Classification:

```text
LowDenominatorMinorLeakageLemma_362:
  PROVEN.
```

This lemma is finite Fourier algebra. It does not prove that `kappa_w^0`
has the displayed expansion or that the tail is small.

### B. Conditional pair-model expansion criterion

Suppose, with a specified diagonal convention, that:

```text
kappa_w^0(a)=H_Q(a)+T_Q(a)
```

where:

```text
Q <= R,
H_Q(a)
  =
  sum_{q<=Q}
  sum_{r in (Z/qZ)^*}
    gamma_{q,r} e_q(r a),
T_{Q,+}(xi)=E_a T_Q(a)e_N(xi a).
```

Let:

```text
L_Q
  =
  (1/(2N eta))
  sum_{q<=Q} q sum_{r in (Z/qZ)^*}|gamma_{q,r}|,

Tau_Q
  =
  sup_{xi in Minor_0(R,eta)} |T_{Q,+}(xi)|.
```

Then:

```text
sup_{xi in Minor_0(R,eta)} |K_+^0(xi)|
  <=
  L_Q+Tau_Q.
```

Consequently:

```text
A_star,|K_+^0|^2(m_{U,V})
  <=
  m_{U,V}(L_Q+Tau_Q)^2.
```

Inserted into the Module 361 mixed criterion, the mixed pair-residual/model
row follows if:

```text
D^(-1)K_UK_V
  (
    E_a |E_pair^0(a)|^2
  )^(1/2)
  m_{U,V}^{1/2}
  (L_Q+Tau_Q)
  =
  o_W(1).
```

Classification:

```text
PairModelExpansionCriterion_362:
  CONDITIONAL.
```

The implication is finite and proved. The expansion, diagonal convention,
and tail estimate are not proved here.

### C. Diagonal atom leakage lemma

Let:

```text
D_B(a)=B 1_{a=0}.
```

Then for every frequency `xi`:

```text
(D_B)_+(xi)
  =
  E_a B 1_{a=0} e_N(xi a)
  =
  B/N.
```

Therefore:

```text
A_star,|(D_B)_+|^2(m)
  =
  min(m,#Minor_0(R,eta)) B^2/N^2.
```

Classification:

```text
DiagonalAtomLeakageLemma_362:
  PROVEN.
```

A diagonal atom is not major-arc supported. It leaks uniformly into all
frequencies. Thus any use of `K_+^0` must specify how the pair diagonal
`a=0` is removed, renormalized, truncated, or separately bounded.

### D. Why current pair-model harmlessness is blocked

The project currently has exact definitions:

```text
kappa_w^0(a),
K_+^0(xi).
```

It does not yet provide all of:

```text
1. an exact finite-cyclic denominator expansion for kappa_w^0,
2. a diagonal convention for a=0,
3. a high-denominator tail bound Tau_Q on Minor_0(R,eta),
4. a range relation making L_Q small enough against K_U,K_V,m_{U,V},
5. compatibility with the fixed P_minor^0 W-order and residue convention.
```

The low-denominator lemma shows why the pair model should be major-arc
concentrated after such a package is supplied. It does not supply the package.

Classification:

```text
CurrentPairModelMinorTopMassClosure_362:
  FALSE / BLOCKED.

PairModelRamanujanTailTarget_362:
  OPEN.

PairModelDiagonalConventionGate_362:
  OPEN.
```

## 6. Edge cases

### Boundary frequencies

Module 278 assigns major arcs using a non-strict inequality. The leakage
lemma uses that minor frequencies satisfy the strict complementary distance
condition. A buffered convention would require restating the bound with the
buffered `eta`.

### Denominators above `R`

The proof only controls denominators `q<=Q<=R`. Denominators above `R` are
part of the tail `T_Q`, not part of the low-denominator leakage estimate.

### Pair diagonal `a=0`

If the pair diagonal is retained as a large atom, it contributes to every
frequency. This is not a prime theorem; it is a finite Fourier fact showing
that a diagonal convention is not optional.

### Cyclic versus integer divisibility

The formal pair singular series is naturally an integer-shift object. The
coefficient `K_+^0` is cyclic over `G_N`. Moving from one to the other is a
range and boundary convention, not an automatic identity.

## 7. Project-map location

```text
PairResidualLargeValueStress_361
  -> PairModelMinorTopMassStress_362
  -> PairModelDiagonalConventionAudit_363.
```

This module attacks the exact pair-model part of the mixed pair-residual row.
It identifies the denominator-expansion, tail, and diagonal gates needed
before `K_+^0` can be treated as harmless on minor arcs.

## 8. What remains open

Still open:

```text
PairModelDiagonalConventionAudit_363(P_minor^0),
PairModelRamanujanTailTarget_362,
PairModelDiagonalConventionGate_362,
PairModelMinorTopMassTarget_361,
PairResidualFourierEnergyTarget_361,
AntiDiagonalRectangleVarianceTarget_360,
RectangleDefectLargeValueTarget_359,
PairResidualLargeValueTarget_359,
DiagonalOverlapLargeValueTarget_359,
CoefficientTopMassProfileCriterion_356 as an estimate,
NoTwistColumnProfileCorrelation_356(P_minor^0),
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
full-gap transfer,
the all-alpha theorem,
and the original selected-average problem.
```

## 9. Red-team audit

Selector check:

```text
All statements remain inside P_minor^0. No actual sharp moving-selector
statement is proved.
```

Gap-object check:

```text
No full-gap, clipped-gap, tail, or empty-interval statement is used.
```

Local-factor check:

```text
The exact pair model kappa_w^0 is retained. No rectangle factor is replaced
by a pair product, and no high-denominator tail is discarded.
```

Limit-order check:

```text
The leakage lemmas are finite cyclic estimates. No N/w/D/R/eta/cutoff limit
is exchanged.
```

Uniformity check:

```text
The criterion names the required uniform expansion and tail estimates but
does not prove them.
```

Endpoint-circularity check:

```text
The proof does not assume PhaseKernelBound_273^0, NarrowMinorArc_3^B,
ResCube_3^sharp, CPC_3^sharp, RBDH_pair_short, or AU^3.
```

Official status check:

```text
No README, global status, or theorem-status index theorem claim is upgraded.
```

## 10. Final classification

```text
PairModelMinorTopMassStress_362(P_minor^0):
  STRUCTURAL / EXTRACTION.

LowDenominatorMinorLeakageLemma_362:
  PROVEN.

DiagonalAtomLeakageLemma_362:
  PROVEN.

PairModelExpansionCriterion_362:
  CONDITIONAL.

CurrentPairModelMinorTopMassClosure_362:
  FALSE / BLOCKED.

PairModelRamanujanTailTarget_362:
  OPEN.

PairModelDiagonalConventionGate_362:
  OPEN.
```

Do not cite this module as a proof that `K_+^0` is minor-small. It proves
only the finite leakage mechanism and isolates the missing expansion, tail,
and diagonal gates.

## Red flags / forbidden upgrades

- Do not treat a low-denominator expansion as complete without a tail bound.
- Do not ignore the pair diagonal `a=0`.
- Do not move from integer-shift singular series to cyclic `G_N` coefficients
  without a range convention.
- Do not use pair-model minor smallness as an input unless the expansion,
  tail, and diagonal gates are supplied.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
