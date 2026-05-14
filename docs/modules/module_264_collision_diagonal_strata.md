# Module 264: Collision and diagonal strata for `CollSigned_263`

## 1. Precise theorem / claim being advanced

This module performs the second proof-or-blocked test required by
`PlanChallenge_5_262`: audit the collision and diagonal strata inside the
signed collision remainder from Module 263.

Define:

```text
CollStrataAudit_264(P_adm).
```

The audit separates three different objects that must not be merged:

```text
exact local-model collisions inside Theta_{w,S}^proj,
absolute collision-defect control for CollNeutral_260,
signed full-cover collision cancellation for CollSigned_263.
```

The conditional conclusions are:

```text
AbsCollStrataGate_264(P_adm)
  => CollNeutral_260(P_adm),

SignedCoverGate_264(P_adm)
  => CollSigned_263(N,w;rho)=o_W(1) over P_adm.
```

The second implication is not the same as `CollNeutral_260`: it controls the
signed collision term in the model-neutrality average, but it does not imply
the absolute defect average required by Module 260.

This module does not prove either gate. It records exactly what their
collision strata would have to control.

## 2. Status label

`CONDITIONAL`

The implications above are conditional decompositions. The structural
classification is deterministic, but the required weighted estimates remain
open.

## 3. Definitions and variables

Use the Phase H admissible family:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
D<|d|<=2D,
w fixed, N -> infinity, then w -> infinity.
```

Write:

```text
Sigma_square={00,10,01,11},
t_{00}=t0, t_{10}=t1, t_{01}=t2, t_{11}=t3.
```

For:

```text
sigma=(a,b) in Sigma_square,
e in {0,1},
```

define:

```text
A_sigma(h,k;t)=a h + b k - t_sigma,
v_{sigma,e}=n + A_sigma(h,k;t) + e d.
```

Thus:

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
Lambda_8=Sigma_square x {0,1}.
```

For two distinct labels:

```text
lambda=(sigma,e),
mu=(sigma',e'),
```

set:

```text
L_{lambda,mu}(d,h,k;t)
  = v_lambda-v_mu
  = A_sigma-A_sigma' + (e-e')d.
```

A collision modulo a prime `p` occurs when:

```text
p | L_{lambda,mu}.
```

The structural zero stratum is:

```text
Z_{lambda,mu}
  = { (d,h,k,t): L_{lambda,mu}(d,h,k;t)=0 }.
```

For `L != 0`, define:

```text
beta_w(L)=sum_{p>w, p|L} 1/p.
```

The reduced projected difference family from Module 208 is:

```text
BaseProj={H_0,K_0,S_0,R_0,K_1,H_1},
```

where:

```text
H_0 = h + t0 - t1,
K_0 = k + t0 - t2,
S_0 = h+k + t0 - t3,
R_0 = h-k + t2 - t1,
K_1 = k + t1 - t3,
H_1 = h + t2 - t3.
```

Every labeled pair difference is, up to sign and multiplicity:

```text
d,
A,
A+d,
A-d
```

with `A in BaseProj`. Hence the reduced nonzero collision load is:

```text
B_w^red(d,h,k;t)
  = beta_w(d)
    + sum_{A in BaseProj}
        ( beta_w(A)+beta_w(A+d)+beta_w(A-d) ),
```

formed only away from the structural zero set.

## 4. The signed collision object

From Module 263:

```text
CollSigned_263
  = sum_{S subset Lambda_8} (-1)^(8-|S|) C_S^P,
```

where:

```text
C_S^P
  = (1/D) sum_{D<|d|<=2D} E_{h,k,t} W_M(t)
      (Theta_{w,S}^proj(d,h,k;t)-Theta_{w,|S|}^gen).
```

Equivalently:

```text
CollSigned_263
  = (1/D) sum_d E_{h,k,t} W_M(t)
      Delta_w^coll(d,h,k;t),
```

where:

```text
Delta_w^coll
  = Omega_w^proj-Omega_w^gen.
```

The absolute collision row from Module 260 is:

```text
CollNeutral_260(P_adm):
  (1/D) sum_d E_{h,k,t} |W_M(t)| |Delta_w^coll(d,h,k;t)|
  = o_W(1).
```

