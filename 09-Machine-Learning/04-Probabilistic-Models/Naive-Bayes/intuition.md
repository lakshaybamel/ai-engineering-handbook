# 🧠 Naive Bayes — Intuition

## 📌 What is Naive Bayes?

Naive Bayes is a **classification algorithm** based on **Bayes' Theorem**.

It predicts the class of data using **probability**.

---

## 🧠 Core Idea

> Choose the class with the **highest probability** given the input features

---

## 📊 Example

### Problem:
Classify whether an email is **Spam or Not Spam**

### Input Features:
- contains "offer"  
- contains "win"  
- contains "free"  

---

👉 Model calculates:

```
P(Spam | Features)
P(Not Spam | Features)
```

👉 Then selects:

```
Higher probability → Final class
```

---

## 📐 Bayes' Theorem

```
P(A | B) = [P(B | A) × P(A)] / P(B)
```

Where:
- `P(A | B)` → Probability of A given B  
- `P(B | A)` → Likelihood  
- `P(A)` → Prior  
- `P(B)` → Evidence  

---

## 🧠 Intuition of Formula

> Probability of class given features  
= (Likelihood × Prior) / Evidence

---

## 🔷 What Does "Naive" Mean?

👉 Assumption:
> All features are **independent**

---

### Example:

In spam detection:
- "free"  
- "win"  

👉 Naive Bayes assumes:

```
P(free AND win | Spam) = P(free | Spam) × P(win | Spam)
```

➡️ This simplifies calculation

---

## ⚠️ Reality

- Features are usually NOT independent  
- But algorithm still works well  

---

## 🔷 Why It Works Well?

- Simple and fast  
- Works well on high-dimensional data  
- Good for text classification  

---

## 📊 How Model Works

```
Input Features
    ↓
Apply Bayes Theorem
    ↓
Compute probabilities for each class
    ↓
Choose highest probability
```

---

## 🎯 Real-World Applications

- Spam detection  
- Sentiment analysis  
- Document classification  
- Medical diagnosis  

---

## ⚠️ Important Points

- Based on probability  
- Assumes feature independence  
- Works well with categorical and text data  

---

## 🧠 Interview Insight

👉 **Question:**<br>
Why is it called Naive Bayes?

👉 **Answer:**<br>
Because it assumes all features are independent, which is a naive assumption in real-world data.

---

## 🧠 One-Line Summary

> Naive Bayes predicts class based on probability using Bayes' theorem with an independence assumption.