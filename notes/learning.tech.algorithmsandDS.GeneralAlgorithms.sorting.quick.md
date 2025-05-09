---
id: v5y1hc4q067o6v9enmpijkz
title: quick
desc: ''
updated: 1746789599726
created: 1746446580679
---

https://www.youtube.com/watch?v=WprjBK0p6rw

- Whats quick sort?
- Whats pivot?
- When do you swap two elements? Do you apply the green < orange condition, after the orange moves or before?
- Is it recursive?
- when do you stop the algorithm?
- Whats the complexity of quick sort?
- is quick from divide and conquer paradigm?


# 📊 Quick Sort – Time & Space Complexity
| Case        | Time Complexity | Notes                                       |
|-------------|------------------|---------------------------------------------|
| **Best**    | O(n log n)       | Balanced partitions                         |
| **Average** | O(n log n)       | Typical case performance                    |
| **Worst**   | O(n²)            | Happens when pivot is always min/max        |

# 🧮 Space Complexity:
- **O(log n)** → Recursive call stack (in-place implementation)
- **O(n)** → If implemented using extra arrays (non in-place)

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
```