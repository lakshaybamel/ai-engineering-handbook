# 🚨 Anomaly Detection

## 📌 Overview

Anomaly Detection is used to identify **unusual or rare data points** that differ significantly from normal data.

👉 Also called:

* Outlier Detection
* Novelty Detection

---

## 🧠 Core Idea

> Anomalies are data points that behave differently from the majority

---

## 📂 Contents

### 🔷 1. DBSCAN (Density-Based)

* [`DBSCAN/README.md`](./DBSCAN/README.md)
* [`DBSCAN/intuition.md`](./DBSCAN/intuition.md)
* [`DBSCAN/dbscan_anomaly.ipynb`](./DBSCAN/dbscan_anomaly.ipynb)

👉 Detects anomalies as **noise points (-1)**

---

### 🔷 2. Isolation Forest

* [`Isolation-Forest/README.md`](./Isolation-Forest/README.md)
* [`Isolation-Forest/intuition.md`](./Isolation-Forest/intuition.md)
* [`Isolation-Forest/isolation_forest.ipynb`](./Isolation-Forest/isolation_forest.ipynb)

👉 Detects anomalies by **isolating points using random splits**

---

### 🔷 3. LOF (Local Outlier Factor)

* [`LOF/README.md`](./LOF/README.md)
* [`LOF/intuition.md`](./LOF/intuition.md)
* [`LOF/lof.ipynb`](./LOF/lof.ipynb)

👉 Detects anomalies using **local density comparison**

---

## ⚙️ Types of Anomaly Detection

### 1. Density-Based

* Example: DBSCAN, LOF
* Based on data density

---

### 2. Isolation-Based

* Example: Isolation Forest
* Based on isolating points

---

### 3. Distance-Based

* Based on distance from neighbors

---

## 🔷 Workflow

```text
Raw Data
   ↓
Preprocessing (Scaling)
   ↓
Apply Model
   ↓
Detect Anomalies
   ↓
Analyze Results
```

---

## 🔷 Use Cases

* Fraud Detection
* Network Intrusion Detection
* Fault Detection in Systems
* Medical Diagnosis
* Credit Card Fraud

---

## ⚠️ Important Points

* Anomalies are rare
* Feature scaling is important
* Choice of algorithm depends on data
* No labels required (unsupervised)

---

## 🎯 Learning Outcome

After completing this section:

* Understand different anomaly detection techniques
* Compare DBSCAN, Isolation Forest, and LOF
* Implement anomaly detection in real datasets

---

## 🧠 Interview Insight

👉 Question:  
What is anomaly detection?

👉 Answer:  
It is the process of identifying rare or unusual data points that deviate significantly from normal behavior.

---

## 🧠 One-Line Summary

> Anomaly detection identifies unusual data points that differ from the majority of the data.
