# Module 303: Row-square moment expansion inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the q=2 expansion selected by Module 302.

Define:

```text
RowSquareMomentExpansion_303(P_minor^0).
```

The object is the concrete square row moment:

```text
ShiftMomentP0_284(2;lambda_j)
  =
  D^(-1) sum_{D<|d|<=2D} E_{d,0}(lambda_j)^2.
```

The goal is not to prove this moment small. The goal is to identify the exact
same-shift frequency-pair kernel that a future theorem would need to control.

Verdict:

```text
RowSquareMomentExpansion_303(P_minor^0):
  STRUCTURAL / EXTRACTION.

RowSquareKernelIdentity_303(lambda_j):
  STRUCTURAL / EXTRACTION.

DiagonalFourthPowerRow_303(lambda_j):
  STRUCTURAL / EXTRACTION, with current proof routes blocked.

OffDiagonalSameShiftRow_303(lambda_j):
  OPEN.

FullFrequencyShortcut_303:
  FALSE / BLOCKED.

FixedFiberShortcut_303:
  FALSE / BLOCKED.

EndpointFourthMomentShortcut_303:
  FALSE / BLOCKED as a proof route.

SameShiftSquareKernelGain_303(P_minor^0):
  OPEN.
```

Thus Module 303 does not prove `RowSquareMomentTarget_302`. It records that
the q=2 row-square target is an exact same-shift restricted-kernel problem
over data-dependent large-spectrum fibers.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The identities below are exact inside the fixed local model `P_minor^0`.
They are not row-barrier smallness, threshold closure, a minor-arc endpoint,
or a selector-transfer theorem.

## 3. Definitions and variables

Work inside the Module 278 family:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

The residual derivative coefficients are:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi)
             = E_{n in G_N} B_d^0(n)e_N(-xi n).
```

For a fixed `lambda_j in Lambda_0`, define the large-spectrum row fiber:

```text
S_{d,j}
  =
  Spec_{d,0}^minor(lambda_j)
  =
  { xi in Minor_0(R,eta):
      |beta_0(d,xi)|>=lambda_j }.
```

Then:

```text
E_{d,0}(lambda_j)
  =
  sum_{xi in S_{d,j}} |beta_0(d,xi)|^2.
```

Define the row-fiber kernel:

```text
K_{d,j}(t)
  =
  sum_{xi in S_{d,j}} e_N(xi t).
```

This kernel is data-dependent because `S_{d,j}` depends on the residual
coefficients `beta_0(d,xi)`.

## 4. Assumptions

This module assumes Modules 278, 284, 297, 300, and 302, plus the active
status ledger.

It uses only:

```text
the finite cyclic Fourier normalization,
the definitions of S_{d,j} and E_{d,0}(lambda_j),
and algebraic expansion of beta_0(d,xi).
```

It does not assume:

```text
SameShiftSquareKernelGain_303(P_minor^0),
RowSquareMomentTarget_302,
RowTailGainTarget_302(q),
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
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

### A. Coefficient-space row-square identity

For fixed `lambda_j`, abbreviate:

```text
S_d=S_{d,j}.
```

Then:

```text
E_{d,0}(lambda_j)^2
  =
  sum_{xi_1 in S_d}
  sum_{xi_2 in S_d}
    |beta_0(d,xi_1)|^2 |beta_0(d,xi_2)|^2.
```

Therefore:

```text
ShiftMomentP0_284(2;lambda_j)
  =
  D^(-1) sum_{D<|d|<=2D}
    sum_{xi_1,xi_2 in S_d}
      |beta_0(d,xi_1)|^2 |beta_0(d,xi_2)|^2.
```

This is an identity. It supplies no smallness.

Classification:

```text
RowSquareKernelIdentity_303(lambda_j):
  STRUCTURAL / EXTRACTION.
```

### B. Diagonal and off-diagonal split

Split the pair `xi_1,xi_2` into:

```text
xi_1=xi_2,
xi_1 != xi_2.
```

The diagonal fourth-power row is:

```text
DiagRowSq_303(lambda_j)
  =
  D^(-1) sum_d
    sum_{xi in S_{d,j}} |beta_0(d,xi)|^4.
```

The off-diagonal same-shift row is:

```text
OffRowSq_303(lambda_j)
  =
  D^(-1) sum_d
    sum_{xi_1 != xi_2 in S_{d,j}}
      |beta_0(d,xi_1)|^2 |beta_0(d,xi_2)|^2.
```

Thus:

```text
ShiftMomentP0_284(2;lambda_j)
  =
  DiagRowSq_303(lambda_j)
  +
  OffRowSq_303(lambda_j).
```

The diagonal piece is contained in the minor fourth-power mass:

```text
DiagRowSq_303(lambda_j)
  <=
  D^(-1) sum_d
    sum_{xi in Minor_0(R,eta)}
      |beta_0(d,xi)|^4.
```

