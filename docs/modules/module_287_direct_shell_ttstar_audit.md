# Module 287: Direct-shell `TT*` cross-term audit

## 1. Precise theorem / claim being advanced

This module starts Phase K by auditing the direct-shell route for the adaptive
shell functional inside `P_minor^0`.

Define:

```text
DirectShellTTStarAudit_287(P_minor^0).
```

The question is whether the `TT*` cross terms of:

```text
X_J(omega)
```

reduce to a known same-family non-endpoint estimate, or whether a genuinely
new theorem is required before the direct-shell route can support
`AdaptiveShellGainP0_285`.

Verdict:

```text
The current ledger does not prove a direct-shell TT* cross-term gain.
```

The missing input is named:

```text
DirectShellCrossTermGain_287(P_minor^0).
```

Status:

```text
OPEN.
```

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module is an audit of the direct-shell route. It proves no bound for
`Xi_273^0`, no `DirectShellBound_280`, no `AdaptiveShellGainP0_285`, no
`PhaseKernelBound_273^0`, and no endpoint estimate.

## 3. Definitions and variables

Work inside `P_minor^0`.

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
J=J_trans_0(lambda;sigma),
e=(d,xi) in J,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

For unit coefficients:

```text
|omega_e|<=1,
```

write:

```text
X_J(omega)
  =
  sum_{e in J} omega_e beta_0(e)
  =
  E_n sum_d B_d^0(n)K_{d,omega}^J(n),
```

where:

```text
K_{d,omega}^J(n)
  =
  sum_{xi in S_d(J)} omega_{d,xi}e_N(-xi n).
```

The target shell functional is:

```text
Xi_273^0(lambda;sigma)
  =
  sup_{|omega_e|<=1}|X_J(omega)|.
```

Since `omega` is adversarial:

```text
Xi_273^0(lambda;sigma)
  =
  sum_{e in J}|beta_0(e)|.
```

This identity is part of the difficulty, not a cancellation estimate.

## 4. Assumptions

This module assumes only Modules 278-286 and the standing status ledger.

It does not assume:

```text
DirectShellCrossTermGain_287,
DirectShellTTStarClosure_287,
AdaptiveShellGainP0_285,
DirectShellBound_280,
UniformFiberBound_280,
SelectionTransfer_280,
PhaseKernelBound_273^0,
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
DegRowsP0Small_282,
MajorDiffBound_282,
PhysDiagLocal_282,
DegFreePhaseGate_282,
LargeSieveBesselClosure_281,
AdaptiveBesselGain_281,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
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

### A. Exact coefficient-space `TT*`

For fixed `omega`:

```text
|X_J(omega)|^2
  =
  sum_{e_1,e_2 in J}
    omega_{e_1}conj(omega_{e_2})
    beta_0(e_1)conj(beta_0(e_2)).
```

Split:

```text
|X_J(omega)|^2
  =
  DiagTT_287(J)
  + CrossTT_287(J,omega),
```

where:

```text
DiagTT_287(J)
  =
  sum_{e in J}|beta_0(e)|^2,

CrossTT_287(J,omega)
  =
  sum_{e_1 != e_2}
    omega_{e_1}conj(omega_{e_2})
    beta_0(e_1)conj(beta_0(e_2)).
```

The diagonal term is:

```text
DiagTT_287(J)=D Eng_0(J).
```

It is controlled only to the extent that the row, column, shell-counting, and
threshold budgets from Modules 281 and 284 are controlled.

The cross term is not an optional perturbation. If `omega_e` is chosen to
align with `beta_0(e)`, then:

```text
|X_J(omega)|^2
  =
  (sum_{e in J}|beta_0(e)|)^2,
```

and the coefficient-space cross terms encode the square of the shell `L^1`
mass.

### B. Exact physical-space `TT*`

Module 279 gives:

```text
|X_J(omega)|^2
  =
  E_{n,m}
    sum_{e_1,e_2 in J}
      omega_{e_1}conj(omega_{e_2})
      B_{d_1}^0(n)conj(B_{d_2}^0(m))
      e_N(-xi_1 n + xi_2 m).
```

After expanding `B_d^0`:

```text
B_{d_1}^0(n)conj(B_{d_2}^0(m))
  =
  f_0(n+d_1)conj(f_0(n))
  conj(f_0(m+d_2))f_0(m).
```

Thus the cross terms are weighted shifted four-point residual correlations
with the restricted shell phase:

```text
e_N(-xi_1 n + xi_2 m).
```

No full-frequency diagonal equation is present because `xi_1,xi_2` range over
the data-dependent shell `J`, not over a complete frequency group.

### C. Cross-term routing

The off-diagonal pairs `e_1 != e_2` split into:

```text
same shift:
  d_1=d_2, xi_1 != xi_2;

same frequency:
  xi_1=xi_2, d_1 != d_2;

fully transverse:
  d_1 != d_2, xi_1 != xi_2.
```

Same-shift pairs route to row-level restricted frequency kernels. They are
not controlled beyond row ceilings unless a same-family row phase estimate is
proved.

Same-frequency pairs route to column-level shifted correlation kernels. They
are not controlled beyond column ceilings unless a same-family frequency
phase estimate is proved.

Fully transverse pairs are the genuine direct-shell `TT*` cross terms.
Their natural local target is:

```text
DirectShellCrossTermGain_287(P_minor^0):
  a uniform bound for CrossTT_287(J,omega), after the same-shift,
  same-frequency, major-difference, physical-diagonal, and side rows are
  routed, strong enough to improve the deterministic row/column shell
  ceilings in the lambda-summed Phase K target.
```

This target is open.

### D. Why Cauchy/Bessel does not close the route

The direct Cauchy step:

```text
|X_J(omega)|^2
  <=
  E_n sum_d |B_d^0(n)|^2
  *
  E_n sum_d |K_{d,omega}^J(n)|^2
