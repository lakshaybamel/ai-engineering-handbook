# 🌳 Ensemble Learning — Bagging

## 📌 Overview

Bagging (Bootstrap Aggregating) is an ensemble learning technique used to improve model performance by combining multiple models.

---

## 🧠 Core Idea

> Train multiple models on different subsets of data and combine their predictions

---

## 🔷 Why Bagging?

Single models (like Decision Trees) can:

* Overfit
* Be unstable

👉 Bagging reduces:

* variance
* overfitting

---

## 🔷 How It Works

### Step 1: Create Multiple Datasets

* Random sampling with replacement (bootstrap)

### Step 2: Train Models

* Train same model on each dataset

### Step 3: Combine Predictions

* Classification → Majority Voting
* Regression → Averaging

---

## 🔷 Example

```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

model = BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=10
)

model.fit(X_train, y_train)
```

---

## 🔷 Key Concepts

### 1. Bootstrap Sampling

* Random sampling with replacement

### 2. Base Learner

* Usually Decision Tree

### 3. Aggregation

* Combine predictions

---

## 🔷 Advantages

* Reduces overfitting
* Improves stability
* Works well with high-variance models

---

## 🔷 Limitations

* Increased computation
* Less interpretable
* Doesn’t reduce bias

---

## 🎯 When to Use

* Model is overfitting
* Data is unstable
* Decision Trees are used

---

## 🧠 Interview Insight

👉 Question:  
Why does bagging reduce overfitting?

👉 Answer:  
Because it reduces variance by averaging multiple models trained on different data samples.

---

## 🧠 One-Line Summary

> Bagging reduces variance by training multiple models on bootstrapped datasets and combining their predictions.
