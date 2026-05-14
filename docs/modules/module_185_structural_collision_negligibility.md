# Module 185: Kernel and range hypotheses for structural collision negligibility

## 1. Precise theorem / claim being advanced

This module gives a conditional counting lemma for the structural collision
strata classified in Module 184. It states explicit hypotheses under which the
kernel-weighted structural collision average:

```text
StructColl(D)
  = (1/D) sum_{D<|d|<=2D} E_{h,k,t} |W_M(t)|
      sum_active 1_{L_{\sigma,e;\sigma',e'}(d,h,k;t)=0}
```

is small.

The claim is conditional: if the `h,k` averaging windows have lengths tending
to infinity and the projection kernel has bounded absolute mass, then the
codimension-one structural strata from Module 184 contribute at most:

```text
O(A_M (1/H + 1/K + 1/min(H,K))) + boundary_error,
```

where:

```text
A_M = E_t |W_M(t)|.
```

Thus `StructColl(D)=o(1)` follows under the stated range and kernel
hypotheses.

## 2. Status label

`CONDITIONAL`

This is a conditional counting lemma. It does not prove the projected
collision-defect estimate, the major-arc model-matching theorem, or the
endpoint.

## 3. Definitions and variables

Let the `h` and `k` averages be over finite windows:

```text
h in I_H,  |I_H| = H
k in I_K,  |I_K| = K.
```

Let:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0) conj(K_M(t1)) conj(K_M(t2)) K_M(t3)
```

and:

```text
A_M = E_t |W_M(t)|.
```

The active structural forms from Module 184 are, up to sign:

```text
h + Delta e d - (t_{10}-t_{00})
h + Delta e d - (t_{11}-t_{01})

k + Delta e d - (t_{01}-t_{00})
k + Delta e d - (t_{11}-t_{10})

h+k + Delta e d - (t_{11}-t_{00})
h-k + Delta e d - (t_{10}-t_{01})
```

with:

```text
Delta e in {-1,0,1}.
```

Pure same-slot forms `+/- d` are absent from the zero-stratum sum because
`D < |d| <= 2D`.

## 4. Assumptions

Assume:

- `D < |d| <= 2D`;
- `H -> infinity` and `K -> infinity` in the relevant limit regime;
- the kernel absolute mass is bounded:

```text
A_M <= C_M
```

uniformly in the required dyadic ranges, or at least:

```text
A_M (1/H + 1/K + 1/min(H,K)) = o(1);
```

- boundary loss from interval endpoints is controlled by a term
  `boundary_error(N,D,H,K,M)`;
- structural strata are counted with the same absolute kernel weight
  `|W_M(t)|` used in Module 183.

## 5. Proof / disproof / reduction

For fixed `d` and `t`, a horizontal stratum has the form:

```text
h = constant(d,t).
```

Therefore:

```text
E_{h in I_H} 1_{h=constant} <= 1/H
```

up to boundary conventions.

Similarly, a vertical stratum gives:

```text
E_{k in I_K} 1_{k=constant} <= 1/K.
```

A diagonal stratum has the form:

```text
h+k = constant(d,t)
```

or:

```text
h-k = constant(d,t).
```

For each fixed `h`, there is at most one `k` solving either equation, and for
each fixed `k`, there is at most one `h`. Hence:

```text
E_{h,k} 1_{h+k=constant} <= 1/min(H,K),
E_{h,k} 1_{h-k=constant} <= 1/min(H,K),
```

again up to boundary conventions.

There are only finitely many active forms: two horizontal square edges, two
vertical square edges, and two diagonals, each with three possible values of
`Delta e`. Therefore:

```text
sum_active E_{h,k} 1_{L=0}
  <= C (1/H + 1/K + 1/min(H,K)) + boundary_error.
```

Multiplying by `|W_M(t)|`, averaging in `t`, and averaging in `d` gives:

```text
StructColl(D)
  <= C A_M (1/H + 1/K + 1/min(H,K))
     + boundary_error(N,D,H,K,M).
```

Thus `StructColl(D)=o(1)` under the assumptions in Section 4.

## 6. Edge cases

- If either `H` or `K` is bounded, diagonal and edge strata may survive.
- If the projection kernel has growing absolute mass, the factor `A_M` can
  erase the codimension-one saving.
- If `h,k` are not averaged over intervals or comparable finite sets, the
  counting bound must be replaced by the correct combinatorial estimate.
- If interval endpoints are sharp, boundary terms must be included explicitly.
- If a later transfer changes the `h,k` windows, this lemma must be rerun in
  the transferred geometry.
- This lemma handles structural zero strata only. Congruence collisions
  modulo primes `p>w` still require the divisor-average estimates from
  Module 183.

## 7. Where it fits in the project map

Module 184 classified the structural collision strata. Module 185 gives a
conditional negligibility criterion:

```text
structural strata
  -> horizontal, vertical, diagonal counting
  -> kernel absolute mass factor
  -> negligible if H,K and A_M are in the right range.
```

After this step, the remaining projected model-neutrality burden is the
nonstructural divisor-average collision defect from Module 183.

## 8. What remains open

This module does not prove:

- the kernel absolute-mass bound for the actual major-arc projection;
- the boundary transfer needed for the sharp interval model;
- the nonstructural divisor-average estimate;
- projected local-model matching;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- any actual sharp moving-selector theorem.

## Red flags / forbidden upgrades

- Do not use this lemma when `H` or `K` is too short.
- Do not drop the projection-kernel absolute mass factor `A_M`.
- Do not treat structural collision negligibility as full collision-defect
  control.
- Do not use this conditional counting lemma as an endpoint proof.
- Do not transfer it to actual sharp moving selectors without all transfer
  packages.