But using the right side as `o_W(1)` is the minor-arc fourth-moment endpoint
strength and is not an available input here. The elementary pointwise route:

```text
DiagRowSq_303(lambda_j)
  <=
  L_{N,w}^4 D^(-1) sum_d E_{d,0}(lambda_j)
```

only returns the Module 300/302 ceiling scale after insertion into the row
barrier.

So:

```text
DiagonalFourthPowerRow_303(lambda_j):
  STRUCTURAL / EXTRACTION, with current proof routes blocked.
```

The genuinely new part for q=2 is the off-diagonal same-shift row:

```text
OffDiagonalSameShiftRow_303(lambda_j):
  OPEN.
```

### C. Physical-space same-shift kernel

Expand each coefficient:

```text
beta_0(d,xi)
  =
  E_n B_d^0(n)e_N(-xi n),

conj(beta_0(d,xi))
  =
  E_m conj(B_d^0(m))e_N(xi m).
```

For two frequencies in the same row:

```text
|beta_0(d,xi_1)|^2 |beta_0(d,xi_2)|^2
  =
  E_{n_1,m_1,n_2,m_2}
    B_d^0(n_1)conj(B_d^0(m_1))
    B_d^0(n_2)conj(B_d^0(m_2))
    e_N(xi_1(m_1-n_1))
    e_N(xi_2(m_2-n_2)).
```

Summing `xi_1,xi_2` independently over `S_{d,j}` gives the exact row-square
kernel:

```text
ShiftMomentP0_284(2;lambda_j)
  =
  D^(-1) sum_{D<|d|<=2D}
  E_{n_1,m_1,n_2,m_2}
    B_d^0(n_1)conj(B_d^0(m_1))
    B_d^0(n_2)conj(B_d^0(m_2))
    K_{d,j}(m_1-n_1)
    K_{d,j}(m_2-n_2).
```

The diagonal frequency contribution is:

```text
DiagRowSq_303(lambda_j)
  =
  D^(-1) sum_d
  E_{n_1,m_1,n_2,m_2}
    B_d^0(n_1)conj(B_d^0(m_1))
    B_d^0(n_2)conj(B_d^0(m_2))
    K_{d,j}(m_1-n_1+m_2-n_2).
```

The off-diagonal contribution is:

```text
OffRowSq_303(lambda_j)
  =
  D^(-1) sum_d
  E_{n_1,m_1,n_2,m_2}
    B_d^0(n_1)conj(B_d^0(m_1))
    B_d^0(n_2)conj(B_d^0(m_2))
    [
      K_{d,j}(m_1-n_1)K_{d,j}(m_2-n_2)
      -
      K_{d,j}(m_1-n_1+m_2-n_2)
    ].
```

This is the exact same-shift restricted-kernel form. It is the q=2 row
analogue of the same-shift pair obstruction already visible in Module 271,
but now with the large-spectrum fiber `S_{d,j}` chosen separately for each
shift.

### D. Eight residual slots

Substituting:

```text
B_d^0(n)=f_0(n+d)conj(f_0(n))
```

into the row-square kernel gives the eight-slot product:

```text
f_0(n_1+d)conj(f_0(n_1))
conj(f_0(m_1+d))f_0(m_1)
f_0(n_2+d)conj(f_0(n_2))
conj(f_0(m_2+d))f_0(m_2).
```

The shift `d` is common to all four derivative factors. Therefore this is not
a generic four independent-shift rectangle. It is a same-shift eight-residual
kernel averaged over the dyadic shift shell.

Any useful estimate must respect:

```text
the same shift d in all four B factors,
the minor-arc restriction,
the data-dependent large-spectrum fiber S_{d,j},
the lambda level lambda_j,
the W-residue and cyclic conventions of P_minor^0,
and the fixed N->infinity then w->infinity order.
```

### E. Why full-frequency orthogonality is only diagnostic

If `S_{d,j}` were the full frequency group `G_N`, then:

```text
K_{d,j}(t)=K_{G_N}(t)=N 1_{t=0}.
```

The physical-space identity would collapse to full-frequency diagonal
relations such as:

```text
m_1=n_1,
m_2=n_2.
```

But in the actual row-square object:

```text
S_{d,j}
  =
  { xi in Minor_0(R,eta):
      |beta_0(d,xi)|>=lambda_j }.
```

This set is restricted and data-dependent. Hence the full-frequency diagonal
collapse is not available.

Classification:

```text
FullFrequencyShortcut_303:
  FALSE / BLOCKED.
```

### F. Why fixed-fiber estimates do not automatically apply

A fixed-set theorem would estimate kernels attached to a prescribed family:

```text
U_d subset Minor_0(R,eta)
```

