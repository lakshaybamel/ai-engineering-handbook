# 📊 Evaluation Metrics (Regression)

Evaluation metrics are used to measure **how well our model is performing**.

👉 They tell us:
> "How good are our predictions?"

---

## 📌 Why Do We Need Evaluation Metrics?

- To check model accuracy  
- To compare different models  
- To improve performance  

---

## 📊 1. Mean Absolute Error (MAE)

### 🔹 Definition

Average of absolute differences between actual and predicted values.

```
MAE = (1/n) * Σ |actual - predicted|
```

---

### 🧠 Intuition

👉 Measures average error (no direction)

- Easy to understand  
- Less sensitive to outliers  

---

## 📊 2. Mean Squared Error (MSE)

### 🔹 Definition

Average of squared differences between actual and predicted values.

```
MSE = (1/n) * Σ (actual - predicted)^2
```

---

### 🧠 Intuition

- Penalizes large errors more  
- Sensitive to outliers  

---

## 📊 3. Root Mean Squared Error (RMSE)

### 🔹 Definition

Square root of MSE:

```
RMSE = √MSE
```

---

### 🧠 Intuition

- Same unit as target variable  
- Easier to interpret than MSE  

---

## 📊 4. R² Score (Coefficient of Determination)

### 🔹 Definition

Measures how well the model explains variance in data.

```
R² = 1 - (SS_res / SS_total)
```

---

### 🧠 Intuition

- R² = 1 → perfect model  
- R² = 0 → no learning  
- R² < 0 → worse than average  

---

## 🔁 Comparison

| Metric | Meaning | Sensitive to Outliers |
|--------|--------|----------------------|
| MAE    | Average error | ❌ Low |
| MSE    | Squared error | ✅ High |
| RMSE   | Scaled MSE    | ✅ High |
| R²     | Model fit     | ❌ Low |

---

## 🎯 When to Use What?

- Use **MAE** → when you want simple interpretation  
- Use **MSE/RMSE** → when large errors matter  
- Use **R²** → to measure overall model performance  

---

## 🔗 Connection to Linear Regression

- These metrics evaluate:
  👉 how good your best fit line is  

---

## ⚠️ Key Points

- No single metric is perfect  
- Always compare multiple metrics  
- Choose based on problem  

---

## 🧠 One-Line Summary

> Evaluation metrics measure how accurate and reliable a machine learning model is.