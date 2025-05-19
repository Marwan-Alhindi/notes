---
id: vgc9r9yl616jd8h6ldmfdma
title: dfs
desc: ''
updated: 1746959306990
created: 1746533904527
---

https://www.youtube.com/watch?v=Urx87-NMm6c

- How does it work?
- What do you use dfs for?
- Which element do you pop from the stack? first, random or last?
- Whats the difference between dfs and bfs? when to use which?
- What are the data structure used for representation of the graph?
- What are the data structure used to allow to visit depth first than breadth?
- What are the data structure used to know which nodes are visited?
- Whats the time complexity of dfs?

#### 💻 Code:
```python
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

dfs(graph, 'A')
```

## 🕒 Time Complexity of DFS (Depth-First Search)

### 🧠 What is DFS?
- A graph traversal algorithm that explores as far as possible along each branch before backtracking.
- Can be implemented **recursively** or using a **stack**.

---

### ✅ Time Complexity:
O(V + E)