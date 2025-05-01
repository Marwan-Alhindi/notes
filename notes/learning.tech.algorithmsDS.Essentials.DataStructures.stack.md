---
id: 2kq6i3yl6njqwr42iw6anuu
title: stack
desc: ''
updated: 1746089924474
created: 1746088755425
---

# ✅ Stack

## Structure:
LIFO (Last In, First Out) using a list.

## Use when:
You need to reverse operations or manage nested states.

## Example:
Undo feature in a text editor.

## Time Complexity:
- Push: O(1) → Appends to end of list; size doesn’t affect this.
- Pop: O(1) → Removes last element without shifting.
- Peek: O(1) → Access last element directly.

## Code:
```python
stack = []
stack.append("edit1")
stack.append("edit2")
print(stack.pop())  # Output: edit2