# Module 297: `E2` minor energy-tail audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the low-level second-energy audit selected by Module 296.

Define:

```text
E2MinorEnergyTailAudit_297(P_minor^0).
```

The audit proves the local fourth-moment low-level tail inside the fixed
`P_minor^0` model:

```text
LowLevelFourthMomentTailP0_297:
  M_low,0(D;R,eta)=o_W(1).
```

More explicitly, it proves:

```text
LowLevelEnergyTailTarget_296(P_minor^0):
  (A_N^0)^2 N^{-2 kappa_lambda}
    E2_minor^0(D;R,eta)=o_W(1)
```

for the `P_minor^0` W-cyclic prime-only model and the declared limiting order
`N -> infinity` first with fixed `w`, then `w -> infinity`.

This closes only the local fourth-moment low-level tail. It does not close
the threshold package, shift/frequency removals, side package, adaptive shell
target, minor-arc theorem, residual cube endpoint, or the original problem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module is an audit with one local proved subrow:

```text
LowLevelFourthMomentTailP0_297:
  PROVEN inside P_minor^0.
```

The module status remains structural because the surrounding side package and
endpoint routes remain open.

## 3. Definitions and variables

Work in the Module 278 family:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
W=W(w)=prod_{p<=w}p,
G_N=Z/NZ,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

The local weight is:

```text
nu_0(n)
  = (phi(W)/W) log(Wn+b) 1_{Wn+b is prime},

f_0(n)=nu_0(n)-1.
```

The residual derivative coefficient is:

```text
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi),
```

with normalized Fourier transform on `G_N`.

The low-level cutoff and second energy are:

```text
A_N^0=sup_{D<|d|<=2D, xi in widehat{G_N}} |beta_0(d,xi)|,
lambda_min=A_N^0 N^{-kappa_lambda},

E2_minor^0(D;R,eta)
  =
  D^(-1) sum_{D<|d|<=2D}
    sum_{xi in Minor_0(R,eta)}
      |beta_0(d,xi)|^2.
```

The low-level fourth-moment piece is:

```text
M_low,0(D;R,eta)
  =
  D^(-1) sum_{D<|d|<=2D}
    sum_{xi in Minor_0(R,eta), |beta_0(d,xi)|<lambda_min}
      |beta_0(d,xi)|^4.
```

## 4. Assumptions

This module assumes only Modules 203, 278, 296, and the active status ledger.

It uses:

```text
normalized Parseval on G_N,
the explicit P_minor^0 prime-only W-cyclic model,
the fixed-w then N->infinity limiting order,
and the trivial pointwise logarithmic envelope for nu_0.
```

It does not assume:

```text
ThresholdBudgetP0_283,
ThresholdBudgetP0Closure_284(q,r),
ShiftRemovalBudget_284(q),
FreqRemovalBudget_284(r),
RowShellBudget_284,
ColumnShellBudget_284,
SigmaColumnShellBudget_284,
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
DegRowsP0Small_282,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransIncBound_269,
MinorArcTransfer_3^B,
NarrowMinorArc_3^B,
selector transfer,
ProjectedModelNeutrality_3^major,
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof

### A. Pointwise logarithmic envelope

For fixed `w`, fixed `W`, and `0<=n<N`, define:

```text
L_{N,w}=1+log(WN+b).
```

Since:

```text
0 <= phi(W)/W <= 1,
0 <= Wn+b <= WN+b,
```

the local weight satisfies:

```text
|nu_0(n)| <= log(WN+b)
```

whenever `Wn+b` is prime, and `nu_0(n)=0` otherwise. Hence:

```text
|f_0(n)|=|nu_0(n)-1| <= L_{N,w}.
```

Therefore:

```text
|B_d^0(n)|
  =
  |f_0(n+d)f_0(n)|
  <= L_{N,w}^2
```

for every cyclic shift `d`.

### B. Fourier envelope bound

By the normalized Fourier definition:

```text
|beta_0(d,xi)|
  =
  |E_{n in G_N} B_d^0(n)e_N(-xi n)|
  <=
  E_{n in G_N}|B_d^0(n)|
  <=
  L_{N,w}^2.
```

Thus:

```text
A_N^0 <= L_{N,w}^2.
```

### C. Parseval second-energy bound

For each fixed `d`, normalized Parseval gives:

```text
sum_{xi in widehat{G_N}} |beta_0(d,xi)|^2
  =
  E_{n in G_N} |B_d^0(n)|^2.
