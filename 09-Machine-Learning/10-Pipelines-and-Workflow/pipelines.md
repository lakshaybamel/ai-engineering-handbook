# 🔗 Machine Learning Pipelines

## 📌 Overview

A Pipeline is a way to **automate the ML workflow** by chaining multiple steps together.

👉 Instead of writing separate code for each step, we combine them

---

## 🧠 Core Idea

> Combine preprocessing + model into a single workflow

---

## 🔷 Why Pipelines?

Without Pipeline:

* Manual preprocessing
* Risk of data leakage
* Repetitive code

With Pipeline:

* Clean code
* Reproducible workflow
* No leakage

---

## 🔷 Example Workflow

```text
Raw Data
   ↓
Scaling
   ↓
Encoding
   ↓
Model Training
```

👉 Pipeline combines all steps

---

## 🔷 Example Code

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipeline.fit(X_train, y_train)
```

---

## 🔷 Key Benefits

* Prevents data leakage
* Simplifies workflow
* Easy to use with GridSearchCV
* Cleaner and modular code

---

## 🔷 When to Use

* Always recommended in ML projects
* When multiple preprocessing steps exist
* When doing hyperparameter tuning

---

## ⚠️ Important Points

* Order of steps matters
* Works with transformers + estimators
* Required for production-ready code

---

## 🧠 Interview Insight

👉 Question:  
What is a Pipeline in Machine Learning?

👉 Answer:  
A pipeline is a sequence of preprocessing and modeling steps combined into a single workflow to ensure clean and consistent processing.

---

## 🧠 One-Line Summary

> Pipeline automates preprocessing and modeling steps into a single clean workflow.
