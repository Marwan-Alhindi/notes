---
id: wzjmjo41l7odmtgupixzsfl
title: binarytrees
desc: ''
updated: 1746090324529
created: 1746090299414
---

# ✅ Binary Tree

## Structure:
Each node has up to 2 children: left and right.

## Use when:
You need to organize data hierarchically with ordered relationships.

## Example:
Expression parsing or representing file structures.

## Time Complexity (unbalanced):
- Insert/Search/Delete: O(n) → In worst-case (like a linked list), tree becomes unbalanced and must scan all nodes.
- In balanced tree: O(log n) → Height is minimal, so operations depend on log of node count.

## Code:
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)