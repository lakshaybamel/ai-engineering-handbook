# 📏 Normalization (Min-Max Scaling)

## 📌 What is Normalization?

Normalization is a feature scaling technique that transforms data into a **fixed range**, usually:

```
0 to 1
```

---

## 📐 Formula

```
x' = (x - min) / (max - min)
```

Where:
- `x` = original value  
- `min` = minimum value of feature  
- `max` = maximum value of feature  

---

## 🧠 Intuition

- Scales all values between 0 and 1  
- Preserves relative differences  
- Makes features comparable  

---

## 📊 Example

| Value      | Normalized |
|------------|------------|
| 10         | 0.0        |
| 20         | 0.5        |
| 30         | 1.0        |

---

## 🔷 Implementation (sklearn)

```python 
id="norm-code-1"
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## ⚠️ Important Rule

👉 Always:  
- Fit on training data  
- Transform both train and test  

---

## 🧠 Why?

- To prevent data leakage  

---

## ⚖️ Normalization vs Standardization

| Feature   | Normalization | Standardization          |
|-----------|---------------|--------------------------|
| Range     | 0 to 1        | Mean = 0, Std = 1        |
| Formula   | Min-Max       | Z-score                  |
| Outliers  | Sensitive ❌   | Less sensitive ✅         |
| Use Case  | Bounded data  | General purpose           |

---

## 🔷 When to Use Normalization?

- When data has known bounds  
- When using:  
  - Neural Networks  
  - Distance-based models (KNN)  

---

## ⚠️ When NOT to Use?

- When data has many outliers  
- When distribution matters  

---

## 🔗 Connection to Scaling

- Both are feature scaling techniques  
- Choice depends on:  
  - Data distribution  
  - Algorithm  

---

## 🧠 Interview Insight

👉 **Question:**<br>
Difference between normalization and standardization?  

👉 **Answer:**<br>
Normalization scales data to a fixed range (0–1), while standardization centers data around mean 0 with unit variance.  

---

## 🧠 One-Line Summary

>Normalization scales features to a fixed range (usually 0–1) using min-max transformation.