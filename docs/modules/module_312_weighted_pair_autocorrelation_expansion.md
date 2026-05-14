# Module 312: Weighted pair autocorrelation expansion inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the structural expansion selected by Module 311.

Define:

```text
WeightedPairAutocorrelationExpansion_312(P_minor^0).
```

The object is the weighted same-frequency shift-pair energy:

```text
WPair(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

The goal is not to prove this energy small. The goal is to rewrite it as an
exact two-shift autocorrelation kernel and identify what a future estimate
would need to control.

Verdict:

```text
WeightedPairAutocorrelationExpansion_312(P_minor^0):
  STRUCTURAL / EXTRACTION.

SameFrequencyAutocorrelationIdentity_312:
  STRUCTURAL / EXTRACTION.

MinorKernelDecomposition_312:
  STRUCTURAL / EXTRACTION.

FullFrequencyAntiDiagonalDiagnostic_312:
  STRUCTURAL / EXTRACTION only.

CurrentAutocorrelationToolsClose_312:
  FALSE / BLOCKED.

AntiDiagonalTwoShiftKernelGain_312(P_minor^0):
  OPEN.
```

The expansion shows that the weighted column-pair route is an anti-diagonal
two-shift autocorrelation problem with a minor-arc cutoff kernel. Current
full-frequency, absolute-kernel, and Cauchy/Parseval tools recover only the
Module 311 ceilings.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The identities below are exact inside the fixed local model `P_minor^0`. They
are not weighted column-pair smallness, threshold closure, adaptive-shell
gain, a minor-arc endpoint, or selector transfer.

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
C_D=S_D/D.
```

The residual derivative coefficients are:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi)
             = E_{n in G_N} B_d^0(n)e_N(-xi n).
```

Define the cyclic autocorrelation of `B_d^0`:

```text
A_d(h)
  =
  E_{n in G_N} B_d^0(n)conj(B_d^0(n+h)).
```

Then:

```text
|beta_0(d,xi)|^2
  =
  E_{h in G_N} A_d(h)e_N(xi h).
```

Define the exact minor-frequency kernel:

```text
K_minor^0(t)
  =
  sum_{xi in Minor_0(R,eta)} e_N(xi t).
```

If the local convention is:

```text
Minor_0(R,eta)=(G_N\{0})\Major_0(R,eta),
```

with `Major_0(R,eta)` not containing zero, also define:

```text
K_major^0(t)
  =
  sum_{xi in Major_0(R,eta)} e_N(xi t),

K_full(t)=sum_{xi in G_N} e_N(xi t)=N 1_{t=0}.
```

Then the exact partition identity is:

```text
K_minor^0(t)=K_full(t)-1-K_major^0(t).
```

If a future convention includes zero in the major set, the displayed
decomposition must be adjusted by the corresponding zero-mode convention. The
direct definition of `K_minor^0` is the invariant object.

## 4. Assumptions

This module assumes Modules 278, 284, 297, 308, 309, 310, and 311, plus the
active status ledger.

It uses only:

```text
the finite cyclic Fourier normalization,
the definitions of B_d^0, beta_0(d,xi), Minor_0(R,eta),
and finite algebraic expansion.
```

It does not assume:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
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

### A. Autocorrelation form of one squared coefficient

By definition:

```text
beta_0(d,xi)
  =
  E_n B_d^0(n)e_N(-xi n),

conj(beta_0(d,xi))
  =
  E_m conj(B_d^0(m))e_N(xi m).
```

Therefore:

```text
|beta_0(d,xi)|^2
  =
  E_{n,m}
    B_d^0(n)conj(B_d^0(m))e_N(xi(m-n)).
```

Writing `h=m-n` gives:

```text
|beta_0(d,xi)|^2
  =
  E_h A_d(h)e_N(xi h),
```

where:

```text
A_d(h)=E_n B_d^0(n)conj(B_d^0(n+h)).
```

This is an exact identity. It is not decay.

### B. Same-frequency weighted pair identity

For two shifts:

```text
|beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2
  =
  E_{h,k}
    A_{d_1}(h)A_{d_2}(k)e_N(xi(h+k)).
