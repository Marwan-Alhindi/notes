---
id: kbbsw9iiif4ba31ee14489o
title: merge
desc: ''
updated: 1746623632045
created: 1746446575498
---

https://www.youtube.com/watch?v=4VqmGXwpLqc

- Whats merge sort?
- Whats the time and space complexity for merge sort?
- Is merge sort usually done recursively?

# 📊 Merge Sort – Time & Space Complexity

| Case        | Time Complexity | Notes                               |
|-------------|------------------|--------------------------------------|
| **Best**    | O(n log n)       | Efficient divide and merge steps     |
| **Average** | O(n log n)       | Consistent performance               |
| **Worst**   | O(n log n)       | Even in worst-case input order       |

# 🧮 Space Complexity: **O(n)**
- Requires additional space for merging.


```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```