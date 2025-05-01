---
id: 1z8n5ls80fb2v3p15ichaeu
title: flownetwork
desc: ''
updated: 1746090700335
created: 1746090689530
---

# ✅ Flow Network

## Structure:
A directed graph where each edge has a capacity and a current flow.

## Use when:
You need to model transportation of resources with limits.

## Example:
Internet bandwidth routing, water supply systems.

## Time Complexity:
- Representation Lookup: O(1) → Capacities and flows are accessed directly per edge.
- Update Flow: O(1) → Adjusting flow value is constant-time.
- Full Network Traversal (e.g., for Ford-Fulkerson): O(V + E) per DFS/BFS call.

## Code:
```python
graph = {
    's': {'a': 10, 'b': 5},
    'a': {'b': 15, 't': 10},
    'b': {'t': 10},
    't': {}
}