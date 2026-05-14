# Module 213: Selector-class transfer line for projected major arcs

## 1. Precise theorem / claim being advanced

This module states the selector-transfer line required before a projected
major-arc estimate in a model, smoothed, frozen, or lifted selector class can
be used for the actual sharp moving selector.

Define:

```text
MajorSelectorTransfer_3^P(P_adm;s_0 -> s_*)
```

for a chosen selector chain from an initial selector class `s_0` to a target
selector class `s_*`.

Conditional claim:

```text
ProjectedMajorTarget_3^B(s_0;P_adm)
  + MajorSelectorTransfer_3^P(P_adm;s_0 -> s_*)
    => ProjectedMajorTarget_3^B(s_*;P_adm).
```

In particular, if:

```text
s_* = sharp-moving,
```

then the target selector is:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

This module does not prove any selector transfer estimate. It states the
normalization and error terms that must be controlled before the project may
upgrade a non-actual selector statement to the actual sharp moving selector.

## 2. Status label

`CONDITIONAL`

The implication follows from the triangle inequality in the projected
fourth-moment norm once every adjacent selector-transfer error is
W-admissible. The transfer estimates themselves remain open.

## 3. Selector classes

Every projected major-arc theorem must declare one of the following selector
classes.

### A. Finite-stage model selector

Write:

```text
s=fs
```

for finite-stage, reference, survivor, core-floor, rebalanced, or hardened
model measures used inside a construction. These selectors may live on a
finite reference probability space rather than on the actual primes.

### B. Hidden Bernoulli lift

Write:

```text
s=bern
```

for an alpha-dependent Bernoulli reference lift. This is a probabilistic
selector class. A high-probability or expectation statement in this class is
not automatically a deterministic statement for the actual selector.

### C. Smoothed finite-band frozen selector

Write:

```text
s=sm
```

for a smooth Fourier-truncated approximation to a dyadic frozen window. A
typical schematic form is:

```text
chi_{alpha,X,M}^{sm}(p)
  approx smooth_M( ||alpha p|| < 1/log X ).
```

The smoothing scale, frequency band, transition width, and denominator range
are part of the selector data.

### D. Sharp frozen dyadic selector

Write:

```text
s=fr
```

for:

```text
chi_{alpha,X}^{fr}(p)=1_{||alpha p||<1/log X}.
```

This selector is sharp on a dyadic shell but freezes the moving threshold at
`X`.

### E. Actual sharp moving selector

Write:

```text
s=mv
```

for:

```text
chi_alpha(p)=1_{||alpha p||<1/log p}.
```

This is the selector in the original problem. It may only be reached from
another selector class through the transfer errors in this module and the
other side packages already named in the project.

## 4. Projected major-arc objects in each selector class

For a selector class `s`, let:

```text
nu_s
```

be the corresponding W-tricked prime or model weight, after the selector has
been applied in that class. Define:

```text
f_s=nu_s-1,
B_{d,s}(n)=f_s(n+d)conj(f_s(n)).
```

If centering is used:

```text
c_{d,s}=E_n B_{d,s}(n),
B_{d,s}^circ=B_{d,s}-c_{d,s}.
```

The projected major-arc norm is:

```text
M_major^{P,s}(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      ||P_M B_{d,s}||_{U^2}^4.
```

Equivalently:

```text
M_major^{P,s}(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} |m_M(xi)|^4 |widehat{B_{d,s}}(xi)|^4,
```

with the zero-mode convention of Modules 206 and 209. If centered cubes are
used, replace `B_{d,s}` by `B_{d,s}^circ` everywhere and add the centering
transfer error below.

The projected physical cube is:

```text
ActualProjCube_{d,s}^P
  = E_{n,h,k,t} W_M(t)
      B_{d,s}(n-t0)
      conj(B_{d,s}(n+h-t1))
      conj(B_{d,s}(n+k-t2))
      B_{d,s}(n+h+k-t3).
```

Selector transfer must be stated for this projected residual object, not only
for the one-point selector or for `f_s`.

## 5. Adjacent selector-transfer errors

Let:

```text
s_a -> s_b
```

be one adjacent step in a chosen transfer chain. If the two selector classes
live on different probability spaces, let:

```text
T_{a->b}
```

be the declared transport map from the `s_a` space to the `s_b` space.

The core projected fourth-moment transfer error is:

```text
SelErr_major^P(a->b;N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      || P_M^b B_{d,b}
          - T_{a->b}(P_M^a B_{d,a}) ||_{U^2}^4.
```

If both selectors live on the same physical interval and use the same
projection, this reduces to:

```text
SelErr_major^P(a->b;N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      || P_M(B_{d,b}-B_{d,a}) ||_{U^2}^4.
```

The full adjacent package must also include the following terms when the
corresponding issue appears in the step.

### A. Boundary transfer

```text
SelBd_major^P(a->b;N,w;rho)=o_W(1).
```

