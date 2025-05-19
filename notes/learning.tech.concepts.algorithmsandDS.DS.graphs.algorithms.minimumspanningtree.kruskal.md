---
id: nwicd05v34oj3d1qs20kpl7
title: kruskal
desc: ''
updated: 1746959182147
created: 1746533874540
---

https://www.youtube.com/watch?v=71UQH7Pr9kU

- Whats kruskal algorithm?
- Whats the purpose of it? What does it contruct?
- Whats the data structure used to represent the graph?
- Whats the data structure used to track parent of each node
- Whats the data structure used to merge components and detect cycles?
- Whats the time complexity for kruskal?

```python
def kruskal(edges, n):
    parent = list(range(n))  # DSU parent initialization

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]  # Path compression
            x = parent[x]
        return x

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False

    # Step 1: sort edges by weight
    edges.sort(key=lambda x: x[2])
    mst_weight = 0
    mst_edges = []

    # Step 2: loop through sorted edges
    for u, v, w in edges:
        if union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges
```
## 🕒 Time Complexity of Kruskal’s Algorithm

### Main Steps:
1. Sort all edges → O(E log E)
2. Iterate through edges and use Union-Find (Disjoint Set Union, DSU) to detect cycles → near O(1) per operation with path compression

---

### ✅ Overall Time Complexity:
O(E log E)
