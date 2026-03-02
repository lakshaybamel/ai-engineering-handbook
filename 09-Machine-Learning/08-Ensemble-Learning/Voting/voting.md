# 🗳️ Voting (Ensemble Method)

## 📌 Overview

Voting is an ensemble technique where multiple models are trained independently, and their predictions are combined to make a final decision.

---

## 🧠 Core Idea

> Combine predictions of multiple models to improve overall performance

---

## 🔷 Types of Voting

### 1. Hard Voting

* Uses majority voting
* Final prediction = most common class

👉 Example:

```python
Model A → 1  
Model B → 0  
Model C → 1  

Final → 1 (majority)
```

---

### 2. Soft Voting

* Uses probability scores
* Final prediction = highest average probability

👉 Example:

```python
Model A → [0.2, 0.8]  
Model B → [0.3, 0.7]  
Model C → [0.4, 0.6]  

Average → [0.3, 0.7] → Class 1
```

---

## 🔷 How It Works

1. Train multiple models (e.g., Logistic Regression, KNN, Decision Tree)
2. Each model makes predictions
3. Combine predictions using voting
4. Output final result

---

## 🔷 Why Voting Works

* Different models learn different patterns
* Combining them reduces individual errors
* Improves generalization

---

## 🔷 Advantages

* Simple to implement
* Improves accuracy
* Reduces model bias

---

## 🔷 Limitations

* Requires multiple models
* Can be slow
* Not effective if all models are similar

---

## 🎯 When to Use

* When multiple models perform reasonably well
* When you want quick ensemble improvement
* When models are diverse

---

## ⚠️ Important Points

* Soft voting usually performs better than hard voting
* Models should be different (diversity is important)
* Requires probability outputs for soft voting

---

## 🧠 Interview Insight

👉 Question:  
Difference between hard voting and soft voting?

👉 Answer:  
Hard voting uses majority class prediction, while soft voting uses average probabilities to decide the final class.

---

## 🧠 One-Line Summary

> Voting combines predictions of multiple models to improve accuracy and robustness.
