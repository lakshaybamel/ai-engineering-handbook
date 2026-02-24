# ⚖️ Overfitting vs Underfitting

## 📌 What is Underfitting?

Underfitting happens when a model is **too simple** and cannot learn patterns from data properly.

👉 It performs **poorly on both training and test data**

---

### 🧠 Intuition

> Model is **not learning enough**

Example:
- Trying to fit a straight line on complex data

---

### 📉 Characteristics

- High training error ❌  
- High testing error ❌  
- Model is too simple  

---

### 🔍 Example

If you predict house prices using only:

```
price = m × area
```

👉 But actual price depends on:
- location
- rooms
- age

➡️ Model will fail → Underfitting

---

## 📌 What is Overfitting?

Overfitting happens when a model **learns too much**, including noise.

👉 It performs:
- **very well on training data**
- **poorly on new (test) data**

---

### 🧠 Intuition

> Model is **memorizing**, not learning

---

### 📈 Characteristics

- Low training error ✅  
- High testing error ❌  
- Model is too complex  

---

### 🔍 Example

Model learns:
- exact data points
- noise
- outliers

➡️ Cannot generalize to new data

---

## 📊 Visual Understanding

### Underfitting:
- Straight line (too simple)

### Good Fit:
- Captures trend properly

### Overfitting:
- Curvy line passing through all points

---

## ⚖️ Key Difference

| Concept        | Underfitting ❌ | Overfitting ❌ |
|----------------|---------------|---------------|
| Model Type     | Too Simple    | Too Complex   |
| Training Error | High          | Low           |
| Testing Error  | High          | High          |
| Learning       | Less          | Too Much      |

---

## 🎯 Ideal Case (Good Fit)

👉 Model should:
- Learn patterns  
- Ignore noise  
- Generalize well  

---

## 🔥 Why This Matters in ML

Because real goal is:

> **Good performance on unseen data**

NOT just training data.

---

## 🛠️ How to Fix Underfitting

- Increase model complexity  
- Add more features  
- Use better algorithm  
- Reduce regularization  

---

## 🛠️ How to Fix Overfitting

- Reduce model complexity  
- Use more data  
- Feature selection  
- Regularization (Lasso, Ridge)  
- Cross-validation  

---

## 🔗 Connection to Regularization

👉 Regularization helps:
- prevent overfitting  
- control model complexity  

We will study:
- Lasso Regression  
- Ridge Regression  
- ElasticNet  

---

## ⚠️ Important Interview Point

> Overfitting = High variance  
> Underfitting = High bias  

---

## 🧠 One-Line Summary

> Underfitting = Model is too simple  
> Overfitting = Model is too complex