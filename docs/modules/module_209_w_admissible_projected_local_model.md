# Module 209: W-admissible projected local-model theorem

## 1. Precise theorem / claim being advanced

This module states the W-admissible theorem needed to turn the exact projected
local model from Modules 206-208 into a usable major-arc input.

Define the missing package:

```text
WProjectedLocalMatch_3^major(P_adm).
```

It asserts that the actual projected cube is matched by the exact projected
residual local model:

```text
MatchErr_major^P(N,w;rho)=o_W(1)
```

uniformly over all admissible projected major-arc parameters:

```text
rho in P_adm(N,w).
```

The claim of this module is a conditional reduction:

```text
WProjectedLocalMatch_3^major(P_adm)
  + ProjectedModelNeutrality_3^major(P_adm)
    => ProjectedMajorTarget_3^B(P_adm).
```

The module also gives a sufficient error ledger for
`WProjectedLocalMatch_3^major`: residual subset-HL matching, synchronized
structural treatment, boundary transfer, kernel tails, W-residue compatibility,
prime-power removal, projection-boundary control, and denominator/range
admissibility.

This is not a proof of any of those inputs.

## 2. Status label

`CONDITIONAL`

The implication is deterministic after the named W-admissible error terms are
assumed. The required estimates remain open.

## 3. Definitions and variables

Use:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)).
```

Let:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff)
```

denote a projected major-arc parameter tuple. The permitted family is:

```text
P_adm(N,w).
```

It contains only parameter choices satisfying the project range restrictions:

```text
D in D_range(N,Hcal),
R and eta in the allowed major-arc range,
P_M has multiplier m_M with m_M(0)=0,
H,K are the h,k averaging-window sizes,
T is the kernel truncation scale when truncation is used.
```

For fixed `rho`, the actual projected cube is:

```text
ActualProjCube_d^P
  = E_{n,h,k} E_t W_M(t)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3).
```

The exact projected local model is:

```text
ModelProjCube_d^P
  = E_{h,k} E_t W_M(t) Omega_w^proj(d,h,k;t),
```

where:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset V(d,h,k;t)}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The matching error is:

```text
MatchErr_major^P(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_d^P - ModelProjCube_d^P|.
```

The projected model-neutrality error is:

```text
NeutralErr_major^P(N,w;rho)
  = |(1/D) sum_{D<|d|<=2D} ModelProjCube_d^P|.
```

The projected major-arc target from Module 206 is:

```text
ProjectedMajorTarget_3^B(N,w;rho):
  |(1/D) sum_{D<|d|<=2D} ActualProjCube_d^P|=o_W(1).
```

## 4. W-admissibility and denominator restrictions

For an error term `Err(N,w;rho)`, define:

```text
Err=o_W(1) over P_adm
```

to mean:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P_adm(N,w)} |Err(N,w;rho)| = 0.
```

Equivalently:

```text
for every eps>0,
there exists w0,
for every w>=w0,
there exists N0(w),
for every N>=N0(w) and every rho in P_adm(N,w),
|Err(N,w;rho)| <= eps.
```

The theorem must use the order:

```text
w fixed,
N -> infinity,
w -> infinity.
```

A diagonal `w=w(N)` is allowed only after this two-stage estimate has been
proved and only if the W-trick side restrictions, such as `W=N^{o(1)}` when
needed, remain valid.

The major-arc denominator package is:

```text
DenAdm(N,w;R,eta,P_M).
```

It requires:

- denominators in the support of `P_M` satisfy `1<=q<=R`;
- the zero frequency is excluded;
- overlap of rational neighborhoods is handled by a multiplier or partition of
  unity with bounded overlap constants;
- buffered arcs are available when comparing sharp and smoothed projections;
- CRT moduli created by projected local-model matching fit within the
  available averaging ranges, or their range errors are separately
  W-admissible;
- constants in the projected HL estimates are uniform over the whole
  denominator family.

This module does not specify a final choice of `R` or `eta`; it specifies what
any such choice must satisfy.

## 5. The W-admissible matching package

`WProjectedLocalMatch_3^major(P_adm)` consists of the following inputs.

### A. Residual projected subset-HL matching

For every subset `S subset V(d,h,k;t)`, suppose the actual tuple average has
the form:

```text
E_n prod_{v in S} nu(v)
  = Theta_{w,S}^proj(d,h,k;t) + Error_S(d,h,k;t),
