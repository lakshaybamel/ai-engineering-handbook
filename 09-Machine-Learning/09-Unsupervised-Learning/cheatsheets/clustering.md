# 📊 Clustering Cheat Sheet

## 📌 Overview

Clustering is an **unsupervised learning technique** used to group similar data points together.

👉 No labels are given
👉 Model finds patterns automatically

---

# 🧠 Core Idea

> Group similar data points and separate dissimilar ones

---

# 🔷 Types of Clustering Algorithms

## 1. Partition-Based Clustering

### 👉 K-Means

* Divides data into K clusters
* Uses centroids
* Based on distance

---

## 2. Hierarchical Clustering

* Builds tree-like structure (dendrogram)
* No need to specify K initially

---

## 3. Density-Based Clustering

### 👉 DBSCAN

* Groups dense regions
* Detects noise (outliers)
* Handles non-linear clusters

---

# ⚙️ K-Means (Most Important)

## 📌 Steps

```text
Choose K
   ↓
Initialize Centroids
   ↓
Assign Points
   ↓
Update Centroids
   ↓
Repeat
```

---

## 🔷 Formula (Distance)

```text
Euclidean Distance:
√((x1 - x2)^2 + (y1 - y2)^2)
```

---

## 🔷 Key Terms

* Centroid → center of cluster
* Inertia → sum of squared distances
* Cluster → group of similar points

---

## 🔷 Choosing K

### 1. Elbow Method

* Plot K vs inertia
* Look for “elbow point”

---

### 2. Silhouette Score

```text
(b - a) / max(a, b)
```

* a → intra-cluster distance
* b → nearest cluster distance

👉 Higher = better

---

## 🔷 Pros

* Simple
* Fast
* Scalable

---

## 🔷 Cons

* Need K
* Sensitive to initialization
* Poor for non-linear data

---

# 🌳 Hierarchical Clustering

## 📌 Types

### Agglomerative (Bottom-Up)

* Start with individual points
* Merge clusters

### Divisive (Top-Down)

* Start with one cluster
* Split

---

## 🔷 Linkage Methods

| Type     | Description     |
| -------- | --------------- |
| Single   | Closest points  |
| Complete | Farthest points |
| Average  | Mean distance   |
| Ward     | Min variance    |

---

## 🔷 Dendrogram

* Tree representation
* Helps choose K

---

## 🔷 Pros

* No need K initially
* Visual structure

---

## 🔷 Cons

* Slow
* Not scalable

---

# 🌌 DBSCAN (Density-Based)

## 📌 Key Parameters

* eps → radius
* min_samples → min points

---

## 🔷 Core Concepts

* Core Point → dense region
* Border Point → near cluster
* Noise → outlier

---

## 🔷 Output

| Label | Meaning  |
| ----- | -------- |
| 0,1,2 | Clusters |
| -1    | Noise    |

---

## 🔷 Pros

* No need K
* Detects outliers
* Handles non-linear shapes

---

## 🔷 Cons

* Sensitive to eps
* Poor for varying densities

---

# ⚖️ Algorithm Comparison

| Feature  | K-Means | Hierarchical | DBSCAN     |
| -------- | ------- | ------------ | ---------- |
| Need K   | Yes     | No           | No         |
| Shape    | Linear  | Flexible     | Non-linear |
| Outliers | No      | Limited      | Yes        |
| Speed    | Fast    | Slow         | Medium     |

---

# ⚠️ Important Rules

* Always scale data
* Choose algorithm based on data shape
* Validate clusters using metrics

---

# 🎯 When to Use What?

## Use K-Means when:

* Data is spherical
* Large dataset
* Need fast solution

---

## Use Hierarchical when:

* Dataset is small
* Need cluster hierarchy

---

## Use DBSCAN when:

* Data is non-linear
* Need outlier detection

---

# 🧠 Interview Quick Points

* K-Means minimizes **inertia**
* DBSCAN detects **noise automatically**
* Hierarchical gives **dendrogram**
* Silhouette Score → cluster quality

---

# 🚀 Real-World Use Cases

* Customer segmentation
* Image segmentation
* Recommendation systems
* Fraud detection

---

# 🧠 One-Line Summary

> Clustering groups similar data points together without labels using distance, hierarchy, or density-based approaches.
