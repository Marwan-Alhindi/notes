---
id: g8s6mxqhz709kubbpmvn9iy
title: insertion
desc: ''
updated: 1746691743052
created: 1746446572210
---


https://www.youtube.com/watch?v=JU767SDMDvA


- Whats insertion sort?
- How does it work with an example?
- Whats the time complexity of it?


# 📊 Insertion Sort – Time & Space Complexity
| Case        | Time Complexity | Notes                                        |
|-------------|------------------|----------------------------------------------|
| **Best**    | O(n)             | Already sorted, minimal shifts               |
| **Average** | O(n²)            | Random order input                           |
| **Worst**   | O(n²)            | Reversed input, maximum shifts               |

# 🧮 Space Complexity: **O(1)**
- In-place sorting, no additional memory needed

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements of arr[0..i-1], that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr
```