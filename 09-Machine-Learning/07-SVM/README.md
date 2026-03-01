# 🧠 Support Vector Machine (SVM)

## 📌 Overview

Support Vector Machine (SVM) is a supervised machine learning algorithm used for:

* Classification
* Regression

It works by finding an optimal boundary that separates data points.

---

## 🔗 Topics Covered

### 1. Intuition

* Hyperplane
* Margin
* Support Vectors

📄 File: [`svm_intuition.md`](./svm_intuition.md)

---

### 2. Hyperparameters

* C (regularization)
* Gamma
* Degree
* Kernel

📄 File: [`hyperparameters.md`](./hyperparameters.md)

---

### 3. Kernels

* Linear
* Polynomial
* RBF
* Sigmoid

📄 File: [`kernels.md`](./kernels.md)

---

### 4. SVM Classifier

* Multi-class classification
* Kernel comparison
* Effect of C

📓 Notebook: [`svm_classifier.ipynb`](./svm_classifier.ipynb)

---

### 5. SVM Regressor (SVR)

* Continuous prediction
* Hyperparameter tuning
* Model evaluation

📓 Notebook: [`svm_regressor.ipynb`](./svm_regressor.ipynb)

---

### 6. GridSearchCV

* Hyperparameter tuning
* Cross-validation
* Best model selection

📓 Notebook: [`gridsearch_cv.ipynb`](./gridsearch_cv.ipynb)

---

### 7. LinearSVR vs SVR

* Comparison of linear vs non-linear regression

📄 File: [`linear_svr_vs_svr.md`](./linear_svr_vs_svr.md)

---

## ⚙️ Workflow

```
Input Data
   ↓
Feature Scaling
   ↓
Choose Kernel
   ↓
Train SVM Model
   ↓
Tune Hyperparameters
   ↓
Evaluate Model
```

---

## ⚠️ Important Points

* Feature scaling is mandatory
* Kernel choice is critical
* Works well for small to medium datasets
* Sensitive to hyperparameters

---

## 🎯 Learning Outcome

After completing this section, the following should be clear:

* How SVM works (intuition)
* Role of kernels
* Importance of hyperparameters
* Difference between SVR and LinearSVR
* How to tune models using GridSearchCV

---

## 🧠 One-Line Summary

> SVM finds an optimal boundary using support vectors and kernels, making it powerful for both classification and regression tasks.
