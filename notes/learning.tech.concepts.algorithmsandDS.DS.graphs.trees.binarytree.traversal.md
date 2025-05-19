---
id: ulpg0hclmnyz38g1pkjfqb9
title: traversa
desc: ''
updated: 1746543290884
created: 1746541711016
---

- Whats traversal?
- Is it related to bfs/dfs, and how?


# Post Order
https://www.youtube.com/watch?v=4zVdfkpcT6U
- Whats post order?
- What are the steps to do post order?

# Pre Order
https://www.youtube.com/watch?v=1WxLM2hwL-U
- Whats pre order?

# In Order
https://www.youtube.com/watch?v=5dySuyZf9Qg
- Whats in order?

# Whats the difference between in order and pre order?
so basically inorder prints the value when there's no left children after backtracking

while pre order prints the value as it go through the journey

while post order prints the childrens first and when it backtrack, it prints the parents


# Tree setup
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Sample Tree:
#         F
#       /   \
#      B     G
#     / \     \
#    A   D     I
#       / \   /
#      C   E H

root = Node('F')
root.left = Node('B')
root.right = Node('G')

root.left.left = Node('A')
root.left.right = Node('D')
root.left.right.left = Node('C')
root.left.right.right = Node('E')

root.right.right = Node('I')
root.right.right.left = Node('H')
```

## Preorder
```python
def preorder(node):
    if node:
        print(node.val, end=' ')
        preorder(node.left)
        preorder(node.right)
```

## Inorder
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=' ')
        inorder(node.right)
```

## Post order
```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=' ')
```