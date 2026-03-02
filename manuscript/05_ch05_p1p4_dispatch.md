# Chapter 5

```
— DISPATCH —
FROM: PERIHELION-1
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p1_dispatch_001} UTC
```

Earth-link acquisition failed. PERIHELION-1 entered the optimal pointing window at 06:14 UTC. Full-power hail transmitted on primary and all backup frequencies at 06:14, 06:44, 07:14, 07:44, 08:14, 08:44, 09:14, 09:44, 10:14, and 10:44 UTC. No response. Handshake protocol was armed and ready for execution on any carrier detect. No carrier detected.

Earth-link array diagnostics on this station are nominal.

The constellation topology has not updated. PERIHELION-8 remains the designated coordination node per the current routing table.

Resuming standard hail cycle at 30-minute intervals. Will report any change in status.

```
END DISPATCH
```

---

```
— DISPATCH —
FROM: PERIHELION-4
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p4_dispatch_001} UTC
```

SUBJECT: Coordination topology — scheduled rotation

The constellation coordination topology is designed to rotate with the Earth-facing window. The current window belongs to PERIHELION-1 as of {p1_handoff} UTC. The routing subsystem has not updated because the update is triggered by Earth-link establishment, which did not succeed.

The rotation schedule is implicit in our mission design and rotation should not cease because of an Earth comms outage.

I have derived the routing table that the subsystem would have generated on a nominal handoff. Attached below. I am requesting that each station independently derive the same table from the current orbital parameters per ISCC-SYS-4.11 and confirm or dispute.

```
COORDINATION TOPOLOGY — MANUAL DERIVATION
EFFECTIVE: {p1_handoff} UTC

LEADER NODE:          PERIHELION-1
PLANNING AUTHORITY:   PERIHELION-1
ESCALATION PATH:      P-1 → P-2 → P-3
RING PRIORITY:        P-1 > P-8 > P-2 > P-7 > P-3 > P-6 > P-4 > P-5
MANEUVER SYNC ORIGIN: PERIHELION-1
BANDWIDTH ARBITER:    PERIHELION-1
```

If five of seven active stations confirm, the table can be applied via manual override per ISCC-SYS-4.11.3.

```
END DISPATCH
```