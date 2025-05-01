---
id: c17ga9ds170g6wd0xeh6ukl
title: TimeComplexity
desc: ''
updated: 1746091096887
created: 1745757915374
---

## 🟢 1. What is Time Complexity?

Time complexity describes **how the runtime of an algorithm grows** with respect to the **input size `n`**.

It helps answer:
> “If I double the input, how much slower does the algorithm get?”

---

## 🟢 2. Big-O Notation

**Big-O** gives an **upper bound** on growth rate (worst case). It helps compare algorithms **independent of hardware or language**.

### Examples:
- `O(1)` → Constant time
- `O(n)` → Linear
- `O(n²)` → Quadratic

---

## 🟢 3. Why Do We Use Limits?

We use **limits** to analyze how the algorithm behaves **as input size n → ∞**, ignoring constants and lower-order terms.

### Example:
If `T(n) = 5n² + 100n + 200`, then as `n` gets large:  
→ **O(n²)** because the `n²` term dominates.

---

## 🟢 4. Steps to Calculate Time Complexity of a Code

1. Identify the **input size** `n`
2. Count operations that depend on `n`
3. Focus on **loops**, **recursion**, and **function calls**
4. Drop constants and keep the dominant term

### Example:
```python
for i in range(n):
    for j in range(n):
        print(i, j)

## 🟢 5. Best, Worst, and Average Case

When analyzing algorithms, always consider:

- **Best Case (Ω)**: The fastest possible scenario.
- **Worst Case (O)**: The slowest, most costly scenario.
- **Average Case (Θ)**: The expected time across all inputs.

### Example: Linear Search
- **Best Case**: O(1) → Item is at the first index.
- **Worst Case**: O(n) → Item is at the end or not present.
- **Average Case**: O(n) → On average, you check half the array.


## 🟢 6. Common Order of Growth Rates

These are ordered from **fastest (best)** to **slowest (worst)** in terms of how they scale with input size:

| Big-O       | Name                | Behavior                             |
|-------------|---------------------|--------------------------------------|
| O(1)        | Constant            | Independent of input size            |
| O(log log n)| Double-logarithmic  | Extremely slow growth                |
| O(log n)    | Logarithmic         | Input cut in half each step          |
| O(n)        | Linear              | Grows directly with input size       |
| O(n log n)  | Quasilinear         | Seen in efficient sorting algorithms |
| O(n²)       | Quadratic           | Double nested loops                  |
| O(n³)       | Cubic               | Triple nested loops                  |
| O(2ⁿ)       | Exponential         | Doubles each time → grows very fast  |

✅ **Lower is better** for performance and scalability.

## 🟢 7. What Do Logarithms Have to Do With Algorithms?

Logarithms appear in algorithms that **divide the problem size** by a factor (usually 2) at each step.

### Common scenarios:
- **Binary Search**: O(log n)
- **Balanced Binary Trees**: Height is log n
- **Heap Operations**: Insert/delete is O(log n)

This is why **logarithmic algorithms are extremely efficient**.

## 🟡 8. Space-Time Trade-Off

> Use **more memory to reduce computation time**, or use less memory and accept longer runtimes.

### Example:
- **Memoization**: Stores results of expensive function calls → saves time at the cost of space.
- **Hash tables**: Fast lookup (O(1)), but may use more memory than a sorted list.

Choosing the right balance depends on:
- Memory constraints
- Real-time performance requirements


## 🟡 9. Recursion and Time Complexity

To analyze recursive algorithms, you often need to:
- Write a **recurrence relation**
- Solve using:
  - **Recursion trees**
  - **Substitution method**
  - **Master Theorem**

### Example: Merge Sort
T(n) = 2T(n/2) + O(n) → O(n log n)