# Module 281: Large-sieve and Bessel benchmark for `Xi_273^0`

## 1. Precise theorem / claim being advanced

This module benchmarks the strongest non-endpoint large-sieve or Bessel-type
estimates currently available for the shell functional `Xi_273^0` inside the
minimal family `P_minor^0`.

Define:

```text
LSBesselBenchmark_281(P_minor^0).
```

The verdict is:

```text
The available non-endpoint Bessel/large-sieve bounds do not prove
PhaseKernelBound_273^0.
```

More precisely:

```text
1. Row and column Bessel/counting bounds are uniform over adaptive shells,
   but reproduce the Module 270/273 trivial ceilings.

2. Fixed-set large-sieve bounds are diagnostics only, because Module 280
   blocks automatic transfer to data-dependent shells.

3. A genuine adaptive large-sieve/Bessel input would have to be a new
   UniformFiberBound_280, SelectionTransfer_280, or DirectShellBound_280.
```

None of those three open routes is proved here.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a benchmark and classification module. It proves only deterministic
benchmark inequalities already below the endpoint; it does not prove the
adaptive gain needed for `PhaseKernelBound_273^0`.

## 3. Definitions and variables

Work in the Module 278 family `P_minor^0` and use Modules 279-280 notation:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
lambda in Lambda_0,
sigma in Lambda_0, sigma>=lambda,
J=J_trans_0(lambda;sigma),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

The shell functional is:

```text
Xi_273^0(lambda;sigma)
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J} omega_{d,xi} beta_0(d,xi) |.
```

Since the phases `omega_{d,xi}` are adversarial and independent, this is
equivalently:

```text
Xi_273^0(lambda;sigma)
  =
  sum_{(d,xi) in J} |beta_0(d,xi)|.
```

This identity is important. It means a linear large-sieve estimate cannot
win by choosing favorable cancellation among the shell coefficients; the
shell functional already takes the worst dual signs.

Let:

```text
C_D = D^(-1) # { d : D<|d|<=2D },
m_minor^0=#Minor_0(R,eta).
```

On the shell `J`:

```text
sigma <= |beta_0(d,xi)| < 2sigma,
E_{d,0}(lambda) <= mu_0(lambda),
N_{xi,0}(lambda) <= K_0(lambda).
```

## 4. Assumptions

This module assumes only the definitions of `P_minor^0` and the audits of
Modules 279-280.

It does not assume:

```text
LargeSieveBesselClosure_281,
AdaptiveBesselGain_281,
UniformFiberBound_280,
SelectionTransfer_280,
DirectShellBound_280,
FixedSetShellTransfer_280,
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

### A. Row Bessel benchmark

For each fixed `d`, shell membership gives:

```text
|beta_0(d,xi)| <= sigma^(-1)|beta_0(d,xi)|^2
```

on `J`, since `|beta_0(d,xi)|>=sigma`.

Therefore:

```text
sum_{xi in S_d(J)} |beta_0(d,xi)|
  <= sigma^(-1)
     sum_{xi in S_d(J)} |beta_0(d,xi)|^2
  <= sigma^(-1) E_{d,0}(lambda)
  <= mu_0(lambda)/sigma.
```

Summing over shifts:

```text
Xi_273^0(lambda;sigma)
  <= # {d:D<|d|<=2D} mu_0(lambda)/sigma.
```

Using Module 273's shell-energy conversion:

```text
Eng(J) <= (2sigma/D) Xi_273^0(lambda;sigma),
```

this gives:

```text
Eng(J) <= 2 C_D mu_0(lambda).
```

Classification:

```text
UniformFiberBound_280 candidate,
but only the already-known row ceiling.
```

It is uniform over adaptive shells, but it is not a new phase-kernel gain.
It closes the transverse sum only if the still-open threshold window from
`ThresholdOnlyClosure_270` is supplied.

### B. Column Bessel/counting benchmark

The shell upper bound gives:

```text
|beta_0(d,xi)| < 2sigma.
```

The column multiplicity bound gives:

```text
#{d:(d,xi) in J} <= K_0(lambda).
```

Thus:

```text
Xi_273^0(lambda;sigma)
  <= 2sigma K_0(lambda)m_minor^0.
```

Again:

```text
Eng(J)
  <= (2sigma/D) Xi_273^0(lambda;sigma)
  <= 4 sigma^2 K_0(lambda)m_minor^0/D.
```

Classification:

```text
UniformFiberBound_280 candidate,
but only the shell-counting version of the column ceiling.
```

It is useful as a diagnostic and may beat the `A_N^2` column ceiling on low
shells, but it does not by itself give the lambda-summed `o(1)` target over
`P_minor^0`.

### C. Global Cauchy/Bessel benchmark

The global Cauchy estimate gives:

```text
Xi_273^0(lambda;sigma)^2
  <= #J sum_{(d,xi) in J} |beta_0(d,xi)|^2.
```

Together with:

```text
#J <= min(
  # {d:D<|d|<=2D} mu_0(lambda)/sigma^2,
  K_0(lambda)m_minor^0
),
```

this reproduces combinations of the row and column ceilings. If one attempts
to solve the inequality through the shell energy itself, the result is again
bounded by terms of the shape:

```text
mu_0(lambda),
sigma^2 K_0(lambda)m_minor^0/D,
```

not a new adaptive phase-kernel estimate.

Classification:

```text
UniformFiberBound_280 candidate,
but no improvement over row/column benchmark without extra structure.
```

### D. Fixed-set large-sieve benchmark

A predetermined family:

```text
U=(U_d)_d, U_d subset Minor_0(R,eta),
```

may admit a fixed-set large-sieve or Bessel estimate for:

```text
Xi_U
  =
  sup_{|omega|<=1}
    | sum_d sum_{xi in U_d} omega_{d,xi} beta_0(d,xi) |.
