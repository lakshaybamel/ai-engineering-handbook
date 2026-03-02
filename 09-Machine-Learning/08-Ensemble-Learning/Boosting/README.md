# 🚀 Boosting

## 📌 Overview

Boosting is an ensemble learning technique where models are trained **sequentially**, and each new model focuses on correcting the errors of previous ones.

---

## 🧠 Core Idea

> Learn from mistakes and improve step-by-step

---

## 🔗 Topics Covered

### 1. Gradient Boosting

* Sequential learning using residuals
* Uses gradient descent to reduce error

📄 Files:

* [`Gradient-Boosting/intuition.md`](./Gradient-Boosting/intuition.md)
* [`Gradient-Boosting/gb_regressor.ipynb`](./Gradient-Boosting/gb_regressor.ipynb)
* [`Gradient-Boosting/gb_classifier.ipynb`](./Gradient-Boosting/gb_classifier.ipynb)

---

### 2. AdaBoost

* Focuses on misclassified data points
* Adjusts weights of samples

📄 Files:

* [`AdaBoost/intuition.md`](./AdaBoost/intuition.md)
* [`AdaBoost/adaboost.ipynb`](./AdaBoost/adaboost.ipynb)

---

### 3. XGBoost

* Optimized version of Gradient Boosting
* Faster and more regularized

📄 Files:

* [`XGBoost/intuition.md`](./XGBoost/intuition.md)
* [`XGBoost/xgboost.ipynb`](./XGBoost/xgboost.ipynb)

---

## ⚙️ Workflow

```text
Initial Model
   ↓
Calculate Errors
   ↓
Train Next Model on Errors
   ↓
Update Predictions
   ↓
Repeat
```

---

## 🔷 Key Characteristics

* Models are trained sequentially
* Each model corrects previous mistakes
* Focus on reducing bias

---

## ⚠️ Important Points

* More powerful than bagging in many cases
* Sensitive to noise
* Requires tuning

---

## 🎯 Learning Outcome

After completing this section:

* Understand sequential learning
* Know difference between boosting algorithms
* Implement Gradient Boosting, AdaBoost, and XGBoost

---

## 🧠 One-Line Summary

> Boosting builds models sequentially, where each model learns from previous errors to improve performance.
