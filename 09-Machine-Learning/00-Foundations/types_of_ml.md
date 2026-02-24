# 🧠 Types of Machine Learning

Machine Learning is mainly divided into three types based on how the model learns from data:

1. Supervised Learning  
2. Unsupervised Learning  
3. Reinforcement Learning  

---

## 1️⃣ Supervised Learning

### 📌 Definition
Supervised Learning is a type of ML where the model learns from **labeled data**.

👉 Each input has a **correct output (label)**.

---

### 🧠 Intuition

Think like:
> Teacher gives questions AND answers → you learn pattern

---

### 📊 Example

| Age | Income | Buy Insurance |
|-----|--------|--------------|
| 25  | 30k    | Yes          |
| 40  | 60k    | No           |

👉 Model learns:

(age, income) → decision


---

### 🔹 Types of Supervised Learning

#### 1. Regression
- Output is continuous (number)
- Examples:
  - House price prediction
  - Salary prediction

---

#### 2. Classification
- Output is category
- Examples:
  - Spam / Not Spam
  - Disease / No Disease

---

### ⚙️ Common Algorithms

- Linear Regression  
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Trees  
- Naive Bayes  

---

## 2️⃣ Unsupervised Learning

### 📌 Definition
Unsupervised Learning is a type of ML where the model learns from **unlabeled data**.

👉 No correct answers are given.

---

### 🧠 Intuition

Think like:
> No teacher → you find patterns yourself

---

### 📊 Example

Customer data without labels:
- age
- spending

👉 Model groups similar customers → **segments**

---

### 🔹 Types of Unsupervised Learning

#### 1. Clustering
- Group similar data points
- Example:
  - Customer segmentation

---

#### 2. Dimensionality Reduction
- Reduce number of features
- Keeps important information
- Example:
  - PCA (Principal Component Analysis)

---

### ⚙️ Common Algorithms

- K-Means Clustering  
- Hierarchical Clustering  
- DBSCAN  
- PCA  

---

## 3️⃣ Reinforcement Learning (RL)

### 📌 Definition
Reinforcement Learning is a type of ML where an agent learns by **interacting with environment** and receiving rewards or penalties.

---

### 🧠 Intuition

Think like:
> Learning by trial and error

---

### 📊 Example

- Game playing (Chess, PUBG bots)
- Self-driving cars

👉 Correct action → reward  
👉 Wrong action → penalty  

---

### ⚙️ Key Concepts

- Agent → learner  
- Environment → where agent acts  
- Action → decision taken  
- Reward → feedback  

---

## 🔁 Quick Comparison

| Type              | Data Type     | Goal                     |
|------------------|--------------|--------------------------|
| Supervised       | Labeled       | Predict output           |
| Unsupervised     | Unlabeled     | Find patterns            |
| Reinforcement    | Interaction   | Maximize reward          |

---

## 🎯 When to Use What?

- Use **Supervised Learning** → when you have labeled data  
- Use **Unsupervised Learning** → when no labels exist  
- Use **Reinforcement Learning** → when decisions are sequential  

---

## 🧠 One-Line Summary

> Supervised → learn with answers  
> Unsupervised → find hidden patterns  
> Reinforcement → learn by rewards  

---