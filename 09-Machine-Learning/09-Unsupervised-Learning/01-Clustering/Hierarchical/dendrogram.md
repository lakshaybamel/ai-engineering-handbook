# 🌳 Dendrogram

## 📌 Overview

A Dendrogram is a **tree-like diagram** used to visualize hierarchical clustering.

👉 It shows how clusters are merged step-by-step

---

## 🧠 Core Idea

> Visualize how data points combine into clusters

---

## 🔷 What It Represents

* Each leaf → a data point
* Each merge → clusters joining
* Height → distance between clusters

---

## 🔷 Structure

```text
      ________
     |        |
   __|__    __|__
  |     |  |     |
 A      B  C     D
```

👉 Bottom → individual points
👉 Top → one big cluster

---

## 🔷 Key Concept: Height

* Vertical axis = distance (similarity measure)

👉 Higher merge = less similar clusters

---

## 🔷 How to Read Dendrogram

### Step 1:

Start from bottom (individual points)

---

### Step 2:

See where clusters merge

---

### Step 3:

Check height of merge

👉 Lower height = more similar

---

## 🔷 Choosing Number of Clusters

👉 Draw a horizontal line

```text
   ________
  |        |
__|__    __|__
|   |    |   |
```

👉 Count number of vertical cuts

👉 That = number of clusters

---

## 🔷 Example Insight

* If clusters merge at high distance → they are very different
* If merge early → very similar

---

## 🔷 Python Example

```python
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

Z = linkage(X, method='ward')

dendrogram(Z)
plt.show()
```

---

## 🔷 Advantages

* Easy visualization
* Helps choose number of clusters
* Shows hierarchical relationships

---

## 🔷 Limitations

* Hard to read for large datasets
* Becomes cluttered
* Computationally expensive

---

## 🎯 When to Use

* Small datasets
* When cluster hierarchy matters
* To decide number of clusters

---

## ⚠️ Important Points

* Height = distance between clusters
* Horizontal cut determines clusters
* Depends on linkage method

---

## 🧠 Interview Insight

👉 Question:  
What is a dendrogram?

👉 Answer:  
A dendrogram is a tree-like diagram used to visualize hierarchical clustering and determine the number of clusters.

---

## 🧠 One-Line Summary

> A dendrogram visualizes how clusters merge and helps decide the optimal number of clusters.
