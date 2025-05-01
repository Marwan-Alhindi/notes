---
id: qxg0zzoa5nofzh1uzr6mvhf
title: queue
desc: ''
updated: 1746089945305
created: 1746088772816
---

# ✅ Queue

## Structure:
FIFO (First In, First Out) using deque.

## Use when:
You need to process elements in arrival order.

## Example:
Handling print jobs or tasks in a queue.

## Time Complexity:
- Enqueue: O(1) → Appending to deque’s end is constant-time.
- Dequeue: O(1) → Removing from front doesn’t depend on size.
- Peek: O(1) → Front element is accessible directly.

## Code:
```python
from collections import deque

queue = deque()
queue.append("job1")
queue.append("job2")
print(queue.popleft())  # Output: job1