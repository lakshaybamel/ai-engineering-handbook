# ⚙️ Hyperparameter Tuning

## 📌 What is Hyperparameter Tuning?

Hyperparameter tuning is the process of finding the **best set of parameters** for a machine learning model to improve its performance.

---

## 🧠 Hyperparameters vs Parameters

### 🔷 Parameters
- Learned by the model during training  
- Example:
  - weights in Linear Regression  

---

### 🔷 Hyperparameters
- Set before training  
- Control model behavior  

---

## 📊 Examples

| Model | Hyperparameter |
|------|---------------|
| Lasso | alpha |
| KNN | number of neighbors (k) |
| Logistic Regression | regularization strength |
| Decision Tree | max_depth |

---

## 🎯 Goal

> Find hyperparameters that give the best performance on validation data

---

# 🔷 Why Tuning is Needed?

- Default values may not be optimal  
- Different datasets require different settings  
- Improves model accuracy and generalization  

---

# 🔷 Methods of Hyperparameter Tuning

---

## 1. Grid Search

### 📌 Concept

Try all possible combinations of parameters

---

### 🔷 Example

```python
from sklearn.model_selection import GridSearchCV

params = {
    "alpha": [0.01, 0.1, 1, 10]
}

grid = GridSearchCV(model, params, cv=5)
grid.fit(X_train, y_train)

print("Best Params:", grid.best_params_)
```

---

## 2. Random Search

### 📌 Concept

Try random combinations instead of all

### 🧠 Advantage

- Faster than Grid Search
- Works well for large parameter space

---
 
## 🔷 Connection with Cross Validation

👉 Both methods use:

- Cross-validation internally

➡️ Gives reliable performance

---

## 🔷 Output of Tuning

- Best parameters
- Best score
- Improved model

---

## ⚠️ Important Points

- Tuning improves performance but increases computation
- Always use validation or cross-validation
- Avoid tuning on test data

---

## 🧠 Interview Insight

👉 **Question:**<br>
What is hyperparameter tuning?

👉 **Answer:**<br>
It is the process of selecting the best set of hyperparameters to improve model performance using techniques like GridSearchCV.

---

## 🧠 One-Line Summary

> Hyperparameter tuning finds the best model settings to improve performance and generalization.