This row implies:

```text
CollSigned_263=o_W(1),
```

but the converse is false in general.

## 5. Exact local-model collisions versus removable defects

For:

```text
S subset Lambda_8,
s=|S|,
```

the exact local factor is:

```text
Theta_{w,S}^proj(d,h,k;t)
  = prod_{p>w}
      (1-1/p)^(-s)
      (1-r_p(S;d,h,k;t)/p).
```

All large-prime congruence collisions are already encoded in the residue count
`r_p(S;d,h,k;t)`. They become defects only after comparison with:

```text
Theta_{w,s}^gen
  = prod_{p>w} (1-1/p)^(-s)(1-s/p).
```

Therefore:

```text
exact model route:
  keep Theta_{w,S}^proj and do not remove collision strata;

generic-defect route:
  compare Theta_{w,S}^proj with Theta_{w,s}^gen,
  then prove the structural and congruence defect averages are small.
```

The project is currently testing the second route. It is not allowed to drop a
stratum from `Theta_{w,S}^proj` and still claim to be averaging the exact
model.

## 6. Structural zero and diagonal strata

The structural zero set is:

```text
Z_struct
  = union_{lambda<mu} Z_{lambda,mu}.
```

Using the reduced forms, this is the union of:

```text
A=0,
A+d=0,
A-d=0
```

for:

```text
A in {H_0,K_0,S_0,R_0,K_1,H_1}.
```

The pure same-slot form:

```text
d=0
```

does not occur because the active dyadic shell has `D<|d|<=2D`.

The edge strata are:

```text
H_0=0, H_0+d=0, H_0-d=0,
H_1=0, H_1+d=0, H_1-d=0,
K_0=0, K_0+d=0, K_0-d=0,
K_1=0, K_1+d=0, K_1-d=0.
```

The diagonal strata are:

```text
S_0=0, S_0+d=0, S_0-d=0,
R_0=0, R_0+d=0, R_0-d=0.
```

The diagonal families are not optional. They are the projected versions of
the `h+k` and `h-k` square diagonals after kernel shifts. Any route that
counts only `h=0`, `k=0`, or `h=k` has lost projected collisions.

Define the structural signed contribution:

```text
StructSigned_264
  = (1/D) sum_d E_{h,k,t} W_M(t)
      Delta_w^coll(d,h,k;t) 1_{Z_struct}.
```

Define the structural absolute contribution:

```text
StructAbs_264
  = (1/D) sum_d E_{h,k,t} |W_M(t)|
      |Delta_w^coll(d,h,k;t)| 1_{Z_struct}.
```

The absolute route requires:

```text
StructAbs_264=o_W(1).
```

A codimension-one count such as Module 185 is not enough by itself unless the
local factor is also bounded or replaced by a synchronized lower-dimensional
model on the stratum.

## 7. Nonstructural congruence strata

On:

```text
G = complement of Z_struct,
```

all active pair differences are nonzero and `beta_w(L)` is defined. For a
prime `p>w`, let `G_p(d,h,k;t)` be the collision graph on `Lambda_8` whose
edges are:

```text
lambda--mu if p | L_{lambda,mu}(d,h,k;t).
```

For `S subset Lambda_8`, let:

```text
delta_p(S;d,h,k;t)=|S|-r_p(S;d,h,k;t).
```

Equivalently, `delta_p(S)` is the loss in the number of occupied residue
classes caused by the graph `G_p` restricted to `S`.

The local Euler-factor comparison gives, for `p>w` large enough:

```text
theta_{p,S}^proj
  = theta_{p,s}^gen (1 + delta_p(S)/(p-s)).
```

Thus every nonstructural collision defect is built out of the functions:

```text
delta_p(S),
p | L_{lambda,mu},
```

plus products of such factors over several primes.

The absolute route controls these by the local-factor envelope:

```text
|Delta_w^coll|
  <= C exp(C B_w^red) B_w^red + tau_w
```

on `G`, with `tau_w` a genuine generic W-tail. This requires the same
small-load and overflow qualifications as Modules 187, 188, and 192.

