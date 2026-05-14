# Module 192: Averaged collision-defect bound under the qualified envelope

## 1. Precise theorem / claim being advanced

This module composes Modules 187-191 into a single conditional averaged
collision-defect statement.

Let:

```text
Delta_w^{coll}(d,h,k;t)
  = Omega_w^{proj}(d,h,k;t) - Omega_w^{gen}
```

be the projected collision defect from Module 182. Define:

```text
CollDef_w(D)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k} E_t |W_M(t)|
        |Delta_w^{coll}(d,h,k;t)|.
```

The conditional claim is:

if structural collision strata and boundary regions are negligible, the local
factor envelope from Module 187 holds on the remaining region, the first
collision-load moment is small, the overflow estimate from Module 188 holds,
and the kernel/range/W-limit hypotheses from Modules 189-191 are verified,
then:

```text
CollDef_w(D)=o_W(1).
```

Here `o_W(1)` means:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{allowed D,H,K,M,T} CollDef_w(D)=0.
```

This is a conditional collision-defect bound. It is not projected
local-model matching and it is not the residual cube endpoint.

## 2. Status label

`CONDITIONAL`

The proof is a composition of prior conditional packages. The conclusion is
usable only after every named hypothesis in Section 4 is supplied for the
actual major-arc projection and parameter ranges.

## 3. Definitions and variables

Use the projected vertices from Modules 181-184:

```text
v_{00,0}=n-t0,             v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,           v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,           v_{01,1}=n+k-t2+d,
v_{11,0}=n+h+k-t3,         v_{11,1}=n+h+k-t3+d.
```

Let the active nonstructural pair-difference forms be:

```text
L_1(d,h,k;t), ..., L_J(d,h,k;t),
J <= 28.
```

For `m != 0`, set:

```text
beta_w(m)=sum_{p>w, p|m} 1/p.
```

The total collision load is:

```text
B_w(d,h,k;t)=sum_{j=1}^J beta_w(L_j(d,h,k;t)).
```

The absolute weighted expectation is:

```text
E_abs F
  = (1/D) sum_{D<|d|<=2D} E_{h,k} E_t |W_M(t)| F(d,h,k;t).
```

Define:

```text
M_1(w)=E_abs B_w,
Ov_w(C)=E_abs exp(C B_w) B_w 1_{B_w>1}.
```

Let `Z_struct` be the union of structural collision strata and boundary
regions removed before applying `beta_w`. Define the structural contribution:

```text
StructDef_w(D)
  = E_abs |Delta_w^{coll}| 1_{Z_struct}.
```

Let `G` be the complement of `Z_struct`.

## 4. Assumptions

Assume the following.

Structural/boundary contribution:

```text
StructDef_w(D)=o_W(1).
```

This may follow from Modules 184-185 only if local factors are bounded enough
on the structural region, or if the region is removed with a matching error
term. Codimension counting alone is not automatically sufficient.

Qualified local-factor envelope:

on `G`,

```text
|Delta_w^{coll}|
  <= C exp(C B_w) B_w + tau_w,
```

where `C` is fixed independently of `N,D,H,K,M,T`, and:

```text
E_abs tau_w 1_G = o_W(1).
```

First collision-load moment:

```text
M_1(w;G)=E_abs B_w 1_G=o_W(1).
```

Overflow:

```text
Ov_w(C;G)=E_abs exp(C B_w) B_w 1_{B_w>1} 1_G=o_W(1).
```

The overflow hypothesis may be supplied by Module 188, for example through the
Module 189 joint-divisibility criterion, the Module 190 kernel/range package,
and the Module 191 W-limit contract.

Kernel/range/W-limit compatibility:

all error terms above are W-admissible in the sense of Module 191, with the
same selector, ranges, kernel, and projected local model.

## 5. Proof / disproof / reduction

Split:

```text
CollDef_w(D)
  <= StructDef_w(D)
     + E_abs |Delta_w^{coll}| 1_G.
```

On `G`, use the Module 187 envelope:

```text
E_abs |Delta_w^{coll}| 1_G
  <= C E_abs exp(C B_w) B_w 1_G
     + E_abs tau_w 1_G.
```

Split the exponential-load term into small and large load:

```text
E_abs exp(C B_w) B_w 1_G
  = E_abs exp(C B_w) B_w 1_{B_w<=1} 1_G
    + E_abs exp(C B_w) B_w 1_{B_w>1} 1_G.
```

On `B_w<=1`:

```text
exp(C B_w) B_w <= e^C B_w.
```

Therefore:

```text
E_abs exp(C B_w) B_w 1_{B_w<=1} 1_G
  <= e^C M_1(w;G)
  = o_W(1).
```

On `B_w>1`, the term is exactly the qualified overflow:

```text
E_abs exp(C B_w) B_w 1_{B_w>1} 1_G
  = Ov_w(C;G)
  = o_W(1).
```

The generic tail is W-admissible by assumption:

```text
E_abs tau_w 1_G=o_W(1).
```

Combining:

```text
CollDef_w(D)
  <= StructDef_w(D)
     + C e^C M_1(w;G)
     + C Ov_w(C;G)
     + E_abs tau_w 1_G
  = o_W(1).
```

This establishes the stated conditional averaged collision-defect bound.

## 6. Edge cases

- If structural strata are merely counted but the local singular factors are
  not bounded on them, `StructDef_w(D)=o_W(1)` has not been proved.
- If `B_w` is defined before removing zero pair-difference forms, `beta_w(0)`
  is invalid and the proof does not start.
- If the overflow estimate is replaced by the first moment `M_1(w)`, the proof
  fails on the rare large-load region.
- If the constant `C` in the local-factor envelope grows with kernel or range
  parameters, Module 191 does not make the generic tail harmless.
- If `E_abs tau_w` hides a first-order `sum 1/p` term, it is not a generic
  W-tail.
- If the kernel absolute mass grows, each `o_W(1)` input must be rechecked
  after multiplying by that growth.
- If the projected local model changes because the projection is smoothed,
  every object in this module must be updated to the smoothed model.

## 7. Where it fits in the project map

The collision branch now has a conditional chain:

```text
Module 182: collision defect identified
Module 187: exponential local-factor envelope
Module 188: overflow criterion
Module 189: exponential-moment / joint-divisibility criterion
Module 190: kernel absolute-mass and range audit
Module 191: W-limit tail uniformity
Module 192: averaged collision-defect composition.
```

Thus Module 192 organizes only the collision-defect subproblem under explicit
hypotheses. The next major-arc task is to combine this with generic projected
model neutrality while keeping the result separate from actual projected
local-model matching.

## 8. What remains open

This module does not prove:

- the structural/boundary contribution `StructDef_w(D)=o_W(1)` for the actual
  sharp interval model;
- the Module 190 kernel/range package for the chosen projection;
- the Module 189 joint-divisibility criterion in the true ranges;
- projected local-model matching;
- minor-arc large-spectrum decay;
- generic projected model neutrality as a final major-arc statement;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem or the all-alpha theorem.

## Red flags / forbidden upgrades

- Do not treat this conditional averaged defect bound as endpoint progress
  beyond its named hypotheses.
- Do not drop the structural contribution or replace it by informal
  codimension language.
- Do not replace the overflow estimate by first-moment divisor averages.
- Do not ignore W-limit quantifiers when summing generic tails.
- Do not treat collision-defect control as projected local-model matching.
- Do not transfer this model estimate to actual sharp moving selectors without
  the full transfer package.