```

Summing over the minor frequencies gives:

```text
WPair(d_1,d_2)
  =
  E_{h,k in G_N}
    A_{d_1}(h)A_{d_2}(k)K_minor^0(h+k).
```

Equivalently, in the original physical variables:

```text
WPair(d_1,d_2)
  =
  E_{n_1,m_1,n_2,m_2}
    B_{d_1}^0(n_1)conj(B_{d_1}^0(m_1))
    B_{d_2}^0(n_2)conj(B_{d_2}^0(m_2))
    K_minor^0((m_1-n_1)+(m_2-n_2)).
```

Classification:

```text
SameFrequencyAutocorrelationIdentity_312:
  STRUCTURAL / EXTRACTION.
```

This is the exact same-frequency analogue of the same-shift kernel in Module
303. The coupling is now:

```text
h+k
```

rather than two independent row-fiber kernels.

### C. Minor-kernel decomposition

Under the standard local partition:

```text
Minor_0(R,eta)=(G_N\{0})\Major_0(R,eta),
```

the exact kernel decomposition is:

```text
K_minor^0(t)=N 1_{t=0}-1-K_major^0(t).
```

Thus:

```text
WPair(d_1,d_2)
  =
  N E_h A_{d_1}(h)A_{d_2}(-h)
  -
  E_{h,k} A_{d_1}(h)A_{d_2}(k)
  -
  E_{h,k} A_{d_1}(h)A_{d_2}(k)K_major^0(h+k).
```

Classification:

```text
MinorKernelDecomposition_312:
  STRUCTURAL / EXTRACTION.
```

This is only an exact partition. It does not say that the full-frequency,
zero-mode, and major-arc pieces are individually small or that their
difference has cancellation at the required scale.

### D. Full-frequency anti-diagonal diagnostic

If the minor cutoff were replaced by the full frequency group, the kernel
would be:

```text
K_full(t)=N 1_{t=0}.
```

The weighted pair would collapse to the anti-diagonal autocorrelation form:

```text
sum_{xi in G_N} |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2
  =
  N E_h A_{d_1}(h)A_{d_2}(-h).
```

This diagnostic is useful because it shows the geometry of the same-frequency
pair: the two increments must satisfy:

```text
(m_1-n_1)+(m_2-n_2)=0 mod N.
```

Classification:

```text
FullFrequencyAntiDiagonalDiagnostic_312:
  STRUCTURAL / EXTRACTION only.
```

It is not a minor-arc estimate. Replacing `K_minor^0` by `K_full` loses the
major-arc subtraction, the zero-mode convention, and the actual minor cutoff.

### E. Eight residual slots and collision load

Substituting:

```text
B_d^0(n)=f_0(n+d)conj(f_0(n))
```

into the physical form gives the eight-slot product:

```text
f_0(n_1+d_1)conj(f_0(n_1))
conj(f_0(m_1+d_1))f_0(m_1)
f_0(n_2+d_2)conj(f_0(n_2))
conj(f_0(m_2+d_2))f_0(m_2),
```

weighted by:

```text
K_minor^0((m_1-n_1)+(m_2-n_2)).
```

For the off-diagonal column-pair row, `d_1 != d_2`. The expansion therefore
has:

```text
two derivative shifts,
one same-frequency anti-diagonal relation,
the minor-arc cutoff kernel,
and many possible residual collision strata among the eight slots.
```

A future estimate must treat these collisions inside the same local family.
It cannot borrow endpoint fourth-moment control or assume a generic local
model that has not been matched to this projection, cutoff, W-residue, and
limiting order.

### F. Why current tools still do not close the weighted pair row

The exact identity allows several immediate but non-closing bounds.

First, using:

```text
|K_minor^0(t)| <= #Minor_0(R,eta)
```

gives only an absolute-kernel ceiling. After summing `d_1,d_2`, this does not
beat the concentration scenario already exposed by Module 311.

Second, replacing `K_minor^0` by `K_full` is only diagnostic. It no longer
estimates the minor projection, and the anti-diagonal term:

```text
N E_h A_{d_1}(h)A_{d_2}(-h)
```

has no same-family saving in the current ledger.

Third, estimating the autocorrelations by Cauchy-Schwarz gives back the two
ceilings from Module 311:

```text
WOff_311 <= D(E2_minor^0)^2,
WOff_311 <= C_D D F4_minor^0.
```

Therefore:

```text
CurrentAutocorrelationToolsClose_312:
  FALSE / BLOCKED.
