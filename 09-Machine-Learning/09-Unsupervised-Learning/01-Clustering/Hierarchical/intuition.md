# 🌳 Hierarchical Clustering — Intuition

## 📌 Overview

Hierarchical Clustering builds clusters in a **tree-like structure**.

👉 Unlike K-Means, it does NOT require choosing K initially

---

## 🧠 Core Idea

> Build clusters step-by-step by merging or splitting data points

---

## 🔷 Types of Hierarchical Clustering

### 1. Agglomerative (Bottom-Up)

* Start with each point as its own cluster
* Merge closest clusters step by step

👉 Most commonly used

---

### 2. Divisive (Top-Down)

* Start with all points in one cluster
* Split into smaller clusters

---

## 🔷 How Agglomerative Clustering Works

### Step 1:

Each data point = separate cluster

---

### Step 2:

Find closest clusters

---

### Step 3:

Merge them

---

### Step 4:

Repeat until:

* one cluster remains
* or desired clusters formed

---

## 🔁 Workflow

```text
Each point = cluster
   ↓
Find closest clusters
   ↓
Merge clusters
   ↓
Repeat
```

---

## 🔷 Distance Between Clusters (Linkage)

### 1. Single Linkage

* Distance between closest points

---

### 2. Complete Linkage

* Distance between farthest points

---

### 3. Average Linkage

* Average distance between points

---

### 4. Ward Method

* Minimizes variance

---

## 🔷 Key Difference from K-Means

| Feature          | K-Means  | Hierarchical |
| ---------------- | -------- | ------------ |
| Need K initially | Yes      | No           |
| Structure        | Flat     | Tree         |
| Output           | Clusters | Dendrogram   |
| Flexibility      | Low      | High         |

---

## 🔷 Visualization: Dendrogram

👉 Tree-like diagram showing how clusters are formed

---

## 🔷 Advantages

* No need to choose K initially
* Works well for small datasets
* Gives hierarchical structure

---

## 🔷 Limitations

* Slow for large datasets
* Cannot undo merges
* Sensitive to noise

---

## 🎯 When to Use

* Small datasets
* Need hierarchical relationships
* When K is unknown

---

## ⚠️ Important Points

* Once clusters merge → cannot split
* Choice of linkage affects result
* Dendrogram helps choose K

---

## 🧠 Interview Insight

👉 Question:  
What is Hierarchical Clustering?

👉 Answer:  
It is a clustering method that builds a tree of clusters by iteratively merging or splitting data points based on distance.

---

## 🧠 One-Line Summary

> Hierarchical clustering builds a tree of clusters by merging or splitting data points step-by-step.
