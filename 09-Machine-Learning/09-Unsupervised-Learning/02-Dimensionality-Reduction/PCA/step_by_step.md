# 🧮 PCA — Step by Step

## 📌 Overview

This file explains **how PCA works mathematically step-by-step**.

👉 Understanding this = strong conceptual clarity

---

## 🧠 Core Idea

> Transform data into new axes where variance is maximum

---

# 🔷 Step 1: Standardize the Data

## 📌 Why?

* Features may have different scales
* PCA is sensitive to scale

---

## 🔷 Formula

```text
X_scaled = (X - mean) / standard_deviation
```

---

## 📌 Result

* Mean = 0
* Variance = 1

---

# 🔷 Step 2: Compute Covariance Matrix

## 📌 What is Covariance?

* Measures how two features vary together

---

## 📌 Covariance Matrix

For dataset with features:

```text
[ X1, X2, X3 ]
```

Matrix looks like:

```text
| Var(X1)   Cov(X1,X2)  Cov(X1,X3) |
| Cov(X2,X1) Var(X2)    Cov(X2,X3) |
| Cov(X3,X1) Cov(X3,X2) Var(X3)    |
```

---

## 📌 Meaning

* Diagonal → variance
* Off-diagonal → relationship between features

---

# 🔷 Step 3: Compute Eigenvalues & Eigenvectors

## 📌 Why?

👉 These define:

* Directions (eigenvectors)
* Importance (eigenvalues)

---

## 🔷 Key Idea

* Eigenvectors → directions of new axes
* Eigenvalues → amount of variance

---

## 📌 Example

```text
Eigenvector → direction  
Eigenvalue → importance of that direction  
```

---

# 🔷 Step 4: Sort Eigenvalues

## 📌 Why?

👉 To select most important components

---

## 🔷 Process

* Sort eigenvalues in descending order
* Select top K values

---

## 📌 Result

* Top components = maximum variance

---

# 🔷 Step 5: Select Principal Components

## 📌 Choose K components

Example:

* Original features = 10
* Choose K = 2

👉 Reduce to 2D

---

## 📌 Criteria

* Explained variance
* Use cumulative variance (e.g., 95%)

---

# 🔷 Step 6: Transform Data

## 📌 Final Step

Project data onto selected components

---

## 🔷 Formula (Conceptual)

```text
X_reduced = X_scaled × Eigenvectors
```

---

## 📌 Result

* Reduced dataset
* Fewer features
* Maximum information preserved

---

# 🔁 Full Workflow

```text
Original Data
   ↓
Standardize Data
   ↓
Compute Covariance Matrix
   ↓
Find Eigenvalues & Eigenvectors
   ↓
Sort Eigenvalues
   ↓
Select Top K Components
   ↓
Transform Data
   ↓
Reduced Dataset
```

---

# 🔷 Explained Variance

## 📌 What is it?

👉 How much information each component keeps

---

## 📌 Example

```text
PC1 → 70% variance  
PC2 → 20% variance  
PC3 → 10% variance  
```

👉 Total = 100%

---

## 📌 Use

* Choose number of components
* Usually keep 90–95% variance

---

# 🔷 Important Notes

* PCA is a linear transformation
* Works best when features are correlated
* Output features are uncorrelated

---

# ⚠️ Common Mistakes

❌ Not scaling data
❌ Choosing too few components
❌ Ignoring explained variance

---

# 🎯 Interview Insight

👉 Question:  
Explain PCA step-by-step

👉 Answer:  

1. Standardize data
2. Compute covariance matrix
3. Find eigenvalues & eigenvectors
4. Select top components
5. Transform data

---

# 🧠 One-Line Summary

> PCA reduces dimensions by projecting data onto top eigenvectors with highest variance.
