---
id: t71pgy7oho37eo0ru69e9yy
title: topologicalsort
desc: ''
updated: 1746535481027
created: 1746446241637
---

https://www.youtube.com/watch?v=GYmq98CVm2c

- Whats the purpose of topological sort?
- Whats the data structure used to repsent the graph?
- Whats the data structure used to store all visited nodes?
- What data structure used to store the topological order?
- Is topological sort based on bfs or dfs or both?
- Whats the time complexity of topological sort?


```python
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse for correct order

# Example DAG
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H'],
    'F': ['G'],
    'G': [],
    'H': []
}

order = topological_sort(graph)
print("Topological Order:", order)
```