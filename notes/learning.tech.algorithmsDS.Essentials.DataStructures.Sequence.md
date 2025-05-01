---
id: csktzmyrel92xyszxemd907
title: Sequence
desc: ''
updated: 1746089905292
created: 1746088445680
---

# ✅ Sequence (List/Array)

## Structure:
Ordered collection of elements, accessed by index.

## Use when:
You need fast index access or ordered iteration.

## Example:
Storing a list of temperature readings.

## Time Complexity:
- Access: O(1) → Indexing like `arr[2]` calculates the address directly.
- Append: O(1) amortized → Most appends don't depend on size; occasional resizing may occur.
- Insertion/Deletion (middle): O(n) → Shifts elements after the position.
- Search: O(n) → Must scan elements one by one.

## Code:
```python
temps = [21.5, 22.0, 23.1]
print(temps[1])  # Output: 22.0