```

Since `Minor_0(R,eta)` is a subset of `widehat{G_N}`:

```text
sum_{xi in Minor_0(R,eta)} |beta_0(d,xi)|^2
  <=
  E_{n in G_N}|B_d^0(n)|^2
  <=
  L_{N,w}^4.
```

Averaging over the two-sided dyadic shift range gives:

```text
E2_minor^0(D;R,eta)
  <=
  C_D L_{N,w}^4,
```

where:

```text
C_D=D^(-1)# { d:D<|d|<=2D }.
```

The dyadic range gives `C_D=O(1)` uniformly in `D`.

### D. Low-level energy-tail target

Combining the previous estimates:

```text
(A_N^0)^2 N^{-2 kappa_lambda} E2_minor^0(D;R,eta)
  <=
  C_D L_{N,w}^8 N^{-2 kappa_lambda}.
```

For fixed `w`, the quantity `L_{N,w}` grows logarithmically in `N`, while
`kappa_lambda>0` is fixed in `P_minor^0`. Hence:

```text
C_D L_{N,w}^8 N^{-2 kappa_lambda} -> 0
```

as `N -> infinity`, uniformly in:

```text
b,D,R,eta,
both signs of d,
and the declared P_minor^0 threshold schedules.
```

Since the first limit is already zero for each fixed `w`, the subsequent
`w -> infinity` limit is also zero in the project order.

Therefore:

```text
LowLevelEnergyTailTarget_296(P_minor^0):
  PROVEN inside P_minor^0.
```

### E. Fourth-moment low-level tail

Module 296 proved the deterministic tail inequality:

```text
M_low,0(D;R,eta)
  <=
  lambda_min^2 E2_minor^0(D;R,eta)
  =
  (A_N^0)^2 N^{-2 kappa_lambda}E2_minor^0(D;R,eta).
```

By the just-proved energy-tail target:

```text
M_low,0(D;R,eta)=o_W(1).
```

Thus:

```text
LowLevelFourthMomentTailP0_297:
  PROVEN inside P_minor^0.
```

## 6. What this proves and does not prove

This proves the local fourth-moment low-level tail for the exact
`P_minor^0` W-cyclic prime-only model.

It does not prove:

```text
ShiftRemovalBudget_284(q),
FreqRemovalBudget_284(r),
RowShellBudget_284,
ColumnShellBudget_284,
SigmaColumnShellBudget_284,
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

It also does not transfer anything from the local W-cyclic model to the
actual sharp moving selector.

## 7. Edge cases

If:

```text
A_N^0=0,
```

then `Lambda_0` is empty and the conclusion is trivial. The proof above
covers both this case and the nonzero-envelope case.

The proof uses only the full-frequency Parseval bound, then restricts to
minor arcs. It does not need major-arc cancellation.

The proof uses a logarithmic pointwise envelope. This is harmless under the
declared limiting order because `N^{-2 kappa_lambda}` beats every fixed
power of `log(WN+b)` for fixed `w`.

If a future module changes the limiting order, lets `w` grow with `N`, or
changes the model weight, this row must be rechecked.

## 8. Project-map location

The local low-level branch now reads:

```text
Module 294:
  low-level row classified.

Module 296:
  pure counting blocked; second-energy tail extracted.

Module 297:
  second-energy tail proved locally inside P_minor^0.
```

The remaining side-package branch is:

```text
ShiftRemovalBudget_284(q)
+ FreqRemovalBudget_284(r)
+ row/column/shell threshold budgets
+ W and dyadic uniformity rows
=> ThresholdBudgetP0Closure_284(q,r)
=> SideRowsP0Ready_283 / SidePkg_291.
```

Only the low-level fourth-moment tail has been closed locally.

## 9. Forbidden upgrades

Do not cite this as:

```text
ThresholdBudgetP0Closure_284(q,r),
SidePkg_291,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
or the original selected-average problem.
```

Do not transfer it to the actual sharp moving selector without a named
transfer theorem. Do not use it to hide shift/frequency removal budgets. Do
not convert a local W-cyclic side-row proof into an endpoint proof.

## 10. Next target

The low-level branch has reached a local closure for the fourth-moment tail.
The next narrow target should leave the low-level row and test the removal
budgets from Module 284:

```text
Module 298:
  ShiftFreqRemovalAudit_298(P_minor^0).
```

This should classify:

```text
ShiftRemovalBudget_284(q),
FreqRemovalBudget_284(r),
and the moment inputs ShiftMomentP0_284(q), MultMomentP0_284(r)
```

without claiming any threshold closure unless the moment estimates and
compatible threshold schedule are actually supplied.
