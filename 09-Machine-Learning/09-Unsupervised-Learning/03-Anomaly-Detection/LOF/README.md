# 📍 LOF (Local Outlier Factor)

## 📌 Overview

Local Outlier Factor (LOF) is an anomaly detection algorithm that identifies outliers based on **local density**.

👉 It compares how dense a point is compared to its neighbors

---

## 🧠 Core Idea

> Anomalies are points that have lower density than their surrounding neighbors

---

## 📂 Contents

### 📄 Concepts

* [`intuition.md`](./intuition.md)

---

### 📓 Implementation

* [`lof.ipynb`](./lof.ipynb)

---

## ⚙️ How It Works

1. For each point → find nearest neighbors (k-neighbors)
2. Compute density of the point
3. Compare with density of neighbors

👉 If density is much lower → anomaly

---

## 🔷 Key Concepts

### 1. k-Nearest Neighbors

* Defines neighborhood

---

### 2. Local Density

* How closely packed the neighbors are

---

### 3. LOF Score

* Measures how isolated a point is

---

## 🔷 Output Interpretation

| LOF Score | Meaning          |
| --------- | ---------------- |
| ≈ 1       | Normal point     |
| > 1       | Possible anomaly |
| >> 1      | Strong anomaly   |

---

## 🔷 Why LOF is Useful

* Detects **local anomalies**
* Works well when data density varies
* More flexible than global methods

---

## 🔷 Advantages

* Captures local patterns
* Works well for complex datasets
* No need for global assumptions

---

## 🔷 Limitations

* Sensitive to choice of neighbors (k)
* Computationally expensive
* Not ideal for very large datasets

---

## 🎯 When to Use

* When data density varies across regions
* When anomalies are local (not global)
* Medium-sized datasets

---

## ⚠️ Important Points

* Requires feature scaling
* Choice of `n_neighbors` is critical
* Works differently from Isolation Forest

---

## 🎯 Learning Outcome

After completing this section:

* Understand density-based anomaly detection
* Learn how LOF detects local outliers
* Implement LOF using sklearn

---

## 🧠 Interview Insight

👉 Question:  
What is LOF?

👉 Answer:  
LOF is an anomaly detection method that identifies outliers based on how their local density compares to their neighbors.

---

## 🧠 One-Line Summary

> LOF detects anomalies by comparing local density of a point with its neighbors.
