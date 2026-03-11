# 📊 Model Evaluation

## 📌 Overview

After training the Artificial Neural Network (ANN), the next step is to **evaluate how well the model performs on unseen data**.

Model evaluation helps determine whether the neural network has successfully learned the patterns in the dataset and can **correctly classify new samples**.

In classification problems, evaluation focuses on measuring **how accurately the model predicts the correct class labels**.

---

## 🎯 Evaluation Metric

For classification tasks, one of the most commonly used metrics is **Accuracy**.

Accuracy measures the proportion of **correct predictions made by the model**.

The formula for accuracy is:

```text
Accuracy = Number of Correct Predictions / Total Predictions
```

Example:

```text
Correct Predictions = 93
Total Samples = 100
Accuracy = 0.93
```

This means the model correctly classified **93% of the samples**.

---

## ⚙️ Generating Predictions

After training the model, predictions are generated using the **test dataset**.

During evaluation, gradient computation is disabled because the model parameters are **not being updated**.

Example:

```python
with torch.no_grad():
    outputs = model(X_test)
```

The model produces **raw class scores (logits)** for each input sample.

---

## 🧩 Converting Predictions to Class Labels

The output layer produces scores for each class.

To obtain the predicted class, we select the class with the **highest score**.

Example:

```python
_, predicted = torch.max(outputs, 1)
```

This operation returns the **index of the class with the highest probability**.

---

## 📈 Calculating Accuracy

Once predictions are obtained, accuracy can be computed by comparing the predicted labels with the actual labels.

Example:

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test.numpy(), predicted.numpy())

print("Accuracy:", accuracy)
```

Example output:

```text
Accuracy: 0.93
```

This indicates that the model correctly classified **93% of the test samples**.

---

## 📊 Interpreting Results

Accuracy values can be interpreted as follows:

| Accuracy  | Interpretation            |
| --------- | ------------------------- |
| < 60%     | Model performs poorly     |
| 60% – 80% | Model performs moderately |
| 80% – 90% | Model performs well       |
| > 90%     | Model performs very well  |

In this example:

```text
Accuracy ≈ 93%
```

This indicates that the neural network has **successfully learned the patterns in the dataset**.

---

## 📉 Monitoring Training Loss

In addition to accuracy, the training loss curve helps understand how the model improved during training.

During training:

* loss gradually decreases
* model predictions become more accurate

Example loss trend:

```text
Epoch 10  → Loss ≈ 1.85
Epoch 50  → Loss ≈ 1.22
Epoch 100 → Loss ≈ 0.68
Epoch 300 → Lower loss and better accuracy
```

A steadily decreasing loss indicates that the **model is learning effectively**.

---

## ⚠️ Important Points

* Evaluation must be performed on **test data**, not training data.
* Accuracy is the most common metric for **classification problems**.
* Predictions are obtained by selecting the **class with the highest output score**.
* Lower training loss generally leads to **higher prediction accuracy**.

---

## 🧠 One-Line Summary

> Model evaluation measures how accurately a trained neural network predicts class labels on unseen data, with accuracy commonly used as the primary metric for classification tasks.
