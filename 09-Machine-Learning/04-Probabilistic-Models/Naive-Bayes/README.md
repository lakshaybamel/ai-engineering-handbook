# 🧠 Naive Bayes

## 📌 Overview

Naive Bayes is a **supervised machine learning algorithm** used for **classification tasks**.

It is based on **Bayes' Theorem** and works using **probability**.

---

## 🧠 Key Idea

Naive Bayes predicts the class by calculating:

> Probability of a class given input features

It selects the class with the **highest probability**.

---

## 📐 Bayes' Theorem

```
P(A | B) = [P(B | A) × P(A)] / P(B)
```

---

## ⚠️ Naive Assumption

- Assumes all features are **independent**  
- This assumption is rarely true in real data  
- Still performs well in practice  

---

## 🔗 Topics Covered

### 1. Intuition

- Basic understanding of probability-based classification  
- Role of Bayes' theorem  
- Feature independence assumption  

📄 File: [`intuition.md`](./intuition.md)

---

### 2. Types of Naive Bayes

- Gaussian Naive Bayes  
- Multinomial Naive Bayes  
- Bernoulli Naive Bayes  

📄 File: [`types.md`](./types.md)

---

### 3. Naive Bayes (Implementation)

- Training model using sklearn  
- Making predictions  
- Evaluating performance  

📓 Notebook: [`naive_bayes.ipynb`](./naive_bayes.ipynb)

---

## ⚙️ Workflow

```
Input Features
    ↓
Apply Bayes Theorem
    ↓
Compute probabilities for each class
    ↓
Select class with highest probability
```

---

## 🎯 Learning Outcome

After completing this section, the following should be clear:

- How Naive Bayes works  
- Role of probability in classification  
- Different types of Naive Bayes  
- How to implement Naive Bayes using sklearn  

---

## ⚠️ Important Points

- Works well with high-dimensional data  
- Fast and efficient  
- Assumes feature independence  
- Commonly used in text classification  

---

## 🧠 One-Line Summary

> Naive Bayes is a probabilistic classifier that uses Bayes' theorem with an independence assumption to pre