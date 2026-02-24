# ⚖️ Regularization

## 📌 Overview

Regularization is a technique used to **prevent overfitting** by controlling model complexity.

In real-world datasets, models can learn:
- actual patterns ✅  
- noise ❌  

👉 Regularization helps the model focus on meaningful patterns.

---

## 🧠 Why Regularization is Needed

When a model becomes too complex:
- It performs well on training data  
- But fails on unseen data  

This is called **overfitting**

👉 Regularization solves this by:
- penalizing large coefficients  
- simplifying the model  

---

## 🔗 Topics Covered

### 1. Overfitting & Underfitting
- Concept of model complexity  
- Bias vs Variance  
- How to detect and fix  

📄 File: [`overfitting_underfitting.md`](./overfitting_underfitting.md)

---

### 2. Lasso, Ridge & ElasticNet
- L1 vs L2 regularization  
- Feature selection using Lasso  
- Combining techniques using ElasticNet  

📄 File: [`lasso_ridge_elasticnet.md`](./lasso_ridge_elasticnet.md)

---

### 3. Lasso Regression (Implementation)
- Applying L1 regularization  
- Feature importance analysis  
- Effect of alpha on model  

📓 Notebook: [`lasso_regression.ipynb`](./lasso_regression.ipynb)

---

### 4. LassoCV (Hyperparameter Tuning)
- Automatic selection of alpha  
- Cross-validation concept  
- Improved model performance  

📓 Notebook: [`lasso_cv.ipynb`](./lasso_cv.ipynb)

---

## ⚙️ Workflow

```
Overfitting Problem
        ↓
Apply Regularization
        ↓
Control Model Complexity
        ↓
Better Generalization
```

---

## 🧠 Key Concepts

- Regularization = penalty on coefficients  
- L1 (Lasso) → feature selection  
- L2 (Ridge) → coefficient shrinkage  
- ElasticNet → combination of L1 + L2  
- Alpha (λ) controls strength of regularization  

---

## 🎯 Learning Outcome

After this section, the following should be clear:

- Difference between overfitting and underfitting  
- How regularization improves model performance  
- When to use Lasso, Ridge, and ElasticNet  
- How to tune hyperparameters using cross-validation  

---

## 🧠 One-Line Summary

> Regularization helps build models that generalize well by reducing overfitting.