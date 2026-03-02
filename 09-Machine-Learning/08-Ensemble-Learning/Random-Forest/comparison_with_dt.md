# ⚖️ Decision Tree vs Random Forest

## 📌 Overview

Decision Tree and Random Forest are both tree-based algorithms, but they differ significantly in performance and behavior.

---

## 🧠 Core Idea

* Decision Tree → Single model
* Random Forest → Multiple trees combined

---

## 🔷 Decision Tree

## 📌 Definition

A Decision Tree splits data recursively based on features to make predictions.

---

## 🔷 Characteristics

* Simple and easy to understand
* Prone to overfitting
* Sensitive to small data changes

---

## 🔷 Example

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
```

---

## 🔷 Random Forest

## 📌 Definition

Random Forest is an ensemble of multiple decision trees trained on different subsets of data.

---

## 🔷 Characteristics

* Combines multiple trees
* Reduces overfitting
* More stable and accurate

---

## 🔷 Example

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)
```

---

# ⚖️ Comparison Table

| Feature          | Decision Tree | Random Forest |
| ---------------- | ------------- | ------------- |
| Model Type       | Single        | Ensemble      |
| Overfitting      | High          | Low           |
| Accuracy         | Moderate      | High          |
| Stability        | Low           | High          |
| Training Time    | Fast          | Slower        |
| Interpretability | High          | Low           |

---

## 🧠 Key Differences

* Decision Tree learns from full dataset → can overfit
* Random Forest uses multiple trees → better generalization

---

## 🔷 When to Use

### Decision Tree

* When interpretability is important
* When dataset is small

### Random Forest

* When accuracy is important
* When dealing with complex data

---

## ⚠️ Important Points

* Random Forest usually outperforms Decision Tree
* Decision Tree is easier to visualize
* Random Forest is more robust

---

## 🧠 Interview Insight

👉 Question:  
Why Random Forest is better than Decision Tree?

👉 Answer:  
Because it combines multiple trees and introduces randomness, reducing overfitting and improving accuracy.

---

## 🧠 One-Line Summary

> Decision Tree is simple but prone to overfitting, while Random Forest improves performance by combining multiple trees.
