# Module 212: Pair, rectangle, and projected cube local-model compatibility

## 1. Precise theorem / claim being advanced

This module records the exact compatibility dictionary between the local
models used in the projected major-arc branch:

```text
kappa_w(d),
Sigma_w(d,h),
Theta_w(d,h,k),
Theta_{w,S}^proj(d,h,k;t),
Omega_w^proj(d,h,k;t).
```

Define:

```text
LocalModelCompat_3^major(P_adm).
```

The claim is structural:

```text
LocalModelCompat_3^major(P_adm)
```

is the ledger of exact face identities and forbidden non-identities needed to
keep pair, rectangle, full cube, and residual projected cube models separate.

It also states the averaged compatibility lemmas that would be required before
a proof route may replace one model by another inside the projected major-arc
average.

This module does not prove any analytic compatibility estimate and does not
close the projected major-arc branch.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The exact face identities follow from the definitions of the local Euler
factors. Every replacement beyond those identities is recorded as a named
open averaged error.

## 3. Definitions and variables

Use the projected vertices from Modules 206-211:

```text
v_{00,0}=n-t0,
v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,
v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,
v_{01,1}=n+k-t2+d,
v_{11,0}=n+h+k-t3,
v_{11,1}=n+h+k-t3+d.
```

Let:

```text
SigmaSq={00,10,01,11}
```

and define the projected base offsets:

```text
A_{00}=-t0,
A_{10}=h-t1,
A_{01}=k-t2,
A_{11}=h+k-t3.
```

Then:

```text
v_{sigma,e}=n+A_sigma+e d,
sigma in SigmaSq,
e in {0,1}.
```

For a labeled subset:

```text
S subset V(d,h,k;t)={v_{sigma,e}},
```

let:

```text
r_p(S;d,h,k;t)
```

be the number of distinct residue classes mod `p` occupied by the offsets
`A_sigma+e d` with labels in `S`.

For `p>w`, the projected subset factor is:

```text
theta_{p,S}^proj(d,h,k;t)
  = (1-1/p)^(-|S|)
      (1-r_p(S;d,h,k;t)/p),
```

and:

```text
Theta_{w,S}^proj(d,h,k;t)
  = prod_{p>w} theta_{p,S}^proj(d,h,k;t).
```

The full projected eight-form factor is:

```text
Theta_w^proj(d,h,k;t)
  = Theta_{w,V(d,h,k;t)}^proj(d,h,k;t).
```

The residual projected model is:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset V(d,h,k;t)}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

For:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
```

write the projected model average:

```text
ModelProjCube_d^P
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

## 4. Exact face identities

### A. Pair faces

For a fixed square slot `sigma`, define:

```text
S_sigma={v_{sigma,0},v_{sigma,1}}.
```

The two offsets differ by `d`, so:

```text
Theta_{w,S_sigma}^proj(d,h,k;t)=kappa_w(d),
```

where:

```text
kappa_w(d)
  = prod_{p>w} (1-1/p)^(-2)
      (1-#{0,-d mod p}/p).
```

This identity is independent of `sigma` and of the translation `A_sigma`.

### B. Rectangle faces

For two square slots `sigma != tau`, define:

```text
S_{sigma,tau}
  ={v_{sigma,0},v_{sigma,1},v_{tau,0},v_{tau,1}}.
```

Let:

```text
H_{sigma,tau}=A_tau-A_sigma.
```

Then:

```text
Theta_{w,S_{sigma,tau}}^proj(d,h,k;t)
  = Sigma_w(d,H_{sigma,tau}),
```

with:

```text
Sigma_w(d,H)
  = prod_{p>w} (1-1/p)^(-4)
      (1-#{0,-d,-H,-H-d mod p}/p).
```

The six projected rectangle displacements are:

```text
H_{00,10}=h+t0-t1,
H_{00,01}=k+t0-t2,
H_{00,11}=h+k+t0-t3,
H_{10,01}=k-h+t1-t2,
H_{10,11}=k+t1-t3,
H_{01,11}=h+t2-t3.
```

Changing the sign of `H` does not change the underlying set of four affine
forms after relabeling, but the projected displacement must still be stated.

### C. Full cube face

For the full labeled set `V`, one has:

```text
Theta_{w,V}^proj(d,h,k;t)=Theta_w^proj(d,h,k;t).
```

When:

```text
t0=t1=t2=t3=0,
```

this reduces to the unprojected two-rectangle factor:

```text
Theta_w^proj(d,h,k;0)=Theta_w(d,h,k),
```

where the eight offsets are:

```text
0,d,h,h+d,k,k+d,h+k,h+k+d.
```

