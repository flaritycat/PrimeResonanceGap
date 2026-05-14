# Module 283: Side-row audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module audits the minimum compatibility and side rows still present after
passing from the broad Phase I environment to the fixed minimal family
`P_minor^0` of Module 278.

Define:

```text
SideRowsP0Audit_283(P_minor^0).
```

The verdict is:

```text
P_minor^0 removes several transfer rows only by internal convention,
but it does not remove W-uniformity, threshold-budget, low-level leakage,
dyadic-uniformity, or shell-selection side rows.
```

Equivalently, a future proof of `PhaseKernelBound_273^0` has two different
tasks:

```text
local task:
  prove the shell estimate wholly inside P_minor^0;

export task:
  transfer any local result to interval, residue-averaged, smoothed/frozen,
  or actual sharp moving-selector worlds.
```

This module concerns the local task. It does not perform the export task.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module is a side-row classification. It proves no side-row smallness, no
`PhaseKernelBound_273^0`, no `PhaseKernelBound_273`, and no endpoint estimate.

## 3. Definitions and variables

Work inside the exact family from Module 278:

```text
P_minor^0:
  W-cyclic prime-only model,
  one fixed reduced residue b mod W,
  cyclic group G_N=Z/NZ with (N,W)=1,
  full cyclic averages,
  fixed two-sided shell D<|d|<=2D,
  N^{delta_D}<=D<=N^{1-delta_D},
  2D<=N/16,
  fixed Major_0(R,eta) and Minor_0(R,eta),
  fixed lambda grid Lambda_0,
  fixed threshold schedules mu_0,K_0,
  fixed base-tail shells J_trans_0(lambda;sigma).
```

Use:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi),
J=J_trans_0(lambda;sigma).
```

The active local target is:

```text
PhaseKernelBound_273^0:
  a same-family bound for Xi_273^0(lambda;sigma)
  over the data-dependent shell J_trans_0(lambda;sigma),
  strong enough for the lambda-summed Gamma_trans^273 target.
```

Define the side-row package:

```text
SideRowsP0_283(P_minor^0)
  =
  WUniformP0_283
  + ThresholdBudgetP0_283
  + LowLevelCutoffP0_283
  + DyadicUniformityP0_283
  + ShellSelectionP0_283
  + ArcBoundaryP0_283
  + ResidueConventionP0_283
  + BoundaryConventionP0_283
  + SelectorConventionP0_283.
```

This sum is a ledger expression, not an analytic inequality.

## 4. Assumptions

This module assumes only Modules 278-282 and the standing status ledger.

It does not assume:

```text
SideRowsP0Ready_283,
WUniformP0_283,
ThresholdBudgetP0_283,
LowLevelCutoffP0_283,
DyadicUniformityP0_283,
ShellSelectionP0_283,
ArcBoundaryP0_283,
ResidueTransferP0_283,
BoundaryTransferP0_283,
SelectorTransferP0_283,
DegRowsP0Small_282,
MajorDiffBound_282,
PhysDiagLocal_282,
DegFreePhaseGate_282,
LargeSieveBesselClosure_281,
AdaptiveBesselGain_281,
UniformFiberBound_280,
SelectionTransfer_280,
DirectShellBound_280,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransGateSideRows_274,
TransIncBound_269,
ThresholdOnlyClosure_270,
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

### A. W-limit uniformity row

Module 278 fixes the meaning of:

```text
Err=o_W(1) over P_minor^0
```

as:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho_0 in P_minor^0(N,w)}
    |Err(N,w;rho_0)| = 0.
```

This declaration removes ambiguity in the order of limits, but it does not
prove any estimate uniform in that order.

Define:

```text
WUniformP0_283:
  every constant and loss in a proposed PhaseKernelBound_273^0 proof remains
  valid after the sup over rho_0 in P_minor^0(N,w) and after the final
  w -> infinity limit.
```

Classification:

```text
WUniformP0_283:
  OPEN.