```

with the same projected vertices, W-trick, intervals, and kernel convention as
the actual cube.

Define the residual signed subset error:

```text
Err_res(d,h,k;t)
  = sum_{S subset V(d,h,k;t)}
      (-1)^(8-|S|) Error_S(d,h,k;t).
```

The required variance-strength residual matching condition is:

```text
ResHLErr_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      | E_{h,k} E_t W_M(t) Err_res(d,h,k;t) |
  = o_W(1).
```

A stronger sufficient form is:

```text
AbsHLErr_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k} E_t |W_M(t)|
        sum_S |Error_S(d,h,k;t)|
  = o_W(1).
```

The stronger form is not required by definition, but it is often easier to
verify. A first-moment asymptotic that is not strong enough to imply one of
these residual estimates does not supply projected local-model matching.

### B. Structural synchronization

Let `Z_struct` be the structural zero set from Module 208. If the subset-HL
input removes `Z_struct`, the same removal must be made on both the actual and
model sides. The resulting error is:

```text
StructSyncErr_major(N,w;rho)=o_W(1).
```

If instead the theorem keeps `Z_struct`, it must use the correct
lower-dimensional exact local model on that stratum. Codimension counting
alone is not enough unless the local factors and kernel weights are also
controlled.

### C. Large-prime collision handling

For exact projected local-model matching, large-prime congruence collisions
are included in:

```text
r_p(S;d,h,k;t)
```

and hence in `Theta_{w,S}^proj`. They should not be removed as an error.

If a proof route first matches a generic collision-free model, it must add the
qualified collision-defect error:

```text
CollDef_w(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k}E_t |W_M(t)|
        |Omega_w^proj(d,h,k;t)-Omega_w^gen|
  = o_W(1),