### D. Residual inclusion-exclusion

The residual projected cube model is not a face. It is the signed
inclusion-exclusion sum:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset V}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

Thus `kappa_w`, `Sigma_w`, and `Theta_w^proj` appear inside the subset
dictionary, but none of them alone is the residual projected model.

## 5. Forbidden pointwise replacements

The following are not identities.

### A. Rectangle is not pair-square

At a prime `p>w`, if there are no collisions among:

```text
0,-d,-H,-H-d,
```

then:

```text
theta_p^Sigma(d,H)
  = (1-1/p)^(-4)(1-4/p),
```

whereas:

```text
theta_p^kappa(d)^2
  = (1-1/p)^(-4)(1-2/p)^2.
```

These differ already at order `1/p^2`. On collision strata the discrepancy
can be larger. Therefore:

```text
Sigma_w(d,H) != kappa_w(d)^2
```

pointwise in general.

### B. Full cube is not a product of rectangles

A product of rectangle factors treats the rectangle events as independent at
each prime. The full eight-form factor uses one union of eight forbidden
classes:

```text
1-r_p(V;d,h,k;t)/p.
```

Therefore no pointwise identity of the form:

```text
Theta_w^proj(d,h,k;t)
  = product of Sigma_w(d,H_{sigma,tau})
```

is available without an explicit local correction factor.

### C. Residual model is not the full cube model

The full eight-form factor is only the `S=V` term. The residual model is:

```text
Omega_w^proj
  = Theta_w^proj
    + signed lower-dimensional subset factors.
```

Hence:

```text
Omega_w^proj != Theta_w^proj
```

in general.

### D. Projected model is not unprojected model

When `t` is not identically zero, the rectangle and cube offsets are shifted
by:

```text
t0,t1,t2,t3.
```

Thus:

```text
Omega_w^proj(d,h,k;t)
```

cannot be replaced by:

```text
Omega_w(d,h,k)
```

unless the projection-shift discrepancy is proved negligible in the same
major-arc normalization.

## 6. Averaged compatibility lemmas required for replacements

Exact face identities may be used freely. Any replacement outside those exact
identities requires one of the following W-admissible averaged lemmas, or a
stronger explicitly stated substitute.

### A. Rectangle-to-pair averaged compatibility

If a route replaces rectangle factors by pair squares, it must prove:

```text
RectPairCompat_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      | E_{h,k,t} W_M(t)
          sum_{sigma<tau} c_{sigma,tau}(d,h,k;t)
          ( Sigma_w(d,H_{sigma,tau}) - kappa_w(d)^2 ) |
  = o_W(1),
```

for the exact signed coefficients `c_{sigma,tau}` created by that route.

A stronger absolute sufficient version is:

```text
RectPairCompat_major^abs(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k,t} |W_M(t)|
        sum_{sigma<tau}
          |Sigma_w(d,H_{sigma,tau}) - kappa_w(d)^2|
  = o_W(1).
```

Neither estimate is supplied by ordinary pair-BDH or by a first-moment
Hardy-Littlewood statement.

### B. Cube-to-rectangle averaged compatibility

If a route replaces the full projected cube factor by a rectangle-built model
`Phi_rect`, it must define:

```text
Phi_rect(d,h,k;t)
```

explicitly from the six rectangle factors and then prove:

```text
CubeRectCompat_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      | E_{h,k,t} W_M(t)
          (Theta_w^proj(d,h,k;t)-Phi_rect(d,h,k;t)) |
  = o_W(1).
```

No default `Phi_rect` is canonical in this project. Choosing one is part of
the proof route and must be recorded.

### C. Residual-to-full-cube averaged compatibility

If a route uses the full eight-form factor in place of the residual model, it
must prove:

```text
ResidualFullCompat_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      | E_{h,k,t} W_M(t)
          (Omega_w^proj(d,h,k;t)-Theta_w^proj(d,h,k;t)) |
  = o_W(1).
```

This is usually too strong to expect without exploiting the full signed
inclusion-exclusion algebra. The safer rule is to keep `Omega_w^proj`
throughout.

### D. Projected-to-unprojected averaged compatibility

If a route removes the projection shifts from the local model, it must prove:

```text
ProjUnprojCompat_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      | E_{h,k,t} W_M(t)
          (Omega_w^proj(d,h,k;t)-Omega_w(d,h,k)) |
  = o_W(1).
```

This requires kernel, boundary, and collision synchronization. It is not a
formal consequence of the definitions.

### E. Marginal absorption compatibility

If pair or rectangle marginals are subtracted through centering, one must
prove that the corresponding lower-dimensional signed subset contribution is
absorbed in the projected normalization:

