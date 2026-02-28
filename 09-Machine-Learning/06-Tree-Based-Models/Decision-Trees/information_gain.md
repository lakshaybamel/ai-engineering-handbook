# 🌳 Information Gain & Variance Reduction

## 📌 Overview

Information Gain is used in Decision Trees to decide:

> ❓ Which feature should be used to split the data

It is based on **reducing impurity**.

---

# 🔷 1. Information Gain (Classification)

## 📌 Definition

Information Gain measures the **reduction in impurity (entropy or gini)** after a split.

---

## 📐 Formula

```
Information Gain = Parent Impurity - Weighted Child Impurity
```

---

## 🧠 Intuition

- Before split → data is mixed  
- After split → data becomes more pure  

👉 Good split = high information gain  

---

## 📊 Example

If parent entropy = 1  

After split:
- Left child entropy = 0.2  
- Right child entropy = 0.3  

👉 New impurity = weighted average  

👉 Information Gain = reduction from 1  

---

## 🎯 Goal

> Choose the split with **maximum information gain**

---

# 🔷 How Decision Tree Uses It

```
For each feature:
Calculate Information Gain
Select feature with highest gain
```

---

## 🔗 Connection to Entropy & Gini

- Information Gain uses:
  - Entropy OR  
  - Gini  

👉 Both measure impurity  

---

# 🔷 2. Variance Reduction (Regression)

## 📌 Definition

In regression, trees use **variance reduction** instead of entropy/gini.

---

## 🧠 Why?

- Output is continuous  
- Not classification  

---

## 📐 Formula

```
Variance Reduction = Parent Variance - Weighted Child Variance
```

---

## 🧠 Intuition

- Good split reduces spread of values  
- Data becomes more consistent  

---

## 📊 Example

Before split:
- Values widely spread  

After split:
- Values grouped tightly  

👉 Variance decreases  

---

## 🎯 Goal

> Choose split with **maximum variance reduction**

---

# ⚖️ Classification vs Regression

| Task | Metric |
|-----|-------|
| Classification | Information Gain |
| Regression | Variance Reduction |

---

# ⚠️ Important Points

- Higher gain = better split  
- Used at every node  
- Core of decision tree building  

---

## 🧠 Interview Insight

👉 **Question:**  
What is Information Gain?

👉 **Answer:**  
It is the reduction in impurity after splitting the data, used to select the best feature in decision trees.

---

## 🧠 One-Line Summary

> Information Gain selects the best split by maximizing impurity reduction, while variance reduction is used for regressio