---
id: xivibxbpmra36203bum92vb
title: binarysearch
desc: ''
updated: 1746692603095
created: 1746446663388
---


https://www.youtube.com/watch?v=eVuPCG5eIr4

- Whats binary search?
- is binary search only applied to a sorted array?!
- What would be the time complexity for the case that the array isnt sorted and the case that its?
- How do you represent binary search with a binary tree?

# 📊 Binary Search – Time & Space Complexity
| Case        | Time Complexity | Notes                                     |
|-------------|------------------|--------------------------------------------|
| **Best**    | O(1)             | Target found at the first middle check     |
| **Average** | O(log n)         | Search space halved each step              |
| **Worst**   | O(log n)         | Target not found or at one end             |

# 🧮 Space Complexity:
- **O(1)** → Iterative version (no extra space)
- **O(log n)** → Recursive version (due to call stack)

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found
```