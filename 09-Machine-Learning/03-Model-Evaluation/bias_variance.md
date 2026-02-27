# ⚖️ Bias vs Variance

## 📌 Overview

Bias and Variance are two types of errors that affect machine learning models.

Understanding them helps in:
- improving model performance  
- avoiding overfitting and underfitting  

---

# 🔷 1. Bias

## 📌 Definition

Bias is the error caused by **simplifying assumptions** in the model.

---

## 🧠 Intuition

> Model is too simple to capture patterns

---

## 📉 Characteristics

- High training error  
- High testing error  
- Underfitting  

---

## 🔍 Example

Fitting a straight line to complex data

---

# 🔷 2. Variance

## 📌 Definition

Variance is the error caused by **model sensitivity to training data**

---

## 🧠 Intuition

> Model learns noise instead of pattern

---

## 📈 Characteristics

- Low training error  
- High testing error  
- Overfitting  

---

## 🔍 Example

Model fits every data point exactly

---

# ⚖️ Bias vs Variance

| Feature | Bias | Variance |
|--------|------|---------|
| Model Type | Simple | Complex |
| Training Error | High | Low |
| Testing Error | High | High |
| Problem | Underfitting | Overfitting |

---

# 🎯 Bias-Variance Tradeoff

## 📌 Concept

> Need balance between bias and variance

---

## 🧠 Goal

- Not too simple  
- Not too complex  

👉 Achieve **good generalization**

---

## 📊 Ideal Case

- Low bias  
- Low variance  

---

# 🔗 Connection to Overfitting

- High Bias → Underfitting  
- High Variance → Overfitting  

---

# 🛠️ How to Reduce Bias

- Increase model complexity  
- Add more features  
- Reduce regularization  

---

# 🛠️ How to Reduce Variance

- Use more data  
- Apply regularization  
- Reduce model complexity  
- Use cross-validation  

---

# ⚠️ Important Points

- Cannot minimize both completely  
- Need balance  
- Depends on dataset and model  

---

## 🧠 Interview Insight

👉 **Question:**<br>
What is bias-variance tradeoff?

👉 **Answer:**<br>
It is the balance between underfitting (high bias) and overfitting (high variance) to achieve optimal model performance.

---

## 🧠 One-Line Summary

> Bias causes underfitting, variance causes overfitting, and the goal is to balance both.