# 🌳 Hierarchical Clustering

## 📌 Overview

Hierarchical Clustering is an unsupervised learning algorithm that builds clusters in a **tree-like structure (dendrogram)**.

👉 It does not require specifying number of clusters initially

---

## 🧠 Core Idea

> Build clusters step-by-step by merging similar data points

---

## 📂 Contents

### 📄 Concepts

* [`intuition.md`](./intuition.md)
* [`dendrogram.md`](./dendrogram.md)

---

### 📓 Implementation

* [`hierarchical.ipynb`](./hierarchical.ipynb)

---

## ⚙️ Workflow

```text
Each point = cluster
   ↓
Find closest clusters
   ↓
Merge clusters
   ↓
Repeat
   ↓
Visualize using dendrogram
```

---

## 🔷 Key Concepts

* Agglomerative Clustering
* Linkage Methods
* Dendrogram
* Distance Metrics

---

## 🎯 Learning Outcome

After completing this section:

* Understand hierarchical clustering
* Read and interpret dendrogram
* Choose optimal number of clusters
* Apply clustering using sklearn

---

## ⚠️ Important Points

* No need to choose K initially
* Works well for small datasets
* Computationally expensive
* Cannot undo cluster merges

---

## 🧠 One-Line Summary

> Hierarchical clustering builds clusters step-by-step and represents them using a dendrogram.