```

discards cross-shift information. Orthogonality gives:

```text
E_n |K_{d,omega}^J(n)|^2 <= #S_d(J).
```

This reproduces row-size and shell-counting controls. It does not prove a
new phase gain, and it does not estimate `CrossTT_287(J,omega)` nontrivially.

Classification:

```text
CauchyBesselDirect_287:
  STRUCTURAL / DIAGNOSTIC only;
  no adaptive-shell gain beyond Modules 281 and 284.
```

### E. Why fixed-set estimates do not close the route

A theorem for a predetermined family:

```text
U=(U_d)_d
```

does not apply to:

```text
U_d=S_d(J)
```

unless it is uniform over the adaptive class or paired with a selection
theorem. This is exactly the Module 280 obstruction.

Classification:

```text
FixedSetDirect_287:
  FALSE / BLOCKED as an automatic route.
```

### F. Why full-frequency orthogonality does not close the route

If a complete frequency set were summed, one could get diagonal equations in
the physical variables. But `J` is:

```text
minor-arc restricted,
large-spectrum selected,
base-threshold selected,
shell-height selected,
row/column threshold selected,
and data-dependent.
```

Therefore the restricted shell phase kernel cannot be replaced by:

```text
n=m
```

or by any full-frequency diagonal system without a separate transfer theorem.

Classification:

```text
FullOrthogonalityShortcut_287:
  FALSE / BLOCKED.
```

### G. Why endpoint tools would be circular

The cross terms can be bounded by assuming any of:

```text
PhaseKernelBound_273^0,
TransIncBound_269,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

But those are endpoint or near-endpoint objects in this branch. They cannot
serve as inputs to prove the direct-shell route.

Classification:

```text
EndpointCrossTermRoute_287:
  FALSE / BLOCKED as a proof route.
```

### H. Minimal non-endpoint theorem that would be useful

The smallest useful theorem visible after this audit is:

```text
DirectShellTTStarClosure_287:
  DirectShellCrossTermGain_287
  + same-shift row phase control
  + same-frequency column phase control
  + MajorDiffBound_282
  + PhysDiagLocal_282
  + SideRowsP0Ready_283
  + ThresholdBudgetP0Closure_284
    => DirectShellBound_280
```

inside `P_minor^0`.

This is a conditional map, not a proved implication with supplied estimates.
Every nonstructural input on the left remains open.

### I. Final verdict

The audit clarifies the direct-shell route:

```text
diagonal coefficient terms:
  row/column energy only;

Cauchy/Bessel:
  returns known ceilings;

fixed-set estimates:
  blocked without selection;

full orthogonality:
  blocked for restricted shells;

endpoint-derived estimates:
  circular;

true direct-shell progress:
  requires DirectShellCrossTermGain_287.
```

Therefore:

```text
DirectShellTTStarAudit_287(P_minor^0)
  is structural only.

DirectShellCrossTermGain_287(P_minor^0)
  remains OPEN.
```

## 6. Edge cases

- If `J` is empty, `X_J(omega)=0` for that shell only.
- If `e_1=e_2`, the contribution is diagonal coefficient energy, not a
  cross-term gain.
- Same-shift and same-frequency off-diagonal pairs are not automatically
  harmless; they route to row and column phase rows.
- The maximizing `omega` makes `Xi_273^0` an `L^1` shell mass. One cannot
  assume favorable phase cancellation among shell coefficients.
- Full-frequency orthogonality applies only to complete frequency sums, not
  to `J`.
- Any cross-term theorem must be uniform over adversarial `omega`.
- Any cross-term theorem must be uniform over the data-dependent shell
  selection.
- A local `P_minor^0` cross-term theorem would still need transfer before it
  could say anything about the actual sharp moving selector.

## 7. Where it fits in the project map

```text
Module 279
  -> exact X_J(omega), TT*, and fourth-power expansions

Module 281
  -> Cauchy/Bessel direct attempt gives row/column ceilings only

Module 285
  -> current adaptive-shell package blocked

Module 286
  -> Phase K starts with direct-shell TT* triage

Module 287
  -> TT* cross-term gain isolated as the missing direct-shell input
```

The next useful step is:

```text
Module 288:
  audit selection complexity for the adaptive shell class S_d(J).
```

## 8. What remains open

This module does not prove:

- `DirectShellCrossTermGain_287`;
- `DirectShellTTStarClosure_287`;
- `AdaptiveShellGainP0_285`;
- `DirectShellBound_280`;
- `UniformFiberBound_280`;
- `SelectionTransfer_280`;
- `PhaseKernelBound_273^0`;
- `ThresholdBudgetP0Closure_284(q,r)`;
- `SideRowsP0Ready_283`;
- `DegRowsP0Small_282`;
- `MajorDiffBound_282`;
- `PhysDiagLocal_282`;
- `DegFreePhaseGate_282`;
- `LargeSieveBesselClosure_281`;
- `AdaptiveBesselGain_281`;
- `PhaseKernelBound_273`;
- `TransverseGateProofPkg_276`;
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

- Do not call coefficient diagonal energy a cross-term gain.
- Do not use Cauchy/Bessel row or column ceilings as a new direct-shell bound.
- Do not treat fixed-set estimates as estimates for `S_d(J)`.
- Do not replace restricted shell phases by full-frequency diagonal equations.
- Do not assume cancellation in the adversarial `omega` variables.
- Do not prove cross-term control from `PhaseKernelBound_273^0`,
  `TransIncBound_269`, `NarrowMinorArc_3^B`, or endpoint equivalents.
- Do not transfer `P_minor^0` statements to the actual sharp moving selector
  without named transfer rows.
