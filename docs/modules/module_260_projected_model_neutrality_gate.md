# Module 260: Projected model-neutrality feasibility gate

## 1. Precise theorem / claim being advanced

This module begins Phase H by formulating the model-side gate for the
projected major-arc branch.

Define:

```text
ProjectedModelNeutralityGate_260(P_adm).
```

The conditional claim is:

```text
ProjectedModelNeutralityGate_260(P_adm)
  => ProjectedModelNeutrality_3^major(P_adm).
```

Here:

```text
ProjectedModelNeutrality_3^major(P_adm):
  NeutralErr_major^P(N,w;rho)=o_W(1)
```

uniformly over:

```text
rho in P_adm(N,w).
```

The model-neutrality error is:

```text
NeutralErr_major^P(N,w;rho)
  = |(1/D) sum_{D<|d|<=2D} ModelProjCube_d^P|,
```

where:

```text
ModelProjCube_d^P
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

The gate isolates exactly what is needed to make this model-side row smaller
than the projected major endpoint:

```text
exact residual model discipline,
generic W-tail cancellation,
kernel signed or absolute budget,
collision-defect control,
denominator and W-limit uniformity,
projection and cutoff convention stability.
```

This module does not prove any of those inputs. It is a conditional gate and
does not prove `WProjectedLocalMatch_3^major`, `ProjectedMajorTarget_3^B`, or
the residual cube endpoint.

## 2. Status label

`CONDITIONAL`

The implication from the named gate to projected model neutrality follows by
decomposing the exact model into a generic collision-free residual model plus
a collision defect. The required uniform estimates remain open.

## 3. Definitions and variables

Use:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
D<|d|<=2D,
w fixed, N -> infinity, then w -> infinity.
```

The projected major-arc operator is:

```text
widehat{P_M F}(xi)=m_M(xi)widehat{F}(xi),
m_M(0)=0.
```

Let:

```text
K_M(t)=sum_xi m_M(xi)e(xi t),
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
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

Let:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

For a labeled subset:

```text
S subset Lambda_8,
s=|S|,
```

let:

```text
r_p(S;d,h,k;t)
```

be the number of distinct residue classes mod `p` occupied by the offsets in
`S`. The exact projected local factor is:

```text
Theta_{w,S}^proj(d,h,k;t)
  = prod_{p>w}
      (1-1/p)^(-s)
      (1-r_p(S;d,h,k;t)/p).
```

The exact projected residual local model is:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset Lambda_8}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The generic collision-free factors are:

```text
Theta_{w,s}^gen
  = prod_{p>w} (1-1/p)^(-s)(1-s/p),

Omega_w^gen
  = sum_{s=0}^8 binom(8,s)(-1)^(8-s) Theta_{w,s}^gen.
```

The collision defect is:

```text
Delta_w^coll(d,h,k;t)
  = Omega_w^proj(d,h,k;t)-Omega_w^gen.
```

The model cube and model-neutrality error are:

```text
ModelProjCube_d^P
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t),

NeutralErr_major^P(N,w;rho)
  = |(1/D) sum_{D<|d|<=2D} ModelProjCube_d^P|.
```

For any error `Err(N,w;rho)`, write:

```text
Err=o_W(1) over P_adm
```

to mean:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P_adm(N,w)} |Err(N,w;rho)|=0.
```

## 4. Assumptions

`ProjectedModelNeutralityGate_260(P_adm)` consists of the following
W-admissible rows.

### A. Exact model convention

The model being averaged is exactly:

```text
Omega_w^proj(d,h,k;t),
```

with the same projected vertices, kernel shifts, W-residue convention,
projection, dyadic range, and cutoff convention as the major-arc branch.

Define:

```text
ModelConv_260(P_adm)
```

as this convention row. It is zero by definition only when no replacement of
the model, projection, denominator range, or cutoff is made.

### B. Generic W-tail row

There is a function:

```text
eps_gen(w) -> 0
```

such that:

```text
|Omega_w^gen| <= eps_gen(w)
```

uniformly in the permitted W-tail model.

A standard sufficient route is:

```text
Theta_{w,s}^gen=1+O_s(G_2(w)),
G_2(w)=sum_{p>w} 1/p^2,
```

which gives:

```text
|Omega_w^gen| <= C_gen G_2(w)
```

after the binomial cancellation:

```text
sum_{s=0}^8 binom(8,s)(-1)^(8-s)=0.
```

This row is:

```text
GenericTail_260(w): eps_gen(w)=o(1).
```

### C. Kernel budget row

Either an absolute route or a signed route must be declared.

The absolute route is:

```text
KernelAbsNeutral_260(P_adm):
  A_W(M) eps_gen(w)=o_W(1),
```

where:

```text
A_W(M)=E_t |W_M(t)|.
```

The signed route is:

```text
KernelSignedNeutral_260(P_adm):
  sup_{rho in P_adm}
  |(1/D) sum_{D<|d|<=2D} E_{h,k,t} W_M(t) Omega_w^gen|
  = o_W(1).
```

If the signed route is used, it must be proved for the exact multiplier,
normalization, truncation, and denominator family. It cannot be inferred from
the absolute boundary rows of Phase G.

### D. Collision-defect row

The exact model may differ from the generic model on congruence and structural
collision strata. The required row is:

```text
CollNeutral_260(P_adm):
  (1/D) sum_{D<|d|<=2D}
    E_{h,k,t} |W_M(t)|
      |Delta_w^coll(d,h,k;t)|
  = o_W(1)
```

uniformly over `rho in P_adm(N,w)`.

If a proof keeps all exact collisions inside `Omega_w^proj` and never passes
through `Omega_w^gen`, it may replace this row by a direct exact-model
neutrality estimate:

```text
ExactModelNeutral_260(P_adm):
  NeutralErr_major^P=o_W(1).
```

That direct route is merely a restatement unless it supplies a smaller
structural or analytic estimate.

### E. Denominator, W-limit, and projection uniformity

The generic-tail constants, collision estimates, and kernel budget must be
uniform over the admissible family. Define:

```text
DenWProjNeutral_260(P_adm)
```

to include:

```text
fixed-w then N -> infinity then w -> infinity limit order,
uniformity over D, R, eta, P_M, H, K, T,
denominator and CRT admissibility,
buffered projection or sharp projection convention,
kernel truncation convention,
W-residue convention,
prime-power convention for the model side.
```

This row is not automatic from the algebra of `Omega_w^proj`.

### F. Boundary and cutoff convention row

Model neutrality is a model-side average. If it is stated in a cyclic model
but later used in an interval target, the boundary and cutoff conventions must
be synchronized with `CycIntTransfer_3^major`. For Module 260 define:

```text
ModelCutNeutral_260(P_adm)
```

as the row asserting that the model average uses the same domain, cutoff,
truncation, and normalization as the intended `NeutralErr_major^P`.

This does not prove the actual cyclic-to-interval transfer for prime weights.
It only prevents the model-neutrality row from silently changing its own
model domain.

### G. The assembled gate

The gate is:

```text
ProjectedModelNeutralityGate_260(P_adm)
  =
  ModelConv_260
  + GenericTail_260
  + (KernelAbsNeutral_260 or KernelSignedNeutral_260)
  + CollNeutral_260
  + DenWProjNeutral_260
  + ModelCutNeutral_260.
```

All rows must hold in the same admissible family and limit order.

## 5. Proof / disproof / reduction

Start with:

```text
NeutralErr_major^P
  = |(1/D) sum_d E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t)|.
```

Use the exact decomposition:

```text
Omega_w^proj(d,h,k;t)
  = Omega_w^gen + Delta_w^coll(d,h,k;t).
```

Then:

```text
NeutralErr_major^P
  <= GenNeutral_260 + CollNeutralTerm_260,
```

where:

```text
GenNeutral_260
  =
  |(1/D) sum_d E_{h,k,t} W_M(t) Omega_w^gen|,

CollNeutralTerm_260
  =
  |(1/D) sum_d E_{h,k,t} W_M(t)
      Delta_w^coll(d,h,k;t)|.
```

For the generic term, either use the signed row directly:

```text
GenNeutral_260=o_W(1),
```

or use the absolute route:

