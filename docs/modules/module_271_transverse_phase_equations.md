# Module 271: Transverse Fourier coefficients and phase equations

## 1. Precise theorem / claim being advanced

This module expands the large Fourier coefficients in the transverse incidence
core from Module 269 and records the exact phase equations generated when two
or more transverse incidences are coupled.

Define:

```text
TransPhaseExpansion_271(s;D,R,eta,w).
```

The purpose is to identify the algebraic object that a future incidence,
restriction, inverse, or correlation theorem would have to control. The
module does not prove such a theorem.

The future analytic row suggested by this extraction is:

```text
PhaseIncidenceGate_271(P_minor):
  a same-family estimate for the shifted f_s-correlation kernels generated
  by transverse same-frequency pairs, same-shift pairs, and rectangles.
```

This row remains open.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The identities below are exact in the chosen finite Fourier model. They do
not prove `TransIncBound_269`, `ThresholdOnlyClosure_270`,
`NarrowMinorArc_3^B`, or any endpoint estimate.

## 3. Definitions and variables

Work in a finite cyclic group `G_N` or in an interval model already transferred
to such a Fourier normalization. For the declared selector/model class `s`,
write:

```text
f_s=nu_s-1
F_{d,s}(n)=f_s(n+d)conj(f_s(n))
B_{d,s}=F_{d,s}
beta_s(d,xi)=widehat{B_{d,s}}(xi)
            = E_n F_{d,s}(n)e(-xi n)
```

The minor arcs and transverse set are those of Modules 269-270:

```text
Minor(R,eta)={xi != 0}\Major(R,eta),

I_trans_s(lambda)
  = { (d,xi) :
        D<|d|<=2D,
        xi in Minor(R,eta),
        |beta_s(d,xi)|>=lambda,
        E_{d,s}(lambda)<=mu(lambda),
        N_{xi,s}(lambda)<=K(lambda) }.
```

For a frequency set `S`, define the exact Fourier kernel:

```text
K_S(t)=sum_{xi in S} e(-xi t).
```

For the full cyclic frequency group:

```text
K_{G_N}(t)=N 1_{t=0}.
```

For a minor-arc set, `K_S` is not a delta kernel in general.

## 4. Assumptions

This module assumes only:

- a fixed selector/model class `s`;
- the finite cyclic Fourier normalization or a named transferred model;
- the Module 269 definition of `I_trans_s(lambda)`;
- the Module 270 threshold audit notation.

It does not assume:

```text
PhaseIncidenceGate_271,
TransIncBound_269,
ThresholdOnlyClosure_270,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
selector transfer,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Single transverse coefficient

For one edge `(d,xi) in I_trans_s(lambda)`:

```text
beta_s(d,xi)
  = E_n f_s(n+d)conj(f_s(n)) e(-xi n).
```

The lower bound:

```text
|beta_s(d,xi)| >= lambda
```

is a correlation with the additive phase `e(xi n)`. It is not, by itself, a
congruence equation. A phase equation appears only after one sums over a
frequency variable or applies an explicit frequency kernel.

Equivalently, choosing a unit phase `omega_{d,xi}` with
`omega_{d,xi} beta_s(d,xi)=|beta_s(d,xi)|`, the edge gives:

```text
Re E_n omega_{d,xi} f_s(n+d)conj(f_s(n)) e(-xi n)
  >= lambda.
```

This is still an inequality, not cancellation or uniformity.

### B. Same-frequency pair expansion

For two shifts coupled through the same frequency `xi`:

```text
beta_s(d1,xi) conj(beta_s(d2,xi))
  =
  E_{n,m}
    f_s(n+d1)conj(f_s(n))
    conj(f_s(m+d2))f_s(m)
    e(-xi(n-m)).
```

If one sums over a frequency set `S`, the exact identity is:

```text
sum_{xi in S} beta_s(d1,xi) conj(beta_s(d2,xi))
  =
  E_{n,m}
    f_s(n+d1)conj(f_s(n))
    conj(f_s(m+d2))f_s(m)
    K_S(n-m).
```

If `S=G_N`, the kernel imposes:

```text
n=m.
```

If `S=Minor(R,eta)` or a large-spectrum subset, no such exact diagonal
replacement is available. The object is the shifted four-point correlation
weighted by `K_S(n-m)`.

This is the first place where ordinary row and column ceilings can miss real
structure: the same-frequency fiber tests correlations between two shift
edges through a minor-arc kernel, not only their count.

### C. Same-shift pair expansion

For two frequencies coupled through the same shift `d`:

```text
beta_s(d,xi1) conj(beta_s(d,xi2))
  =
  E_{n,m}
    f_s(n+d)conj(f_s(n))
    conj(f_s(m+d))f_s(m)
    e(-xi1 n + xi2 m).
```

If one sums over a constrained frequency pair set `Xi subset G_N^2`, the
kernel is:

```text
K_Xi(n,m)=sum_{(xi1,xi2) in Xi} e(-xi1 n + xi2 m).
```

For the diagonal constraint `xi1=xi2` over the full group, the imposed equation
is again:

```text
n=m.
```

For minor arcs or large-spectrum subsets, the diagonal equation is replaced by
the corresponding restricted kernel. This distinction is essential: a
large-spectrum same-shift pair is not automatically a diagonal four-point
moment.

### D. Transverse rectangle expansion

The natural bipartite rectangle in the graph `I_trans_s(lambda)` consists of:

```text
(d1,xi1), (d1,xi2), (d2,xi1), (d2,xi2)
  all in I_trans_s(lambda).
