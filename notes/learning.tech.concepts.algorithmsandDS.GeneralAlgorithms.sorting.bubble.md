---
id: 37xzm1lxf3g0mqp1v98onl6
title: bubble
desc: ''
updated: 1746623444246
created: 1746446561472
---

https://www.youtube.com/watch?v=xli_FI7CuzA

- How does bubble sort works?
- Whats the time complexity for bubble sort?

# 📊 Bubble Sort – Time & Space Complexity

| Case        | Comparisons       | Swaps            | Time Complexity |
|-------------|-------------------|------------------|-----------------|
| **Best**    | N - 1 (no swaps)  | 0                | O(n)*           |
| **Average** | ~N² / 2           | ~N² / 2          | O(n²)           |
| **Worst**   | N(N - 1) / 2      | N(N - 1) / 2     | O(n²)           |

> 🧠 *Best case assumes the algorithm has been optimized to detect if the list is already sorted.



```py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```