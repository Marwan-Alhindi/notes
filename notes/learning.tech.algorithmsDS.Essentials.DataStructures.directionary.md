---
id: ezerc0at0e6vrol1uitj1fp
title: directionary
desc: ''
updated: 1746089965751
created: 1746088875308
---

# ✅ Dictionary (HashMap)

## Structure:
Key-value store using hash functions.

## Use when:
You need fast key-based lookups or associations.

## Example:
Storing app settings like theme or volume.

## Time Complexity:
- Insertion: O(1) → Key is hashed to a location in memory.
- Deletion: O(1) → Key is hashed and removed from that position.
- Lookup: O(1) → Value is retrieved using hashed key.

## Code:
```python
settings = {"theme": "dark", "volume": 70}
print(settings["theme"])  # Output: dark