This covers endpoint losses, cyclic-to-interval changes, dyadic shell
boundaries, and vertices moved outside the valid interval after forming the
projected cube.

### B. Transition transfer

```text
TransWin_major^P(a->b;N,w;rho)=o_W(1).
```

This covers the boundary layer between a smoothed selector and a sharp window,
including points where:

```text
||alpha p|| approx 1/log X
```

or, for the moving selector:

```text
||alpha p|| approx 1/log p.
```

### C. Moving-window transfer

For the frozen-to-moving step:

```text
MoveWin_major^P(fr->mv;N,w;rho)=o_W(1)
```

must control the difference between:

```text
1/log X
```

and:

```text
1/log p
```

after the selector has been propagated through `B_d` and the projected
fourth-moment cube.

### D. Prefix safety

```text
Prefix_major^P(a->b;N,w;rho)=o_W(1).
```

This controls primes or model points below the stable dyadic range, including
short initial intervals where the frozen threshold, W-trick normalization, or
finite-stage construction does not match the target object.

### E. Denominator transfer

```text
DenSel_major^P(a->b;N,w;rho)=o_W(1).
```

This controls changes in rational denominators created by smoothing,
finite-band truncation, Bernoulli lifting, W-tricking, and the major-arc
projection. It must be compatible with:

```text
DenAdm(N,w;R,eta,P_M).
```

### F. Tail transfer

```text
TailSel_major^P(a->b;N,w;rho)=o_W(1).
```

This includes Fourier tails of smoothed selectors, dyadic tails, construction
tails, and unbounded-weight tails after forming `B_{d,s}`.

### G. Projection transfer

```text
ProjSel_major^P(a->b;N,w;rho)=o_W(1).
```

This controls changes in:

```text
P_M, m_M, K_M, t, R, eta
```

between selector classes. A selector approximation before projection does not
automatically remain small after applying `P_M` and taking the `U^2` fourth
moment.

### H. W-residue transfer

```text
WResSel_major^P(a->b;N,w;rho)=o_W(1).
```

Selector changes must preserve the W-tricked residue classes at every
projected vertex. Failures belong here or to the W-residue package, but must
not be absorbed into `Omega_w^proj`.

### I. Prime-power transfer

```text
PPSel_major^P(a->b;N,w;rho)=o_W(1).
```

If one selector class is prime-only and another uses a von-Mangoldt-type
weight, the difference must be routed through the projected fourth-moment
prime-power package of Module 211.

### J. Centering and zero-mode transfer

If centered products are used, require:

```text
CenterSel_major^P(a->b;N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      |c_{d,b}-c_{d,a}|^4
  = o_W(1),
```

or the corresponding projected zero-mode leakage estimate after interval and
kernel truncation. This prevents selector changes from reintroducing the
zero-frequency term.

## 6. Full transfer package

For an adjacent step `a->b`, define:

```text
AdjSelTransfer_major^P(a->b;P_adm)
```

to mean that every relevant error in Section 5 is W-admissible:

```text
SelErr_major^P
 + SelBd_major^P
 + TransWin_major^P
 + MoveWin_major^P
 + Prefix_major^P
 + DenSel_major^P
 + TailSel_major^P
 + ProjSel_major^P
 + WResSel_major^P
 + PPSel_major^P
 + CenterSel_major^P
 = o_W(1).
```

The displayed sum means that each needed component satisfies:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P_adm(N,w)} Err(N,w;rho)=0.
```

The limit order is:

```text
w fixed,
N -> infinity,
w -> infinity.
```

For a chain:

```text
s_0 -> s_1 -> ... -> s_J=s_*,
```

define:

```text
MajorSelectorTransfer_3^P(P_adm;s_0 -> s_*)
```

to mean:

```text
AdjSelTransfer_major^P(s_j->s_{j+1};P_adm)
```

for every `0<=j<J`.

A common target chain is:

```text
fs -> bern -> sm -> fr -> mv,
```

but the project may use a shorter chain if every skipped edge is replaced by a
direct adjacent-style package with the same projected fourth-moment strength.

## 7. Assumptions

The transfer package assumes:

- the selector class is declared before the theorem is stated;
- the same dyadic `d` range is used on both sides of each adjacent step;
- each selector class has a declared W-tricked weight `nu_s`;
- every transport map `T_{a->b}` is stated before being used;
- projection operators and major-arc denominator ranges are either identical
  across the step or included in `ProjSel_major^P` and `DenSel_major^P`;
- boundary, W-residue, prime-power, and centering errors are not hidden inside
  the selector notation;
- all transfer estimates are uniform over `rho in P_adm(N,w)`;
- the fixed-`w`, `N -> infinity`, then `w -> infinity` limit order is used;
- the target `mv` selector is the actual sharp moving selector
  `chi_alpha(p)=1_{||alpha p||<1/log p}`.

No assumption in this list proves a transfer error. Each only states the
objects that must be present before the conditional triangle-inequality
argument can be applied.

## 8. Conditional proof / reduction

For an adjacent step `a->b`, write:

```text
X_{d,a}=P_M^a B_{d,a},
X_{d,b}=P_M^b B_{d,b}.
```

By:

```text
|u+v|^4 <= 8|u|^4+8|v|^4,
```

and the Fourier form of the `U^2` norm:

```text
||X_{d,b}||_{U^2}^4
  <= 8 ||T_{a->b}X_{d,a}||_{U^2}^4
     + 8 ||X_{d,b}-T_{a->b}X_{d,a}||_{U^2}^4.
