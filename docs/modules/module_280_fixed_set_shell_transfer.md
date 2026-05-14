# Module 280: Fixed-set estimates versus data-dependent shells

## 1. Precise theorem / claim being advanced

This module audits whether estimates proved for predetermined frequency sets
can be transferred to the data-dependent shell sets appearing in
`Xi_273^0`.

Define:

```text
FixedSetShellAudit_280(P_minor^0).
```

The verdict is:

```text
Fixed-set estimates do not automatically imply PhaseKernelBound_273^0.
```

They can be used only through one of the following additional inputs:

```text
UniformFiberBound_280,
SelectionTransfer_280,
or DirectShellBound_280.
```

None of these inputs is proved here. The automatic shortcut:

```text
fixed frequency-set theorem => data-dependent shell theorem
```

is blocked.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a compatibility and obstruction audit. It does not prove
`PhaseKernelBound_273^0`, `TransIncBound_269`, or `NarrowMinorArc_3^B`.

## 3. Definitions and variables

Work inside the fixed family `P_minor^0` of Module 278.

Use the Module 279 notation:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
J=J_trans_0(lambda;sigma),
S_d(J)={xi:(d,xi) in J},
D_xi(J)={d:(d,xi) in J},
beta_0(d,xi)=widehat{B_d^0}(xi).
```

For any predetermined fiber family:

```text
U=(U_d)_{D<|d|<=2D},
U_d subset Minor_0(R,eta),
```

define:

```text
X_U(omega)
  =
  sum_{D<|d|<=2D}
  sum_{xi in U_d}
    omega_{d,xi} beta_0(d,xi),

Xi_U
  =
  sup_{|omega_{d,xi}|<=1} |X_U(omega)|.
```

Predetermined means:

```text
U may depend on rho_0, d, R, eta, and the declared model conventions,
but not on beta_0, Spec_{d,0}^minor(lambda), E_{d,0}(lambda),
N_{xi,0}(lambda), BadShift_0(lambda), BadFreq_0(lambda), I_trans_0(lambda),
or J_trans_0(lambda;sigma).
```

The actual shell family is:

```text
U_d=S_d(J),
```

where membership is equivalent to the conjunction:

```text
D<|d|<=2D,
xi in Minor_0(R,eta),
|beta_0(d,xi)| >= lambda,
sigma <= |beta_0(d,xi)| < 2sigma,
E_{d,0}(lambda) <= mu_0(lambda),
N_{xi,0}(lambda) <= K_0(lambda).
```

Thus `S_d(J)` is not predetermined.

## 4. Assumptions

This module assumes only Modules 278 and 279.

It does not assume:

```text
FixedSetShellTransfer_280,
UniformFiberBound_280,
SelectionTransfer_280,
DirectShellBound_280,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransGateSideRows_274,
DegFreePhaseGate_275,
TransIncBound_269,
ThresholdOnlyClosure_270,
PhaseIncidenceGate_271,
AvailableToolClosure_272,
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

## 5. Proof / disproof / reduction

### A. Why a fixed-set theorem misses the target

A typical fixed-set theorem would have the form:

```text
FixedSetBound_280(Y):
  Xi_U <= Y(U;rho_0)
```

for each predetermined family `U`.

The shell target is:

```text
Xi_273^0(lambda;sigma)
  =
  Xi_{S(J)}
```

with:

```text
S(J)=(S_d(J))_d.
```

But `S(J)` is defined from the same coefficients `beta_0(d,xi)` whose
correlations the theorem is meant to bound. Therefore the implication:

```text
FixedSetBound_280(Y) for predetermined U
  => Xi_{S(J)} <= Y(S(J);rho_0)
```

is not a valid proof step unless the fixed-set theorem is explicitly uniform
over such beta-dependent choices or a selection theorem transfers it.

This is the same obstruction in a smaller room: the selection is part of the
large-spectrum problem, not an external parameter.

### B. No monotone domination by the full minor set

One might try:

```text
S_d(J) subset Minor_0(R,eta)
```

and then replace `S_d(J)` by the full minor set. This is not valid for
phase-cancellation estimates.

For complex sums with adversarial coefficients:

```text
sup_{|omega|<=1}
  | sum_{xi in S_d(J)} omega_{d,xi} beta_0(d,xi) |
```

is not controlled by cancellation in:

```text
sum_{xi in Minor_0(R,eta)} c_{d,xi} beta_0(d,xi)
```

for fixed coefficients `c_{d,xi}`. Enlarging a signed or complex sum can add
cancellation rather than preserve size. The only monotone replacement is the
absolute trivial bound:

```text
sum_{(d,xi) in J} |beta_0(d,xi)|,
```

which is exactly the shell mass that `Xi_273^0` was introduced to improve.

Thus full-minor estimates are not shell estimates unless they are formulated
as uniform operator or maximal inequalities over all fibers.

### C. The entropy barrier

The collection of possible fibers is enormous:

```text
S_d(J) subset Minor_0(R,eta)
```

with row and column constraints and with membership decided by `beta_0`.
A naive union bound over all fiber families costs roughly:

```text
exp( sum_d #Minor_0(R,eta) )
```

