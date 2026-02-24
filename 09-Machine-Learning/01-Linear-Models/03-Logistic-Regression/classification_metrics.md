# 📊 Classification Metrics

## 📌 Why Evaluation Metrics?

After training a classification model, it is important to measure:

> ❓ How well the model is performing

Accuracy alone is **not always enough**, especially for imbalanced datasets.

---

## 🔢 Confusion Matrix

A confusion matrix shows the comparison between **actual** and **predicted** values.

|                | Predicted Positive | Predicted Negative |
|----------------|-------------------|-------------------|
| Actual Positive | True Positive (TP) | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN) |

---

## 🧠 Key Terms

- **True Positive (TP)** → Correctly predicted positive  
- **True Negative (TN)** → Correctly predicted negative  
- **False Positive (FP)** → Wrongly predicted positive  
- **False Negative (FN)** → Wrongly predicted negative  

---

## 📊 1. Accuracy

```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

### 🧠 Intuition
- Percentage of correct predictions  

### ⚠️ Limitation
- Not reliable for imbalanced datasets  

---

## 📊 2. Precision

```
Precision = TP / (TP + FP)
```

### 🧠 Intuition
> Out of predicted positives, how many are actually correct?

### 🎯 Use Case
- Important when **false positives are costly**
  - Example: spam detection  

---

## 📊 3. Recall (Sensitivity)

```
Recall = TP / (TP + FN)
```

### 🧠 Intuition
> Out of actual positives, how many were correctly identified?

### 🎯 Use Case
- Important when **false negatives are costly**
  - Example: disease detection  

---

## 📊 4. F1 Score

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

### 🧠 Intuition
- Balance between Precision and Recall  

---

## 📊 5. Specificity

```
Specificity = TN / (TN + FP)
```

### 🧠 Intuition
- Ability to correctly identify negatives  

---

## 📊 6. ROC Curve

- Graph between:
  - True Positive Rate (Recall)
  - False Positive Rate  

---

## 📊 7. AUC (Area Under Curve)

- Measures overall performance  
- Value range:
  - 0.5 → random  
  - 1 → perfect model  

---

## ⚖️ When to Use What?

| Scenario | Metric |
|---------|--------|
| Balanced dataset | Accuracy |
| False Positive costly | Precision |
| False Negative costly | Recall |
| Need balance | F1 Score |

---

## 🔗 Connection to Logistic Regression

Logistic Regression outputs probabilities:

```
0 to 1
```

👉 Metrics help evaluate how well classification is done.

---

## ⚠️ Important Points

- Accuracy alone is misleading in imbalanced data  
- Always check Precision & Recall  
- F1 Score is preferred in many real-world cases  

---

## 🧠 Interview Insight

👉 Question:
Why is accuracy not enough?

👉 Answer:
Because in imbalanced datasets, a model can achieve high accuracy by predicting the majority class, but still perform poorly on the minority class.

---

## 🧠 One-Line Summary

> Classification metrics evaluate model performance beyond accuracy using precision, recall, and F1 score.