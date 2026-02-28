# 🌳 Pruning in Decision Trees

## 📌 Overview

Pruning is the process of **reducing the size of a decision tree** to:

- avoid overfitting  
- improve generalization  

---

## 🧠 Why Pruning is Needed?

Decision Trees tend to:

- grow very deep  
- memorize training data  

👉 This leads to **overfitting**

---

## 🔗 Connection

- Deep tree → high variance  
- Pruning → reduces variance  

---

# 🔷 Types of Pruning

---

## 1. Pre-Pruning (Early Stopping)

## 📌 Concept

Stop tree growth **before it becomes too complex**

---

## 🧠 Conditions to Stop

- Maximum depth reached  
- Minimum samples required for split  
- Minimum samples in leaf  
- Minimum impurity decrease  

---

## 🔷 Example (sklearn)

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5
)
```

---

## 🎯 Advantage

- Faster training
- Prevents very deep trees

---

## ⚠️ Limitation

- May stop too early → underfitting

---

## 2. Post-Pruning (Cost Complexity Pruning)

## 📌 Concept

- First grow full tree
- Then remove unnecessary branches

---

## 🧠 Idea

Remove nodes that do not improve performance

---

## 🔷 Implementation (sklearn)

```python
model = DecisionTreeClassifier(ccp_alpha=0.01)
```

---

## 🎯 Advantage

- More accurate than pre-pruning
- Better control over overfitting

---

## ⚠️ Limitation

- More computational cost

---

## 🔷 Common Pruning Rules

- Remove nodes with low information gain  
- Remove nodes that do not improve validation performance  
- Reduce tree depth  

## ⚖️ Pre-Pruning vs Post-Pruning

| Feature        | Pre-Pruning          | Post-Pruning       |
|----------------|----------------------|--------------------|
| When applied   | Before full growth   | After full growth  |
| Speed          | Faster               | Slower             |
| Risk           | Underfitting         | Better control     |

## 🎯 Goal of Pruning

Balance between:
- model complexity  
- generalization  

## ⚠️ Important Points

- Pruning reduces overfitting  
- Improves performance on unseen data  
- Important for decision trees  

## 🧠 Interview Insight

👉 **Question:**  
Why do we use pruning in decision trees?  

👉 **Answer:**  
To reduce overfitting by limiting tree complexity and improving generalization.  

## 🧠 One-Line Summary

> Pruning controls decision tree complexity to reduce overfitting and improve generalization.