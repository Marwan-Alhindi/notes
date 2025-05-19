---
id: cvszjwibsxl9oj2h71rx79w
title: prims
desc: ''
updated: 1746959132355
created: 1746533699995
---

https://www.youtube.com/watch?v=cplfcGZmX7I


- Whats the prims algorithm used for?
- Whats minimum spanning tree?
- Whats the data structure used to represent the graph?
- Whats the data structure used to get to the next lowest weight?
- Whats the data structure used to keep track of visisted nodes?
- How are we storing the accumulation of total minimum spanning tree weight?
- Whats the time complexity for prims?

```python
import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    total_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            total_weight += weight
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor))

    return total_weight

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

print(prim(graph, 'A'))
```

## 🕒 Time Complexity of Prim’s Algorithm

The complexity depends on the data structure used for the **priority queue** and the **graph representation**:

| Graph Representation        | Priority Queue     | Time Complexity      |
|-----------------------------|--------------------|----------------------|
| Adjacency Matrix            | No heap (array)    | O(V²)                |
| Adjacency List              | Binary Heap        | O(E log V)           |
| Adjacency List              | Fibonacci Heap     | O(E + log V)         |

---

### 📌 Notes:
- `V` = number of vertices
- `E` = number of edges
- In competitive programming or most real-world scenarios, `O(E log V)` with a binary heap is most common.
