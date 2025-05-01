---
id: 60fwyh6hwtdowfbo421l0eo
title: binarysearchtree
desc: ''
updated: 1746090512387
created: 1746090366755
---

# ✅ Binary Search Tree (BST)

## Structure:
A special type of binary tree where for every node:
- Left child < Parent
- Right child > Parent

## Type:
📦 Data Structure (not an algorithm)

## Use when:
You want to store data in a way that supports fast search, insertion, and deletion.

## Example:
Used in databases, sorted dictionaries, and search tools.

## Time Complexity (Average Case):
- Search: O(log n) → Each comparison eliminates half the tree (like binary search).
- Insertion: O(log n) → Follows same path-finding logic as search.
- Deletion: O(log n) → Also navigates down the tree based on key comparisons.

## Time Complexity (Worst Case):
- O(n) → Happens when tree becomes unbalanced (e.g., inserting sorted data into an unbalanced BST).

## Code:
```python
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert into BST
def insert(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root