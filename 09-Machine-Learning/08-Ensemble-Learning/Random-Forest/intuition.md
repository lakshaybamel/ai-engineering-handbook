# 🌳 Random Forest — Intuition

## 📌 Overview

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions.

It is based on **bagging + randomness**.

---

## 🧠 Core Idea

> Train many decision trees on different data and combine their results

---

## 🔷 Why Random Forest?

Decision Trees:

* Overfit easily ❌
* Are unstable ❌

👉 Random Forest solves this by:

* reducing variance
* improving stability

---

## 🔷 How It Works

### Step 1: Bootstrap Sampling

* Create multiple datasets using sampling with replacement

### Step 2: Train Multiple Trees

* Train a decision tree on each dataset

### Step 3: Random Feature Selection

* At each split, choose random subset of features

### Step 4: Combine Predictions

* Classification → Majority Voting
* Regression → Averaging

---

## 🔷 Key Difference from Bagging

👉 Random Forest adds:

* **Random feature selection**

---

## 🧠 Key Insight

> Not all features are used at every split → increases diversity

---

## 🔷 Example

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
```

---

## 🔷 Why It Works Well

* Reduces overfitting
* Handles large datasets
* Works well with non-linear data

---

## 🔷 Advantages

* High accuracy
* Robust to noise
* Less overfitting than decision trees

---

## 🔷 Limitations

* Slower than single tree
* Less interpretable
* Requires more memory

---

## 🎯 When to Use

* Dataset is complex
* Decision Tree is overfitting
* Need better generalization

---

## ⚖️ Decision Tree vs Random Forest

| Feature     | Decision Tree | Random Forest |
| ----------- | ------------- | ------------- |
| Overfitting | High          | Low           |
| Stability   | Low           | High          |
| Accuracy    | Medium        | High          |

---

## 🧠 Interview Insight

👉 Question:  
Why Random Forest performs better than Decision Tree?

👉 Answer:  
Because it combines multiple trees and introduces randomness, which reduces overfitting and improves generalization.

---

## 🧠 One-Line Summary

> Random Forest improves decision trees by combining multiple randomized trees to reduce overfitting and increase accuracy.
