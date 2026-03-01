# 🧠 Kernels in SVM

## 📌 Overview

Kernels are used in SVM to handle **non-linear data**.

They allow SVM to create complex decision boundaries without explicitly transforming data.

---

## 🧠 Core Idea

> Map data to a higher dimension where it becomes linearly separable

---

## 🔷 Why Kernels are Needed?

Sometimes data cannot be separated using a straight line.

👉 Example:

* Circular data
* Complex patterns

---

## ❌ Without Kernel

* Cannot separate non-linear data

---

## ✅ With Kernel

* Data becomes separable in higher dimension

---

## 🔷 Kernel Trick

Instead of transforming data manually:

👉 SVM uses a **kernel function**

👉 It computes similarity directly in higher dimension

---

## 🎯 Key Benefit

* Avoids expensive computations
* Makes SVM efficient

---

# 🔷 Common Kernel Types

---

## 1. Linear Kernel

## 📌 Definition

No transformation — works on original data.

---

## 🧠 Use When

* Data is linearly separable
* Large datasets

---

## 📐 Formula

```
K(x, y) = x · y
```

---

## 🔷 2. Polynomial Kernel

## 📌 Definition

Creates curved decision boundaries using polynomial functions.

---

## 🧠 Use When

* Data has polynomial relationship

---

## 📐 Formula

```
K(x, y) = (x · y + c)^d
```

Where:

* d = degree

---

## 🔷 3. RBF Kernel (Most Important)

## 📌 Definition

Radial Basis Function maps data into infinite dimensions.

---

## 🧠 Intuition

* Measures similarity based on distance

---

## 📐 Formula

```
K(x, y) = exp(-γ ||x - y||²)
```

---

## 🎯 Use When

* Data is complex
* Non-linear separation required

👉 Default and most commonly used

---

## 🔷 4. Sigmoid Kernel (Less Used)

## 📌 Definition

Works similar to neural networks.

---

## 🧠 Use When

* Rarely used in practice

---

# ⚖️ Kernel Comparison

| Kernel     | Use Case                 |
| ---------- | ------------------------ |
| Linear     | Simple, large datasets   |
| Polynomial | Curved relationships     |
| RBF        | Complex, non-linear data |
| Sigmoid    | Rare usage               |

---

# ⚠️ Important Points

* Kernel choice affects performance
* RBF is default in most cases
* Requires hyperparameter tuning

---

## 🧠 Interview Insight

👉 Question:  
What is the kernel trick?

👉 Answer:  
It allows SVM to operate in higher dimensions without explicitly transforming data.

---

## 🧠 One-Line Summary

> Kernels allow SVM to handle non-linear data by mapping it into higher dimensions using the kernel trick.