chosen independently of `beta_0`.

The row-square kernel uses:

```text
U_d=S_{d,j},
```

where membership is determined by the same coefficients being estimated.
Therefore a fixed-fiber estimate would need either:

```text
uniformity over the whole admissible data-dependent class,
or a selection-transfer theorem from fixed fibers to S_{d,j}.
```

Neither input is present in the current ledger.

Classification:

```text
FixedFiberShortcut_303:
  FALSE / BLOCKED.
```

### G. Why endpoint fourth moments do not close this module

The inequality:

```text
DiagRowSq_303(lambda_j)
  <=
  D^(-1) sum_d
    sum_{xi in Minor_0(R,eta)}
      |beta_0(d,xi)|^4
```

is true. But treating the right side as small is exactly minor-arc
fourth-moment endpoint strength.

Moreover, the off-diagonal same-shift row is not controlled by the diagonal
fourth-power mass alone. It measures the simultaneous concentration of many
large frequencies in the same shift row.

Therefore:

```text
EndpointFourthMomentShortcut_303:
  FALSE / BLOCKED as a proof route.
```

### H. Extracted target

The useful q=2 target can now be stated in kernel form.

Define:

```text
SameShiftSquareKernelGain_303(P_minor^0):
  prove same-family bounds for

    D^(-1) sum_d
    E_{n_1,m_1,n_2,m_2}
      B_d^0(n_1)conj(B_d^0(m_1))
      B_d^0(n_2)conj(B_d^0(m_2))
      K_{d,j}(m_1-n_1)
      K_{d,j}(m_2-n_2)

  uniformly over lambda_j in Lambda_0,
  with enough lambda-summed saving to imply RowSquareMomentTarget_302.
```

Equivalently, find quantities `V_j` such that:

```text
ShiftMomentP0_284(2;lambda_j)^(1/2) <= V_j
```

and:

```text
sum_j lambda_j^2 (L_j C_D)^(1/2) V_j=o_W(1).
```

Status:

```text
SameShiftSquareKernelGain_303(P_minor^0):
  OPEN.
```

## 6. Edge cases

If:

```text
A_N^0=0
```

or:

```text
Lambda_0=emptyset,
```

then the row-square sums are empty for that tuple. This does not prove a
uniform q=2 row gain.

If `S_{d,j}=emptyset` for a fixed `d`, then `K_{d,j}=0` for that row. This is
local bookkeeping only.

If `S_{d,j}` has one frequency, the off-diagonal row for that fixed shift is
empty. The diagonal fourth-power row still requires control after averaging
over shifts and summing over lambda.

The two-sided normalization keeps:

```text
C_D=D^(-1)# { d:D<|d|<=2D }
```

in the later row-barrier weights. This module does not normalize it away.

The kernel `K_{d,j}` is not a smooth major/minor cutoff. It is the exact
large-spectrum fiber kernel.

Nothing here transfers from `P_minor^0` to the actual sharp moving selector.

## 7. Project-map location

The row side of the threshold branch now reads:

```text
Module 300:
  energy-only row-barrier route blocked.

Module 302:
  first-energy Markov distribution route blocked;
  endpoint fourth-moment route blocked as circular.

Module 303:
  q=2 row-square moment expanded into an exact same-shift
  data-dependent restricted-kernel problem.
```

The local implication still sought is:

```text
SameShiftSquareKernelGain_303(P_minor^0)
  => RowSquareMomentTarget_302
  => RowMomentGainTarget_300(2)
  => possible RowBarrierP0_284(2)=o_W(1).
```

Every arrow after the structural identity requires analytic estimates not
proved here.

## 8. What remains open

Still open:

```text
SameShiftSquareKernelGain_303(P_minor^0),
OffDiagonalSameShiftRow_303(lambda_j),
RowSquareMomentTarget_302,
RowTailGainTarget_302(q),
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdBudgetP0Closure_284(q,r),
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

Do not cite `RowSquareKernelIdentity_303(lambda_j)` as a bound.

Do not replace the exact data-dependent kernel `K_{d,j}` by a full-frequency
delta kernel.

Do not replace `S_{d,j}` by a fixed frequency set without a uniform theorem
or a selection-transfer row.

Do not prove the off-diagonal same-shift row by assuming:

```text
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
PhaseKernelBound_273^0,
selector transfer,
or the original selected-average problem.
```

Do not move this local row-square expansion to the actual sharp moving
selector without transfer rows.

## 10. Next target

The next scheduled iteration is the thirteenth plan update:

```text
Module 304:
  PlanUpdate_13_304.
```

That plan update should decide whether the next mathematical branch should
attempt a proof-or-blocked audit of `SameShiftSquareKernelGain_303`, or first
define a smaller fixed-fiber/selection-transfer subproblem for the kernels
`K_{d,j}`.
