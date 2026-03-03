# 🚨 Anomaly Detection Cheat Sheet

## 📌 Overview

Anomaly Detection is the process of identifying **unusual patterns or outliers** in data.

👉 These are data points that **deviate significantly** from normal behavior

---

# 🧠 Core Idea

> Normal data follows patterns → anomalies break those patterns

---

# 🔍 What is an Anomaly?

* Rare data point
* Different from majority
* Can indicate:

  * fraud
  * errors
  * system failures

---

# 🔷 Types of Anomalies

## 1. Point Anomalies

* Single data point is abnormal

👉 Example: One very high transaction

---

## 2. Contextual Anomalies

* Abnormal in a specific context

👉 Example: High temperature in winter

---

## 3. Collective Anomalies

* Group of points is abnormal

👉 Example: unusual pattern in time series

---

# ⚙️ Approaches to Anomaly Detection

## 1. Statistical Methods

* Based on distribution (mean, std)
* Example: Z-score

---

## 2. Distance-Based Methods

* Points far from others → anomaly

👉 Example: k-NN

---

## 3. Density-Based Methods

* Low-density regions → anomalies

👉 Example: LOF

---

## 4. Isolation-Based Methods

* Easy to isolate → anomaly

👉 Example: Isolation Forest

---

## 5. Clustering-Based Methods

* Points not belonging to clusters → anomaly

👉 Example: DBSCAN

---

# 🔷 Algorithms Covered

## 1. 🌲 Isolation Forest

### Idea:

* Anomalies require fewer splits

### Key Points:

* Fast
* Works well on large datasets
* No distance calculation

---

## 2. 📍 LOF (Local Outlier Factor)

### Idea:

* Compare local density

### Key Points:

* Detects local anomalies
* Sensitive to neighbors

---

## 3. 🔵 DBSCAN (for Anomaly Detection)

### Idea:

* Noise points = anomalies

### Key Points:

* Works for non-linear data
* Detects clusters + outliers

---

# 🔷 Comparison Table

| Algorithm        | Idea       | Best For        | Limitation          |
| ---------------- | ---------- | --------------- | ------------------- |
| Isolation Forest | Isolation  | Large datasets  | Needs tuning        |
| LOF              | Density    | Local anomalies | Slow                |
| DBSCAN           | Clustering | Non-linear data | Parameter sensitive |

---

# ⚙️ General Workflow

```text
Data Collection
   ↓
Preprocessing (Scaling)
   ↓
Choose Algorithm
   ↓
Train Model
   ↓
Detect Anomalies
   ↓
Evaluate Results
```

---

# 🔷 Code Snippets

## Isolation Forest

```python id="if1"
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.05)
model.fit(X)

preds = model.predict(X)  # -1 = anomaly
```

---

## LOF

```python id="lof1"
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors=20)
preds = lof.fit_predict(X)
```

---

## DBSCAN

```python id="db1"
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.5, min_samples=5)
labels = db.fit_predict(X)

# -1 label = anomaly
```

---

# 🔷 Evaluation Metrics

* Precision
* Recall
* F1 Score
* ROC-AUC

👉 Often difficult due to lack of labeled data

---

# ⚠️ Important Points

* Always scale features
* Choosing parameters is critical
* Outliers ≠ always errors (may be useful info)
* Domain knowledge matters

---

# 🎯 When to Use

* Fraud detection
* Network security
* Fault detection
* Data cleaning

---

# 🚀 Real-World Applications

* Credit card fraud detection
* Intrusion detection systems
* Medical diagnosis
* Manufacturing defect detection

---

# 🧠 Interview Quick Points

* Isolation Forest → isolation-based
* LOF → density-based
* DBSCAN → clustering-based
* Anomaly detection often **unsupervised**

---

# 🧠 One-Line Summary

> Anomaly detection identifies rare and unusual data points that deviate from normal patterns.
