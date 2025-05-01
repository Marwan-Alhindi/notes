---
id: mc5y0x1mck5byparm76vis9
title: Sets
desc: ''
updated: 1746089869895
created: 1746088128710
---

# ✅ Set

## Structure:
Unordered collection of unique elements. No duplicates.

## Use when:
You need to check for membership or remove duplicates efficiently.

## Example:
Keeping track of unique user IDs in a system.

## Time Complexity:
- Insertion: O(1) → Uses a hash function to determine where to place the item, so the number of items already in the set doesn't matter.
- Deletion: O(1) → Uses the hash to directly locate the item for removal.
- Lookup: O(1) → Hash lookup lets you check existence without scanning all items.

## Code:
```python
visited = set()
visited.add("node1")
if "node2" not in visited:
    visited.add("node2")