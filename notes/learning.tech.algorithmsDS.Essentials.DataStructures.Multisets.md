---
id: rr0mjdbzbstueqbiday3ne1
title: Multisets
desc: ''
updated: 1746089890315
created: 1746088394607
---

# ✅ Multiset (Counter)

## Structure:
Like a set but allows duplicates and counts each item's frequency.

## Use when:
You want to count how many times each item appears.

## Example:
Counting word frequencies in a document.

## Time Complexity:
- Insertion: O(1) → The key is hashed and its count is incremented, unaffected by total keys.
- Deletion: O(1) → Decreasing the count or removing the key uses direct hash access.
- Lookup: O(1) → Counts are retrieved directly by the hashed key.

## Code:
```python
from collections import Counter

words = ["a", "b", "a", "c", "b", "a"]
counter = Counter(words)
print(counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})