# 🌐 DBSCAN Clustering

## 📌 Overview

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is an unsupervised learning algorithm that forms clusters based on **data density**.

👉 It can detect clusters of any shape
👉 It can also identify noise (outliers)

---

## 🧠 Core Idea

> Dense regions form clusters, sparse regions are treated as noise

---

## 📂 Contents

### 📄 Concepts

* [`intuition.md`](./intuition.md)
* [`comparison_with_kmeans.md`](./comparison_with_kmeans.md)

---

### 📓 Implementation

* [`dbscan.ipynb`](./dbscan.ipynb)

---

## ⚙️ Workflow

```text
Pick a point
   ↓
Find neighbors within ε
   ↓
If neighbors ≥ MinPts → form cluster
   ↓
Expand cluster
   ↓
Else → mark as noise
```

---

## 🔷 Key Concepts

* Epsilon (ε)
* MinPts
* Core Points
* Border Points
* Noise Points

---

## 🎯 Learning Outcome

After completing this section:

* Understand density-based clustering
* Apply DBSCAN using sklearn
* Detect outliers in data
* Compare DBSCAN with K-Means

---

## ⚠️ Important Points

* No need to choose K
* Works well with non-linear clusters
* Sensitive to parameter selection
* Struggles with varying density

---

## 🧠 One-Line Summary

> DBSCAN forms clusters based on density and automatically detects noise points.
