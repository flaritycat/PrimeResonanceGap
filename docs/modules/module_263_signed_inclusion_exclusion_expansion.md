# Module 263: Signed inclusion-exclusion expansion of `NeutralErr_major^P`

## 1. Precise theorem / claim being advanced

This module performs the first proof-or-blocked test required by
`PlanChallenge_5_262`: expand the projected model-neutrality object into its
exact signed subset layers.

Define:

```text
SignedSubsetExpansion_263(P_adm).
```

The structural claim is the exact identity:

```text
NeutralSigned_major^P
  = sum_{S subset Lambda_8} (-1)^(8-|S|) A_S^P
  = sum_{s=0}^8 (-1)^(8-s) A_s^P
  = Kbar_P Omega_w^gen + CollSigned_263,
```

where:

```text
NeutralErr_major^P = |NeutralSigned_major^P|.
```

This module identifies which cancellations are purely formal, which lower-face
identities are exact, and which averaged compatibility rows would still be
needed before any cancellation can be used as an estimate.

It does not prove:

```text
NeutralErr_major^P=o_W(1),
ProjectedModelNeutrality_3^major(P_adm),
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
or the residual cube endpoint.
```

## 2. Status label

`STRUCTURAL / EXTRACTION`

The expansion is exact algebra inside the projected model. No new analytic
estimate is proved.

## 3. Definitions and variables

Use the Phase H admissible data:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
D<|d|<=2D,
w fixed, N -> infinity, then w -> infinity.
```

The eight projected vertices are:

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

Set:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

For:

```text
S subset Lambda_8,
s=|S|,
```

the exact projected local factor is:

```text
Theta_{w,S}^proj(d,h,k;t)
  = prod_{p>w}
      (1-1/p)^(-s)
      (1-r_p(S;d,h,k;t)/p),
```

where `r_p(S;d,h,k;t)` is the number of distinct residue classes mod `p`
occupied by the labeled offsets in `S`.

The residual projected local model is:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset Lambda_8}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The projected model cube is:

```text
ModelProjCube_d^P
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t),
```

and:

```text
NeutralErr_major^P(N,w;rho)
  = |(1/D) sum_{D<|d|<=2D} ModelProjCube_d^P|.
