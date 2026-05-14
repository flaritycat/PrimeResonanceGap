# Module 193: Generic projected model neutrality after collision removal

## 1. Precise theorem / claim being advanced

This module combines the generic W-tail calculation from Module 182 with the
conditional averaged collision-defect bound from Module 192.

Let the projected residual model be:

```text
Omega_w^{proj}(d,h,k;t)
  = Omega_w^{gen} + Delta_w^{coll}(d,h,k;t).
```

Define the signed projected-model average:

```text
Model_w(D)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k} E_t W_M(t) Omega_w^{proj}(d,h,k;t).
```

The conditional claim is:

if the generic collision-free residual model satisfies:

```text
|Omega_w^{gen}| <= C_gen G_2(w),
G_2(w)=sum_{p>w}1/p^2,
```

the projection kernel has W-admissible absolute mass:

```text
A_W(M)=E_t |W_M(t)|,
A_W(M) G_2(w)=o_W(1),
```

and the Module 192 collision-defect bound holds:

```text
CollDef_w(D)=o_W(1),
```

then:

```text
Model_w(D)=o_W(1).
```

This is a projected model-neutrality statement conditional on the named
inputs. It is not projected local-model matching and it does not prove the
major-arc estimate for the actual prime weight.

## 2. Status label

`CONDITIONAL`

The conclusion follows from explicit hypotheses: generic W-tail uniformity,
kernel absolute-mass control, and the Module 192 collision-defect bound. The
actual verification of those hypotheses in the sharp interval model remains
open.

## 3. Definitions and variables

Use the projected vertices:

```text
v_{00,0}=n-t0,             v_{00,1}=n-t0+d,
v_{10,0}=n+h-t1,           v_{10,1}=n+h-t1+d,
v_{01,0}=n+k-t2,           v_{01,1}=n+k-t2+d,
v_{11,0}=n+h+k-t3,         v_{11,1}=n+h+k-t3+d.
```

For `S` a subset of these eight vertices, the projected local factor is:

```text
Theta_{w,S}^{proj}(d,h,k;t).
```

The projected residual model is:

```text
Omega_w^{proj}
  = sum_{S} (-1)^(8-|S|) Theta_{w,S}^{proj}.
```

The generic collision-free factors depend only on `s=|S|`:

```text
Theta_{w,s}^{gen}
  = prod_{p>w} (1-1/p)^(-s) (1-s/p).
```

Thus:

```text
Omega_w^{gen}
  = sum_{s=0}^8 binom(8,s) (-1)^(8-s) Theta_{w,s}^{gen}.
```

The collision defect is:

```text
Delta_w^{coll}
  = Omega_w^{proj} - Omega_w^{gen}.
```

The signed kernel is:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0) conj(K_M(t1)) conj(K_M(t2)) K_M(t3),
```

and the absolute kernel mass is:

```text
A_W(M)=E_t |W_M(t)|.
```

## 4. Assumptions

Assume:

- the projected local model from Module 181 is the model being averaged;
- the generic factors above are valid for all `0<=s<=8`;
- the generic W-tail constants are uniform in the sense of Module 191:

```text
|Theta_{w,s}^{gen}-1| <= C_s G_2(w)
```

with fixed `C_s`;

- the kernel absolute mass satisfies:

```text
A_W(M) G_2(w)=o_W(1);
```

- the averaged collision-defect estimate from Module 192 holds:

```text
CollDef_w(D)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k}E_t |W_M(t)| |Delta_w^{coll}(d,h,k;t)|
  = o_W(1);
```

- all boundary, structural, kernel-tail, and CRT range errors are included in
  the Module 192 hypotheses;
- the W-limit order is fixed `w`, then `N -> infinity`, then `w -> infinity`.

## 5. Proof / disproof / reduction

First estimate the generic model. Since:

```text
Theta_{w,s}^{gen}=1+O_s(G_2(w)),
```

we have:

```text
Omega_w^{gen}
  = sum_{s=0}^8 binom(8,s)(-1)^(8-s)
    (1+O_s(G_2(w))).
```

The constant part cancels:

```text
sum_{s=0}^8 binom(8,s)(-1)^(8-s) = (1-1)^8=0.
```

Therefore:

```text
|Omega_w^{gen}| <= C_gen G_2(w).
```

Now decompose the signed projected-model average:

```text
Model_w(D)
  = E_{d,h,k,t}^{signed}
      W_M(t) Omega_w^{gen}
    + E_{d,h,k,t}^{signed}
      W_M(t) Delta_w^{coll}(d,h,k;t).
```

The generic term is bounded without using cancellation:

```text
|E_t W_M(t) Omega_w^{gen}|
  <= A_W(M) |Omega_w^{gen}|
  <= C_gen A_W(M) G_2(w)
  = o_W(1).
```

The collision term is bounded by the absolute collision-defect average:

```text
|E_{d,h,k,t} W_M(t) Delta_w^{coll}|
  <= E_{d,h,k,t} |W_M(t)| |Delta_w^{coll}|
  = CollDef_w(D)
  = o_W(1).
```

Combining the two estimates gives:

```text
Model_w(D)=o_W(1).
```

This proves the stated conditional projected model-neutrality estimate.

## 6. Edge cases

- If `A_W(M)` grows too quickly, the generic W-tail `G_2(w)` may not survive
  the kernel average.
- Signed cancellation in `W_M` is not used; any argument that uses it must
  state a separate signed-kernel lemma.
- If the projected model changes because the projection is smoothed, the
  generic factors and the kernel mass must be rechecked for that model.
- If structural regions are removed on the collision-defect side but not on
  the projected model side, the decomposition is no longer synchronized.
- If `Omega_w^{gen}` is replaced by a full eight-form model instead of the
  residual inclusion-exclusion sum, the binomial cancellation is lost.
- If constants in `Theta_{w,s}^{gen}=1+O_s(G_2(w))` depend on `N` or kernel
  parameters, Module 191 does not apply.

## 7. Where it fits in the project map

The major-arc projected model branch now has:

```text
Module 181: correct projected residual model
Module 182: generic/collision decomposition
Module 192: conditional averaged collision-defect bound
Module 193: conditional projected model neutrality.
```

This organizes a conditional model-neutrality package for the projected local
model. It remains separate from:

```text
actual projected cube
  = projected local model + o(1),
```

which is the projected local-model matching theorem still to be specified.
Module 194 records it as `ProjectedLocalMatch_3^major` and lists its
dependencies.

## 8. What remains open

This module does not prove:

- the Module 192 hypotheses for the actual projected kernel;
- kernel absolute-mass control in the sharp major-arc projection;
- `ProjectedLocalMatch_3^major`;
- boundary transfer from cyclic/smoothed models to the sharp interval model;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem or the all-alpha theorem.

## Red flags / forbidden upgrades

- Do not treat projected model neutrality as projected local-model matching.
- Do not use signed kernel cancellation unless a signed-kernel theorem is
  stated and proved.
- Do not replace the residual inclusion-exclusion model by the full
  eight-form model.
- Do not ignore the factor `A_W(M)` in the generic W-tail term.
- Do not transfer this model estimate to actual sharp moving selectors without
  the full transfer package.
