# 📊 Train, Validation & Test Data

## 📌 Overview

In Machine Learning, data is divided into different parts to:
- train the model  
- tune the model  
- evaluate performance  

---

## 🔷 1. Training Data

### 📌 Definition
Used to **train the model**

---

### 🧠 Intuition
> Model learns patterns from this data

---

### 📊 Usage
- Fit the model  
- Learn parameters (weights)

---

## 🔷 2. Validation Data

### 📌 Definition
Used to **tune the model**

---

### 🧠 Intuition
> Helps decide how to improve the model

---

### 📊 Usage
- Hyperparameter tuning  
- Model selection  

---

## 🔷 3. Test Data

### 📌 Definition
Used to **evaluate final performance**

---

### 🧠 Intuition
> Simulates unseen real-world data

---

### 📊 Usage
- Final evaluation only  
- Not used during training  

---

# ⚙️ Data Split Example

```
Dataset → Train + Validation + Test
```

Typical split:

- Training → 70%  
- Validation → 15%  
- Test → 15%  

---

# 🔁 Common Practice (Simplified)

In many cases:

```
Train + Test Split
```

Then use:
- Cross-validation instead of validation set  

---

# 🧠 Why Not Use Same Data?

If same data is used for training and testing:

👉 Model may memorize data  
👉 Leads to overfitting  

---

# 🔗 Connection to Your Work

You used:

```python
train_test_split()
```

👉 This creates:

- Training data
- Testing data

Validation can be handled using:

- Cross-validation

---

## ⚠️ Important Points

- Never use test data for training
- Validation helps in tuning
- Test data should be untouched

---

## 🧠 Interview Insight

👉 **Question:**<br>
Why do we need validation data?

👉 **Answer:**<br>
To tune hyperparameters and select the best model without affecting test data performance.

---

## 🧠 One-Line Summary

> Training data learns, validation data tunes, and test data evaluates the model.