# 🧠 K-Nearest Neighbors (KNN) — Intuition

## 📌 What is KNN?

K-Nearest Neighbors (KNN) is a **supervised machine learning algorithm** used for:

- Classification  
- Regression  

It makes predictions based on **similar data points**.

---

## 🧠 Core Idea

> Similar data points are close to each other

---

## 📊 Example

### Problem:
Classify whether a person has a disease or not

### Input:
- age  
- cholesterol  
- blood pressure  

---

👉 KNN finds:
- K nearest data points (neighbors)

👉 Then:
- Majority vote → classification  
- Average → regression  

---

## 🔷 How KNN Works


1. Choose value of K
2. Calculate distance from new point to all data points
3. Select K nearest neighbors
4. Take majority vote (classification)


---

## 📏 Distance Metric

Most common:

`
Euclidean Distance
`
```
d = √[(x1 - x2)² + (y1 - y2)²]
```

---

## 🧠 Intuition

- Points close to each other → similar  
- Far points → different  

---

## 📊 Visualization (Concept)

- New data point placed in space  
- Nearest neighbors decide its class  

---

## 🔷 Choosing K

- Small K → noisy model  
- Large K → smoother but less flexible  

---

## 🎯 Example

If K = 3:

- 2 neighbors → Class A  
- 1 neighbor → Class B  

👉 Final prediction → Class A  

---

## 🔗 Important Note

KNN does NOT learn a model

👉 It stores entire dataset and predicts during runtime

---

## ⚠️ Important Points

- Sensitive to feature scaling  
- Requires distance calculation  
- Works well for small datasets  

---

## 🎯 Real-World Applications

- Recommendation systems  
- Pattern recognition  
- Image classification  

---

## 🧠 Interview Insight

👉 **Question:**<br>
Why is KNN called a lazy learner?

👉 **Answer:**<br>
Because it does not train a model; it stores data and performs computation during prediction.

---

## 🧠 One-Line Summary

> KNN predicts based on similarity by finding the nearest data points.