# 📊 Confusion Matrix

## 📌 What is Confusion Matrix?

Confusion Matrix is a table used to evaluate the performance of a **classification model**.

It compares:
- Actual values  
- Predicted values  

---

## 📊 Structure

|                | Predicted Positive | Predicted Negative |
|----------------|-------------------|-------------------|
| Actual Positive | True Positive (TP) | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN) |

---

## 🧠 Key Terms

### 🔷 True Positive (TP)
- Model correctly predicts positive  
- Example: Disease → predicted as disease  

---

### 🔷 True Negative (TN)
- Model correctly predicts negative  
- Example: No disease → predicted as no disease  

---

### 🔷 False Positive (FP)
- Model predicts positive incorrectly  
- Example: No disease → predicted as disease  

👉 Also called **Type I Error**

---

### 🔷 False Negative (FN)
- Model predicts negative incorrectly  
- Example: Disease → predicted as no disease  

👉 Also called **Type II Error**

---

## 📊 Example

| Actual | Predicted |
|--------|----------|
| 1 | 1 |
| 0 | 1 |
| 1 | 0 |
| 0 | 0 |

👉 Counts:
- TP = 1  
- FP = 1  
- FN = 1  
- TN = 1  

---

## 🧠 Why Confusion Matrix is Important?

- Gives detailed insight into model performance  
- Helps calculate:
  - Accuracy  
  - Precision  
  - Recall  
  - F1 Score  

---

## ⚠️ Accuracy Limitation

Confusion matrix helps understand why:

👉 Accuracy alone is not enough

Example:
- 95% data = negative  
- Model predicts all negative  

👉 Accuracy = 95%  
👉 But model is useless  

---

## 🔗 Connection to Metrics

From confusion matrix we derive:

- Accuracy  
- Precision  
- Recall  
- F1 Score  

---

## ⚠️ Important Points

- Used only for classification  
- Base for all evaluation metrics  
- Helps understand error types  

---

## 🧠 Interview Insight

👉 **Question:**<br>
Why use confusion matrix?

👉 **Answer:**<br>
Because it provides a detailed breakdown of correct and incorrect predictions, helping evaluate model performance beyond accuracy.

---

## 🧠 One-Line Summary

> Confusion Matrix shows how well a classification model performs by comparing actual and predicted values.