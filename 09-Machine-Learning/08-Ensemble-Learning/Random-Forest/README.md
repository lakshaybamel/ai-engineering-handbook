# 🌳 Random Forest

## 📌 Overview

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions to improve accuracy and reduce overfitting.

It is based on:

* Bagging
* Random feature selection

---

## 🧠 Core Idea

> Combine multiple decision trees trained on different data and features to get better predictions

---

## 🔗 Topics Covered

### 1. Intuition

* How Random Forest works
* Bootstrap sampling
* Random feature selection

📄 File: [`intuition.md`](./intuition.md)

---

### 2. Out Of Bag (OOB)

* Internal validation technique
* Uses unused samples for evaluation

📄 File: [`oob.md`](./oob.md)

---

### 3. Implementation

* Train Random Forest model
* Evaluate performance
* Use OOB score
* Analyze feature importance

📓 Notebook: [`random_forest.ipynb`](./random_forest.ipynb)

---

### 4. Comparison with Decision Tree

* Overfitting
* Stability
* Accuracy differences

📄 File: [`comparison_with_dt.md`](./comparison_with_dt.md)

---

## ⚙️ Workflow

```
Input Data
   ↓
Bootstrap Sampling
   ↓
Train Multiple Decision Trees
   ↓
Random Feature Selection
   ↓
Combine Predictions
```

---

## ⚠️ Important Points

* Reduces overfitting compared to Decision Trees
* Works well on complex datasets
* Provides feature importance
* Requires more computation

---

## 🎯 Learning Outcome

After completing this section, the following should be clear:

* How Random Forest improves Decision Trees
* Role of bootstrap sampling and randomness
* What is OOB score
* How to implement Random Forest

---

## 🧠 One-Line Summary

> Random Forest improves decision trees by combining multiple randomized trees to achieve better accuracy and generalization.
