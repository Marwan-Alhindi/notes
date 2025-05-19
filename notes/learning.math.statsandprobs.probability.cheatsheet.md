---
id: lsasdfwtr3mc1mqwaj7dpln
title: Cheatsheet
desc: ''
updated: 1746957120516
created: 1746956889482
---

# 🧠 Basic Probability Concepts – Cheat Sheet

---

## 🔹 1. Experiment
A process or action that leads to one or more outcomes.  
**Example**: Tossing a coin, rolling a die.

---

## 🔹 2. Outcome
A possible result of an experiment.  
**Example**: Getting a 5 when rolling a die.

---

## 🔹 3. Sample Space (S)
The set of all possible outcomes of an experiment.  
**Example**:  
For rolling a die:  
`S = {1, 2, 3, 4, 5, 6}`

---

## 🔹 4. Event (A)
A subset of the sample space. It could be one or more outcomes.  
**Example**:  
Event A = rolling an even number  
`A = {2, 4, 6}`

---

## 🔹 5. Random Variable (X)
A function that assigns a real number to each outcome in the sample space.

- **Discrete Random Variable**: Countable outcomes (e.g., number of heads in 3 coin tosses)  
- **Continuous Random Variable**: Uncountable outcomes (e.g., height, weight)

---

# 📊 Calculating Probability
P(A) = (Number of favorable outcomes) / (Total number of outcomes)

## 🧾 1. **Addition Rule**
- For **mutually exclusive** events A and B:
P(A ∪ B) = P(A) + P(B)
- For **non-mutually exclusive** events:
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

## 🔁 2. **Multiplication Rule**
- For **independent** events:
P(A ∩ B) = P(A) × P(B)
- For **dependent** events:
P(A ∩ B) = P(A) × P(B|A)

## 🎯 3. **Conditional Probability**
The probability of A given that B has occurred:
P(A | B) = P(A ∩ B) / P(B)

## 🧠 4. **Bayes' Theorem**
P(B | A) = [P(A | B) × P(B)] / P(A)

## 🔗 8. **Independence**
Events A and B are independent if:
P(A ∩ B) = P(A) × P(B)

## 🔄 9. **Mutually Exclusive Events**
P(A ∩ B) = 0

## 📈 10. **Permutation and Combination (Counting Laws)**
### 👉 Permutation (Order matters)
P(n, r) = n! / (n − r)!

### 👉 Combination (Order doesn’t matter)
C(n, r) = n! / [r! × (n − r)!]