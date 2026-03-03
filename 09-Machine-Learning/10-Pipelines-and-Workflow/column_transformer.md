# 🧩 Column Transformer

## 📌 Overview

ColumnTransformer is used to apply **different transformations to different columns**.

👉 Useful when dataset has:

* Numerical features
* Categorical features

---

## 🧠 Core Idea

> Apply different preprocessing to different columns

---

## 🔷 Why Needed?

Example:

* Scale numerical data
* Encode categorical data

👉 Both require different transformations

---

## 🔷 Example

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['age', 'salary']),
    ('cat', OneHotEncoder(), ['gender', 'city'])
])
```

---

## 🔷 Combined with Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('model', LogisticRegression())
])
```

---

## 🔷 Advantages

* Handles mixed data types
* Clean and organized preprocessing
* Integrates with pipelines

---

## 🔷 When to Use

* Dataset has both categorical & numerical features
* Complex preprocessing required

---

## ⚠️ Important Points

* Must specify column names or indices
* Works best with pipelines
* Prevents manual preprocessing mistakes

---

## 🧠 Interview Insight

👉 Question:
What is ColumnTransformer?

👉 Answer:
It allows applying different preprocessing steps to different columns in a dataset.

---

## 🧠 One-Line Summary

> ColumnTransformer applies different transformations to different columns efficiently.