```

If `T_{a->b}` is norm-compatible up to the side errors in
`AdjSelTransfer_major^P`, then after averaging over `D<|d|<=2D`:

```text
M_major^{P,b}
  <= C M_major^{P,a}
     + C AdjErr_major^P(a->b),
```

where `AdjErr_major^P(a->b)` is the sum of the adjacent transfer errors.

Iterating along the chain gives:

```text
M_major^{P,s_*}
  <= C_J M_major^{P,s_0}
     + C_J sum_{j<J} AdjErr_major^P(s_j->s_{j+1}).
```

Thus, if:

```text
M_major^{P,s_0}=o_W(1)
```

and:

```text
MajorSelectorTransfer_3^P(P_adm;s_0 -> s_*)
```

holds, then:

```text
M_major^{P,s_*}=o_W(1).
```

This proves the conditional selector-transfer claim. It does not estimate any
transfer error.

The same argument applies to the physical projected cube form because:

```text
M_major^{P,s}
```

and:

```text
(1/D) sum_d ActualProjCube_{d,s}^P
```

are the same projected `U^2` fourth moment under the conventions of Module
206, up to the already named boundary, centering, and zero-mode terms.

## 9. Edge cases

- A pointwise or first-moment selector approximation does not imply
  `SelErr_major^P=o_W(1)` after forming `B_d`.
- The product `B_d=f(n+d)conj(f(n))` can amplify selector errors at either
  endpoint of the shifted pair.
- Smoothing errors concentrate near the threshold boundary and must be
  measured after projection.
- Frozen dyadic estimates can fail near dyadic endpoints unless prefix and
  boundary terms are included.
- The moving window `1/log p` changes across a dyadic shell; this is not
  automatically lower order in the projected fourth moment.
- Hidden Bernoulli estimates require a deterministic extraction or
  high-probability-to-deterministic transfer before they apply to a fixed
  alpha.
- If the selector change alters denominator support, the major-arc partition
  can change.
- If prime powers are present in one class but not another, Module 211 is
  required.
- If W-residue compatibility is broken by a selector step, the Euler product
  `Omega_w^proj` no longer describes the local model.
- If centered cubes are used, zero-mode leakage must be controlled after the
  selector change.

## 10. Where it fits in the project map

The Phase C chain now has:

```text
Module 206
  -> exact projected major-arc target
Module 207
  -> exact projected local singular factors
Module 208
  -> projected collision stratification
Module 209
  -> W-admissible projected local-model theorem
Module 210
  -> cyclic-to-interval boundary transfer
Module 211
  -> prime-power and small-prime transfer
Module 212
  -> local-model compatibility ledger
Module 213
  -> projected major-arc selector transfer line.
```

This module fills the selector-transfer slot left open in Modules 206 and 209.
It prepares the next iteration, Module 214, which is the scheduled third
9-iteration plan update.

## 11. What remains open

This module does not prove:

- `MajorSelectorTransfer_3^P(P_adm;s_0 -> s_*)`;
- any adjacent selector-transfer package;
- deterministic extraction from the hidden Bernoulli lift;
- smoothed-to-sharp frozen transfer;
- frozen-to-moving transfer;
- denominator transfer for projected major arcs;
- tail transfer in projected fourth-moment norm;
- W-residue selector transfer;
- prime-power selector transfer;
- centering and zero-mode selector transfer;
- `WProjectedLocalMatch_3^major`;
- `LocalModelCompat_3^major`;
- `CycIntTransfer_3^major`;
- `PPSPTransfer_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not transfer a finite-stage, Bernoulli, smoothed, or frozen selector
  estimate to the actual sharp moving selector without
  `MajorSelectorTransfer_3^P`.
- Do not measure selector transfer only at the one-point `chi` level; measure
  it after forming `B_d` and applying `P_M`.
- Do not treat smoothing, threshold, prefix, denominator, tail, W-residue, or
  prime-power errors as cosmetic.
- Do not use a high-probability Bernoulli statement as a deterministic theorem
  for a fixed alpha without an extraction step.
- Do not transfer minor-arc selector estimates to major arcs without checking
  the projection and denominator packages.
- Do not claim projected local-model matching, projected major-arc
  cancellation, the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
