---
id: o6yp261ehiut5ihaazm22er
title: heaps
desc: ''
updated: 1746090636365
created: 1746090625542
---

# ✅ Heap

## Structure:
A complete binary tree where every parent is <= (min-heap) or >= (max-heap) its children.

## Use when:
You need fast access to the minimum or maximum value.

## Example:
Priority queues, scheduling tasks, Dijkstra’s algorithm.

## Time Complexity:
- Insert: O(log n) → New element is added at bottom and bubbled up.
- Remove Min/Max: O(log n) → Top element removed and tree is re-heapified.
- Peek: O(1) → Root is always the min/max.

## Code:
```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # Output: 1