```text
GenNeutral_260
  <= E_t |W_M(t)| |Omega_w^gen|
  <= A_W(M) eps_gen(w)
  = o_W(1).
```

For the collision term:

```text
CollNeutralTerm_260
  <= (1/D) sum_d E_{h,k,t} |W_M(t)|
       |Delta_w^coll(d,h,k;t)|
  = o_W(1)
```

by `CollNeutral_260`.

The convention and uniformity rows ensure that these estimates are for the
same `rho in P_adm(N,w)` and the same fixed-`w`, `N -> infinity`, then
`w -> infinity` order. Thus:

```text
NeutralErr_major^P=o_W(1)
```

uniformly over `P_adm`, which is:

```text
ProjectedModelNeutrality_3^major(P_adm).
```

This proves only the conditional implication from the gate.

## 6. Edge cases

- If the proof changes `P_M`, smoothing, denominator ranges, cutoff, or
  kernel truncation, it is mixed and needs transfer rows back to the original
  `P_adm` target.
- If `A_W(M)` grows faster than `eps_gen(w)` decays, the absolute route fails.
- If signed kernel cancellation is used, it belongs to
  `KernelSignedNeutral_260`, not to Phase G boundary rows.
- If collision strata are removed without `CollNeutral_260`, the proof has
  changed the exact model.
- If the model is replaced by the full eight-form factor, the residual
  binomial cancellation is not the same argument.
- If the projected model is replaced by the unprojected model, the kernel
  shifts `t0,t1,t2,t3` have been lost.
- Pair and rectangle face identities may be used only as exact face
  identities; using them as the full residual model is blocked.
- Treating the rectangle local factor as the pointwise square of the pair
  local factor remains forbidden.
- A model-neutrality statement in one selector or model class does not move to
  the actual sharp moving selector.
- This row does not supply residual subset-HL matching for actual prime
  weights.

## 7. Where it fits in the project map

Phase H starts here:

```text
Module 259:
  PlanUpdate_8_259 selects projected model-neutrality feasibility.

Module 260:
  ProjectedModelNeutralityGate_260(P_adm).
```

The projected major-arc branch remains:

```text
WProjectedLocalMatch_3^major(P_adm)
  + ProjectedModelNeutrality_3^major(P_adm)
    => ProjectedMajorTarget_3^B(P_adm).
```

Module 260 attacks only the second input:

```text
ProjectedModelNeutrality_3^major(P_adm).
```

It does not prove the matching input, the projected major target, or any
minor-arc statement.

The next scheduled module is:

```text
Module 261:
  Reflective_3.md, the required memory log after the post-Reflective_1 count
  reaches 80.
```

## 8. What remains open

This module does not prove:

- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
- `GenericTail_260`;
- `KernelAbsNeutral_260`;
- `KernelSignedNeutral_260`;
- `CollNeutral_260`;
- `DenWProjNeutral_260`;
- `ModelCutNeutral_260`;
- `WProjectedLocalMatch_3^major(P_adm)`;
- `ProjectedMajorTarget_3^B(P_adm)`;
- `CycIntTransfer_3^major(P_adm)`;
- `PPSPTransfer_3^major(P_adm)`;
- `MajorSelectorTransfer_3^P`;
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

- Do not treat model neutrality as projected local-model matching.
- Do not cite this module as a proof of `ProjectedModelNeutrality_3^major`;
  it only states a conditional gate.
- Do not prove the generic row by replacing `Omega_w^proj` with the full
  eight-form model.
- Do not discard collision strata without `CollNeutral_260`.
- Do not use signed kernel cancellation unless `KernelSignedNeutral_260` is
  explicitly proved in the same `P_adm` family.
- Do not use Phase G absolute boundary rows as signed model cancellation.
- Do not change projection, cutoff, denominator range, dyadic shell,
  W-residue convention, selector class, or limit order while calling the row
  local.
- Do not use ordinary pair-BDH, rectangle-BDH, first-moment HL, or generic HL
  as projected model neutrality.
- Do not close this gate by assuming `ProjectedMajorTarget_3^B`,
  `WProjectedLocalMatch_3^major`, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
