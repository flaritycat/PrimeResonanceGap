# Module 311: Weighted column-pair energy audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module audits the weighted coefficient-pair criterion isolated in Module
310.

Define:

```text
WeightedColumnPairEnergyAudit_311(P_minor^0).
```

The question is whether the weighted pair energy:

```text
WPair(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2
```

is smaller than the unweighted column multiplicity problem under current
Parseval/Cauchy inputs, or whether it again gives only ceiling-scale bounds.

Verdict:

```text
WeightedColumnPairEnergyAudit_311(P_minor^0):
  STRUCTURAL / EXTRACTION.

EnergySquareWPairCeiling_311:
  STRUCTURAL / EXTRACTION.

FourthPowerWPairCeiling_311:
  STRUCTURAL / EXTRACTION.

WeightedCurrentToolsClose_311:
  FALSE / BLOCKED.

WeightedColumnSecondMomentTarget_311(P_minor^0):
  OPEN.

WeightedPairAutocorrelationExpansion_312(P_minor^0):
  OPEN next target.
```

Current Cauchy/Parseval estimates do not prove a weighted off-diagonal gain.
They recover large energy-square ceilings. The weighted route remains open,
but it now needs structural expansion rather than another first-moment
distribution pass.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is an audit of a possible weighted route. It proves no column-barrier
smallness, no threshold closure, no adaptive-shell gain, no minor-arc endpoint,
and no selector transfer.

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
L_{N,w}=1+log(WN+b).
```

The local Fourier coefficients are:

```text
beta_0(d,xi)=widehat{B_d^0}(xi),
B_d^0(n)=f_0(n+d)conj(f_0(n)).
```

Define the minor-arc row energy:

```text
E_d^minor
  =
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d,xi)|^2,

E2_minor^0(D;R,eta)
  =
  D^(-1) sum_d E_d^minor.
```

Define the row fourth energy:

```text
F_d^minor
  =
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d,xi)|^4,

F4_minor^0(D;R,eta)
  =
  D^(-1) sum_d F_d^minor.