```

It is not enough to prove a fixed-`w`, fixed-`D`, fixed-threshold estimate
unless the proof explicitly preserves the displayed limit order.

### B. Threshold-budget row

The family fixes threshold schedules:

```text
mu_0(lambda), K_0(lambda).
```

The shell membership uses:

```text
|beta_0(d,xi)| >= lambda,
E_{d,0}(lambda) <= mu_0(lambda),
N_{xi,0}(lambda) <= K_0(lambda),
sigma <= |beta_0(d,xi)| < 2sigma.
```

This avoids post-hoc threshold selection, but the threshold budget itself is
still an analytic row.

Define:

```text
ThresholdBudgetP0_283:
  a same-family choice of mu_0,K_0 and lambda grid such that
  row, column, base-tail, and threshold-boundary losses are all summable in
  the final lambda-summed Gamma_trans^273 target.
```

Classification:

```text
ThresholdBudgetP0_283:
  OPEN.
```

This is the local `P_minor^0` version of the tension found in Module 270. The
large thresholds useful for removing bad shifts and persistent frequencies
can conflict with the small thresholds needed for trivial row/column ceilings.

### C. Low-level cutoff row

Module 278 defines:

```text
lambda_min=A_N^0 N^{-kappa_lambda}
```

and includes only:

```text
lambda >= lambda_min.
```

The lower levels:

```text
|beta_0(d,xi)| < lambda_min
```

are not part of `Xi_273^0`. They were excluded by convention from the Phase J
shell test.

Define:

```text
LowLevelCutoffP0_283:
  the contribution of all levels below lambda_min is negligible in the
  local minor-arc target, uniformly over P_minor^0.
```

Classification:

```text
LowLevelCutoffP0_283:
  OPEN.
```

This row is local/model-side, not selector transfer. It is also not proved by
the definition of the lambda grid.

### D. Dyadic-uniformity row

The family fixes:

```text
N^{delta_D} <= D <= N^{1-delta_D},
2D <= N/16,
D<|d|<=2D,
```

and includes both signs of `d`.

A proof for one `D`, one sign, or one shell height `sigma` is not a proof of
the local Phase J input unless it survives:

```text
all D in the declared range,
all lambda in Lambda_0,
all sigma=lambda_k>=lambda,
both signs of d,
all admissible R,eta,
and all rho_0 in P_minor^0(N,w).
```

Define:

```text
DyadicUniformityP0_283:
  the proposed local shell estimate is uniform over the declared dyadic,
  lambda, sigma, major/minor, residue, and W parameters.
```

Classification:

```text
DyadicUniformityP0_283:
  OPEN.
```

The dyadic restrictions are useful because they remove endpoint ranges from
the local test, but they do not by themselves make the shell sum small.

### E. Shell-selection row

The shell:

```text
J_trans_0(lambda;sigma)
```

is data-dependent. Its membership depends on the same coefficients
`beta_0(d,xi)` whose shell functional is being estimated.

Define:

```text
ShellSelectionP0_283:
  a same-family theorem controlling Xi_273^0 on the actual adaptive shell
  J_trans_0(lambda;sigma), not merely on predetermined fibers.
```

Classification:

```text
ShellSelectionP0_283:
  OPEN.
```

This row packages the obstruction from Modules 280-281:

```text
fixed frequency-set estimates
  do not automatically control adaptive shell fibers.
```

Thus `ShellSelectionP0_283` can be supplied only by one of:

```text
UniformFiberBound_280,
SelectionTransfer_280,
DirectShellBound_280,
or a new same-family theorem explicitly stronger than the fixed-set bound.
```

None of these is currently proved.

### F. Arc-boundary row

Inside `P_minor^0`, `Minor_0(R,eta)` is fixed with the non-strict convention
of Module 278. Therefore no arc-boundary transfer is needed to state
`Xi_273^0` for that exact tuple.

However, two arc-boundary issues remain:

```text
1. If a proof changes R, eta, the buffer convention, or the major/minor split,
   it has left the exact tuple and needs an arc-boundary row.

