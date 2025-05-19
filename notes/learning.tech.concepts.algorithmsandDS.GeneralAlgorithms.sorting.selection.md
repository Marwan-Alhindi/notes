---
id: ewqorh3ak9jpr8ca8564buy
title: selection
desc: ''
updated: 1746691465770
created: 1746446565731
---


https://www.youtube.com/watch?v=g-PGLbMth_g


- Whats selection sort?
- How does it work - explain with an example
- Whats the complexity of selection sort?

## 📊 Selection Sort – Time & Space Complexity
| Case        | Time Complexity | Notes                                 |
|-------------|------------------|----------------------------------------|
| **Best**    | O(n²)            | Always scans the remaining unsorted part |
| **Average** | O(n²)            | No matter the input order             |
| **Worst**   | O(n²)            | Worst case same as best               |

### 🧮 Space Complexity: **O(1)**
- In-place sorting algorithm (no extra memory needed)

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Find the minimum in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```