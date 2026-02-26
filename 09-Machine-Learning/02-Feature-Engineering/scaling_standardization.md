# 📏 Feature Scaling & Standardization

## 📌 What is Feature Scaling?

Feature Scaling is the process of bringing all features to a **similar scale** so that no feature dominates others.

---

## 🧠 Why Scaling is Needed?

Example:

| Feature | Value   |
|---------|---------|
| Age     | 25      |
| Salary  | 500000  |

👉 Salary dominates due to large magnitude

➡️ Model gives more importance to it

---

## ⚠️ Problem Without Scaling

- Slower convergence  
- Poor performance  
- Biased learning  

---

## 🔷 When is Scaling Required?

- Logistic Regression  
- KNN  
- SVM  
- Gradient Descent based models  

---

## 🔷 When Scaling is NOT Required?

- Decision Trees  
- Random Forest  

---

# 🔷 Standardization (Z-score Scaling)

## 📌 Concept

Transforms data to have:
- Mean = 0  
- Standard Deviation = 1  

---

## 📐 Formula

```
z = (x - mean) / std
```

---

## 🧠 Intuition

- Centers data around 0  
- Maintains distribution shape  
- Handles outliers better than normalization  

---

## 🔷 Implementation (sklearn)

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

## ⚠️ Important Rule

👉 Always:  
- Fit on training data  
- Transform both train and test  

---

## 🧠 Why?

- To avoid data leakage  

---

## 🔷 Feature Scaling vs Standardization

| Feature        | Feature Scaling        | Standardization            |
|----------------|------------------------|----------------------------|
| Goal           | Scale values           | Normalize distribution     |
| Range          | Depends                | Mean = 0, Std = 1          |
| Outliers       | Sensitive              | Less sensitive             |

---

## ⚠️ Common Mistake

❌ Scaling before train-test split  
👉 Leads to data leakage  

---

## 🔗 Connection to Your Models

- Logistic Regression → sensitive to scale  
- KNN → distance-based (very sensitive)  
- SVM → highly sensitive  

---

## 🧠 Interview Insight

👉 **Question:**<br>
Why is scaling important?  

👉 **Answer:**<br>
Because features with larger values can dominate the model, leading to biased learning.  

---

## 🧠 One-Line Summary

> Feature scaling ensures all features contribute equally by bringing them to a similar scale.