2. If a minor-minor combination creates a major-like difference, it belongs
   to MajorDiffBound_282, not to a harmless convention.
```

Define:

```text
ArcBoundaryP0_283:
  zero only for a proof that keeps exactly the Module 278 Major_0/Minor_0
  convention; otherwise an open transfer row.
```

Classification:

```text
ArcBoundaryP0_283:
  STRUCTURAL / EXTRACTION as an internal convention;
  OPEN when the proof changes the arc convention or needs major-difference
  control.
```

This is why `MajorDiffBound_282` remains a separate open analytic row.

### G. Boundary and cyclic-cutoff row

Inside `P_minor^0`, the average is over the full cyclic group:

```text
G_N=Z/NZ.
```

All shifts in `B_d^0(n)` are cyclic. There is no interval endpoint, no moving
prefix, and no interval cutoff.

Define:

```text
BoundaryConventionP0_283:
  cyclic wraparound and interval-boundary errors are absent inside P_minor^0.
```

Classification:

```text
BoundaryConventionP0_283:
  STRUCTURAL / EXTRACTION inside P_minor^0;
  not interval transfer.
```

The corresponding actual-target row remains outside the local test and is
part of the broader minor-arc transfer problem.

### H. Residue and prime-power row

Inside `P_minor^0`, the model is:

```text
nu_0(n)=(phi(W)/W)log(Wn+b)1_{Wn+b is prime}
```

for one fixed reduced residue `b mod W`. Prime powers are not included.

Thus the following are internal conventions:

```text
fixed W-residue b,
prime-only model,
no W-residue averaging,
no prime-power restoration.
```

Define:

```text
ResidueConventionP0_283:
  the proof remains in the fixed W-residue prime-only model.
```

Classification:

```text
ResidueConventionP0_283:
  STRUCTURAL / EXTRACTION inside P_minor^0;
  OPEN as soon as a proof averages over residues, changes residue class,
  restores prime powers, or transfers to actual primes.
```

Large-prime coincidences with `p>w` are not removed by this convention. They
belong to the local phase and correlation rows.

### I. Selector row

Inside `P_minor^0`, the selector/model class is fixed:

```text
s0 = W-cyclic prime-only model in the residue b mod W.
```

There is no smoothed selector, frozen dyadic selector, Bernoulli lift,
finite-stage selector, interval selector, or actual sharp moving alpha
selector.

Define:

```text
SelectorConventionP0_283:
  the proof never changes selector/model class.
```

Classification:

```text
SelectorConventionP0_283:
  STRUCTURAL / EXTRACTION inside P_minor^0;
  not selector transfer.
```

Any use for the original selected-average problem still requires a separate
selector-transfer theorem through the residual derivative and adaptive shell
selection.

### J. Minimum local side package

For a proof that stays wholly inside `P_minor^0`, the minimum nonzero local
side package is:

```text
SideRowsP0Ready_283
  =
  WUniformP0_283
  + ThresholdBudgetP0_283
  + LowLevelCutoffP0_283
  + DyadicUniformityP0_283
  + ShellSelectionP0_283
```

together with any analytic degeneracy rows from Module 282:

```text
DegRowsP0Small_282,
MajorDiffBound_282,
PhysDiagLocal_282,
DegFreePhaseGate_282.
```

The internally zero convention rows are:

```text
BoundaryConventionP0_283,
ResidueConventionP0_283,
SelectorConventionP0_283,
ArcBoundaryP0_283 for the exact fixed arc convention only.
```

These zero rows are not transfer theorems.

Classification:

```text
SideRowsP0Ready_283:
  OPEN.
```

### K. Conditional use statement

The strongest valid local implication after this audit is:

```text
SideRowsP0Ready_283
  + DegRowsP0Small_282
  + a same-family shell estimate for Xi_273^0
    => PhaseKernelBound_273^0.
