# ⚡ AdaBoost — Intuition

## 📌 Overview

AdaBoost (Adaptive Boosting) is an ensemble learning algorithm that builds models **sequentially**, focusing more on **misclassified data points**.

---

## 🧠 Core Idea

> Give more importance to mistakes and improve them step-by-step

---

## 🔷 How It Works

### Step 1: Assign Equal Weights

* Initially, all data points have equal importance

---

### Step 2: Train First Model

* A weak learner (usually a small decision tree) is trained

---

### Step 3: Identify Mistakes

* Check which points are misclassified

---

### Step 4: Increase Weights of Errors

* Misclassified points get higher weight
* Correct ones get lower weight

---

### Step 5: Train Next Model

* Focuses more on difficult (misclassified) points

---

### Step 6: Repeat

* Continue improving step-by-step

---

### Step 7: Final Prediction

* Combine all models using **weighted voting**

---

## 🧠 Key Insight

> Hard examples get more attention in each iteration

---

## 🔷 Why "Adaptive"?

Because the model **adapts** by changing weights based on errors.

---

## 🔷 Example (Concept)

```python id="ab1"
Model 1 → mistakes
Increase weights of mistakes
Model 2 → focuses on those mistakes
Repeat → better model
```

---

## 🔷 Important Components

### 1. Weak Learner

* Usually a decision stump (depth = 1 tree)

### 2. Weights

* Control importance of data points

### 3. Learning Rate

* Controls contribution of each model

---

## 🔷 Advantages

* Improves weak models
* Works well for classification
* Simple and effective

---

## 🔷 Limitations

* Sensitive to noise and outliers
* Can overfit noisy data
* Sequential → slower

---

## 🎯 When to Use

* Dataset is clean
* Need to improve weak models
* Classification tasks

---

## ⚠️ Important Points

* Works best with simple models
* Misclassified points dominate learning
* Noise can affect performance

---

## 🧠 Interview Insight

👉 Question:  
How does AdaBoost work?

👉 Answer:  
AdaBoost trains models sequentially and increases the weight of misclassified data points so that future models focus on correcting those errors.

---

## 🧠 One-Line Summary

> AdaBoost improves performance by giving more importance to misclassified points and learning from mistakes iteratively.
