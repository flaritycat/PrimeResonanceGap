# Module 191: W-limit order and generic tail uniformity

## 1. Precise theorem / claim being advanced

This module fixes the limit-order contract needed by Modules 187-190. The
project uses:

```text
W = prod_{p<=w} p
```

and finite-local estimates must be proved with `w` fixed while `N -> infinity`,
then `w -> infinity`.

The claim advanced here is a conditional uniformity lemma:

if all constants in the generic Euler-product tails are independent of
`N,D,H,K,M,T` inside the permitted parameter family, then the tails of the
forms

```text
sum_{p>w} 1/p^2,
prod_{p>w} (1+O(1/p^2))-1,
prod_{w<p<=B_*} (1+K_0(exp(lambda J/p)-1)/p)-1
```

are negligible in the projective W-limit order.

This module also records the negative side: any term with only

```text
sum_{p>w} 1/p
```

is not a generic tail. It must be controlled by divisor averages, collision
load estimates, or another arithmetic input. It cannot be discarded by the
W-limit order alone.

## 2. Status label

`CONDITIONAL`

The deterministic tail inequalities are elementary under fixed-complexity
constants. Their use in the actual major-arc package is conditional on the
kernel, range, boundary, and model-matching estimates being uniform in the
same W-limit order.

## 3. Definitions and variables

Let `P(N,w)` denote the permitted parameter family at scale `N` and W-trick
level `w`. It may include:

```text
D,H,K,M,T,B_*(N,T)
```

subject to the range restrictions of the endpoint branch.

For an error term `Err(N,w;rho)` with `rho in P(N,w)`, define W-admissibility:

```text
Err = o_W(1)
```

if:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P(N,w)} |Err(N,w;rho)| = 0.
```

The quantifier form is:

```text
for every eps>0,
there exists w0,
for every w>=w0,
there exists N0(w),
for every N>=N0(w) and every rho in P(N,w),
|Err(N,w;rho)| <= eps.
```

Define the generic summable tail:

```text
G_2(w)=sum_{p>w} 1/p^2.
```

For fixed constants `c,lambda,J,K_0`, define:

```text
E_c(w)=prod_{p>w} (1+c/p^2)-1,
```

and:

```text
F_{lambda,J,K_0}(w,B)
  = prod_{w<p<=B}
      (1 + K_0(exp(lambda J/p)-1)/p)-1.
```

Here `J<=28` is fixed cube complexity, `lambda` is fixed before the
W-limit is taken, and `B` may be as large as the finite envelope
`B_*(N,T)`.

## 4. Assumptions

Assume:

- `J`, `lambda`, `K_0`, and all local Euler-product constants are fixed
  independently of `N,D,H,K,M,T`;
- the relevant estimates are uniform over `rho in P(N,w)` for fixed `w`;
- kernel truncation and range choices do not make the constants in the
  `O(1/p^2)` terms grow with `N`;
- any non-generic arithmetic errors, such as CRT range errors or kernel tails
  in exponential expansions, are separately W-admissible in the sense above;
- the W-trick is used with `N -> infinity` first and `w -> infinity` second.

If a later argument chooses a diagonal function `w=w(N)`, it must be obtained
after the double-limit estimates are proved and must preserve the required
range conditions, including `W=N^{o(1)}` when that restriction is active.

## 5. Proof / disproof / reduction

The basic bound is:

```text
G_2(w)=sum_{p>w} 1/p^2 <= sum_{n>w} 1/n^2 = O(1/w).
```

Hence:

```text
G_2(w) -> 0.
```

For fixed `c`:

```text
0 <= E_c(w)
  <= exp(c G_2(w))-1
  = O_c(G_2(w)).
```

Thus `E_c(w)=o_W(1)` whenever its constant `c` is fixed across the permitted
parameter family.

For the Module 189 exponential product, write:

```text
a_p = exp(lambda J/p)-1.
```

For `p>2 lambda J`, with the harmless convention that `w` is eventually this
large:

```text
a_p <= C_{lambda,J}/p.
```

Therefore:

```text
0 <= F_{lambda,J,K_0}(w,B)
  <= exp(C_{lambda,J,K_0} sum_{w<p<=B} 1/p^2)-1
  <= exp(C_{lambda,J,K_0} G_2(w))-1
  = O_{lambda,J,K_0}(G_2(w)).
```

The estimate is uniform in the finite cutoff `B`, hence uniform in the envelope
`B_*(N,T)`.

Consequently, terms in Modules 187-190 that are genuinely bounded by fixed
multiples of these summable tails are W-admissible:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P(N,w)} C G_2(w) = 0.
```

However:

```text
sum_{w<p<=B} 1/p
```

is not uniformly small as `B` grows. Any expression of this size is not a
generic Euler tail. In the present project those expressions are exactly where
the beta-load, collision, CRT, or divisor-average machinery is needed.

## 6. Edge cases

- If the constant multiplying `G_2(w)` depends on `N`, `M`, `T`, or
  `B_*(N,T)`, the generic tail argument can fail.
- If `lambda` is allowed to grow with `N` or with the major-arc denominator
  range, the Module 189 product is no longer covered by this fixed-constant
  lemma.
- If `J` changes because the model complexity changes, the tail estimate must
  be rerun with the new complexity.
- If `w` is chosen as a function of `N` before fixed-`w` estimates are proved,
  residue equidistribution and boundary savings may be lost.
- If kernel truncation enlarges `B_*(N,T)`, the `p^{-2}` product remains
  uniformly controlled, but first-order `1/p` terms do not.
- Prime powers are not automatically covered by the square-summable prime
  tail unless a separate prime-power transfer or exclusion package supplies
  the required summable bound.
- A smoothed projection and a sharp projection may have different constants;
  switching projection type restarts the uniformity check.

## 7. Where it fits in the project map

Modules 187-190 use generic Euler tails at several points:

```text
local factor expansion
  -> tail_w from O(1/p^2) terms

exponential moment product
  -> exp(O(sum_{p>w}1/p^2))

kernel/range audit
  -> finite cutoff B_*(N,T) in prime products.
```

Module 191 supplies the W-limit bookkeeping that makes those tails legitimate
only when their constants are uniform:

```text
fixed w
  -> N -> infinity uniformly over allowed ranges
  -> w -> infinity
  -> optional slow diagonal w(N).
```

This module supports the major-arc collision-control branch. It does not prove
projected local-model matching and it does not address the minor-arc branch.
Module 192 is the next composition step using this W-admissibility contract.

## 8. What remains open

This module does not prove:

- uniform kernel absolute-mass bounds for the actual major-arc projection;
- W-admissibility of the Module 190 kernel-tail and CRT range errors;
- verification of the Module 192 collision-defect hypotheses for the actual
  projected kernel;
- projected local-model matching;
- structural and boundary negligibility for the sharp interval model;
- minor-arc large-spectrum decay;
- prime-power transfer for the endpoint;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem or the all-alpha theorem.

## Red flags / forbidden upgrades

- Do not take `w -> infinity` before proving the fixed-`w`, `N -> infinity`
  estimate.
- Do not discard `sum_{p>w}1/p` terms as generic tails.
- Do not let constants hidden in `O(1/p^2)` grow with the finite range or
  projection parameters.
- Do not choose a fast-growing diagonal `w(N)` without checking `W=N^{o(1)}`
  and all interval/range losses.
- Do not treat W-limit bookkeeping as projected local-model matching.
- Do not transfer this model estimate to actual sharp moving selectors without
  the full transfer package.