```text
MargAbsorb_major(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      | E_{h,k,t} W_M(t)
          sum_{S in Lower}
            a_S Theta_{w,S}^proj(d,h,k;t) |
  = o_W(1).
```

Here `Lower` and the coefficients `a_S` must be exactly those generated by the
centering or projection argument. A vague statement that lower-dimensional
marginals are harmless is not enough.

## 7. Assumptions

This compatibility ledger assumes:

- the same projected vertices are used on the actual and model sides;
- primes `p<=w` have been handled by the W-trick and residue package;
- prime-power artifacts have been routed to `PPSPTransfer_3^major`;
- boundary and cyclic-to-interval issues have been routed to
  `CycIntTransfer_3^major`;
- collision strata are treated by the exact `r_p(S;d,h,k;t)` factors unless a
  separate collision-defect estimate is explicitly invoked;
- all averaged compatibility estimates use the fixed-`w`, `N -> infinity`,
  then `w -> infinity` order;
- the selector class is fixed before comparing local models.

## 8. Proof / reduction

For a subset `S`, the local factor depends only on the number of distinct
forbidden residue classes:

```text
r_p(S;d,h,k;t).
```

For a pair face `S_sigma`, translating by `A_sigma` leaves the two offsets:

```text
0,d.
```

Thus `r_p(S_sigma)=#{0,-d mod p}` and the factor is `kappa_w(d)`.

For a rectangle face `S_{sigma,tau}`, translating by `A_sigma` leaves:

```text
0,d,H_{sigma,tau},H_{sigma,tau}+d.
```

After sign reversal this is the defining set for `Sigma_w(d,H_{sigma,tau})`.

For the full face `S=V`, the definition is exactly the full projected
eight-form factor. If all `t_i=0`, the projected offsets reduce to the
unprojected two-rectangle offsets, giving `Theta_w(d,h,k)`.

Finally, expanding:

```text
f=nu-1
```

over the eight projected vertices gives the signed sum defining
`Omega_w^proj`. This proves the exact compatibility identities and also shows
why the forbidden replacements are additional analytic assumptions rather
than algebraic consequences.

## 9. Edge cases

- If `H_{sigma,tau}=0`, a rectangle face collapses structurally and must use
  the exact `Sigma_w(d,0)` factor, not a generic four-class factor.
- If `H_{sigma,tau}=d` or `H_{sigma,tau}=-d`, two rectangle vertices collide;
  this belongs to the collision stratification of Module 208.
- If `d=0`, the pair face collapses, but the dyadic range `D<|d|<=2D` removes
  this stratum from the main endpoint average.
- If `t` has long tails, projected and unprojected local models can differ on
  sets that are also boundary errors.
- If the kernel has signs or complex phases, absolute compatibility estimates
  may be much stronger than the signed estimate actually needed.
- If a proof route changes the selector class, local-factor compatibility does
  not supply selector transfer.
- If primes `p<=w` are accidentally inserted into both the W-trick and the
  Euler product, the small-prime contribution is double counted.
- If prime powers remain in `nu`, the local prime-only factors do not describe
  the actual weight without Module 211's transfer package.
- If a lower-dimensional subset is omitted from `Omega_w^proj`, the residual
  inclusion-exclusion no longer matches `f=nu-1`.

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
  -> local-model compatibility ledger.
```

This module is a guardrail before Module 213's selector-class transfer line.
It clarifies which model substitutions are exact and which require new
averaged estimates.

## 11. What remains open

This module does not prove:

- `RectPairCompat_major=o_W(1)`;
- `RectPairCompat_major^abs=o_W(1)`;
- `CubeRectCompat_major=o_W(1)`;
- `ResidualFullCompat_major=o_W(1)`;
- `ProjUnprojCompat_major=o_W(1)`;
- `MargAbsorb_major=o_W(1)`;
- `WProjectedLocalMatch_3^major`;
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

- Do not replace `Sigma_w(d,H)` pointwise by `kappa_w(d)^2`.
- Do not replace `Theta_w^proj` by a product of rectangle factors without
  `CubeRectCompat_major`.
- Do not replace `Omega_w^proj` by `Theta_w^proj` without
  `ResidualFullCompat_major`.
- Do not remove projection shifts from the model without
  `ProjUnprojCompat_major`.
- Do not use pair-BDH, first-moment Hardy-Littlewood, or rectangle first
  moments as substitutes for the averaged compatibility lemmas above.
- Do not treat exact face identities as endpoint cancellation.
- Do not hide collision, boundary, W-residue, prime-power, projection, or
  selector errors inside local-model notation.
- Do not claim projected local-model matching, projected major-arc
  cancellation, the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