```

This blocks only the current full-frequency, absolute-kernel, and
Cauchy/Parseval routes. It is not a proof that no anti-diagonal two-shift
theorem can exist.

### G. Extracted target

The next analytic target is now sharper than the weighted-pair name alone.

Define:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0):
  prove a same-family estimate for

    D^(-1) sum_{d_1 != d_2}
      E_{h,k}
        A_{d_1}(h)A_{d_2}(k)K_minor^0(h+k)

  strong enough, after the Module 310 threshold conversion and Module 284
  column-barrier weights, to beat the first-incidence ceiling.
```

The estimate must be uniform over:

```text
dyadic shift shells,
minor arc parameters R,eta,
threshold grid Lambda_0,
W-residue b mod W,
the fixed N -> infinity then w -> infinity order,
and the declared selector class of P_minor^0.
```

Status:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0):
  OPEN.
```

This target is still local to `P_minor^0`. It is not actual sharp moving
selector transfer and does not prove the residual cube endpoint.

## 6. Edge cases

If `Minor_0(R,eta)` is empty, then `K_minor^0=0` and `WPair(d_1,d_2)=0` for
that local tuple. This is local vacuity, not a uniform column-barrier theorem.

If `d_1=d_2`, the expansion gives the diagonal fourth-power row
`F_d^minor`; the column-pair obstruction from Module 310 is the off-diagonal
case `d_1 != d_2`.

If `h+k=0`, the full-frequency diagnostic has support, but the actual minor
kernel is `N-1-K_major^0(0)` under the displayed partition. The major and
zero pieces cannot be discarded without proof.

If `h=0` or `k=0`, the autocorrelation contains local `|B_d^0|^2` mass. These
are possible diagonal or near-diagonal strata, not automatic savings.

If a future theorem controls only a fixed pair `d_1,d_2`, it still must be
summed over the off-diagonal dyadic shift shell with the exact normalization
`D^(-1)`.

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

Module 312:
  weighted pair energy expands to an exact anti-diagonal two-shift
  autocorrelation kernel with the minor cutoff K_minor^0.
```

The local implication still sought is:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0)
  => WeightedColumnSecondMomentTarget_311(P_minor^0)
  => WeightedColumnPairEnergyTarget_310(P_minor^0)
  => possible progress on the Module 284 column barriers.
```

Every arrow after the structural identity requires analytic estimates not
proved here.

## 8. What remains open

Still open:

```text
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
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

Do not cite `SameFrequencyAutocorrelationIdentity_312` as a weighted
column-pair gain. It is an identity.

Do not cite `MinorKernelDecomposition_312` as cancellation between full,
zero, and major pieces.

Do not replace the exact minor kernel `K_minor^0` by the full-frequency
anti-diagonal kernel without a theorem controlling the zero and major
corrections.

Do not cite `FullFrequencyAntiDiagonalDiagnostic_312` as a minor-arc
estimate.

Do not cite `CurrentAutocorrelationToolsClose_312` as a theorem that no
anti-diagonal two-shift route can exist. It blocks only the current tools.

Do not cite `AntiDiagonalTwoShiftKernelGain_312(P_minor^0)` as proved.

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

Do not move this local `P_minor^0` expansion to the actual sharp moving
selector without transfer rows.

## 10. Next target

The next scheduled iteration is the fourteenth plan update:

```text
Module 313:
  PlanUpdate_14_313.
```

That update should decide whether to attack
`AntiDiagonalTwoShiftKernelGain_312(P_minor^0)` directly, first separate
minor-kernel full/zero/major rows, or pause the column branch if the target is
already endpoint-strength under the current local toolkit.
