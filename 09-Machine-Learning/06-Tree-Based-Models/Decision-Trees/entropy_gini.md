# 🌳 Entropy & Gini Impurity

## 📌 Overview

Entropy and Gini Impurity are metrics used in Decision Trees to measure:

> ❓ How pure or impure a dataset is

They help the model decide:
👉 where to split the data

---

## 🧠 What is Impurity?

- Pure → all data points belong to same class  
- Impure → mixed classes  

---

## 🔷 1. Entropy

## 📌 Definition

Entropy measures the level of **uncertainty or randomness** in the data.

---

## 📐 Formula

```
Entropy = - Σ (p × log₂ p)
```

Where:
- `p` = probability of each class  

---

## 🧠 Intuition

- High entropy → mixed data  
- Low entropy → pure data  

---

## 📊 Values

| Case | Entropy |
|-----|--------|
| All same class | 0 |
| 50-50 split | 1 (maximum) |

---

## 🔷 Example

If dataset has:
- 50% Yes  
- 50% No  

👉 Entropy = 1 (high impurity)

---

## 🔷 2. Gini Impurity

## 📌 Definition

Gini measures the probability of **incorrect classification**

---

## 📐 Formula

```
Gini = 1 - Σ (p²)
```

---

## 🧠 Intuition

- Measures how often a randomly chosen element would be misclassified  

---

## 📊 Values

| Case | Gini |
|-----|------|
| Pure node | 0 |
| 50-50 split | 0.5 |

---

## 🔷 Example

If:
- 50% Yes  
- 50% No  

👉 Gini = 0.5  

---

# ⚖️ Entropy vs Gini

| Feature | Entropy | Gini |
|--------|--------|------|
| Range | 0 to 1 | 0 to 0.5 |
| Speed | Slower (log) | Faster |
| Use | More theoretical | More practical |

---

## 🧠 Key Difference

- Entropy uses logarithm  
- Gini is simpler and faster  

---

## 🎯 Which One is Better?

👉 Both give similar results  

👉 In practice:
- Gini is used more (faster)  

---

## 🔗 Connection to Decision Trees

Decision Tree chooses split that:

👉 Minimizes impurity  
👉 (low entropy / low gini)

---

## ⚠️ Important Points

- Used only for classification  
- Helps find best split  
- Lower value = better split  

---

## 🧠 Interview Insight

👉 **Question:**  
Difference between Entropy and Gini?

👉 **Answer:**  
Both measure impurity, but entropy uses log and is slower, while Gini is simpler and faster.

---

## 🧠 One-Line Summary

> Entropy and Gini measure impurity in data and help decision trees find the best split.