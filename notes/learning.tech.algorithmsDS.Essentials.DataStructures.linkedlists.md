---
id: etexiuplofbeb5skqrmritx
title: linkedlists
desc: ''
updated: 1746089985139
created: 1746088912454
---

# ✅ Linked List

## Structure:
Each node contains data and a reference to the next node.

## Use when:
You frequently insert/delete from the front or in the middle.

## Example:
Implementing a dynamic playlist or undo buffer.

## Time Complexity:
- Access: O(n) → Must traverse node by node.
- Insertion at head: O(1) → Update head pointer only.
- Insertion in middle: O(n) → Need to traverse to insert location.
- Deletion: O(1) if pointer to node is known, O(n) otherwise.

## Code:
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = Node(10)
head.next = Node(20)
print(head.next.val)  # Output: 20