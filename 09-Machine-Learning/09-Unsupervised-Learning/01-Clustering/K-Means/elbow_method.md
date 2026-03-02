# 📉 Elbow Method

## 📌 Overview

The Elbow Method is used to find the **optimal number of clusters (K)** in K-Means.

---

## 🧠 Core Idea

> Choose K where adding more clusters stops giving significant improvement

---

## 🔷 Why Needed?

K-Means requires choosing **K manually** ❌

👉 Elbow Method helps select a good value of K ✔

---

## 🔷 Key Concept: Inertia

* Inertia = sum of squared distances of points from their cluster centroid

👉 Lower inertia = better clustering

---

## 🔷 How It Works

### Step 1: Run K-Means for multiple K values

Example:

```python
K = 1, 2, 3, 4, 5, ...
```

---

### Step 2: Calculate inertia for each K

---

### Step 3: Plot graph

* X-axis → number of clusters (K)
* Y-axis → inertia

---

### Step 4: Find "Elbow Point"

👉 The point where curve bends sharply

---

## 🔁 Workflow

```text
Choose range of K
   ↓
Train K-Means for each K
   ↓
Compute inertia
   ↓
Plot graph
   ↓
Find elbow point
```

---

## 🔷 Visualization Idea

```text
Inertia
  |
  |\
  | \
  |  \
  |   \__
  |       \__
  |
  +----------------
        K
```

👉 The bend = optimal K

---

## 🔷 Interpretation

* Before elbow → large decrease in inertia
* After elbow → small improvement

👉 So choose K at elbow

---

## 🔷 Advantages

* Simple and easy to understand
* Helps avoid random selection of K

---

## 🔷 Limitations

* Elbow not always clear
* Sometimes multiple bends
* Subjective interpretation

---

## 🎯 When to Use

* While applying K-Means
* To choose optimal number of clusters

---

## ⚠️ Important Points

* Always scale data before applying K-Means
* Combine with other methods if unclear
* Works best when clusters are well-defined

---

## 🧠 Interview Insight

👉 Question:  
What is the Elbow Method?

👉 Answer:  
It is a technique used to determine the optimal number of clusters by plotting inertia vs K and selecting the point where the decrease slows down.

---

## 🧠 One-Line Summary

> Elbow Method finds optimal K where adding more clusters gives diminishing returns.
