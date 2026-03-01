# ⚙️ SVM Hyperparameters

## 📌 Overview

Hyperparameters control how the SVM model learns and performs.

They directly affect:

* model complexity
* decision boundary
* overfitting vs underfitting

---

## 🔷 1. C (Regularization Parameter)

## 📌 Definition

C controls the trade-off between:

* maximizing margin
* minimizing classification error

---

## 🧠 Intuition

* Small C → allow some errors → wider margin
* Large C → fewer errors → narrow margin

---

## 📊 Behavior

| C Value | Effect                              |
| ------- | ----------------------------------- |
| Small C | More margin, more errors (underfit) |
| Large C | Less margin, fewer errors (overfit) |

---

## 🎯 Key Idea

> C controls how strict the model is

---

## 🔷 2. Kernel

## 📌 Definition

Kernel defines how data is transformed to make it separable.

---

## 🧠 Common Kernels

* Linear
* Polynomial
* RBF (Radial Basis Function)

---

## 🎯 Key Idea

> Kernel helps handle non-linear data

---

## 🔷 3. Gamma (γ)

## 📌 Definition

Gamma controls how far the influence of a single data point reaches.

---

## 🧠 Intuition

* Low gamma → far reach → smooth boundary
* High gamma → close reach → complex boundary

---

## 📊 Behavior

| Gamma | Effect                   |
| ----- | ------------------------ |
| Low   | Smooth decision boundary |
| High  | Complex, wiggly boundary |

---

## ⚠️ Important

* High gamma → overfitting
* Low gamma → underfitting

---

## 🔷 4. Degree (For Polynomial Kernel)

## 📌 Definition

Degree defines complexity of polynomial decision boundary.

---

## 🧠 Intuition

* Higher degree → more complex boundary
* Lower degree → simpler boundary

---

## 🔷 5. Epsilon (For Regression - SVR)

## 📌 Definition

Epsilon defines a margin where no penalty is given to errors.

---

## 🧠 Intuition

* Larger epsilon → fewer support vectors
* Smaller epsilon → more precise fitting

---

## ⚖️ Summary Table

| Parameter | Role                          |
| --------- | ----------------------------- |
| C         | Controls margin vs error      |
| Kernel    | Handles non-linearity         |
| Gamma     | Controls influence of points  |
| Degree    | Complexity of polynomial      |
| Epsilon   | Error tolerance in regression |

---

## ⚠️ Important Points

* Proper tuning is critical
* Wrong values → poor performance
* Use GridSearchCV for tuning

---

## 🧠 Interview Insight

👉 Question:  
What is the role of C in SVM?

👉 Answer:  
C controls the trade-off between margin size and classification error.

---

## 🧠 One-Line Summary

> SVM hyperparameters control model complexity, margin, and decision boundary behavior.