```

Its oriented Fourier product is:

```text
R_s(d1,d2;xi1,xi2)
  =
  beta_s(d1,xi1)
  conj(beta_s(d2,xi1))
  conj(beta_s(d1,xi2))
  beta_s(d2,xi2).
```

Expanding gives:

```text
R_s(d1,d2;xi1,xi2)
  =
  E_{n1,n2,n3,n4}
    F_{d1,s}(n1)
    conj(F_{d2,s}(n2))
    conj(F_{d1,s}(n3))
    F_{d2,s}(n4)
    e(-xi1(n1-n2))
    e( xi2(n3-n4)).
```

If `xi1` and `xi2` are summed independently over the full frequency group,
orthogonality imposes:

```text
n1=n2,
n3=n4.
```

Then the kernel collapses to shifted endpoint correlations involving the two
shifts `d1,d2`. Over minor arcs or over a large-spectrum subset, the exact
object remains:

```text
K_{S1}(n1-n2) K_{S2}(n3-n4)
```

or the corresponding restricted two-frequency kernel. It cannot be replaced
by two diagonal equations without a separate major/minor kernel estimate.

### E. General oriented incidence product

For edges `e_j=(d_j,xi_j)` and signs `epsilon_j in {+1,-1}`, define:

```text
F_{+,d,s}(n)=F_{d,s}(n),
F_{-,d,s}(n)=conj(F_{d,s}(n)).
```

Then:

```text
prod_j beta_s(d_j,xi_j)^{epsilon_j}
  =
  E_{n_1,...,n_k}
    prod_j F_{epsilon_j,d_j,s}(n_j)
    e(-sum_j epsilon_j xi_j n_j),
```

where exponent `epsilon_j=-1` means complex conjugation of the coefficient.

If the frequency tuple is summed over a constraint family `Xi subset G_N^k`,
the exact phase kernel is:

```text
K_{Xi,epsilon}(n_1,...,n_k)
  =
  sum_{(xi_1,...,xi_k) in Xi}
    e(-sum_j epsilon_j xi_j n_j).
```

Only for specific complete frequency families does this kernel become a
Kronecker system of linear equations. For restricted minor arcs, large
spectra, W-residue slices, or selector-dependent families, the kernel remains
part of the analytic problem.

### F. Consequence for the next gate

The future `PhaseIncidenceGate_271` cannot merely count incidences. It must
control at least one of the following exact objects in the same selector/model
class:

```text
same-frequency pair kernels:
  E_{n,m} F_{d1,s}(n)conj(F_{d2,s}(m))K_S(n-m),

same-shift pair kernels:
  E_{n,m} F_{d,s}(n)conj(F_{d,s}(m))K_Xi(n,m),

rectangle kernels:
  E_{n1,n2,n3,n4}
    F_{d1,s}(n1)conj(F_{d2,s}(n2))
    conj(F_{d1,s}(n3))F_{d2,s}(n4)
    K(n1,n2,n3,n4).
```

This explains why Module 270's threshold-only audit is not obviously enough:
row and column bounds control local mass, but the phase kernels control how
mass aligns across shifts and frequencies.

## 6. Edge cases

- Fixed `xi` is not an equation; frequency summation is what creates a phase
  kernel.
- A minor-arc kernel is not the full orthogonality delta.
- A large-spectrum subset is data-dependent; its kernel cannot be replaced by
  a fixed smooth major/minor kernel without a new selection argument.
- Same-frequency pairs and same-shift pairs are different tests.
- Rectangles require four transverse edges; the row and column ceilings limit
  their number but do not estimate the weighted rectangle correlation.
- Conjugation signs must be tracked. Dropping them changes the phase kernel.
- W-residue restrictions, prime powers, truncation, and selector transfer can
  alter the allowed frequency families and cannot be appended afterward.
- Full-frequency identities are diagnostics only unless a transfer from the
  restricted minor-arc kernel is proved.

## 7. Where it fits in the project map

```text
Module 269
  -> TransIncCore_269, the transverse weighted graph

Module 270
  -> ThresholdRemovalAudit_270, the row/column threshold test

Module 271
  -> TransPhaseExpansion_271, the exact phase-kernel objects behind
     transverse pairs and rectangles
```

The next useful step is:

```text
Module 272:
  compare available tools against these exact phase-kernel objects:
  large sieve, additive energy, ordinary pair-BDH, rectangle-BDH,
  first-moment HL, and generic finite-complexity HL.
```

## 8. What remains open

This module does not prove:

- `PhaseIncidenceGate_271`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
- transverse energy smallness;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- selector transfer to the actual sharp moving selector;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- `ProjectedMajorTarget_3^B`, `WProjectedLocalMatch_3^major`,
  or `ProjectedModelNeutrality_3^major`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not replace restricted minor-arc kernels by full-frequency diagonal
  equations.
- Do not treat phase expansion as cancellation.
- Do not count unweighted rectangles as a substitute for weighted residual
  correlations.
- Do not use pair-BDH, rectangle-BDH, or first-moment HL until Module 272
  checks whether they match the exact phase-kernel objects.
- Do not move between selector/model classes without a named transfer theorem.
- Do not use `PhaseIncidenceGate_271` as an input to prove itself or the
  endpoint it would imply.
