---
id: s9j6nmqiklj86efb6kao1pb
title: huffman
desc: ''
updated: 1746090606833
created: 1746090600280
---

# ✅ Huffman Tree

## Structure:
A binary tree built from bottom-up where characters with lower frequency have longer depth.

## Use when:
You want to compress data using variable-length prefix codes.

## Example:
ZIP file compression, MP3 encoding.

## Time Complexity:
- Build: O(n log n) → Uses a min-heap to repeatedly combine lowest-frequency nodes.
- Lookup: O(n) → Decoding involves traversing from root to leaf.

## Code:
```python
import heapq
from collections import Counter

freq = Counter("aabbbcccc")
heap = [[weight, char] for char, weight in freq.items()]
heapq.heapify(heap)

while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)
    heapq.heappush(heap, [lo[0]+hi[0], [lo, hi]])