before using row/column restrictions, far beyond the logarithmic losses
available in the lambda-summed transverse target.

Even after row and column constraints, the admissible family can still be too
large unless a genuine entropy, VC, chaining, sparse domination, or stopping
time theorem is proved in the same model. No such theorem is in the current
ledger.

### D. Three admissible routes

The first admissible route is:

```text
UniformFiberBound_280(Y):
  Xi_U <= Y(size(U),rho_0)
```

uniformly for every fiber family `U=(U_d)` satisfying the same row and column
constraints as the shell, with constants independent of how `U` was selected.

If this is proved with a lambda-summable `Y`, then it can be applied to
`U=S(J)`.

The second admissible route is:

```text
SelectionTransfer_280:
  predetermined fixed-set estimates
  + an entropy/stopping-time/selection theorem
  => the same bound for S(J).
```

This route must pay every loss from selecting:

```text
|beta_0(d,xi)| >= lambda,
sigma <= |beta_0(d,xi)| < 2sigma,
E_{d,0}(lambda) <= mu_0(lambda),
N_{xi,0}(lambda) <= K_0(lambda).
```

The third admissible route is:

```text
DirectShellBound_280:
  estimate X_J(omega) directly from the Module 279 phase expansion,
  without passing through a predetermined frequency-set theorem.
```

This is the cleanest route if a future non-endpoint large-sieve or Bessel
argument can be made to see the shell itself.

### E. What remains blocked

The following shortcuts are blocked:

```text
FixedSetBound_280 for one prescribed U
  => PhaseKernelBound_273^0.

Large sieve for fixed S
  => Xi_273^0 for S_d(J).

Full minor-arc estimate
  => arbitrary shell-fiber estimate.

Unweighted graph count
  => weighted residual shell cancellation.

Endpoint minor-arc smallness
  => selection transfer.
```

They may become components only after one of the admissible routes above is
supplied.

### F. Conditional classification

Inside `P_minor^0`:

```text
FixedSetShellTransfer_280
```

has status:

```text
OPEN.
```

The automatic transfer shortcut has status:

```text
FALSE / BLOCKED.
```

This module narrows Module 281: the next benchmark should not ask whether a
large-sieve or Bessel estimate exists for a fixed set only. It should ask
whether such an estimate is uniform over the adaptive fiber class, whether it
comes with a selection theorem, or whether it can estimate `X_J(omega)`
directly.

## 6. Edge cases

- If `J` is empty, the shell bound is trivial for that shell only.
- If a fixed-set theorem is uniform over all subsets with constants depending
  only on row/column sizes, then it is no longer merely a fixed-set theorem;
  it is `UniformFiberBound_280`.
- If a proof conditions on `J` after observing `beta_0`, independence or
  predetermined-set hypotheses are lost.
- Row constraints `E_{d,0}(lambda)<=mu_0(lambda)` depend on the whole row,
  not only on a single edge.
- Column constraints `N_{xi,0}(lambda)<=K_0(lambda)` depend on all shifts.
- The shell height `sigma` and base threshold `lambda` remain separate.
- Bounds depending on the exact identity of `J` are not uniform over
  `P_minor^0` unless their dependence is quantified.
- A proof in a smoothed, interval, residue-averaged, or sharp selector family
  is outside `P_minor^0` until a transfer row is supplied.

## 7. Where it fits in the project map

```text
Module 278
  -> MinimalTransverseFamily_278(P_minor^0)

Module 279
  -> XiDualPhaseExpansion_279(P_minor^0)

Module 280
  -> FixedSetShellAudit_280(P_minor^0)
     automatic fixed-set to shell-set transfer blocked
```

The next useful step is:

```text
Module 281:
  benchmark the strongest non-endpoint large-sieve or Bessel-type estimate
  available for Xi_273^0 in P_minor^0, explicitly testing whether it is
  UniformFiberBound_280, SelectionTransfer_280, or DirectShellBound_280.
```

## 8. What remains open

This module does not prove:

- `FixedSetShellTransfer_280`;
- `UniformFiberBound_280`;
- `SelectionTransfer_280`;
- `DirectShellBound_280`;
- `PhaseKernelBound_273^0`;
- any bound for `Xi_273^0`;
- `PhaseKernelBound_273`;
- `TransverseGateProofPkg_276`;
- `TransGateSideRows_274`;
- `DegFreePhaseGate_275`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
- `PhaseIncidenceGate_271`;
- `AvailableToolClosure_272`;
- `MinorArcTransfer_3^B`;
- `NarrowMinorArc_3^B`;
- selector transfer to the actual sharp moving selector;
- `ProjectedModelNeutrality_3^major`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat a fixed-set theorem as a data-dependent shell theorem.
- Do not replace shell fibers by the full minor set using monotonicity of a
  signed or complex sum.
- Do not hide an exponential selection cost inside a logarithmic loss.
- Do not condition on `J` as if it were independent of `beta_0`.
- Do not estimate `FixedSetShellTransfer_280` by assuming
  `PhaseKernelBound_273^0`, `TransIncBound_269`, or `NarrowMinorArc_3^B`.
- Do not cite Module 280 as a large-sieve or Bessel estimate.
