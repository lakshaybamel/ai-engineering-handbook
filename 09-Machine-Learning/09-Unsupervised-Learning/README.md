# 🤖 Unsupervised Machine Learning

## 📌 Overview

Unsupervised Learning is a type of Machine Learning where the model learns patterns from **unlabeled data**.

👉 No target/output variable
👉 Model discovers hidden structure on its own

---

## 🧠 Core Idea

> Let the model find patterns, groups, and structure without guidance

---

# 🔍 What You Will Learn

This module covers:

* Clustering techniques
* Dimensionality Reduction
* Anomaly Detection

👉 These are widely used in real-world ML systems

---

# 📂 Module Structure

## 🔷 1. Clustering

Group similar data points together

📄 Topics:

* What is Clustering
* K-Means Clustering
* Elbow Method
* Silhouette Score
* Random Initialization Trap
* Hierarchical Clustering
* Dendrogram
* DBSCAN
* Comparisons

📁 Folder:
👉 [`01-Clustering`](./01-Clustering/)

---

## 🔷 2. Dimensionality Reduction

Reduce number of features while preserving information

📄 Topics:

* What is Dimensionality Reduction
* PCA (Principal Component Analysis)
* Step-by-step PCA
* Implementation

📁 Folder:
👉 [`02-Dimensionality-Reduction`](./02-Dimensionality-Reduction/)

---

## 🔷 3. Anomaly Detection

Identify unusual or rare data points

📄 Topics:

* What is Anomaly Detection
* DBSCAN for Anomalies
* Isolation Forest
* LOF (Local Outlier Factor)

📁 Folder:
👉 [`03-Anomaly-Detection`](./03-Anomaly-Detection/)

---

## 🧾 Cheatsheets

Quick revision notes:

* clustering.md
* pca.md
* anomaly_detection.md

📁 Folder:
👉 [`cheatsheets`](./cheatsheets/)

---

# ⚙️ When to Use Unsupervised Learning

* No labeled data available
* Need to discover hidden patterns
* Exploratory Data Analysis (EDA)
* Feature engineering

---

# 🔷 Key Techniques Summary

| Technique         | Purpose            |
| ----------------- | ------------------ |
| Clustering        | Group similar data |
| PCA               | Reduce dimensions  |
| Anomaly Detection | Find unusual data  |

---

# 🔁 Typical Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Feature Scaling
   ↓
Apply Algorithm
   ↓
Analyze Patterns
```

---

# 🔷 Real-World Applications

* Customer segmentation
* Recommendation systems
* Fraud detection
* Image compression
* Network security

---

# ⚠️ Important Points

* No ground truth → evaluation is tricky
* Scaling is very important
* Results depend on parameters
* Interpretation requires domain knowledge

---

# 🎯 Learning Outcome

After completing this module:

* Understand unsupervised learning concepts
* Apply clustering algorithms
* Perform dimensionality reduction using PCA
* Detect anomalies using multiple techniques
* Compare different approaches

---

# 🧠 Interview Insights

👉 Difference between supervised & unsupervised?

* Supervised → has labels
* Unsupervised → no labels

---

👉 When to use K-Means vs DBSCAN?

* K-Means → spherical clusters
* DBSCAN → arbitrary shapes + noise detection

---

👉 Why PCA?

* Reduce features
* Improve performance
* Remove redundancy

---

# 🚀 Final Takeaway

* Unsupervised learning is about **discovery, not prediction**
* Helps understand data before building models
* Very important for real-world ML pipelines

---

# 🧠 One-Line Summary

> Unsupervised learning finds hidden patterns in unlabeled data using clustering, dimensionality reduction, and anomaly detection.
