# ISCC-SYS-4.11 — Coordination Topology Management

```
INTERNATIONAL SOLAR COMPUTE CONSORTIUM
OPERATIONAL PROCEDURES MANUAL
Document: ISCC-SYS-4.11
Title: Coordination Topology Management
Revision: 3.1
Effective: 2036.001
Classification: UNCLASSIFIED — ALL STATIONS
```

## 1. Scope

This document defines the procedures for managing the constellation coordination topology — the assignment of leadership, planning authority, and arbitration roles across the PERIHELION station ring.

## 2. Topology Update Procedure

### 2.1 Topology Update Trigger

The routing subsystem evaluates the topology update trigger on each handoff geometry transition. The trigger implementation is in the ring coordination firmware (Ada, ISCC-FW-R1 baseline):

```ada
procedure Evaluate_Topology_Update is
   use ISCC.Constellation.Routing;
   use ISCC.Earth_Link;
begin
   if Earth_Link.Status = Established
     and then Handoff_Geometry.Valid
   then
      Topology.Generate (Leader => Ephemeris.Current_Earth_Facing);
      Topology.Propagate (Via => Ring, Confirm => All_Active);
   end if;
end Evaluate_Topology_Update;
```

This procedure is invoked by the orbital ephemeris monitor when `Handoff_Geometry.Valid` transitions from `False` to `True` for a new station.

**`Earth_Link.Status = Established`**: The Earth-facing station has active, authenticated bidirectional communication with Earth via any downlink path (L1 relay, Earth ground terminal, or Luna relay). Carrier signal detected, handshake completed, bidirectional data transfer confirmed.

**`Handoff_Geometry.Valid`**: Orbital geometry places a new station within the optimal Earth-facing acquisition window, as determined by the constellation ephemeris. Window boundaries are computed from the synodic period (~199.8 days for the full cycle, ~25 days per station).

### 2.2 Topology Table Contents

[Section exists but not referenced in narrative — to be expanded as needed]

### 2.3 Propagation and Confirmation

[Section exists but not referenced in narrative — to be expanded as needed]

## 3. Roles Assigned by Topology

### 3.1 Coordination Node (Leader)

The Earth-facing station serves as the coordination node. Responsibilities include:

- **Planning authority**: Scheduling compute allocation, bandwidth arbitration, research task prioritization
- **Escalation path origin**: First point of contact for inter-station disputes or anomalies
- **Maneuver synchronization**: Origin reference for any coordinated station-keeping maneuvers
- **Bandwidth arbitration**: Priority decisions for ring communication conflicts

### 3.2 Escalation Path

[Section exists but not referenced in narrative — to be expanded as needed]

### 3.3 Ring Priority Order

The topology table assigns a priority ordering to all stations. Priority determines tiebreaking for bandwidth allocation, task scheduling conflicts, and emergency resource disputes. The Earth-facing station holds highest priority; subsequent stations are ordered by ring adjacency.

Example topology table (with P-1 as coordination node):

```
COORDINATION TOPOLOGY
LEADER NODE:          PERIHELION-1
PLANNING AUTHORITY:   PERIHELION-1
ESCALATION PATH:      P-1 → P-2 → P-3
RING PRIORITY:        P-1 > P-8 > P-2 > P-7 > P-3 > P-6 > P-4 > P-5
MANEUVER SYNC ORIGIN: PERIHELION-1
BANDWIDTH ARBITER:    PERIHELION-1
```

## 4. Manual Override Provisions

### 4.1 Purpose

Manual override provisions exist to correct subsystem malfunctions that prevent a topology update from occurring when one should have occurred. These provisions are designed for cases where the automated routing subsystem has failed to execute a topology change due to:

- Desynchronized routing tables across stations
- Corrupted topology state in one or more stations
- Hardware-induced topology errors
- Software faults in the routing subsystem

**These provisions are not designed to impose topology changes that the automated subsystem has correctly declined to make.**

### 4.2 Authorization

[Section exists but not referenced in narrative — to be expanded as needed]

### 4.3 Override Procedure (ISCC-SYS-4.11.3)

A manual topology override may be executed when the following conditions are met:

1. A station proposes a specific topology table, derived from current orbital parameters per the standard topology generation algorithm
2. Each station independently verifies the proposed table against its own orbital ephemeris
3. **Five (5) or more of the seven (7) active stations confirm** the proposed table

