# 🧠 K-Nearest Neighbors (KNN)

## 📌 Overview

K-Nearest Neighbors (KNN) is a **supervised machine learning algorithm** used for:

- Classification  
- Regression  

It makes predictions based on **similarity (distance)** between data points.

---

## 🧠 Key Idea

> Data points that are close to each other are likely to belong to the same class

---

## ⚙️ How It Works

```
Input Data Point
    ↓
Calculate distance from all training points
    ↓
Select K nearest neighbors
    ↓
Majority vote (classification)
```

---

## 📏 Distance Metric

Most commonly used:

- Euclidean Distance  

---

## 🔗 Topics Covered

### 1. Intuition

- Understanding similarity-based learning  
- How KNN makes predictions  

📄 File: [`intuition.md`](./intuition.md)

---

### 2. Limitations

- High computational cost  
- Sensitive to scaling  
- Curse of dimensionality  

📄 File: [`limitations.md`](./limitations.md)

---

### 3. KNN (Implementation)

- Model training using sklearn  
- Feature scaling  
- Evaluation using classification metrics  

📓 Notebook: [`knn.ipynb`](./knn.ipynb)

---

## ⚠️ Important Points

- Requires feature scaling  
- Sensitive to value of K  
- No training phase (lazy learning)  

---

## 🎯 Learning Outcome

After completing this section, the following should be clear:

- How KNN works  
- Importance of distance metrics  
- Effect of scaling on model  
- How to implement KNN using sklearn  

---

## 🧠 One-Line Summary

> KNN predicts based on similarity by selecting the nearest data points using distance metrics.