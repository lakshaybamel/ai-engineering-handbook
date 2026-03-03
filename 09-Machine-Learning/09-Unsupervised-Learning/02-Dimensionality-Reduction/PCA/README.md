# 📉 PCA (Principal Component Analysis)

## 📌 Overview

PCA (Principal Component Analysis) is a dimensionality reduction technique used to transform high-dimensional data into fewer dimensions while preserving maximum information.

👉 It converts original features into **new uncorrelated features (principal components)**

---

## 🧠 Core Idea

> Project data onto directions where variance is maximum

---

## 📂 Contents

### 📄 Concepts

* [`intuition.md`](./intuition.md)
* [`step_by_step.md`](./step_by_step.md)

---

### 📓 Implementation

* [`pca.ipynb`](./pca.ipynb)

---

## ⚙️ Workflow

```text
Original Data
   ↓
Feature Scaling
   ↓
Covariance Matrix
   ↓
Eigenvalues & Eigenvectors
   ↓
Select Top Components
   ↓
Transform Data
```

---

## 🔷 Key Concepts

### 1. Principal Components

* New features created from original data
* Capture maximum variance

---

### 2. Explained Variance

* Measures how much information each component retains

---

### 3. Dimensionality Reduction

* Reduces number of features
* Improves efficiency

---

## 📊 Why PCA is Important

* Reduces computation time
* Removes noise
* Helps in visualization (2D/3D)
* Avoids curse of dimensionality

---

## 🔷 Advantages

* Faster model training
* Removes redundant features
* Improves performance

---

## 🔷 Limitations

* Loss of interpretability
* Information loss possible
* Assumes linear relationships

---

## 🎯 When to Use

* High-dimensional data
* Feature reduction required
* Visualization of complex data

---

## ⚠️ Important Points

* Always apply **feature scaling before PCA**
* Choose components based on explained variance
* PCA is sensitive to scale

---

## 🧠 Learning Outcome

After completing this section:

* Understand PCA intuition and math
* Apply PCA using sklearn
* Choose optimal number of components
* Visualize high-dimensional data

---

## 🧠 Interview Insight

👉 Question:  
What is PCA?

👉 Answer:  
PCA is a dimensionality reduction technique that transforms data into new orthogonal components that capture maximum variance.

---

## 🧠 One-Line Summary

> PCA reduces dimensionality by transforming data into components that capture maximum varianc