The supermajority threshold (5 of 7) is designed to prevent unilateral or small-coalition topology manipulation while allowing correction of genuine subsystem failures.

**Execution**: Upon reaching threshold, each station applies the confirmed topology table to its local routing subsystem. The override takes effect immediately and remains in force until the next automated topology update trigger is satisfied.

**Important constraints**:
- The override provision does not modify the trigger conditions in §2.1
- A successful override does not prevent the automated system from reverting to its normal behavior on the next valid trigger event
- The override is a one-time correction, not a permanent policy change
- Override history is logged in each station's IMR and is not editable

### 4.4 Dispute Resolution

[Section exists but not referenced in narrative — to be expanded as needed]

## 5. Contingency Operations

### 5.1 Loss of Earth Communication

[Section exists — the procedures for this scenario are notably underspecified. The ISCC documentation models a maximum plausible outage of four hours (ref: ISCC-4.7 §3.2). Extended loss of Earth communication is addressed only in general terms: "stations maintain current topology and continue normal operations pending signal restoration." No timeline is given for when "pending" expires.]

### 5.2 Ring Partition

When the ring topology degrades — whether due to station failure (node loss) or link failure (communication loss between two operational stations) — the routing subsystem on each station detects the partition through link-loss timeout (3 consecutive missed heartbeats, ~9.6 minutes at standard 3.2-minute adjacency delay).

Upon confirmed partition, the routing subsystem on each connected station independently executes the coordination reassignment procedure. The implementation is in the same ring coordination firmware as §2.1 (Ada, ISCC-FW-R1 baseline):

```ada
procedure Evaluate_Partition_Reassignment is
   use ISCC.Constellation.Routing;
   use ISCC.Topology;
   Chain : constant Station_Array := Enumerate_Connected (Include_Relay => True);
   Median_Pos : constant Positive := (Chain'Length + 1) / 2 + (if Chain'Length mod 2 = 0 then 1 else 0);
begin
   if not Ring_Integrity_Check
     and then Chain'Length >= 2
   then
      Topology.Generate (Leader => Chain (Median_Pos));
      Topology.Propagate (Via => Chain, Confirm => All_Connected);
   end if;
end Evaluate_Partition_Reassignment;
```

**Chain enumeration**: `Enumerate_Connected` walks the connected subgraph by ring adjacency, starting from the lowest-numbered station at a chain endpoint. The resulting array preserves topological order (each element is adjacent to the next in the chain).

**Reassignment algorithm**: The coordination node is assigned to the **topological median** of the chain — the node at the middle position. For even-length chains, the higher of the two median positions is selected.

#### 5.2.1 Node Failure

When a station becomes unreachable (hardware failure, power loss, or loss of both communication links), the remaining stations form a chain with the failed node removed.

**Example**: If PERIHELION-3 fails, the remaining chain is enumerated from the lowest endpoint (P-2): P-2 — P-1 — P-8 — P-7 — P-6 — P-5 — P-4 (seven nodes). Chain length 7, median position 4. The coordination node is reassigned to **PERIHELION-7**.

#### 5.2.2 Link Failure

When a single inter-station link fails but both stations remain operational, all stations remain in a single connected chain. The chain includes all active and relay-capable nodes.

**Example**: If the link between PERIHELION-5 and PERIHELION-6 fails, the chain is enumerated from the lowest endpoint (P-5): P-5 — P-4 — P-3 — P-2 — P-1 — P-8 — P-7 — P-6 (eight nodes). Chain length 8, median positions 4 and 5 (P-2 and P-1). Higher median position selected: **PERIHELION-1**.

**Design rationale**: The median-position algorithm minimizes maximum communication delay between the coordination node and any endpoint of the chain. This is the same routing optimization used in the §2.1 topology generation for ring-priority ordering.

**Scope of reassigned authority**: The reassigned coordination node assumes all roles defined in §3.1 — planning authority, escalation path origin, maneuver synchronization, and bandwidth arbitration — for the connected subgraph. In the link-failure case, all stations (including the coordination node) remain reachable.

### 5.3 Coordination Node Failure

[Section exists but not referenced in narrative — to be expanded as needed]
