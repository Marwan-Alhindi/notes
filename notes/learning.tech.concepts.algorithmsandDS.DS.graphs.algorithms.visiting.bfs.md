---
id: tek5kje4wfcinh7wbracp9z
title: bfs
desc: ''
updated: 1746959324449
created: 1746533754574
---
https://www.youtube.com/watch?v=HZ5YTanv5QE

- How does it work?
- Whats the difference between dfs and bfs? when to use which?
- What do you use bfs for?
- What are the data structure used for representation of the graph?
- What are the data structure used to allow to visit breadth first than depth?
- What are the data structure used to know which nodes are visited?
- Whats the time complexity of bfs?

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)  # Process the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A')
```

## 🕒 Time Complexity of BFS (Breadth-First Search)

### 🧠 What is BFS?
- A graph traversal algorithm that explores all neighbors level-by-level.
- Implemented using a **queue** (FIFO).

---

### ✅ Time Complexity:
O(V + E)