## 8. Absolute collision-strata gate

Define:

```text
AbsCollStrataGate_264(P_adm)
```

as the conjunction of:

```text
1. ModelConv_260 and AvgFaceCompat_263 in the same P_adm family.

2. Structural/boundary contribution:
   StructAbs_264=o_W(1).

3. Qualified local envelope on G:
   |Delta_w^coll| <= C exp(C B_w^red) B_w^red + tau_w,
   with E_abs tau_w=o_W(1).

4. First nonstructural collision-load moment:
   E_abs B_w^red 1_G=o_W(1).

5. Overflow control:
   E_abs exp(C B_w^red) B_w^red
     1_{B_w^red>1} 1_G=o_W(1).

6. Denominator, W-limit, projection, cutoff, and dyadic uniformity as in
   DenWProjNeutral_260 and ModelCutNeutral_260.
```

Here:

```text
E_abs F
  = (1/D) sum_{D<|d|<=2D} E_{h,k,t} |W_M(t)| F(d,h,k;t).
```

### Conditional implication

Assuming `AbsCollStrataGate_264(P_adm)`, split:

```text
(1/D) sum_d E_{h,k,t} |W_M| |Delta_w^coll|
  <= StructAbs_264
     + E_abs |Delta_w^coll| 1_G.
```

On `G`, use the qualified local envelope:

```text
E_abs |Delta_w^coll| 1_G
  <= C E_abs exp(C B_w^red) B_w^red 1_G
     + E_abs tau_w 1_G.
```

Split the exponential term at `B_w^red<=1` and `B_w^red>1`. The small-load
part is bounded by:

```text
C e^C E_abs B_w^red 1_G=o_W(1),
```

and the large-load part is exactly the overflow row. Therefore:

```text
CollNeutral_260(P_adm)
```

holds. This proves only the conditional implication:

```text
AbsCollStrataGate_264(P_adm)
  => CollNeutral_260(P_adm).
```

The gate itself remains open.

## 9. Signed full-cover filter

The signed route asks whether some collision terms cancel before absolute
values are taken.

For a finite collection `E` of collision events, let:

```text
supp(E) subset Lambda_8
```

be the set of labels touched by the pair differences appearing in `E`.

The basic signed Boolean identity is:

```text
sum_{S subset Lambda_8} (-1)^(8-|S|) F(S cap U)=0
```

whenever:

```text
U != Lambda_8.
```

Indeed, the variables outside `U` contribute:

```text
sum_{T subset Lambda_8\U} (-1)^(|Lambda_8\U|-|T|)=0.
```

Therefore, in the idealized constant-generic background, a collision monomial
whose label support does not cover all eight vertices is killed by the signed
residual sum.

This is a real structural filter, but it is not yet an estimate for
`CollSigned_263`, because the exact factors also contain:

```text
Theta_{w,s}^gen,
generic Euler tails depending on s,
kernel and cutoff asymmetries,
structural zero strata,
products of collision factors at several primes.
```

The filter says:

```text
proper-support collision monomials cancel only after their size-only and
domain-dependent remainders are controlled.
```

It does not say that all pair, rectangle, or low-dimensional collision
effects vanish in the actual projected average.

## 10. Signed cover gate

Define:

```text
SignedCoverGate_264(P_adm)
```

as the conjunction of:

```text
1. Exact signed averaging:
   no absolute values before the subset sum and the same W_M as in
   CollSigned_263.

2. Structural signed contribution:
   StructSigned_264=o_W(1), or a synchronized exact lower-dimensional model
   for every structural zero stratum.

3. Proper-support cancellation compatibility:
   every collision expansion term with support U != Lambda_8 is either
   exactly canceled by the signed Boolean identity or bounded by an explicit
   generic-tail/domain-error row.

4. Full-cover collision estimate:
   the remaining collision clusters whose supports cover all eight labels
   have signed weighted average o_W(1).

5. Multi-prime overflow compatibility:
   products of collision factors over several primes satisfy the same
   fixed-w, N -> infinity, w -> infinity order.

6. No replacement of Omega_w^proj by a pair face, rectangle face, full
   eight-form layer, or unprojected model.
```

