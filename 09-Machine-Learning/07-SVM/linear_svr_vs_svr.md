# ⚖️ LinearSVR vs SVR

## 📌 Overview

Both **LinearSVR** and **SVR** are used for regression tasks in Support Vector Machines.

👉 The key difference lies in:

* how they model relationships
* how they handle data complexity

---

## 🔷 1. SVR (Support Vector Regressor)

## 📌 Definition

SVR is a flexible regression model that can handle **non-linear relationships** using kernels.

---

## 🧠 Key Idea

> Uses kernel trick to model complex patterns

---

## 🔷 Features

* Supports kernels (RBF, polynomial, etc.)
* Can model non-linear data
* More powerful but slower

---

## 🔷 Example

```python
from sklearn.svm import SVR

model = SVR(kernel='rbf')
model.fit(X_train, y_train)
```

---

## 🔷 When to Use

* Data is non-linear
* Complex relationships exist
* Small to medium datasets

---

---

## 🔷 2. LinearSVR

## 📌 Definition

LinearSVR is a simplified version of SVR that assumes a **linear relationship** between features and target.

---

## 🧠 Key Idea

> Works like linear regression but with SVM principles

---

## 🔷 Features

* No kernel support
* Faster training
* Works well for large datasets

---

## 🔷 Example

```python
from sklearn.svm import LinearSVR

model = LinearSVR()
model.fit(X_train, y_train)
```

---

## 🔷 When to Use

* Data is linearly separable
* Large datasets
* Faster training required

---

# ⚖️ Comparison Table

| Feature      | SVR          | LinearSVR |
| ------------ | ------------ | --------- |
| Relationship | Non-linear   | Linear    |
| Kernel       | Yes          | No        |
| Speed        | Slower       | Faster    |
| Complexity   | High         | Low       |
| Dataset Size | Small/Medium | Large     |

---

# 🧠 Key Differences

* SVR → flexible but computationally expensive
* LinearSVR → simple and fast

---

# ⚠️ Important Points

* Both require feature scaling
* SVR gives better accuracy for complex data
* LinearSVR is efficient for large datasets

---

## 🧠 Interview Insight

👉 Question:  
Difference between SVR and LinearSVR?

👉 Answer:  
SVR supports kernels and handles non-linear data, while LinearSVR is faster and works only with linear relationships.

---

## 🧠 One-Line Summary

> SVR handles complex non-linear data using kernels, while LinearSVR is a faster linear version for large datasets.
