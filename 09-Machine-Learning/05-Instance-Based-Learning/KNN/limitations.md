# ⚠️ Limitations of K-Nearest Neighbors (KNN)

## 📌 Overview

KNN is simple and effective, but it has several limitations that affect its performance in real-world scenarios.

---

# 🔷 1. High Computational Cost

## 📌 Problem

KNN calculates distance from the new point to **all training data points**

---

## 🧠 Impact

- Slow prediction  
- Not suitable for large datasets  

---

# 🔷 2. Memory Intensive

## 📌 Problem

KNN stores the entire dataset

---

## 🧠 Impact

- High memory usage  
- Not efficient for large-scale applications  

---

# 🔷 3. Sensitive to Feature Scaling

## 📌 Problem

Distance depends on feature values

---

## 🧠 Example

| Feature | Value |
|--------|------|
| Age | 25 |
| Salary | 500000 |

👉 Salary dominates distance  

---

## ✅ Solution

- Apply scaling (Standardization / Normalization)

---

# 🔷 4. Curse of Dimensionality

## 📌 Problem

In high dimensions:
- Distance becomes less meaningful  

---

## 🧠 Impact

- All points appear similar  
- Model performance degrades  

---

# 🔷 5. Sensitive to Noise

## 📌 Problem

Outliers can affect nearest neighbors

---

## 🧠 Impact

- Wrong predictions  

---

# 🔷 6. Choosing Optimal K is Difficult

## 📌 Problem

- Small K → overfitting  
- Large K → underfitting  

---

## 🧠 Impact

- Performance depends heavily on K  

---

# 🔷 7. Imbalanced Data Problem

## 📌 Problem

Majority class dominates prediction

---

## 🧠 Impact

- Biased predictions  

---

# ⚠️ Important Points

- Works best with small, clean datasets  
- Requires preprocessing  
- Not suitable for very large datasets  

---

## 🧠 Interview Insight

👉 **Question:**<br>
What are the main limitations of KNN?

👉 **Answer:**<br>
High computation cost, sensitivity to scaling, curse of dimensionality, and difficulty in choosing K.

---

## 🧠 One-Line Summary

> KNN is simple but suffers from high computation cost, sensitivity to scaling, and poor performance on large or high-dimensional data.