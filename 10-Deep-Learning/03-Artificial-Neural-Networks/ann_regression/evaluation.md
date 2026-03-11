# 📊 Model Evaluation

## 📌 Overview

After training the Artificial Neural Network (ANN), the next step is **evaluating how well the model performs on unseen data**.

Model evaluation helps us determine whether the neural network has successfully learned the relationship between **input features and the target variable**.

For regression tasks, evaluation typically measures the **difference between predicted values and actual values**.

In the ANN regression notebook, we evaluate the model using the **Root Mean Squared Error (RMSE)** metric.

---

## 🎯 Why Model Evaluation is Important

Training loss only shows how well the model performs on the **training data**.

However, we want to know how well the model performs on **new data that it has never seen before**.

That is why we evaluate the model using the **test dataset**.

Dataset split used in the notebook:

```text
Training Data → Used to train the neural network
Testing Data → Used to evaluate model performance
```

This ensures that the model **generalizes well to new data**.

---

## 📉 Root Mean Squared Error (RMSE)

For regression models, one of the most common evaluation metrics is **Root Mean Squared Error (RMSE)**.

RMSE measures the **average prediction error** between predicted and actual values.

The formula for RMSE is:

```math
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}
```

Where:
```math
(y_i) → Actual Value
```
```math
(\hat{y}_i) → Predicted Value
```
```math
(n) → Number Of Samples
```

RMSE is useful because it expresses the error **in the same unit as the target variable**.

---

## ⚙️ Evaluating the Model in PyTorch

After training, predictions are generated using the **test dataset**.

Example from the notebook:

```python
with torch.no_grad():
    predictions = model(X_test)
```

We disable gradient calculations during evaluation because **we are not updating model parameters**.

The predictions and actual values are then converted to NumPy arrays.

```python
predictions = predictions.numpy()
actual = y_test.numpy()
```

Finally, RMSE is calculated using the `mean_squared_error` function from **scikit-learn**.

```python
rmse = np.sqrt(mean_squared_error(actual, predictions))

print("RMSE:", rmse)
```

---

## 📊 Interpreting the Result

Example result from the notebook:

```text
RMSE: 452.65
```

This means the model's predictions differ from the true values by approximately:

```text
≈ 452 units on average
```

A **lower RMSE** indicates better model performance.

---

## 📈 Visualizing Model Performance

Another useful way to evaluate regression models is to compare:

```text
Actual Values vs Predicted Values
```

This can be visualized using a **scatter plot**.

Example:

```python
plt.scatter(actual, predictions)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted")
plt.show()
```

If the model performs well, most points should lie **close to the diagonal line**, indicating accurate predictions.

---

## ⚠️ Important Points

* Model evaluation should always be performed on **test data**.
* RMSE is widely used for **regression problems**.
* Lower RMSE indicates **better prediction accuracy**.
* Visualization can help understand prediction quality.

---

## 🧠 One-Line Summary

> Model evaluation measures how accurately a trained neural network predicts unseen data, with RMSE commonly used to assess regression model performance.
