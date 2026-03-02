# 🧱 Stacking (Stacked Generalization)

## 📌 Overview

Stacking is an advanced ensemble technique where multiple models are combined using a **meta-model** that learns how to best combine their predictions.

---

## 🧠 Core Idea

> Use one model to learn from the predictions of other models

---

## 🔷 How It Works

### Step 1: Train Base Models

* Train multiple models (e.g., Logistic Regression, KNN, Decision Tree)

---

### Step 2: Get Predictions

* Each model makes predictions

👉 These predictions become new features

---

### Step 3: Train Meta Model

* A new model (meta-model) is trained on these predictions

---

### Step 4: Final Prediction

* Meta-model combines predictions to give final output

---

## 🔷 Example (Concept)

```python id="st1"
Base Models:
Model A → 0
Model B → 1
Model C → 1

Meta Model Input → [0, 1, 1]
Meta Model Output → 1
```

---

## 🔷 Why Stacking Works

* Different models capture different patterns
* Meta-model learns how to combine them
* Improves overall performance

---

## 🔷 Components

### 1. Base Models

* First layer models

### 2. Meta Model

* Final model that combines predictions

---

## 🔷 Advantages

* High performance
* Combines strengths of multiple models
* More flexible than voting

---

## 🔷 Limitations

* More complex
* Risk of overfitting
* Requires careful design

---

## 🎯 When to Use

* When multiple models perform well
* When you need better performance than voting
* Advanced ML setups

---

## ⚠️ Important Points

* Meta-model should be simple
* Avoid data leakage (use cross-validation)
* More computation required

---

## 🧠 Interview Insight

👉 Question:  
Difference between Voting and Stacking?

👉 Answer:  
Voting combines predictions directly, while stacking uses a meta-model to learn how to combine predictions.

---

## 🧠 One-Line Summary

> Stacking combines multiple models using a meta-model that learns the best way to combine their predictions.