### Conditional implication

Expand the Euler-product comparison on `G` into collision monomials plus a
generic tail. Group each monomial by its touched label support `U`.

The terms with:

```text
U != Lambda_8
```

are canceled or paid for by row 3. The terms with:

```text
U = Lambda_8
```

are paid for by row 4. Structural terms are paid for by row 2, and overflow
and limit-order defects by row 5. Therefore:

```text
CollSigned_263=o_W(1)
```

over `P_adm`.

This is a conditional signed route only. It does not imply the absolute
defect row `CollNeutral_260`.

## 11. Verdict for the Phase H collision row

The collision row has two live but unproved routes:

```text
Absolute route:
  AbsCollStrataGate_264(P_adm)
    => CollNeutral_260(P_adm).

Signed route:
  SignedCoverGate_264(P_adm)
    => CollSigned_263=o_W(1).
```

The absolute route is compatible with Module 260, but it may be too expensive
because it pays `|W_M|`, structural singular factors, first moments, and
overflow.

The signed route is potentially smaller because proper-support collision
terms are formally filtered by inclusion-exclusion. It is also riskier: the
surviving full-cover clusters may be close to the original endpoint, and any
proof that assumes projected major cancellation is circular.

The next module should therefore test the kernel route with this split in
mind:

```text
Module 265:
  decide whether the absolute kernel budget can support the generic and
  collision gates, or whether signed kernel cancellation is being smuggled in.
```

## 12. Edge cases

- If `beta_w(L)` is formed on a structural zero stratum, the argument is
  invalid.
- If diagonal forms `S_0`, `R_0`, or their `+d` and `-d` shifts are omitted,
  the collision geometry is incomplete.
- If a codimension-one count is used without bounding the local factor on the
  stratum, `StructAbs_264=o_W(1)` has not been proved.
- If the signed full-cover filter is applied after taking absolute values,
  the cancellation is gone.
- If `Theta_{w,s}^gen` is replaced by `1` without paying the generic W-tail,
  the signed filter has been overstated.
- If a proper-support collision is called canceled while the cutoff or
  denominator domain depends on labels outside its support, the domain-error
  row is missing.
- If the signed route controls `CollSigned_263`, it still does not prove
  `CollNeutral_260`.
- If a signed collision proof assumes `ProjectedMajorTarget_3^B`,
  `WProjectedLocalMatch_3^major`, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3`, Phase H has become circular.

## 13. Where it fits in the project map

The Phase H chain is now:

```text
Module 260:
  ProjectedModelNeutralityGate_260(P_adm) names CollNeutral_260.

Module 263:
  SignedSubsetExpansion_263(P_adm) isolates CollSigned_263.

Module 264:
  CollStrataAudit_264(P_adm) splits collision control into absolute
  collision-strata and signed full-cover routes.
```

The next module should be:

```text
Module 265:
  kernel absolute budget versus signed kernel cancellation.
```

## 14. What remains open

This module does not prove:

- `AbsCollStrataGate_264(P_adm)`;
- `SignedCoverGate_264(P_adm)`;
- `StructAbs_264=o_W(1)`;
- `StructSigned_264=o_W(1)`;
- the first collision-load moment for `B_w^red`;
- the overflow estimate for `B_w^red`;
- the full-cover signed collision estimate;
- `CollNeutral_260`;
- `CollSigned_263=o_W(1)`;
- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
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

- Do not identify signed collision cancellation with the absolute row
  `CollNeutral_260`.
- Do not apply divisor loads before removing or separately modeling
  structural zero strata.
- Do not omit projected diagonal forms or kernel-shifted forms.
- Do not use ordinary pair-BDH, rectangle-BDH, first-moment HL, generic HL, or
  finite-complexity HL as a substitute for the collision gates.
- Do not replace `Omega_w^proj` by the full eight-form model, a pair face, a
  rectangle face, or an unprojected model.
- Do not replace rectangle local factors by products or squares of pair
  factors.
- Do not move between selectors, projections, denominator ranges, cutoff
  conventions, W-residue conventions, or W-limit orders without named transfer
  rows.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3` is proved.
