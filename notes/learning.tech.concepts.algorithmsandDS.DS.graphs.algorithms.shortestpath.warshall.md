---
id: 42w7r8oeyzyu8t0u5ay53c2
title: warshall
desc: ''
updated: 1746959232813
created: 1746534284898
---

https://www.youtube.com/watch?v=4OQeCuLYj-4


- Whats the purpose of warshall?
- Whats the goal of dijkstra and warshall?
- Hows warshall different than dijkstra?
- Whats the data structure used to store all the distances?
- Whats the data structure used to store the shortest distances between all the nodes?
- Whats the time complexity for the algoirthm?

```python
def floyd_warshall(graph):
  V = len(graph)
  dist = [row[:] for row in graph]  # Make a copy of the input matrix

  for k in range(V):           # Intermediate node
      for i in range(V):       # From node
          for j in range(V):   # To node
              if dist[i][k] + dist[k][j] < dist[i][j]:
                  dist[i][j] = dist[i][k] + dist[k][j]
  
  return dist
```

### ✅ Time Complexity:
O(V³)
- The algorithm uses **3 nested loops** over the vertices, resulting in cubic time complexity.
