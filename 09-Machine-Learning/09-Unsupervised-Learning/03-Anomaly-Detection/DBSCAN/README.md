# 🚨 DBSCAN for Anomaly Detection

## 📌 Overview

DBSCAN can be used not only for clustering but also for **anomaly (outlier) detection**.

👉 It identifies points that do not belong to any cluster as **anomalies**

---

## 🧠 Core Idea

> Points that are not part of any dense region are considered anomalies

---

## 📂 Contents

### 📄 Concepts

* [`intuition.md`](./intuition.md)

---

### 📓 Implementation

* [`dbscan_anomaly.ipynb`](./dbscan_anomaly.ipynb)

---

## ⚙️ How It Works for Anomaly Detection

1. DBSCAN forms clusters based on density
2. Points that do not fit into any cluster are labeled as **-1**
3. These points are treated as **anomalies**

---

## 🔷 Key Parameters

### 1. eps

* Radius to search neighbors

---

### 2. min_samples

* Minimum points required to form a dense region

---

## 🔷 Output Interpretation

| Label     | Meaning               |
| --------- | --------------------- |
| 0,1,2,... | Cluster IDs           |
| -1        | Anomaly (Noise Point) |

---

## 🎯 Why Use DBSCAN for Anomaly Detection

* No need to specify number of clusters
* Automatically detects outliers
* Works well for irregular data shapes

---

## ⚠️ Important Points

* Sensitive to `eps` value
* Requires feature scaling
* Not ideal for high-dimensional data

---

## 🔷 When to Use

* Density-based anomaly detection
* When clusters are not clearly separable
* When outliers are far from dense regions

---

## 🎯 Learning Outcome

After completing this section:

* Understand how DBSCAN detects anomalies
* Identify noise points as outliers
* Apply DBSCAN for real-world anomaly detection

---

## 🧠 Interview Insight

👉 Question:  
How does DBSCAN detect anomalies?

👉 Answer:  
DBSCAN labels points that do not belong to any dense cluster as noise (label -1), which are treated as anomalies.

---

## 🧠 One-Line Summary

> DBSCAN detects anomalies as points that do not belong to any cluster (noise points).