```

with the small-load or overflow hypotheses from Modules 187-192. This is a
route-specific sufficient condition, not part of the exact model definition.

### D. Boundary and kernel-tail errors

The theorem must include:

```text
CycIntBd_major(N,w;rho)=o_W(1),
TailBd_major(N,w;rho,T)=o_W(1),
BoundaryMatch(N,w;rho)=o_W(1).
```

These cover cyclic wraparound, interval cutoffs, vertices moved outside valid
ranges, and kernel truncation. They are not Euler-factor errors.

### E. W-residue and small-prime errors

Primes `p<=w` are handled by the W-trick. The matching package requires:

```text
WResBd_major(N,w;rho)=o_W(1).
```

This includes residue-class failures caused by projection shifts, boundary
cutoffs, or incompatible tuple forms.

### F. Prime-power removal

If `nu` is von-Mangoldt-like or otherwise includes prime-power artifacts, the
projected fourth-moment version of prime-power transfer is required:

```text
PPErr_major(N,w;rho)=o_W(1).
```

### G. Projection-boundary compatibility

If `P_M` is smoothed but the target is sharp, or if a buffered major-arc
partition is used, the projection discrepancy must be W-admissible:

```text
ProjBd_major(N,w;rho)=o_W(1).
```

This is the major-arc analogue of the threshold/boundary discipline from the
minor-arc transfer modules.

### H. Selector class declaration

The theorem must declare the selector class. If the target is the actual sharp
moving selector:

```text
chi_alpha(p)=1_{||alpha p||<1/log p},
```

then a separate projected selector-transfer error is required:

```text
SelErr_major^P(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      ||P_M(B_{d,sharp}-B_{d,model})||_{U^2}^4
  = o_W(1).
```

Without this, the theorem applies only to the stated model, W-tricked,
smoothed, or frozen selector class.

## 6. Conditional proof / reduction

Expand:

```text
B_d(x)=f(x+d)conj(f(x)),  f=nu-1.
```

Then:

```text
ActualProjCube_d^P
  = E_{h,k,t} W_M(t)
      sum_{S subset V(d,h,k;t)}
        (-1)^(8-|S|)
        E_n prod_{v in S} nu(v),
```

up to boundary, W-residue, prime-power, projection, and selector-transfer
terms appropriate to the chosen model.

Insert the subset-HL matching formula:

```text
E_n prod_{v in S} nu(v)
  = Theta_{w,S}^proj + Error_S.
```

The local-model terms combine by inclusion-exclusion:

```text
sum_S (-1)^(8-|S|) Theta_{w,S}^proj
  = Omega_w^proj.
```

Therefore:

```text
ActualProjCube_d^P - ModelProjCube_d^P
  = E_{h,k,t} W_M(t) Err_res(d,h,k;t)
    + structural/boundary/W-residue/prime-power/projection/selector errors.
```

Averaging the absolute value over `D<|d|<=2D` gives:

```text
MatchErr_major^P
  <= ResHLErr_major
     + StructSyncErr_major
     + CycIntBd_major
     + TailBd_major
     + BoundaryMatch
     + WResBd_major
     + PPErr_major
     + ProjBd_major
     + SelErr_major^P,
```

plus `CollDef_w` if the route passes through a generic collision-free model
instead of matching the exact `Theta_{w,S}^proj` factors directly.

If every displayed error is `o_W(1)` uniformly over `rho in P_adm(N,w)`, then:

```text
MatchErr_major^P=o_W(1).
```

Finally:

```text
|(1/D)sum_d ActualProjCube_d^P|
  <= MatchErr_major^P + NeutralErr_major^P.
```

Thus:

```text
WProjectedLocalMatch_3^major(P_adm)
  + ProjectedModelNeutrality_3^major(P_adm)
    => ProjectedMajorTarget_3^B(P_adm).
```

This proves only the conditional reduction.

## 7. Edge cases

- Matching only the full eight-form local model is insufficient; all subsets
  `S` are needed for the residual expansion.
- A first-moment tuple asymptotic is insufficient unless it yields the
  residual absolute-in-`d` matching error.
- Large-prime collisions are not errors in the exact local model; they become
  errors only when replacing the exact model by a generic collision-free one.
- Structural strata cannot be removed only on the actual side.
- A smoothed projection changes the multiplier and therefore the physical
  kernel; its model must match that projection.
- If constants depend on `R`, `eta`, `M`, `T`, or the CRT envelope, the
  W-admissibility statement can fail.
- Boundary and kernel-tail errors are not covered by Euler products.
- Prime-power removal must be in projected fourth-moment or projected-cube
  form, not merely a first-moment assertion.
- The actual sharp moving selector requires its own projected transfer error.

## 8. Where it fits in the project map

The Phase C chain now has:

```text
Module 206
  -> exact projected major-arc target
Module 207
  -> exact projected local singular factors
Module 208
  -> projected collision stratification
Module 209
  -> W-admissible projected local-model theorem.
```

The major-arc branch is now organized as:

```text
actual projected cube
  -> WProjectedLocalMatch_3^major
  -> exact projected residual model Omega_w^proj
  -> ProjectedModelNeutrality_3^major
  -> ProjectedMajorTarget_3^B.
```

The next scheduled module is the cyclic-to-interval boundary audit for the
projected major-arc model.

## 9. What remains open

This module does not prove:

- `WProjectedLocalMatch_3^major(P_adm)`;
- residual subset-HL matching for all `S`;
- structural synchronization on `Z_struct`;
- the Module 192 collision-defect hypotheses for the actual projection;
- W-admissible boundary and kernel-tail transfer;
- W-residue compatibility for the projected vertices;
- prime-power removal in projected fourth-moment norm;
- projection-boundary transfer between smoothed and sharp major arcs;
- selector transfer to the actual sharp moving selector;
- `ProjectedModelNeutrality_3^major` without its conditional hypotheses;
- `ProjectedMajorTarget_3^B` unconditionally;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite `WProjectedLocalMatch_3^major` unless all W-admissible error
  terms in the chosen route are supplied.
- Do not take `w -> infinity` before the fixed-`w`, `N -> infinity` estimates.
- Do not use a diagonal `w(N)` before proving the double-limit theorem.
- Do not replace the exact projected residual model by the full eight-form
  model or by the unprojected model.
- Do not discard structural or large-prime collision strata unless the route
  explains whether they are included in the exact model or estimated as an
  error.
- Do not hide boundary, kernel-tail, W-residue, prime-power, projection, or
  selector errors in a generic `o(1)`.
- Do not replace the rectangle local model by a pointwise square of the pair
  local model.
- Do not claim projected major-arc cancellation, the residual cube endpoint,
  the original problem, the all-alpha theorem, the unconditional finite-type
  theorem, `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
