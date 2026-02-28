# 🌳 Decision Trees

## 📌 Overview

Decision Trees are supervised machine learning algorithms used for:

- Classification  
- Regression  

They work by splitting data into smaller subsets based on feature values.

---

## 🧠 Key Idea

> Split the data recursively to make it more pure at each step

---

## 🔗 Topics Covered

### 1. Entropy & Gini

- Measure impurity of data  
- Used to decide how good a split is  

📄 File: [`entropy_gini.md`](./entropy_gini.md)

---

### 2. Information Gain & Variance Reduction

- Selects the best feature for splitting  
- Maximizes impurity reduction  

📄 File: [`information_gain.md`](./information_gain.md)

---

### 3. Pruning

- Prevents overfitting  
- Controls tree complexity  

📄 File: [`pruning.md`](./pruning.md)

---

### 4. Decision Tree Classifier

- Predicts categorical output  
- Includes pre-pruning and post-pruning  

📓 Notebook: [`decision_tree_classifier.ipynb`](./decision_tree_classifier.ipynb)

---

### 5. Decision Tree Regressor

- Predicts continuous values  
- Uses variance reduction  

📓 Notebook: [`decision_tree_regressor.ipynb`](./decision_tree_regressor.ipynb)

---

## ⚙️ Workflow

```
Input Data
    ↓
Calculate impurity (Entropy/Gini)
    ↓
Select best feature (Information Gain)
    ↓
Split data
    ↓
Repeat recursively
    ↓
Apply pruning
```

---

## ⚠️ Important Points

- Easy to understand and visualize  
- Can handle non-linear data  
- No need for feature scaling  
- Prone to overfitting  

---

## 🎯 Learning Outcome

After completing this section, the following should be clear:

- How decision trees split data  
- Difference between entropy and gini  
- How information gain works  
- Importance of pruning  
- How to implement classifier and regressor  

---

## 🧠 One-Line Summary

> Decision Trees split data based on impurity reduction, and pruning helps control overfitting for better generalization.