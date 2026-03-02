# 🤖 Ensemble Learning

## 📌 Overview

Ensemble Learning combines multiple machine learning models to improve accuracy, stability, and generalization.

Instead of relying on a single model, we use a group of models to make better predictions.

---

## 🧠 Core Idea

> Multiple weak/strong models together perform better than a single model

---

## 🔗 Topics Covered

### 1. Bagging

* Parallel learning
* Reduces variance
* Uses bootstrap sampling

📄 Files:

* [`bagging.md`](./bagging.md)
* [`Bagging/bagging_classifier.ipynb`](./Bagging/bagging_classifier.ipynb)
* [`Bagging/bagging_regressor.ipynb`](./Bagging/bagging_regressor.ipynb)

---

### 2. Boosting

* Sequential learning
* Each model corrects previous errors
* Reduces bias

📄 Files:

* [`boosting.md`](./boosting.md)
* [`Boosting/README.md`](./Boosting/README.md)

#### Algorithms Covered

* Gradient Boosting
* AdaBoost
* XGBoost

---

### 3. Random Forest

* Multiple decision trees
* Uses bagging + feature randomness
* Reduces overfitting

📄 Files:

* [`Random-Forest/README.md`](./Random-Forest/README.md)
* [`Random-Forest/intuition.md`](./Random-Forest/intuition.md)
* [`Random-Forest/oob.md`](./Random-Forest/oob.md)
* [`Random-Forest/random_forest.ipynb`](./Random-Forest/random_forest.ipynb)
* [`Random-Forest/comparison_with_dt.md`](./Random-Forest/comparison_with_dt.md)

---

### 4. Voting

* Combines predictions from multiple models
* Hard voting (majority)
* Soft voting (probability-based)

📄 Files:

* [`Voting/voting.md`](./Voting/voting.md)
* [`Voting/voting.ipynb`](./Voting/voting.ipynb)

---

### 5. Stacking

* Uses a meta-model to combine predictions
* Learns how to combine models

📄 Files:

* [`Stacking/stacking.md`](./Stacking/stacking.md)
* [`Stacking/stacking.ipynb`](./Stacking/stacking.ipynb)

---

## ⚙️ Ensemble Types Summary

| Method   | Learning Style | Goal                |
| -------- | -------------- | ------------------- |
| Bagging  | Parallel       | Reduce variance     |
| Boosting | Sequential     | Reduce bias         |
| Voting   | Parallel       | Combine predictions |
| Stacking | Meta-learning  | Learn combination   |

---

## ⚠️ Important Points

* Ensemble methods improve performance
* Model diversity is important
* More computation required
* Overfitting can still occur

---

## 🎯 Learning Outcome

After completing this section:

* Understand different ensemble techniques
* Know when to use each method
* Implement Bagging, Boosting, Voting, and Stacking
* Compare ensemble methods

---

## 🧠 One-Line Summary

> Ensemble learning combines multiple models to achieve better performance than a single model.
