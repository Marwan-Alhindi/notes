---
id: mhiwla520zs4qwgnz0emxs6
title: dijkstra
desc: ''
updated: 1746791873902
created: 1746533967784
---

https://www.youtube.com/watch?v=_lHSawdgXpI

- Whats dijksta algorithm and whats the purpose of it?
- How does it work?
- Whats the data structure used to represent the graph?
- Whats the data structure used to get to the next closest node?
- whats the data structure used to store and update the shortest distances?
- Whats the data structure used to store visited nodes?
- Whats the time complexity for dihjkstra?

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > distances[node]:
            continue  # Skip if already visited with a shorter path

        for neighbor, weight in graph[node]:
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print(dijkstra(graph, 'A'))