```

Such an estimate can be useful if:

```text
U is fixed independently of beta_0,
or the estimate is uniform over all U with constants depending only on
declared size parameters.
```

But the actual shell uses:

```text
U_d=S_d(J),
```

which is selected from `beta_0` through large-spectrum, shell-height, row,
and column tests.

Classification:

```text
fixed-set-only diagnostic,
unless upgraded to UniformFiberBound_280 or SelectionTransfer_280.
```

This benchmark is blocked from proving `PhaseKernelBound_273^0` by
Module 280.

### E. Maximal or selection large-sieve benchmark

A useful adaptive theorem would have to look like:

```text
SelectionTransfer_280:
  fixed-set estimates
  + admissible entropy/stopping-time/maximal selection control
  => bounds for S_d(J).
```

or:

```text
UniformFiberBound_280:
  Xi_U <= Y(size data;rho_0)
  for all row/column-admissible U,
  with lambda-summable Y.
```

No such theorem is currently in the active ledger. A naive union bound over
all possible fibers has exponential selection cost and is not compatible with
the dyadic lambda-summed endpoint.

Classification:

```text
SelectionTransfer_280 candidate in principle,
OPEN in the current ledger.
```

### F. Direct-shell Bessel benchmark

Using Module 279:

```text
X_J(omega)
  =
  E_n sum_d B_d^0(n)K_{d,omega}^J(n).
```

A direct Bessel/Cauchy attempt gives:

```text
|X_J(omega)|^2
  <=
  E_n sum_d |B_d^0(n)|^2
  *
  E_n sum_d |K_{d,omega}^J(n)|^2
```

after discarding cross-shift cancellation. Orthogonality gives:

```text
E_n |K_{d,omega}^J(n)|^2
  <= #S_d(J).
```

This again leads to row-size and shell-counting controls, not to cancellation
from the residual products. Keeping the cross terms instead produces the
Module 279 `TT*` four-form, which needs a genuine correlation estimate not
presently supplied by Bessel alone.

Classification:

```text
DirectShellBound_280 candidate only if the TT* cross terms are estimated
nontrivially.
```

The purely Cauchy/Bessel version is too weak.

### G. Endpoint-derived large-spectrum estimates

One can force the desired benchmark by assuming any of:

```text
M_minor=o(1),
NarrowMinorArc_3^B,
TransIncBound_269,
PhaseKernelBound_273^0,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

Classification:

```text
endpoint-strength / blocked.
```

These assumptions cannot be used in a module meant to build the transverse
proof package.

### H. Final benchmark verdict

The strongest currently available non-endpoint Bessel benchmark inside
`P_minor^0` is:

```text
Xi_273^0(lambda;sigma)
  <= min(
       # {d:D<|d|<=2D} mu_0(lambda)/sigma,
       2sigma K_0(lambda)m_minor^0
     )
```

and consequently:

```text
Eng(J)
  <= min(
       2 C_D mu_0(lambda),
       4 sigma^2 K_0(lambda)m_minor^0/D
     ).
```

This is uniform over the adaptive shell, but it is precisely the deterministic
row/column ceiling package already isolated earlier. It does not establish:

```text
LargeSieveBesselClosure_281,
AdaptiveBesselGain_281,
or PhaseKernelBound_273^0.
```

Therefore Module 281 leaves the Phase J phase-kernel route open and narrows
the next diagnostic to degeneracy and side-row interaction inside
`P_minor^0`.

## 6. Edge cases

- If `J` is empty, every benchmark is vacuous for that shell only.
- The identity `Xi_273^0=sum_J |beta_0|` uses adversarial unit coefficients;
  it is not a cancellation statement.
- The row benchmark depends on the same `mu_0(lambda)` used in the ordered
  bad-shift removal.
- The column benchmark depends on the same `K_0(lambda)` used in the
  persistent-frequency removal.
- Replacing `sigma^2` by `A_N^2` weakens the shell-counting bound and returns
  to the Module 270 column ceiling.
- A large-sieve theorem for a fixed frequency set remains fixed-set-only
  unless it is uniform over adaptive fibers or paired with a selection
  theorem.
- Any proof that estimates `X_J(omega)` by assuming minor-arc smallness is
  circular in this branch.

## 7. Where it fits in the project map

```text
Module 278
  -> MinimalTransverseFamily_278(P_minor^0)

Module 279
  -> XiDualPhaseExpansion_279(P_minor^0)

Module 280
  -> FixedSetShellAudit_280(P_minor^0)

Module 281
  -> LSBesselBenchmark_281(P_minor^0)
     available non-endpoint Bessel bounds are row/column diagnostics only
```

The next useful step is:

```text
Module 282:
  audit routed degeneracy rows inside P_minor^0 and decide which are
  local/model-side and which are already endpoint-strength.
```

## 8. What remains open

This module does not prove:

- `LargeSieveBesselClosure_281`;
- `AdaptiveBesselGain_281`;
- `UniformFiberBound_280`;
- `SelectionTransfer_280`;
- `DirectShellBound_280`;
- `FixedSetShellTransfer_280`;
- `PhaseKernelBound_273^0`;
- any nontrivial bound for `Xi_273^0` beyond row/column ceilings;
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

- Do not cite Bessel or large sieve as an adaptive shell estimate unless the
  adaptive-fiber or selection theorem is supplied.
- Do not count the deterministic row/column ceilings as a new
  `PhaseKernelBound_273^0`.
- Do not hide the `omega` supremum; it turns the shell functional into an
  `L^1` mass.
- Do not use endpoint-strength large-spectrum smallness as a benchmark input.
- Do not move out of `P_minor^0` without a named transfer row.
