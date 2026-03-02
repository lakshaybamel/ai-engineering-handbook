# 🧠 Types of Ensemble Learning

## 📌 Overview

Ensemble learning combines multiple models to improve performance.

There are mainly **two types of ensembles**:

* Homogeneous Ensemble
* Heterogeneous Ensemble

---

## 🔷 1. Homogeneous Ensemble

## 📌 Definition

All models used are of the **same type**.

---

## 🧠 Example

* Multiple Decision Trees
* Multiple Logistic Regression models

---

## 🔷 Algorithms

* Bagging
* Random Forest
* Boosting (same base learner)

---

## 🧠 Key Idea

> Same algorithm, different data or parameters

---

## 🔷 How It Works

* Train multiple models of same type
* Combine their outputs

---

## 🔷 Advantages

* Simple to implement
* Works well with unstable models (like trees)

---

## 🔷 Example Code

```python id="h2f6gk"
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
```

---

---

## 🔷 2. Heterogeneous Ensemble

## 📌 Definition

Different types of models are combined.

---

## 🧠 Example

* Logistic Regression + Decision Tree + SVM

---

## 🔷 Techniques

* Voting
* Stacking
* Blending

---

## 🧠 Key Idea

> Combine different algorithms to capture different patterns

---

## 🔷 Advantages

* More powerful
* Captures diverse patterns

---

## 🔷 Example Code

```python id="5m2l8y"
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

model = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression()),
        ('dt', DecisionTreeClassifier())
    ],
    voting='hard'
)

model.fit(X_train, y_train)
```

---

# ⚖️ Comparison

| Feature     | Homogeneous | Heterogeneous |
| ----------- | ----------- | ------------- |
| Models      | Same        | Different     |
| Complexity  | Low         | High          |
| Diversity   | Less        | More          |
| Performance | Good        | Better        |

---

## ⚠️ Important Points

* Diversity in models improves performance
* More complex ensembles require more tuning
* Not always necessary for simple problems

---

## 🧠 Interview Insight

👉 Question:  
Difference between homogeneous and heterogeneous ensemble?

👉 Answer:  
Homogeneous ensembles use the same type of models, while heterogeneous ensembles combine different types of models.

---

## 🧠 One-Line Summary

> Ensemble learning can use either similar models (homogeneous) or different models (heterogeneous) to improve performance.
