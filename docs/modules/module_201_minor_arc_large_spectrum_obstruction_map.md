# Module 201: Minor-arc spectral large-spectrum obstruction map

## 1. Precise theorem / claim being advanced

This module maps what a failure of minor-arc decay must look like.

The minor-arc target is:

```text
M_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4
  = o(1),
```

where:

```text
B_d(n)=f(n+d)conj(f(n)),   f=nu-1.
```

The deterministic claim is:

```text
If M_minor(D) is not small, then after choosing a low threshold lambda_0,
at least one named obstruction must occur:

low-level L^2 leakage,
dyadic large-spectrum count obstruction,
adaptive energy-tail obstruction,
bad-shift concentration,
persistent minor-frequency concentration,
or transverse incidence concentration.
```

This module does not prove that any obstruction is absent. It names the
possible failure modes that future minor-arc work must exclude.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The implications are deterministic consequences of the layer-cake and dyadic
decompositions in Modules 180 and 197. No analytic minor-arc cancellation is
proved here.

## 3. Definitions and variables

Use the notation of Modules 179-200:

```text
f=nu-1
B_d(n)=f(n+d)conj(f(n))
widehat{B_d}(xi)=E_n B_d(n)e(-xi n)
Minor(R,eta)={xi != 0}\Major(R,eta)
```

For `lambda>0`, define the minor-arc large spectrum:

```text
Spec_d^minor(lambda)
  = { xi in Minor(R,eta) : |widehat{B_d}(xi)| >= lambda }.
```

The averaged count profile is:

```text
L_minor(lambda;D)
  = (1/D) sum_{D<|d|<=2D} #Spec_d^minor(lambda).
```

The averaged energy-tail profile is:

```text
E_minor(>=lambda;D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Spec_d^minor(lambda)}
        |widehat{B_d}(xi)|^2.
```

The low-level `L^2` envelope is:

```text
E2_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^2.
```

For a family of frequency sets:

```text
T={T_d subset Minor(R,eta)}_{D<|d|<=2D},
```

write:

```text
size_D(T)=(1/D) sum_{D<|d|<=2D} #T_d,

energy_D(T)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in T_d} |widehat{B_d}(xi)|^2.
```

The adaptive restriction envelope is:

```text
R_{2,B}^minor(rho;D)
  = sup_{T_d subset Minor(R,eta), size_D(T)<=rho} energy_D(T).
```

For incidence bookkeeping, define:

```text
I_lambda
  = { (d,xi) : D<|d|<=2D, xi in Spec_d^minor(lambda) }.
```

For each shift and frequency:

```text
E_d(lambda)
  = sum_{xi in Spec_d^minor(lambda)} |widehat{B_d}(xi)|^2,

N_xi(lambda)
  = # { d : D<|d|<=2D, xi in Spec_d^minor(lambda) }.
```

Large spectrum means actual shifted correlations:

```text
xi in Spec_d^minor(lambda)
  => |E_n f(n+d)conj(f(n))e(-xi n)| >= lambda.
```

## 4. Assumptions

This module assumes:

- the finite cyclic Fourier model or a transferred interval model;
- normalized Fourier transform;
- major/minor arcs are already separated;
- zero frequency is excluded;
- an upper Fourier envelope `A_N` satisfies
  `|widehat{B_d}(xi)|<=A_N`;
- a low threshold `lambda_0` and dyadic grid
  `lambda_j in [lambda_0,A_N]` have been chosen;
- boundary, W-limit, prime-power, and selector transfer are not silently
  imported.

## 5. Proof / disproof / reduction

### A. First obstruction: low-level leakage

By Module 180:

```text
M_minor(D)
  <= lambda_0^2 E2_minor(D)
     + C sum_{lambda_j in [lambda_0,A_N]}
          lambda_j^4 L_minor(lambda_j;D).
```

Therefore, if:

```text
M_minor(D) >= eps
```

and:

```text
lambda_0^2 E2_minor(D) < eps/2,
```

then some dyadic `lambda_j` must satisfy:

```text
lambda_j^4 L_minor(lambda_j;D)
  >= c eps / J,
```

where `J` is the number of dyadic thresholds and `c>0` is an absolute
constant. If the low-level term is not small, the first obstruction is:

```text
LowLevelLeak(lambda_0):
  lambda_0^2 E2_minor(D) is not small.
```

This obstruction is not a large-spectrum phenomenon. It says the sea of small
minor-arc coefficients is too energetic.

### B. Second obstruction: dyadic count failure

If low-level leakage is absent but `M_minor(D)` remains large, then for some
dyadic `lambda`:

```text
CountObs(lambda):
  lambda^4 L_minor(lambda;D) is not small.
```

This can happen in two visibly different ways:

```text
sparse-spike obstruction:
  L_minor(lambda;D) is small but lambda is large;

dense-plateau obstruction:
  lambda is moderate but L_minor(lambda;D) is too large.
```

The first asks for pointwise or near-pointwise exclusion of large minor-arc
correlations. The second asks for genuine density decay of the minor-arc large
spectrum.

### C. Third obstruction: adaptive energy-tail failure

By Module 197:

```text
M_minor(D)
  = integral_0^infty
      2 lambda E_minor(>=lambda;D) dlambda.
```

Dyadically, if low-level leakage is absent and `M_minor(D)` is large, then for
some dyadic `lambda`:

```text
EnergyObs(lambda):
  lambda^2 E_minor(>=lambda;D) is not small.
```

