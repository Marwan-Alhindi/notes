---
id: yoq9jh7sdl90xaan9tb85pq
title: graphs
desc: ''
updated: 1746090032174
created: 1746090024933
---

## Structure:
A set of nodes (vertices) connected by edges (can be directed or undirected).

## Use when:
You need to model relationships, paths, or networks.

## Example:
Social networks, road maps, internet routing.

## Time Complexity (Adjacency List):
- Add Vertex: O(1) → Just append a key with an empty list.
- Add Edge: O(1) → Append to a vertex’s adjacency list.
- Lookup Neighbors: O(1) → Each node’s neighbors are stored directly.
- Search (e.g. BFS/DFS): O(V + E) → You may need to touch every vertex and edge once.

## Code:
```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
print(graph["A"])  # Output: ['B', 'C']