# 🔁 Cross Validation

## 📌 What is Cross Validation?

Cross Validation is a technique used to evaluate model performance more reliably by using **different subsets of data for training and validation**.

---

## 🧠 Why Cross Validation is Needed?

Using a single train-test split can lead to:
- biased results  
- dependency on specific split  

👉 Cross Validation solves this by:
- using multiple splits  
- averaging performance  

---

# 🔷 K-Fold Cross Validation

## 📌 Concept

- Data is divided into **K equal parts (folds)**  
- Model is trained and validated **K times**

---

## 🔁 Process

For K = 5:

1. Split data into 5 parts  
2. Train on 4 parts, test on 1 part  
3. Repeat until each part is used as test  

---

## 📊 Example

| Fold | Training Data | Validation Data |
|------|--------------|----------------|
| 1 | 4 parts | 1 part |
| 2 | 4 parts | 1 part |
| ... | ... | ... |
| 5 | 4 parts | 1 part |

---

## 📈 Final Result

```
Final Score = Average of all folds
```

---

# 🔷 Implementation (sklearn)

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)

print("Scores:", scores)
print("Average Score:", scores.mean())
```

---

## 🔷 Advantages

- Better performance estimate
- Reduces overfitting risk
- Uses full dataset efficiently

---

## ⚠️ Important Points

- Slower than simple train-test split
- Used mainly during model evaluation
- Common values of K:
    - 5
    - 10

---

## 🔗 Connection to Your Workflow

Instead of:
```
Train → Test once
```
Use:
```
Train → Validate multiple times
```

---

## 🧠 Interview Insight

👉 **Question:**<br>
Why use cross-validation?

👉 **Answer:**<br>
To get a more reliable estimate of model performance by evaluating it on multiple data splits.

---

## 🧠 One-Line Summary

> Cross Validation evaluates model performance by training and testing on multiple data splits.