At that threshold, let:

```text
T_d=Spec_d^minor(lambda).
```

Then:

```text
size_D(T)=L_minor(lambda;D),
energy_D(T)=E_minor(>=lambda;D).
```

Thus either the density profile is too large:

```text
L_minor(lambda;D) > Lambda_*(lambda;D),
```

or the adaptive restriction envelope fails:

```text
R_{2,B}^minor(L_minor(lambda;D);D)
  is too large.
```

This is the precise Module 197 obstruction.

### D. Fourth obstruction: bad-shift concentration

The energy-tail obstruction may be concentrated on a small set of shifts.
For `mu>0`, define:

```text
BadShift(lambda,mu)
  = { d : E_d(lambda) >= mu }.
```

Since:

```text
E_minor(>=lambda;D)
  = (1/D) sum_{D<|d|<=2D} E_d(lambda),
```

a large energy-tail forces either many moderately bad shifts or a few very bad
ones. Future estimates must therefore control not only:

```text
#Spec_d^minor(lambda)
```

on average, but the weighted energy carried by exceptional shifts.

This is why counting bad shifts without energy weights is not enough.

### E. Fifth obstruction: persistent minor-frequency concentration

The same incidence set may concentrate on a few minor frequencies. For each
minor frequency:

```text
N_xi(lambda)
  = # { d : xi in Spec_d^minor(lambda) }.
```

If some `xi in Minor(R,eta)` has large `N_xi(lambda)`, then many shifts
satisfy:

```text
|E_n f(n+d)conj(f(n))e(-xi n)| >= lambda.
```

This is a persistent minor-frequency obstruction. It suggests a correlation
problem in the shift variable:

```text
d -> E_n f(n+d)conj(f(n))e(-xi n).
```

A successful minor-arc proof must show that such persistent minor phases are
rare or energetically negligible.

### F. Sixth obstruction: transverse incidence concentration

If neither bad shifts nor persistent frequencies dominate, the obstruction is
spread across many `(d,xi)` incidences:

```text
I_lambda
  = { (d,xi) : xi in Spec_d^minor(lambda) }.
```

This transverse case is the hardest to dismiss by one-dimensional averaging.
It asks for a genuine incidence or restriction estimate for the family:

```text
widehat{B_d}(xi)
  = E_n f(n+d)conj(f(n))e(-xi n).
```

In Module 197 language, this is exactly the need for:

```text
R_{2,B}^minor(rho;D) <= Psi_*(rho;D).
```

### G. Resulting obstruction tree

The failure of minor-arc decay is therefore routed as:

```text
M_minor(D) not small
  -> LowLevelLeak(lambda_0)
  or CountObs(lambda)
  or EnergyObs(lambda)
       -> density failure
       -> adaptive restriction failure
            -> bad-shift concentration
            -> persistent minor-frequency concentration
            -> transverse incidence concentration.
```

This tree is structural. The next analytic problem is to prove that every
branch of the tree is impossible or small in the W-tricked short-shift range.

## 6. Edge cases

- The dyadic loss `J` may matter if `A_N/lambda_0` is large. Later estimates
  must budget logarithmic losses explicitly.
- Low-level leakage cannot be dismissed by large-spectrum counting.
- Sparse spikes and dense plateaus require different tools; one estimate may
  not control both.
- A small number of shifts can carry large energy and still have small
  unweighted density.
- A persistent minor frequency is not a major-arc frequency by definition; it
  is an obstruction to proving that only major arcs carry structured mass.
- The incidence map depends on the selected Fourier model and may change under
  interval-to-cyclic transfer.
- Collision hyperplanes in the physical cube may create apparent spectrum and
  must be separated from genuine minor-arc obstruction.
- Prime-power artifacts in `nu` may create spurious large coefficients unless
  removed or transferred.

## 7. Where it fits in the project map

Module 201 follows the Phase B reductions:

```text
Module 197
  -> density/energy criterion
Module 198
  -> ordinary pair-BDH shortcut blocked
Module 199
  -> ordinary rectangle/HL shortcuts blocked
Module 200
  -> dyadic derivative U^2 is exact but not new
Module 201
  -> obstruction tree for minor-arc large-spectrum failure.
```

The next scheduled iteration is the first 15-iteration plan challenge. It
should ask whether Phase B is still the right route after identifying the
minor-arc obstruction tree.

## 8. What remains open

This module does not prove:

- low-level `L^2` control;
- dyadic large-spectrum density decay;
- adaptive restriction-energy bounds;
- bad-shift energy bounds;
- persistent minor-frequency exclusion;
- transverse incidence estimates;
- any major-arc estimate using `Omega_w`;
- `ProjectedLocalMatch_3^major`;
- minor-arc fourth-moment decay;
- transfer to actual sharp moving selectors;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem, all-alpha theorem, or
  unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite the obstruction tree as a proof of minor-arc cancellation.
- Do not ignore low-level `L^2` leakage.
- Do not treat large-spectrum counts as adaptive energy control.
- Do not replace shift-energy bounds by unweighted bad-shift counts.
- Do not treat persistent minor frequencies as major arcs.
- Do not use ordinary pair-BDH, ordinary rectangle-BDH, or first-moment HL as
  substitutes for the incidence/restriction estimates named here.
- Do not transfer cyclic, smoothed, frozen, projected, or model estimates to
  the actual sharp moving selector without the full transfer package.
