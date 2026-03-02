# 📊 Clustering

## 📌 Overview

Clustering is an **unsupervised learning technique** used to group similar data points together.

👉 No labels are provided
👉 The model discovers hidden patterns in data

---

## 🧠 Core Idea

> Group similar data points into clusters based on distance or density

---

## 🔗 Topics Covered

### 🔷 1. K-Means Clustering

* Most popular clustering algorithm
* Groups data into K clusters

📄 Files:

* [`K-Means/README.md`](./K-Means/README.md)
* [`K-Means/intuition.md`](./K-Means/intuition.md)
* [`K-Means/elbow_method.md`](./K-Means/elbow_method.md)
* [`K-Means/silhouette_score.md`](./K-Means/silhouette_score.md)
* [`K-Means/random_initialization.md`](./K-Means/random_initialization.md)
* [`K-Means/kmeans.ipynb`](./K-Means/kmeans.ipynb)
* [`K-Means/choosing_k.ipynb`](./K-Means/choosing_k.ipynb)

---

### 🔷 2. Hierarchical Clustering

* Builds clusters in a tree-like structure
* Uses dendrogram for visualization

📄 Files:

* [`Hierarchical/README.md`](./Hierarchical/README.md)
* [`Hierarchical/intuition.md`](./Hierarchical/intuition.md)
* [`Hierarchical/dendrogram.md`](./Hierarchical/dendrogram.md)
* [`Hierarchical/hierarchical.ipynb`](./Hierarchical/hierarchical.ipynb)

---

### 🔷 3. DBSCAN

* Density-based clustering algorithm
* Handles noise and non-linear clusters

📄 Files:

* [`DBSCAN/README.md`](./DBSCAN/README.md)
* [`DBSCAN/intuition.md`](./DBSCAN/intuition.md)
* [`DBSCAN/dbscan.ipynb`](./DBSCAN/dbscan.ipynb)
* [`DBSCAN/comparison_with_kmeans.md`](./DBSCAN/comparison_with_kmeans.md)

---

### 🔷 4. Comparisons

* Compare different clustering algorithms

📄 Files:

* [`comparisons.md`](./comparisons.md)

---

## ⚙️ Workflow

```text
Understand Data
   ↓
Choose Clustering Algorithm
   ↓
Apply Model
   ↓
Evaluate Clusters
   ↓
Interpret Results
```

---

## 🔷 Key Concepts

* Distance Metrics
* Centroids
* Density
* Dendrogram
* Cluster Evaluation

---

## 🎯 Learning Outcome

After completing this section:

* Understand different clustering techniques
* Choose the right algorithm for your data
* Evaluate clustering performance
* Handle real-world clustering problems

---

## ⚠️ Important Points

* No labels in clustering
* Choosing the right algorithm is crucial
* Data scaling is often required
* Different algorithms work for different data shapes

---

## 🧠 Interview Insight

👉 Question:  
What is clustering in machine learning?

👉 Answer:  
Clustering is an unsupervised learning technique that groups similar data points together based on patterns and distance.

---

## 🧠 One-Line Summary

> Clustering groups similar data points together to discover hidden patterns in unlabeled data.
