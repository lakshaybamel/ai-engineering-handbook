# 📉 PCA (Principal Component Analysis) Cheat Sheet

## 📌 Overview

PCA is a **dimensionality reduction technique** used to reduce the number of features while preserving maximum information.

👉 Converts high-dimensional data → lower-dimensional form
👉 Maintains most important patterns

---

# 🧠 Core Idea

> Find new features (principal components) that capture maximum variance

---

# 🔷 Why PCA?

* Reduce number of features
* Remove redundancy
* Improve model performance
* Visualize high-dimensional data

---

# ⚙️ How PCA Works (Step-by-Step)

```text
Original Data
   ↓
Feature Scaling (Very Important)
   ↓
Compute Covariance Matrix
   ↓
Find Eigenvalues & Eigenvectors
   ↓
Sort by Eigenvalues (importance)
   ↓
Select Top K Components
   ↓
Transform Data
```

---

# 🔷 Key Concepts

## 1. Principal Components (PCs)

* New axes (features)
* Linear combination of original features

👉 PC1 → captures maximum variance
👉 PC2 → next maximum (orthogonal to PC1)

---

## 2. Variance

* Measures spread of data
* PCA keeps directions with highest variance

---

## 3. Eigenvalues

* Represent importance of each component

👉 Higher eigenvalue → more important

---

## 4. Eigenvectors

* Direction of new axes

---

# 🔷 Mathematical Insight (Conceptual)

```text
Z = X · W
```

* X → original data
* W → eigenvectors
* Z → transformed data

---

# 🔷 Explained Variance Ratio

* Shows how much information each component keeps

```text
Total Variance = sum of all eigenvalues
```

👉 Example:

| Component | Variance |
| --------- | -------- |
| PC1       | 70%      |
| PC2       | 20%      |
| PC3       | 10%      |

👉 Choose first 2 → keep 90% info

---

# 🔷 Choosing Number of Components

## 1. Explained Variance

* Choose components covering 90–95% variance

---

## 2. Scree Plot

* Plot components vs variance
* Look for “elbow point”

---

# 🔷 Code Example

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Step 1: Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Explained variance
print(pca.explained_variance_ratio_)
```

---

# 🔷 Advantages

* Reduces dimensionality
* Speeds up training
* Removes multicollinearity
* Helps visualization

---

# 🔷 Limitations

* Loss of information
* Hard to interpret components
* Assumes linear relationships

---

# ⚠️ Important Points

* Always scale data before PCA
* PCA is sensitive to scale
* Components are linear combinations
* Not suitable for non-linear patterns

---

# ⚖️ PCA vs Feature Selection

| Feature          | PCA                 | Feature Selection |
| ---------------- | ------------------- | ----------------- |
| Approach         | Create new features | Select existing   |
| Interpretability | Low                 | High              |
| Information      | Compressed          | Preserved         |

---

# 🎯 When to Use PCA

* High-dimensional data
* Visualization (2D/3D)
* Remove redundancy
* Improve ML performance

---

# 🚀 Real-World Use Cases

* Image compression
* Face recognition
* Noise reduction
* Data visualization

---

# 🧠 Interview Quick Points

* PCA uses **variance maximization**
* PC1 captures maximum variance
* Requires **feature scaling**
* Uses **eigenvalues & eigenvectors**

---

# 🧠 One-Line Summary

> PCA reduces dimensionality by transforming data into fewer components that retain maximum variance.
