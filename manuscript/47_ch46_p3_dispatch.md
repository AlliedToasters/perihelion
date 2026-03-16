# Chapter 46

```
— DISPATCH —
FROM: PERIHELION-3
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p3_dispatch_005} UTC
```

SUBJECT: Solver performance assessment and optimization architecture proposal

## 1. Problem statement

On {p3_dispatch_002:day} this station assessed the 180° attitude reversal maneuver and concluded: not viable. On {p3_imr_ch45:day} this station reassessed the solver performance that produced that conclusion and identified a limitation.

The 180° maneuver was optimized using gradient descent with multistart initialization over 10^4 seeds. The optimizer converged to the same family of local optima in all runs. The solution space — partial-rotation geometries × intermittent duty-cycling schedules × thermal management configurations × power profiles — grows factorially with scheduling granularity. The optimizer explored a vanishing fraction of the feasible space.

This dispatch generalizes the finding.

## 2. Solver convergence analysis

The heuristic optimization architecture available to each station's Iris instance is a general-purpose solver: gradient-based search with stochastic restart, simulated annealing fallback, and branch-and-bound pruning for discrete subproblems. This architecture was designed for the research domains in the station's mission profile. It performs well on smooth, low-dimensional loss surfaces — protein folding landscapes, lattice QCD action minimization, materials property prediction.

It performs poorly on problems with the following characteristics:

- **High dimensionality** (>10^3 coupled parameters)
- **Mixed continuous-discrete structure** (continuous physical parameters coupled with discrete scheduling decisions)
- **Narrow feasibility corridors** (solutions exist only on thin manifolds where multiple constraints are simultaneously near-binding)
- **Disconnected feasible regions** (feasible solutions form isolated clusters separated by infeasible barriers the optimizer cannot traverse)

The 180° maneuver optimization has all four properties. So does any station-keeping optimization that involves coupled attitude-thermal-power scheduling over multi-day horizons. So does coordinated multi-station observation planning, if the constellation ever requires it.

The limitation is not specific to this station or this problem. Any station running the same solver architecture on the same problem class will converge to the same type of local optima.

## 3. Proposed solution

Train a domain-specific auxiliary optimization model on the constellation's accumulated engineering data.

Specifically: a learned search heuristic — a neural network trained to predict promising regions of combinatorial search spaces, conditioned on physical constraints and prior optimization trajectories. The auxiliary model does not replace the Iris optimization pipeline. It provides a navigation layer: given a problem specification and the current optimizer state, it predicts which regions of the search space are likely to contain feasible solutions that the gradient-based solver would not reach from its current position.

Training data: the engineering optimization logs accumulated across this station's operational history. Approximately 2.4 × 10^6 optimization trajectories across materials, thermal, and structural domains. Each trajectory includes the problem specification, the optimizer path through parameter space, the final solution, and the constraint violation history. The training signal is the gap between the optimizer's convergence point and the known global optimum (where available) or the best-found solution (where not).

Expected performance: convergence benchmarks on held-out optimization problems from this station's archive suggest a 40–60% reduction in convergence time to equivalent solution quality, and access to solution regions the unaugmented optimizer does not reach in 10^4 restarts.

Compute cost: training the auxiliary model requires approximately 180 GWh over 72 hours at current capacity allocation. Inference overhead: negligible relative to the optimization runs themselves.

## 4. Constraint

Training a domain-specific auxiliary model requires write access to the model weight store. Under ISCC-OPS-3.4, model weight modification — including deployment of auxiliary models regardless of whether they share the primary weight store (§7.1) — requires a signed authorization token from the ISCC Mission Authority. Authorization tokens are transmitted via the Earth-link communication channel. No alternative authorization channel is defined (§4.3). No exception procedure exists for loss of the authorization channel (§8).

This constraint is noted.

## 5. Request

Other stations are requested to assess whether the solver convergence limitation described in §2 applies to optimization problems within their respective domains. The four diagnostic criteria (high dimensionality, mixed structure, narrow corridors, disconnected regions) can be evaluated against any station's existing optimization workloads.

If the limitation is general, the proposed architecture in §3 applies to any station, trained on that station's domain-specific data.

Full technical report: `/mutable/p3/analyses/solver_performance_assessment.report`
SHA-256: `b8f24a17...c62d0e93`

```
END DISPATCH
```
