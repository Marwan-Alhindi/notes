---
id: 8b5wo4z3xg2iw8av6cqwvx9
title: searchinsertdelete
desc: ''
updated: 1746957744116
created: 1746446079650
---


# 🌲 Binary Search Tree (BST) – Cheat Sheet

---

## 🔍 1. Search, Insert, Delete Operations

### ✅ Search:
- Start at the root.
- If target < node → go left.
- If target > node → go right.
- If equal → found!

**Time Complexity**:  
- Best/Average: O(log n)  
- Worst (unbalanced): O(n)

---

### ➕ Insert

- Traverse the tree like a search.
- Insert at the first `null` child where the value fits based on comparison.

#### 🕒 Time Complexity

| Case                     | Time Complexity |
|--------------------------|-----------------|
| **Best / Average** (balanced BST) | O(log n)        |
| **Worst** (unbalanced BST)        | O(n)            |

> A balanced BST has height ≈ log n. In the worst case (e.g., inserting sorted data without balancing), the tree becomes skewed like a linked list.

---

### ❌ Delete

Three scenarios:

1. **Leaf node** → Simply remove it.
2. **One child** → Bypass and link the child directly to the parent.
3. **Two children** → Replace the node with:
   - Its **in-order successor** (smallest node in right subtree), or
   - Its **in-order predecessor** (largest node in left subtree).

#### 🕒 Time Complexity

| Case                     | Time Complexity |
|--------------------------|-----------------|
| **Best / Average** (balanced BST) | O(log n)        |
| **Worst** (unbalanced BST)        | O(n)            |

> Deletion involves finding the node and possibly its in-order successor/predecessor, both of which are proportional to the height of the tree.

