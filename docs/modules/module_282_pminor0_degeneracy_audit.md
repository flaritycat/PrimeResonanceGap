# Module 282: Degeneracy audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module revisits the degeneracy routing of Module 275 inside the fixed
minimal family `P_minor^0` from Module 278.

Define:

```text
DegRowsP0Audit_282(P_minor^0).
```

The verdict is:

```text
P_minor^0 removes some transfer degeneracies by convention,
but it does not prove the row, column, major-difference, physical-diagonal,
or deg-free transverse estimates.
```

The local model simplification is useful:

```text
cyclic boundary/cutoff degeneracy,
prime-power restoration,
and selector-change degeneracy
are absent inside P_minor^0.
```

But this is only an internal model statement. It does not transfer to the
actual sharp moving selector or to interval averages.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a classification audit. It proves no degeneracy smallness, no
`PhaseKernelBound_273^0`, and no endpoint estimate.

## 3. Definitions and variables

Work in:

```text
P_minor^0:
  W-cyclic prime-only model,
  one fixed reduced residue b mod W,
  full cyclic average on G_N,
  fixed Minor_0(R,eta),
  fixed dyadic shell D<|d|<=2D,
  fixed threshold schedules mu_0,K_0.
```

Use:

```text
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi),
J=J_trans_0(lambda;sigma).
```

For a fourth-power shell expansion, write:

```text
e_i=(d_i,xi_i) in J,
i=1,2,3,4.
```

Module 279 gives:

```text
|X_J(omega)|^4
  =
  E_{n_1,n_2,n_3,n_4}
    sum_{e_1,e_2,e_3,e_4 in J}
      Omega_4(e_1,e_2,e_3,e_4)
      B_{d_1}^0(n_1)
      conj(B_{d_2}^0(n_2))
      conj(B_{d_3}^0(n_3))
      B_{d_4}^0(n_4)
      e_N(-xi_1 n_1 + xi_2 n_2 + xi_3 n_3 - xi_4 n_4).
```

Define a priority-routed degeneracy ledger:

```text
RoutedDegRows_282(P_minor^0)
  =
  ShiftDiag_282
  + FreqDiag_282
  + RepeatEdge_282
  + MajorDiff_282
  + PhysDiag_282
  + BoundaryCutoff_282
  + WPP_282
  + Selector_282.
```

The priority order is:

```text
RepeatEdge,
ShiftDiag,
FreqDiag,
MajorDiff,
PhysDiag,
BoundaryCutoff,
WPP,
Selector,
DegFree.
```

This order is only for disjoint bookkeeping; it is not an estimate.

## 4. Assumptions

This module assumes only Modules 278-281 and the fixed conventions of
`P_minor^0`.

It does not assume:

```text
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

### A. Shift-diagonal row

The shift-diagonal class is:

```text
d_i=d_j
```

for at least two active edges, after repeated-edge cases have been removed.

Inside `P_minor^0`, this is local/model-side because the row threshold is
part of the fixed family:

```text
E_{d,0}(lambda) <= mu_0(lambda)
```

on the transverse shell. The deterministic row ceiling from Module 281 is
available.

Classification:

```text
ShiftDiag_282:
  local/model-side diagnostic,
  smallness OPEN unless the lambda-summed threshold window is proved.
```

It is not endpoint-strength by itself, but it becomes endpoint-strength if
one removes it by assuming `TransIncBound_269`, `NarrowMinorArc_3^B`, or
`ResCube_3^sharp`.

### B. Frequency-diagonal row

The frequency-diagonal class is:

```text
xi_i=xi_j
```

for at least two active edges, after repeated-edge cases have been removed.

Inside `P_minor^0`, this is local/model-side because the column threshold is
part of the fixed family:

```text
N_{xi,0}(lambda) <= K_0(lambda).
```

Classification:

```text
FreqDiag_282:
  local/model-side diagnostic,
  smallness OPEN unless multiplicity and lambda-summed threshold rows are
  proved.
```

As with the row diagonal, it is not a transverse estimate.

### C. Repeated-edge row

The repeated-edge row is:

```text
(d_i,xi_i)=(d_j,xi_j).
```

It is a subcase of both row and column degeneracy. In `P_minor^0` it is
routed first so it is not double-counted.

Classification:

```text
RepeatEdge_282:
  local/model-side diagnostic,
  controlled only to the extent ShiftDiag_282 and FreqDiag_282 are controlled.
```

No new cancellation is created by identifying a repeated edge.

### D. Major-difference row

Even when:

```text
xi_i in Minor_0(R,eta),
```

signed combinations from the fourth-power phase can satisfy:

```text
xi_i - xi_j near a/q,
xi_i + xi_j near a/q,
or -xi_1+xi_2+xi_3-xi_4 near a/q
```

for small `q`. These are major-like relations among minor frequencies.

Inside `P_minor^0`, this row is still local/model-side because the arc
partition is fixed. But it is not automatically small.

Define the open local row:

```text
MajorDiffBound_282(P_minor^0):
  contribution of major-like signed frequency relations inside the shell
  is lambda-summably negligible or can be routed to a declared major/minor
  boundary package in the same family.
```

Classification:

```text
MajorDiff_282:
  local/model-side OPEN row.
```

It becomes endpoint-strength if controlled by assuming the whole minor-arc
fourth moment or projected major target.

### E. Physical-diagonal row

Physical diagonals arise only after a frequency kernel is collapsed or
partially localized. In the restricted shell problem, full-frequency
orthogonality is not available.

If a proof isolates a relation such as:

```text
n_i=n_j,
n_i+d_i=n_j+d_j,
or another equality among the eight residual slots,
```

then the required estimate is a local shifted-correlation row in the exact
same W-cyclic model.

Define:

```text
PhysDiagLocal_282(P_minor^0):
  same-family shifted-correlation estimates for physical diagonal
  contributions generated by the restricted shell phase kernel.
