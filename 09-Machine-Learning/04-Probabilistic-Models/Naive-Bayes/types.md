# 📊 Types of Naive Bayes

## 📌 Overview

Naive Bayes has different variants based on the type of data.

Each type assumes a different distribution of features.

---

# 🔷 1. Gaussian Naive Bayes

## 📌 Used For
- Continuous numerical data  

---

## 🧠 Assumption
Features follow a **normal (Gaussian) distribution**

---

## 📊 Example

- Age  
- Salary  
- Height  

---

## 🎯 When to Use?

- When features are real-valued numbers  
- Common in general ML problems  

---

## 🔷 Implementation

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
```

---

# 🔷 2. Multinomial Naive Bayes

## 📌 Used For

- Count data (discrete values)

---

## 🧠 Assumption

Features represent frequency/counts

---

## 📊 Example

- Number of times a word appears in a document

---

## 🎯 When to Use?

- Text classification
- NLP tasks

---

## 🔷 Implementation

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
```

---

# 🔷 3. Bernoulli Naive Bayes

## 📌 Used For

- Binary data (0 or 1)

---

## 🧠 Assumption

Features represent presence or absence

---

## 📊 Example

- Word present (1) or not (0)

---

## 🎯 When to Use?

- Binary feature datasets
- Text classification with binary features

---

## 🔷 Implementation

```python
from sklearn.naive_bayes import BernoulliNB

model = BernoulliNB()
```

----

# ⚖️ Comparison

| Type       | Data Type   | Use Case                |
|------------|-------------|-------------------------|
| Gaussian   | Continuous  | General ML problems     |
| Multinomial| Counts      | Text classification     |
| Bernoulli  | Binary      | Presence/absence data   |

---

## ⚠️ Important Points
- Choice depends on data type  
- Using wrong type reduces performance  
- All follow same Bayes principle  

---

## 🧠 Interview Insight

👉 **Question:**<br>
Difference between Gaussian and Multinomial Naive Bayes?  

👉 **Answer:**<br>
Gaussian is used for continuous data, while Multinomial is used for count-based data like text frequency.  

---

## 🧠 One-Line Summary

> Different Naive Bayes types are used based on whether data is continuous, count-based, or binary.