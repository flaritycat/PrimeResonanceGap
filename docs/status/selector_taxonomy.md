# Selector taxonomy

Every theorem must state which selector it uses.

## Actual sharp moving selector

```text
chi_alpha(p)=1_{||alpha p||<1/log p}
```

This is the selector in the original problem.

## Sharp frozen dyadic selector

```text
chi_{alpha,X}^{fr}(p)=1_{||alpha p||<1/log X}
```

Useful on dyadic shells, but not automatically equivalent to the actual moving selector.

## Smoothed finite-band frozen selector

A smooth Fourier-truncated approximation to the frozen selector.

## Hidden Bernoulli lift

A probabilistic reference model with alpha-dependent Bernoulli variables.

## Finite-stage/reference/survivor measures

Model or construction measures used in recursive constructions or survivor arguments.

## Transfer requirements

To upgrade a non-actual selector statement to the actual selector, include:

- boundary transfer;
- moving `1/log p` transition control;
- prefix safety;
- denominator control;
- tail control;
- sharp-window transfer;
- recursive engine compatibility when relevant.