```

Define the weighted same-frequency pair energy:

```text
WPair(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2,
```

and its off-diagonal shift-pair average:

```text
WOff_311
  =
  D^(-1) sum_{d_1 != d_2} WPair(d_1,d_2).
```

Module 310's threshold conversion says:

```text
PairOff_310(lambda_j)
  <=
  lambda_j^(-4) WOff_311.
```

Thus a weighted pair route must make `WOff_311`, after the
`lambda_j^(-4)` conversion and Module 284 column-barrier weights, smaller
than the first-incidence ceilings.

## 4. Assumptions

This module assumes Modules 278, 284, 297, 298, 299, 300, 307, 308, 309, and
310, plus the active status ledger.

It uses only:

```text
Module 297's local second-energy and pointwise logarithmic bounds,
Cauchy-Schwarz,
Parseval-type row energy bookkeeping,
and finite sums.
```

It does not assume:

```text
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
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

### A. Energy-square ceiling

For every shift pair:

```text
WPair(d_1,d_2)
  <=
  E_{d_1}^minor E_{d_2}^minor.
```

Therefore:

```text
WOff_311
  <=
  D^(-1)
  (
    sum_d E_d^minor
  )^2
  =
  D (E2_minor^0(D;R,eta))^2.
```

Module 297 gives:

```text
E2_minor^0(D;R,eta) <= C_D L_{N,w}^4.
```

Hence:

```text
WOff_311
  <=
  C_D^2 D L_{N,w}^8.
```

Classification:

```text
EnergySquareWPairCeiling_311:
  STRUCTURAL / EXTRACTION.
```

This is a valid ceiling. It is not a gain. After the Module 310 conversion:

```text
PairOff_310(lambda_j)
  <=
  lambda_j^(-4) D (E2_minor^0)^2,
```

which is useful only if the extra factor `E2_minor^0/lambda_j^2` is small
enough compared with the first-incidence scale. The declared local family does
not force that uniformly over the dyadic lambda grid.

### B. Fourth-power Cauchy ceiling

Cauchy-Schwarz gives:

```text
WPair(d_1,d_2)
  <=
  (F_{d_1}^minor)^(1/2)
  (F_{d_2}^minor)^(1/2).
```

Thus:

```text
WOff_311
  <=
  D^(-1)
  (
    sum_d (F_d^minor)^(1/2)
  )^2.
```

Applying Cauchy over the shift shell:

```text
(
  sum_d (F_d^minor)^(1/2)
)^2
  <=
  S_D sum_d F_d^minor.
```

Therefore:

```text
WOff_311
  <=
  C_D D F4_minor^0(D;R,eta).
```

The current pointwise envelope gives:

```text
F_d^minor
  <=
  (A_N^0)^2 E_d^minor
  <=
  L_{N,w}^4 E_d^minor.
```

Consequently:

```text
F4_minor^0(D;R,eta)
  <=
  L_{N,w}^4 E2_minor^0(D;R,eta)
  <=
  C_D L_{N,w}^8,
```

and again:

```text
WOff_311
  <=
  C_D^2 D L_{N,w}^8.
```

Classification:

```text
FourthPowerWPairCeiling_311:
  STRUCTURAL / EXTRACTION.
```

This route would become meaningful only if a same-family average fourth-power
row estimate for the minor coefficients were supplied. That is not available
in the current ledger and cannot be assumed inside a module meant to reduce
the minor endpoint.

### C. Weighted column second moment formulation

The full weighted pair sum can be written as:

```text
sum_{d_1,d_2} WPair(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    (
      sum_d |beta_0(d,xi)|^2
    )^2.
```

Thus the weighted route is a column second moment, but now for the weights:

```text
M_xi
  =
  sum_d |beta_0(d,xi)|^2.
```

The first moment is:

```text
sum_xi M_xi
  =
  sum_d E_d^minor
  =
  D E2_minor^0(D;R,eta).
```

Without a distribution theorem for the weighted columns `M_xi`, this second
moment can concentrate on few frequencies and is not controlled by the first
moment at the needed strength.

Define:

```text
WeightedColumnSecondMomentTarget_311(P_minor^0):
  a same-family estimate for
    sum_xi (sum_d |beta_0(d,xi)|^2)^2
  strong enough, after the Module 310 threshold conversion and Module 284
  column-barrier weights, to beat the first-incidence ceiling.
```

Classification:

```text
WeightedColumnSecondMomentTarget_311(P_minor^0):
  OPEN.
```

### D. Current-tools verdict

The current weighted route has two visible estimates:

```text
WOff_311 <= D(E2_minor^0)^2,
WOff_311 <= C_D D F4_minor^0.
```

With only Module 297:

```text
E2_minor^0 <= C_D L_{N,w}^4,
F4_minor^0 <= C_D L_{N,w}^8.
```

Both estimates give:

```text
WOff_311 <= C_D^2 D L_{N,w}^8.
```

After multiplication by `lambda_j^(-4)`, this does not force a useful
column-barrier contribution for the full dyadic lambda grid. In particular,
small lambda levels make the conversion loss severe, and the active family
does not include a compensating weighted-column distribution theorem.

Therefore:

```text
WeightedCurrentToolsClose_311:
  FALSE / BLOCKED.
```

This is not a disproof of a weighted pair route. It says only that current
Parseval/Cauchy inputs recover ceilings.

### E. Why the next step should be structural

Repeating first-moment distribution language for:

```text
M_xi=sum_d |beta_0(d,xi)|^2
```

would reproduce the same concentration problem. The next useful question is
not another Markov audit. It is whether `WPair(d_1,d_2)` has an exact physical
or autocorrelation expansion that connects it to a previously named phase
kernel, diagonal class, or genuinely new local obstruction.

Define:

```text
WeightedPairAutocorrelationExpansion_312(P_minor^0):
  expand WPair(d_1,d_2) using autocorrelation kernels of B_d^0 and the
  minor-arc frequency cutoff, then classify the resulting physical rows.
```

Classification:

```text
WeightedPairAutocorrelationExpansion_312(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If `Minor_0(R,eta)` is empty, the weighted pair energy is zero locally. That
is a degenerate local case, not a minor-arc theorem.

If `Lambda_0` is empty, the threshold conversion is vacuous. This is not a
useful column-barrier closure.

If `d_1=d_2`, the weighted pair energy becomes `F_d^minor`; Module 310's
column obstruction is the off-diagonal shift-pair row.

If a future estimate controls only:

```text
sum_xi M_xi,
```

it is only first weighted incidence and does not control the second weighted
column moment.

If a future fourth-power estimate is supplied, it must be same-family,
non-endpoint, and compatible with the lambda weights, W-limit order, dyadic
ranges, and threshold schedules.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The column branch now reads:

```text
Module 308:
  first-incidence column estimates give only barrier ceilings.

Module 309:
  layer-cake with first-moment tails collapses back to first incidence.

Module 310:
  r=2 column multiplicity becomes same-frequency shift-pair incidence.

Module 311:
  weighted coefficient-pair energy still gives only current-tool ceilings.
```

The next smaller question is structural:

```text
WeightedPairAutocorrelationExpansion_312(P_minor^0).
```

It may reveal a known phase-kernel row, a routed diagonal class, or simply a
new open weighted-pair obstruction. It must not be treated as a proof in
advance.

## 8. What remains open

Still open:

```text
WeightedPairAutocorrelationExpansion_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
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

Do not cite `EnergySquareWPairCeiling_311` or
`FourthPowerWPairCeiling_311` as weighted column-pair smallness.

Do not cite `WeightedCurrentToolsClose_311` as a theorem that no weighted
pair route can exist. It blocks only the current Cauchy/Parseval route.

Do not cite `WeightedColumnSecondMomentTarget_311(P_minor^0)` or
`WeightedPairAutocorrelationExpansion_312(P_minor^0)` as proved.

Do not import a fourth-moment endpoint estimate to close the weighted pair
row.

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
Module 312:
  WeightedPairAutocorrelationExpansion_312(P_minor^0).
```

It should expand the weighted same-frequency pair energy through
autocorrelation kernels and the minor-arc cutoff, then classify whether the
result is a routed diagonal, a known phase-kernel object, or a new open row.
