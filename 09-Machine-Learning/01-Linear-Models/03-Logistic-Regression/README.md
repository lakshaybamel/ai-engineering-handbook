# 🧠 Logistic Regression

## 📌 Overview

Logistic Regression is a **supervised machine learning algorithm** used for **classification problems**.

It predicts the **probability** of a data point belonging to a particular class.

---

## 🧠 Key Idea

Instead of predicting a continuous value, Logistic Regression:

- Uses a **linear equation**
- Applies a **sigmoid function**
- Outputs a **probability (0 to 1)**

---

## ⚙️ How It Works

`
Input Features → Linear Equation → Sigmoid Function → Probability → Class
`

---

## 📊 Types of Problems

- Binary Classification  
  - Yes / No  
  - 0 / 1  
- Examples:
  - Disease Prediction  
  - Spam Detection  
  - Fraud Detection  

---

## 🔗 Topics Covered

### 1. Intuition

- Understanding classification vs regression  
- Why Logistic Regression is used  
- Role of sigmoid function  

📄 File: [`intuition.md`](./intuition.md)

---

### 2. Cost Function

- Why MSE is not suitable  
- Log Loss (Binary Cross Entropy)  
- Optimization using Gradient Descent  

📄 File: [`cost_function.md`](./cost_function.md)

---

### 3. Classification Metrics

- Confusion Matrix  
- Accuracy, Precision, Recall, F1 Score  
- ROC & AUC  

📄 File: [`classification_metrics.md`](./classification_metrics.md)

---

### 4. Logistic Regression (Implementation)

- Model training using sklearn  
- Prediction and probability output  
- Evaluation using classification metrics  

📓 Notebook: [`logistic_regression.ipynb`](./logistic_regression.ipynb)

---

## ⚠️ Important Concepts

- Output is probability, not direct class  
- Uses sigmoid function  
- Threshold (default = 0.5) decides class  
- Sensitive to feature scaling  

---

## 🎯 Learning Outcome

After completing this section, the following should be clear:

- How Logistic Regression works  
- Difference between regression and classification  
- Role of sigmoid function  
- How to evaluate classification models  
- How to implement Logistic Regression using sklearn  

---

## 🧠 One-Line Summary

> Logistic Regression predicts probabilities using a sigmoid function to perform classification tasks.