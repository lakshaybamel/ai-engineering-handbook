# 🎯 K-Means Clustering

## 📌 Overview

K-Means is an unsupervised learning algorithm used to group similar data points into **K clusters**.

👉 It works by minimizing the distance between data points and their cluster centers (centroids)

---

## 🧠 Core Idea

> Divide data into K groups such that points in the same group are similar

---

## 📂 Contents

### 📄 Concepts

* [`intuition.md`](./intuition.md)
* [`elbow_method.md`](./elbow_method.md)
* [`silhouette_score.md`](./silhouette_score.md)
* [`random_initialization.md`](./random_initialization.md)

---

### 📓 Implementation

* [`kmeans.ipynb`](./kmeans.ipynb)
* [`choosing_k.ipynb`](./choosing_k.ipynb)

---

## ⚙️ Workflow

```text
Choose K
   ↓
Initialize Centroids
   ↓
Assign Points to Nearest Cluster
   ↓
Update Centroids
   ↓
Repeat until convergence
```

---

## 🔷 Key Concepts

* Centroid
* Distance (Euclidean)
* Inertia
* Initialization
* Choosing K

---

## 🎯 Learning Outcome

After completing this section:

* Understand how K-Means works
* Apply clustering using sklearn
* Choose optimal number of clusters
* Evaluate clustering performance

---

## ⚠️ Important Points

* Requires selecting K manually
* Sensitive to initialization
* Works best with spherical clusters
* Needs feature scaling

---

## 🧠 One-Line Summary

> K-Means groups data into K clusters by minimizing distance between points and their centroids.
