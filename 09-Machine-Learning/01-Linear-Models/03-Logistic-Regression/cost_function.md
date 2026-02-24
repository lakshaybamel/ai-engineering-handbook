# 📉 Logistic Regression — Cost Function

## 📌 Why Do We Need a Cost Function?

The cost function measures:

> ❓ How wrong the model predictions are

👉 Goal:
- Minimize error  
- Improve predictions  

---

## ⚠️ Problem with Linear Regression Cost Function

Linear Regression uses:

```
Mean Squared Error (MSE)
```

👉 But MSE is NOT suitable for Logistic Regression because:

- Sigmoid function is non-linear  
- MSE creates a **non-convex curve**  
- Leads to multiple local minima  

➡️ Optimization becomes difficult  

---

## ✅ Solution: Log Loss (Binary Cross Entropy)

Logistic Regression uses:

> **Log Loss (Binary Cross Entropy)**

---

## 📐 Formula

```
Cost = - [ y log(p) + (1 - y) log(1 - p) ]
```

Where:
- `y` = actual value (0 or 1)  
- `p` = predicted probability  

---

## 🧠 Intuition

### Case 1: Correct Prediction

- If y = 1 and p ≈ 1  
👉 log(p) → close to 0  
👉 loss → very small ✅  

---

### Case 2: Wrong Prediction

- If y = 1 and p ≈ 0  
👉 log(p) → very large negative  
👉 loss → very large ❌  

---

👉 So:

> **Wrong confident predictions are heavily penalized**

---

## 📊 Behavior Summary

| Prediction | Actual | Loss |
|-----------|--------|------|
| 0.9 | 1 | Low |
| 0.1 | 1 | High |
| 0.8 | 0 | High |
| 0.2 | 0 | Low |

---

## 📈 Why Log Loss Works Well

- Produces **convex curve**  
- Easier optimization  
- Strong penalty for wrong predictions  

---

## 🔁 Final Cost (Over Dataset)

For all data points:

```
Total Cost = Average of individual losses
```

---

## ⚙️ Optimization

👉 Goal:
Minimize cost using:

- Gradient Descent  

---

## 🔗 Connection to Gradient Descent

```
Cost Function → Compute Error
        ↓
Gradient Descent → Update Weights
        ↓
Better Predictions
```

---

## ⚠️ Important Points

- MSE is NOT used in Logistic Regression  
- Log Loss is standard  
- Output must be probability (0–1)  

---

## 🧠 Interview Insight

👉 Question:
Why not use MSE in Logistic Regression?

👉 Answer:
Because it creates a non-convex loss surface, making optimization difficult. Log Loss provides a convex function which is easier to minimize.

---

## 🧠 One-Line Summary

> Logistic Regression uses Log Loss to penalize wrong predictions and optimize classification performance.