```

Classification:

```text
PhysDiag_282:
  local/model-side if PhysDiagLocal_282 is proved;
  endpoint-strength if one controls it by assuming unrestricted residual
  fourth-moment smallness.
```

`PhysDiagLocal_282` is open.

### F. Boundary and cutoff row

The family `P_minor^0` uses:

```text
full cyclic average over G_N,
cyclic shifts,
no interval cutoff,
no moving prefix,
no truncation change.
```

Therefore:

```text
BoundaryCutoff_282(P_minor^0)=0
```

as an internal convention statement.

Classification:

```text
BoundaryCutoff_282:
  STRUCTURAL / EXTRACTION inside P_minor^0,
  not a transfer theorem for interval or sharp-selector targets.
```

The corresponding actual-target row remains part of `MinorArcTransfer_3^B`.

### G. W-residue and prime-power row

The family `P_minor^0` uses a fixed reduced W-residue and a prime-only model:

```text
nu_0(n)=(phi(W)/W)log(Wn+b)1_{Wn+b is prime}.
```

Prime powers are excluded by definition. For primes `p<=w`, the W-residue
condition keeps `Wn+b` away from zero modulo `p`.

Thus the small-prime and prime-power restoration row is absent internally:

```text
WPP_282(P_minor^0)=0
```

as a model convention.

Classification:

```text
WPP_282:
  STRUCTURAL / EXTRACTION inside P_minor^0,
  not a proof of prime-power or W-residue transfer for the actual target.
```

Large-prime coincidences `p>w` are not removed by this row; they belong to
the actual phase/local-correlation problem.

### H. Selector row

The selector/model class is fixed:

```text
s0 = W-cyclic prime-only model in residue b mod W.
```

No smoothed, frozen, interval, Bernoulli, or sharp moving selector is used
inside `P_minor^0`. Therefore:

```text
Selector_282(P_minor^0)=0
```

as an internal model statement.

Classification:

```text
Selector_282:
  STRUCTURAL / EXTRACTION inside P_minor^0,
  not selector transfer.
```

Any use for the actual sharp moving selector still requires the relevant
selector-transfer rows.

### I. Degenerate-row package inside `P_minor^0`

The local package that would be needed before using degeneracy routing is:

```text
DegRowsP0Small_282
  =
  ShiftDiag_282 small
  + FreqDiag_282 small
  + RepeatEdge_282 absorbed
  + MajorDiffBound_282
  + PhysDiagLocal_282
```

with:

```text
BoundaryCutoff_282=WPP_282=Selector_282=0
```

only inside the model family.

This package is open.

### J. Deg-free remainder

After the priority-routed classes are removed, the remaining shell is the
same-family deg-free transverse problem:

```text
DegFreePhaseGate_282(P_minor^0):
  estimate X_J(omega) or its TT*/fourth-power expansion on the complement
  of the routed degeneracy classes, strongly enough for
  PhaseKernelBound_273^0.
```

Classification:

```text
DegFreePhaseGate_282:
  OPEN.
```

It is the local `P_minor^0` version of the Module 275 remainder gate.

### K. Final verdict

Inside `P_minor^0`, the degeneracy audit improves the bookkeeping:

```text
boundary/cutoff, WPP, and selector degeneracies vanish by convention.
```

But the active analytic rows remain:

```text
ShiftDiag_282,
FreqDiag_282,
MajorDiffBound_282,
PhysDiagLocal_282,
DegFreePhaseGate_282.
```

The deterministic row/column diagnostics from Modules 280-281 do not prove
their lambda-summed smallness. Therefore:

```text
DegRowsP0Audit_282(P_minor^0)
  is structural only.
```

## 6. Edge cases

- A row or column diagonal can be local/model-side and still not small enough
  for the lambda-summed target.
- A major-like difference between minor frequencies is not a contradiction;
  it is a separate open row.
- A physical diagonal is available only if a proof creates or isolates it;
  restricted shell kernels do not collapse by full orthogonality.
- `BoundaryCutoff_282=0` is a cyclic-model convention, not interval transfer.
- `WPP_282=0` is a prime-only W-model convention, not prime-power transfer.
- `Selector_282=0` is a fixed-model convention, not sharp selector transfer.
- Degeneracy classes can overlap; the priority order prevents double
  counting but does not estimate any class.
- Any degeneracy estimate obtained from `PhaseKernelBound_273^0`,
  `TransIncBound_269`, or `NarrowMinorArc_3^B` is circular.

## 7. Where it fits in the project map

```text
Module 275
  -> global degeneracy routing for P_minor

Module 278
  -> fixed local family P_minor^0

Module 279
  -> exact shell phase expansion

Module 280
  -> fixed-set transfer blocked

Module 281
  -> Bessel benchmark gives only row/column diagnostics

Module 282
  -> degeneracy audit inside P_minor^0
```

The next useful step is:

```text
Module 283:
  audit the minimum side rows still needed for P_minor^0:
  W-limit, cutoff, boundary, threshold, residue, and selector conventions.
```

## 8. What remains open

This module does not prove:

- `DegRowsP0Small_282`;
- `MajorDiffBound_282`;
- `PhysDiagLocal_282`;
- `DegFreePhaseGate_282`;
- `DegFreePhaseGate_275`;
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

- Do not treat internal model zeros as transfer theorems.
- Do not call row or column diagnostics small without the lambda-summed row.
- Do not collapse restricted shell kernels to physical diagonals.
- Do not hide major-difference terms inside the minor remainder.
- Do not use endpoint-strength estimates to remove degeneracies.
- Do not move `P_minor^0` statements to the actual sharp moving selector.
