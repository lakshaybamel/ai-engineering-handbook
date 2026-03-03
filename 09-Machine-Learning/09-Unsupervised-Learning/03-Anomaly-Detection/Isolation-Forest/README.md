# 🌲 Isolation Forest

## 📌 Overview

Isolation Forest is an anomaly detection algorithm that identifies outliers by **isolating data points using random splits**.

👉 It is efficient and widely used for detecting anomalies in large datasets

---

## 🧠 Core Idea

> Anomalies are easier to isolate compared to normal data points

---

## 📂 Contents

### 📄 Concepts

* [`intuition.md`](./intuition.md)

---

### 📓 Implementation

* [`isolation_forest.ipynb`](./isolation_forest.ipynb)

---

## ⚙️ Workflow

```text
Random Feature Selection
   ↓
Random Split Value
   ↓
Build Isolation Trees
   ↓
Measure Path Length
   ↓
Detect Anomalies
```

---

## 🔷 Key Concepts

* Isolation Trees
* Random Splitting
* Path Length
* Anomaly Score

---

## 🎯 Why Isolation Forest

* Detects anomalies efficiently
* Works well on large datasets
* No need for distance calculation
* Handles high-dimensional data

---

## ⚠️ Important Points

* Uses `contamination` parameter to define anomaly proportion
* Works faster than distance-based methods
* Scaling is recommended
* Based on randomness → results may vary slightly

---

## 🎯 Learning Outcome

After completing this section:

* Understand isolation-based anomaly detection
* Learn how anomalies are identified
* Implement Isolation Forest using sklearn

---

## 🧠 Interview Insight

👉 Question:  
What is Isolation Forest?

👉 Answer:  
It is an anomaly detection algorithm that isolates anomalies using random feature splits, where anomalies require fewer splits to isolate.

---

## 🧠 One-Line Summary

> Isolation Forest detects anomalies by isolating points that require fewer splits in random trees.