```

This is only a conditional map. The left side is not proved here.

To leave `P_minor^0`, one would additionally need the export package:

```text
BoundaryTransferP0_283
+ ResidueTransferP0_283
+ SelectorTransferP0_283
+ prime-power restoration
+ interval/prefix/cutoff transfer
+ actual sharp moving-selector transfer.
```

This export package is not part of the proved local row.

### L. Final verdict

The audit narrows the local target:

```text
inside P_minor^0:
  boundary, fixed-residue, prime-only, and selector-change rows are
  conventions;

still open inside P_minor^0:
  W-uniformity,
  threshold budget,
  low-level cutoff,
  dyadic uniformity,
  adaptive shell selection,
  major-difference control,
  physical-diagonal control,
  row/column lambda-summed smallness,
  and deg-free phase control.
```

Therefore:

```text
SideRowsP0Audit_283(P_minor^0)
  is structural only.
```

## 6. Edge cases

- If `A_N^0=0`, the lambda grid is empty for that tuple; this does not prove
  a uniform minor-arc theorem.
- If a proof estimates only one `lambda` or one `sigma`, it has not supplied
  the lambda-summed target.
- If a proof changes `R`, `eta`, or uses a buffered major/minor split, the
  exact `P_minor^0` arc convention no longer applies without a side row.
- If a proof averages over `b mod W`, it has left the fixed-residue family.
- If a proof uses interval averages, cyclic wraparound is no longer a
  harmless convention.
- If a proof uses a smoothed or frozen selector, it is not a proof inside
  `P_minor^0` unless the selector class is explicitly changed and a transfer
  row is supplied.
- If a proof quotes a fixed-set large-sieve estimate, it still has to handle
  the adaptive shell-selection row.
- Internal convention zeros may be used only for the local model. They cannot
  be exported to the original selected-average problem.

## 7. Where it fits in the project map

```text
Module 278
  -> MinimalTransverseFamily_278(P_minor^0)

Module 279
  -> XiDualPhaseExpansion_279(P_minor^0)

Module 280
  -> fixed-set shell transfer blocked

Module 281
  -> Bessel benchmark leaves adaptive gain open

Module 282
  -> degeneracy rows audited

Module 283
  -> minimum side rows audited
```

The next useful step is:

```text
Module 284:
  test ThresholdBudgetP0_283 against the row/column ceilings and the
  lambda-summed target, without assuming PhaseKernelBound_273^0.
```

## 8. What remains open

This module does not prove:

- `SideRowsP0Ready_283`;
- `WUniformP0_283`;
- `ThresholdBudgetP0_283`;
- `LowLevelCutoffP0_283`;
- `DyadicUniformityP0_283`;
- `ShellSelectionP0_283`;
- `MajorDiffBound_282`;
- `PhysDiagLocal_282`;
- `DegRowsP0Small_282`;
- `DegFreePhaseGate_282`;
- `LargeSieveBesselClosure_281`;
- `AdaptiveBesselGain_281`;
- `UniformFiberBound_280`;
- `SelectionTransfer_280`;
- `DirectShellBound_280`;
- `PhaseKernelBound_273^0`;
- `PhaseKernelBound_273`;
- `TransverseGateProofPkg_276`;
- `TransGateSideRows_274`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
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

- Do not treat a side-row convention as side-row smallness.
- Do not treat the fixed W-residue model as residue-averaged or actual-prime
  control.
- Do not treat cyclic averaging as interval boundary transfer.
- Do not treat a fixed selector/model class as sharp moving-selector transfer.
- Do not call the threshold schedule harmless without proving the
  lambda-summed threshold budget.
- Do not quote fixed-set estimates as adaptive shell estimates.
- Do not use `PhaseKernelBound_273^0`, `TransIncBound_269`,
  `NarrowMinorArc_3^B`, or any endpoint object as an input to prove the local
  side rows.
