# 📊 Regression vs Classification

Regression and Classification are the two main types of **Supervised Machine Learning problems**.

---

## 📌 What is Regression?

### 🔹 Definition
Regression is used when the output is a **continuous numerical value**.

---

### 🧠 Intuition

> Predicting "how much" or "how many"

---

### 📊 Examples

- House price prediction  
- Salary prediction  
- Insurance cost prediction  

---

### 📥 Input → Output

(age, bmi, smoker) → insurance cost

---

### ⚙️ Common Algorithms

- Linear Regression  
- Ridge Regression  
- Lasso Regression  

---

## 📌 What is Classification?

### 🔹 Definition
Classification is used when the output is a **category or class label**.

---

### 🧠 Intuition

> Predicting "which category"

---

### 📊 Examples

- Spam / Not Spam  
- Disease / No Disease  
- Pass / Fail  

---

### 📥 Input → Output

(age, cholesterol) → heart disease (Yes/No) 

---

### ⚙️ Common Algorithms

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Trees  
- Naive Bayes  

---

## 🔁 Key Differences

| Feature            | Regression                    | Classification              |
|--------------------|-----------------------------|-----------------------------|
| Output Type        | Continuous (number)         | Categorical (label)         |
| Example            | Price, Salary               | Spam, Disease               |
| Goal               | Predict value               | Predict class               |
| Algorithms         | Linear, Ridge, Lasso        | Logistic, KNN, Trees        |

---

## ⚠️ Important Concept

Sometimes classification outputs look like numbers (0 and 1), but:

👉 They represent **categories**, not continuous values

Example:

0 = No disease<br>
1 = Disease


---

## 🔍 Visualization Difference

- Regression → best fit line/curve  
- Classification → decision boundary  

---

## 🎯 When to Use What?

- Use **Regression** → when output is numeric  
- Use **Classification** → when output is category  

---

## 🧠 One-Line Summary

> Regression predicts numbers, Classification predicts categories.