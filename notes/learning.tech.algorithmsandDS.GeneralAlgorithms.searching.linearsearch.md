---
id: 1ru0svmhx5touov4seudag2
title: linearsearch
desc: ''
updated: 1746692806985
created: 1746446659099
---

https://www.youtube.com/watch?v=19hcyQN8J7o

- Whats linear search?


# 📊 Linear Search – Time & Space Complexity
| Case        | Time Complexity | Notes                                       |
|-------------|------------------|----------------------------------------------|
| **Best**    | O(1)             | Target is the first element                  |
| **Average** | O(n)             | Target is somewhere in the middle            |
| **Worst**   | O(n)             | Target is at the end or not present          |

# 🧮 Space Complexity: **O(1)**
- No extra memory used; search is done in-place

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found
    return -1  # Not found