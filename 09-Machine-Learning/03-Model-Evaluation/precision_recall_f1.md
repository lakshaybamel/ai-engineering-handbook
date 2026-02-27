# 📊 Precision, Recall & F1 Score

## 📌 Overview

Precision, Recall, and F1 Score are evaluation metrics used to measure the performance of a **classification model**, especially when data is imbalanced.

These metrics are derived from the **confusion matrix**.

---

## 🔗 Confusion Matrix Reference

|                | Predicted Positive | Predicted Negative |
|----------------|-------------------|-------------------|
| Actual Positive | TP | FN |
| Actual Negative | FP | TN |

---

# 🔷 1. Precision

## 📐 Formula

```
Precision = TP / (TP + FP)
```

---

## 🧠 Intuition

> Out of all predicted positives, how many are actually correct?

---

## 🎯 When Precision is Important?

- When **false positives are costly**

### Example:
- Spam detection  
- Predicting fraud (false alarm is costly)

---

# 🔷 2. Recall (Sensitivity)

## 📐 Formula

```
Recall = TP / (TP + FN)
```

---

## 🧠 Intuition

> Out of all actual positives, how many were correctly identified?

---

## 🎯 When Recall is Important?

- When **false negatives are dangerous**

### Example:
- Disease detection  
- Fraud detection  

---

# 🔷 3. F1 Score

## 📐 Formula

```
F1 Score = 2 × (Precision × Recall) / (Precision + Recall)
```

---

## 🧠 Intuition

- Balance between Precision and Recall  
- Useful when both are important  

---

# 📊 Example

| Metric | Value |
|-------|------|
| Precision | 0.80 |
| Recall | 0.60 |
| F1 Score | 0.69 |

---

## ⚖️ Trade-off

- High Precision → Low Recall  
- High Recall → Low Precision  

👉 Need balance → F1 Score  

---

## ⚠️ Important Points

- Accuracy can be misleading  
- Precision & Recall give deeper insight  
- F1 Score balances both  

---

## 🔗 Connection to Models

Used in:
- Logistic Regression  
- KNN  
- Naive Bayes  
- All classification models  

---

## 🧠 Interview Insight

👉 **Question:**<br>
Difference between Precision and Recall?

👉 **Answer:**<br>
Precision measures correctness of positive predictions, while Recall measures how many actual positives were captured.

---

## 🧠 One-Line Summary

> Precision measures correctness, Recall measures completeness, and F1 Score balances both.