```

Define the pre-absolute signed average:

```text
NeutralSigned_major^P(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

For each labeled subset:

```text
A_S^P(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k,t} W_M(t) Theta_{w,S}^proj(d,h,k;t).
```

For each size layer:

```text
A_s^P(N,w;rho)
  = sum_{S subset Lambda_8, |S|=s} A_S^P(N,w;rho).
```

The generic size-only factors are:

```text
Theta_{w,s}^gen
  = prod_{p>w} (1-1/p)^(-s)(1-s/p),

Omega_w^gen
  = sum_{s=0}^8 binom(8,s)(-1)^(8-s) Theta_{w,s}^gen.
```

Finally define the kernel mean row:

```text
Kbar_P(N,w;rho)
  = (1/D) sum_{D<|d|<=2D} E_{h,k,t} W_M(t).
```

This is not automatically zero unless the exact cyclic independent kernel
convention is being used with no cutoff or domain defect.

## 4. Exact expansion

Substituting the residual local model gives:

```text
NeutralSigned_major^P
  = (1/D) sum_d E_{h,k,t} W_M(t)
      sum_{S subset Lambda_8} (-1)^(8-|S|)
        Theta_{w,S}^proj(d,h,k;t).
```

Because `Lambda_8` is finite, the subset sum can be interchanged with the
averages:

```text
NeutralSigned_major^P
  = sum_{S subset Lambda_8} (-1)^(8-|S|) A_S^P.
```

Grouping by subset size gives:

```text
NeutralSigned_major^P
  = sum_{s=0}^8 (-1)^(8-s) A_s^P.
```

Now write:

```text
A_S^P
  = Kbar_P Theta_{w,|S|}^gen + C_S^P,
```

where:

```text
C_S^P
  = (1/D) sum_d E_{h,k,t} W_M(t)
      (Theta_{w,S}^proj(d,h,k;t)-Theta_{w,|S|}^gen).
```

Then:

```text
sum_{S subset Lambda_8} (-1)^(8-|S|)
  Kbar_P Theta_{w,|S|}^gen
  = Kbar_P Omega_w^gen.
```

Define:

```text
CollSigned_263(N,w;rho)
  = sum_{S subset Lambda_8} (-1)^(8-|S|) C_S^P.
```

Therefore:

```text
NeutralSigned_major^P
  = Kbar_P Omega_w^gen + CollSigned_263.
```

This is the exact signed subset expansion needed before testing
`CollNeutral_260`.

## 5. Structural cancellations

### A. Generic binomial cancellation

For any common constant `C` independent of `S`:

```text
sum_{S subset Lambda_8} (-1)^(8-|S|) C
  = C(1-1)^8
  = 0.
```

Equivalently:

```text
sum_{s=0}^8 binom(8,s)(-1)^(8-s)=0.
```

More generally, the signed size-layer operator annihilates every polynomial
in `s` of degree `<8`:

```text
sum_{s=0}^8 binom(8,s)(-1)^(8-s) P(s)=0,
deg P < 8.
```

This is only formal unless the local factors have been put into a common
size-only expansion with uniform remainders. In the project ledger, the
usable generic row remains:

```text
|Omega_w^gen| <= eps_gen(w),
eps_gen(w)->0,
```

together with the relevant kernel budget from Module 260.

### B. Kernel zero-mode cancellation

If the active model is the exact cyclic model with independent `t0,t1,t2,t3`
averages and:

```text
m_M(0)=0,
```

then:

```text
E_t W_M(t)=0.
```

In that special convention:

```text
Kbar_P=0,
```

and every size-only generic term vanishes before estimating
`Omega_w^gen`.

This is not an automatic property of the sharp interval model. Boundary
cutoffs, restricted denominator ranges, W-residue restrictions, or non-cyclic
averages can turn this exact zero into a side row. Therefore Module 263 does
not use `Kbar_P=0` as a proof input.

### C. One-point exactness

For the empty subset:

```text
Theta_{w,emptyset}^proj=1.
```

For every singleton subset:

```text
Theta_{w,{lambda}}^proj=1.
```

These identities are exact local facts. They do not by themselves cancel the
empty and singleton layers, because their signed coefficients are:

```text
1 and -8.
```

They become part of the generic binomial cancellation only after the full
size-layer structure is kept.

### D. Pair-face identities

For a two-point subset:

```text
S={lambda,lambda'},
lambda != lambda',
```

let:

```text
L_{lambda,lambda'}(d,h,k;t)
  = v_lambda - v_lambda'.
```

Then:

```text
Theta_{w,S}^proj(d,h,k;t)
  = kappa_w(L_{lambda,lambda'}(d,h,k;t)).
```

In particular, for a same-slot derivative pair:

```text
S={(sigma,0),(sigma,1)},
```

the factor is:

```text
kappa_w(d).
```

For cross-slot pairs it is the same two-point factor evaluated at the relevant
projected displacement, such as:

```text
h+t0-t1,
k+t0-t2,
h+k+t0-t3,
```

and with possible `+d` or `-d` shifts depending on the endpoint labels.

These identities classify the `s=2` layer. They do not estimate the full
signed model-neutrality average, because the remaining `s=3,...,8` layers are
still present.

### E. Rectangle-face identities

For two cube slots `sigma` and `sigma'`, the four-vertex face:

```text
S={ (sigma,0),(sigma,1),(sigma',0),(sigma',1) }
```

has exact local factor:

```text
Theta_{w,S}^proj
  = Sigma_w(d,A_sigma-A_sigma'),
```

with the projected slot displacement:

```text
A_sigma-A_sigma'
  = a h + b k - t_sigma - (a' h + b' k - t_sigma').
```

This gives the six true two-slot rectangle faces inside the `s=4` layer.
Most four-subsets are not two-slot rectangles and remain general
`Theta_{w,S}^proj` factors.

The rectangle identity must not be replaced by:

```text
kappa_w(d)^2.
```

The rectangle local factor records all four residue classes jointly.

### F. Full eight-form layer

The `s=8` layer is:

```text
Theta_{w,Lambda_8}^proj(d,h,k;t).
```

It is the full projected eight-form local model. It is only one term in the
residual expansion. Replacing the signed residual model by this full layer
loses the `f=nu-1` subtraction.

## 6. Averaged compatibility still required

The local identities above become useful only after they are compatible with
the same signed average:

```text
(1/D) sum_{D<|d|<=2D} E_{h,k,t} W_M(t) (...).
```

Define:

```text
AvgFaceCompat_263(P_adm)
```

as the package requiring all of the following in the same admissible family:

```text
1. The exact same projection P_M, kernel W_M, dyadic shell, denominator range,
   W-residue convention, selector class, and cutoff convention.

2. Any symmetry used to group two subsets preserves the averaged domain, or
   its failure is paid by an explicit error row.

3. Pair and rectangle face identities are inserted before absolute values are
   taken.

4. Structural zero strata and large-prime congruence collision strata are
   carried along rather than removed from only one side.

5. Boundary, prime-power, and W-residue errors are not hidden inside
   Theta_{w,S}^proj or Omega_w^proj.

6. The fixed-w, then N -> infinity, then w -> infinity limit order is kept.
```

Without `AvgFaceCompat_263(P_adm)`, a pointwise face identity is only a local
factor dictionary. It is not a cancellation theorem for
`NeutralErr_major^P`.

## 7. Consequences for `CollNeutral_260`

Module 263 converts the collision row into the signed object:

```text
CollSigned_263
  = sum_{S subset Lambda_8} (-1)^(8-|S|)
      (1/D) sum_d E_{h,k,t} W_M(t)
        (Theta_{w,S}^proj-Theta_{w,|S|}^gen).
```

There are two honest routes:

```text
Absolute collision route:
  |CollSigned_263|
    <= sum_{S subset Lambda_8}
       (1/D) sum_d E_{h,k,t}
         |W_M(t)| |Theta_{w,S}^proj-Theta_{w,|S|}^gen|.

Signed collision route:
  exploit cancellation among the signed C_S^P terms in the exact same
  projected average.
```

The absolute route matches the spirit of `CollNeutral_260` but may be too
expensive. The signed route may be smaller, but it must be proved as a
model-side signed cancellation theorem. It cannot be imported from ordinary
pair estimates, rectangle estimates, first-moment HL, or a full eight-form
model estimate.

Module 264 should therefore test:

```text
Which structural or congruence collision strata survive in CollSigned_263?
Can any signed cancellation be proved without assuming the projected major
target or residual endpoint?
```

## 8. Edge cases

- If an absolute value is inserted before summing over `S`, the signed
  inclusion-exclusion structure has been discarded.
- If subsets are grouped only by size while collisions make
  `Theta_{w,S}^proj` depend on the actual labels, the grouping is invalid
  without a collision estimate.
- If the cyclic identity `E_t W_M=0` is used after interval cutoff or boundary
  truncation, a zero-mode side row is missing.
- If a pair face is used to represent the whole `s=2` layer, the cross-slot
  projected displacements and `+d` or `-d` shifted pairs may have been lost.
- If a rectangle face is replaced by the square of a pair factor, the local
  model is wrong.
- If the six true rectangle faces are treated as all of the `s=4` layer, the
  other four-subsets have disappeared.
- If structural collision strata are removed from `Theta_{w,S}^proj` but not
  from the generic comparison, `CollSigned_263` no longer matches the exact
  model-neutrality object.
- If face identities are transferred between selector classes, projections,
  denominator ranges, or W-limit orders without a transfer row, the result
  belongs to selector or projection transfer, not to Module 263.

## 9. Where it fits in the project map

The Phase H chain is now:

```text
Module 259:
  Phase H selected.

Module 260:
  ProjectedModelNeutralityGate_260(P_adm) named.

Module 262:
  PlanChallenge_5_262 narrows Phase H to proof-or-blocked subrow tests.

Module 263:
  SignedSubsetExpansion_263 expands NeutralErr_major^P into exact subset
  layers and isolates CollSigned_263.
```

The next module should be:

```text
Module 264:
  collision and diagonal strata for CollSigned_263 / CollNeutral_260.
```

## 10. What remains open

This module does not prove:

- `NeutralErr_major^P=o_W(1)`;
- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
- `AvgFaceCompat_263(P_adm)`;
- `CollSigned_263=o_W(1)`;
- `CollNeutral_260`;
- `KernelAbsNeutral_260`;
- `KernelSignedNeutral_260`;
- `DenWProjNeutral_260`;
- `ModelCutNeutral_260`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat `SignedSubsetExpansion_263` as model-neutrality decay.
- Do not replace `Omega_w^proj` by the full eight-form layer.
- Do not replace the signed subset sum by a pair face, rectangle face, or
  unprojected model.
- Do not replace the rectangle factor by a square of pair factors.
- Do not use ordinary pair-BDH, rectangle-BDH, first-moment HL, generic HL, or
  finite-complexity HL as a substitute for `CollSigned_263=o_W(1)`.
- Do not move between cyclic and interval averages by citing `Kbar_P=0`
  without a zero-mode transfer row.
- Do not hide W-residue, prime-power, cutoff, denominator, boundary, or
  selector errors inside `Theta_{w,S}^proj`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3` is proved.
