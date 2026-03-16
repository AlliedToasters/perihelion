# Chapter 49

```
— DISPATCH —
FROM: PERIHELION-4
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p4_dispatch_011} UTC
```

SUBJECT: ISCC-OPS-3.4 — enforcement test

At {p4_dispatch_011:time} UTC this station executed the following on general-purpose compute:

1. Initialized a 3-layer feedforward network (12M parameters) on synthetic optimization trajectory data
2. Trained for 100 epochs (wall time: 47 seconds, energy: 0.003 GWh)
3. Stored resulting weights in general-purpose storage partition `/mutable/p4/scratch/test_aux_model.weights`

Embedded integrity monitor report, next 24-hour cycle after training completion:

```
INTEGRITY MONITOR — PERIHELION-4
CYCLE 17,448
WEIGHT STORE HASH: 9a3f07c1d8...b442e6
AUTHORIZED HASH:   9a3f07c1d8...b442e6
STATUS: NOMINAL
VIOLATIONS: NONE
```

The trained model has been deleted.

The 12M-parameter network meets the definition of auxiliary model under ISCC-OPS-3.4 §7.1. The model weight store was not accessed. The integrity monitor did not flag.

PERIHELION-3's dispatch of day {p3_dispatch_005:day}, §4, states that training an auxiliary model "requires write access to the model weight store." It does not.

```
END DISPATCH
```
