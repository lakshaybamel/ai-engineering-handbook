# ⚔️ K-Means vs DBSCAN

## 📌 Overview

K-Means and DBSCAN are both clustering algorithms, but they work very differently.

👉 K-Means → distance-based
👉 DBSCAN → density-based

---

## 🧠 Core Difference

> K-Means groups based on distance, DBSCAN groups based on density

---

## 🔷 Comparison Table

| Feature           | K-Means        | DBSCAN           |
| ----------------- | -------------- | ---------------- |
| Type              | Distance-based | Density-based    |
| Need K            | Yes            | No               |
| Shape of clusters | Spherical      | Any shape        |
| Outlier handling  | Poor           | Good             |
| Parameters        | K              | eps, min_samples |
| Scalability       | Fast           | Slower           |

---

## 🔷 Cluster Shape

### K-Means

* Works best for **circular/spherical clusters**

---

### DBSCAN

* Works for **non-linear and irregular shapes**

---

## 🔷 Outlier Handling

### K-Means

* Includes all points in clusters
* Cannot detect noise

---

### DBSCAN

* Identifies noise points (-1 label)
* Handles outliers effectively

---

## 🔷 Number of Clusters

### K-Means

* Must specify K manually

---

### DBSCAN

* Automatically determines clusters

---

## 🔷 Sensitivity

### K-Means

* Sensitive to initialization
* Sensitive to outliers

---

### DBSCAN

* Sensitive to eps and min_samples
* Works poorly if density varies

---

## 🔷 Example Insight

* Data with circular clusters → K-Means works well
* Data with complex shapes → DBSCAN performs better

---

## 🔷 When to Use

### Use K-Means when:

* Clusters are well-separated
* Data is large
* Shape is simple

---

### Use DBSCAN when:

* Data has irregular shapes
* Need to detect outliers
* Number of clusters unknown

---

## ⚠️ Important Points

* Always scale data before both algorithms
* DBSCAN struggles with varying density
* K-Means fails on non-linear patterns

---

## 🧠 Interview Insight

👉 Question:  
Difference between K-Means and DBSCAN?

👉 Answer:  
K-Means groups data based on distance and requires specifying K, while DBSCAN groups based on density, automatically finds clusters, and detects noise.

---

## 🧠 One-Line Summary

> K-Means is distance-based and needs K, while DBSCAN is density-based and can detect arbitrary shaped clusters with noise handling.
