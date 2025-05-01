---
id: nalewnzuujuvveymycdn8gq
title: trees
desc: ''
updated: 1746090203444
created: 1746090077195
---

# ✅ Tree (General)

## Structure:
A hierarchical data structure consisting of nodes, where each node has a parent (except the root) and zero or more children. No cycles allowed.

## Use when:
You need to model hierarchical relationships such as organization charts, file systems, or decision structures.

## Example:
A file explorer where folders contain other folders/files.

## Time Complexity (Generic):
- Insert/Search/Delete: O(n) → In an unstructured tree, you may need to scan all nodes.
- In structured trees (e.g., binary search trees): O(log n) on average if balanced.

## Code:
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

root = TreeNode("root")
child1 = TreeNode("child1")
child2 = TreeNode("child2")
root.children.append(child1)
root.children.append(child2)
# Continuing from your existing tree
child1_1 = TreeNode("child1_1")
child1_2 = TreeNode("child1_2")
child1.children.append(child1_1)
child1.children.append(child1_2)

child2_1 = TreeNode("child2_1")
child2.children.append(child2_1)