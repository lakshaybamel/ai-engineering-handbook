# 🧠 Regularization: Lasso, Ridge & ElasticNet

## 📌 Why Regularization?

Regularization is used to **prevent overfitting**.

👉 It controls how complex a model can become.

---

### 🧠 Intuition

> Penalize large coefficients so model stays simple

Instead of letting model freely learn:

```
y = w1x1 + w2x2 + w3x3 + ...
```

👉 We add a **penalty** to keep weights small.

---

## ⚖️ General Idea

Modified loss function:

```
Loss = Error + Penalty
```

👉 Penalty controls model complexity.

---

# 🔷 Ridge Regression (L2 Regularization)

## 📌 Concept

Adds penalty as **square of coefficients**

```
Penalty = λ (w1² + w2² + w3² + ...)
```

---

## 🧠 Intuition

- Reduces size of coefficients  
- Keeps all features  
- Does NOT make coefficients zero  

---

## 📊 Key Points

- Prevents overfitting  
- Works well when all features are useful  
- Handles multicollinearity  

---

## 🎯 When to Use?

👉 When:
- all features matter  
- you don’t want feature elimination  

---

# 🔶 Lasso Regression (L1 Regularization)

## 📌 Concept

Adds penalty as **absolute value of coefficients**

```
Penalty = λ (|w1| + |w2| + |w3| + ...)
```

---

## 🧠 Intuition

- Shrinks some coefficients to **zero**  
- Automatically does **feature selection**  

---

## 📊 Key Points

- Can remove irrelevant features  
- Produces sparse model  
- Helps in simpler interpretation  

---

## 🎯 When to Use?

👉 When:
- many features  
- some features are useless  
- need feature selection  

---

# 🔷 ElasticNet (L1 + L2)

## 📌 Concept

Combination of Lasso + Ridge

```
Penalty = λ1 (|w|) + λ2 (w²)
```

---

## 🧠 Intuition

> Balance between:
- feature selection (Lasso)
- stability (Ridge)

---

## 📊 Key Points

- Handles correlated features better than Lasso  
- More flexible  
- Combines strengths of both  

---

# ⚖️ Comparison Table

| Feature            | Ridge (L2) | Lasso (L1) | ElasticNet |
|--------------------|-----------|-----------|-----------|
| Shrinks coefficients | ✅        | ✅        | ✅        |
| Makes coefficients zero | ❌     | ✅        | ✅        |
| Feature selection   | ❌        | ✅        | ✅        |
| Handles multicollinearity | ✅ | ⚠️        | ✅        |

---

# 📉 Effect on Model

- Without regularization → Overfitting  
- With regularization → Better generalization  

---

# 🔥 Role of λ (Lambda)

- Controls strength of regularization  

👉 If λ is:
- 0 → no regularization  
- very high → model too simple (underfit)

---

# 🧠 Visual Intuition

- Ridge → shrinks weights smoothly  
- Lasso → forces some weights to 0  

---

# ⚠️ Important Interview Points

- L1 = feature selection  
- L2 = coefficient shrinkage  
- ElasticNet = combination  

👉 Most common question:
> Why Lasso gives sparse model?

Answer:
👉 Because L1 penalty can make coefficients exactly zero

---

## 🔗 Practical Implementation

- Lasso Regression can be implemented using `sklearn.linear_model.Lasso`
- `LassoCV` helps in automatic selection of optimal lambda (α)

👉 Further exploration:
- Ridge Regression
- ElasticNet
---

# 🧠 One-Line Summary

> Regularization = Adding penalty to control model complexity and prevent overfitting