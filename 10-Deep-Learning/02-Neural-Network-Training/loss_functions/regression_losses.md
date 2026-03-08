# 📉 Loss Functions for Regression

## 📌 What is a Loss Function?

A **Loss Function** measures how far the model’s prediction is from the actual value.

In regression problems, the output is a **continuous value** such as:

* house price
* temperature
* sales prediction
* stock price

The loss function calculates the **error between predicted values and actual values**.

Example:

```
Actual Price = ₹50,00,000
Predicted Price = ₹45,00,000
```

The loss function measures **how big this error is**.

During training, the model tries to **minimize this loss**.

---

## 🧠 Intuition

Think of a loss function as a **score that tells how wrong the model is**.

```
Small loss → model prediction is good
Large loss → model prediction is poor
```

The goal of training is:

```
Minimize the loss
```

This is done by adjusting the **weights and biases** of the neural network.

---

## ⚙️ Common Regression Loss Functions

Several loss functions are used in regression problems.

The most common ones are:

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

---

## 1️⃣ Mean Squared Error (MSE)

Mean Squared Error is the **most commonly used loss function for regression**.

Formula:

```
MSE = (1/n) Σ (y - ŷ)²
```

Where:

* `y` = actual value
* `ŷ` = predicted value
* `n` = number of samples

Example:

```
Actual = 10
Predicted = 8
```

Error:

```
(10 - 8)² = 4
```

Advantages:

* heavily penalizes large errors
* smooth and easy for gradient-based optimization

Limitations:

* sensitive to **outliers**

---

## 2️⃣ Mean Absolute Error (MAE)

MAE calculates the **average absolute difference** between predicted and actual values.

Formula:

```
MAE = (1/n) Σ |y - ŷ|
```

Example:

```
Actual = 10
Predicted = 8
```

Error:

```
|10 - 8| = 2
```

Advantages:

* less sensitive to outliers
* easier to interpret

Limitations:

* gradients are less smooth compared to MSE

---

## 3️⃣ Root Mean Squared Error (RMSE)

RMSE is the **square root of MSE**.

Formula:

```
RMSE = √(MSE)
```

RMSE gives the error in the **same unit as the target variable**.

Example:

If predicting house prices:

```
RMSE = ₹1,00,000
```

This means predictions are off by about **₹1,00,000 on average**.

Advantages:

* interpretable because units match the target variable

---

## 📊 Comparison of Regression Loss Functions

| Loss Function | Formula                 | Characteristics                 |
| ------------- | ----------------------- | ------------------------------- |
| MSE           | Mean of squared errors  | Penalizes large errors strongly |
| MAE           | Mean of absolute errors | More robust to outliers         |
| RMSE          | Square root of MSE      | Error in same unit as target    |

---

## 🎯 When to Use Each Loss Function

Use **MSE** when:

* large errors should be penalized heavily
* training deep learning models

Use **MAE** when:

* dataset contains **many outliers**

Use **RMSE** when:

* you want error in **original units**

---

## ⚠️ Key Points to Remember

* Loss functions measure **model error during training**.
* Regression problems require **continuous output loss functions**.
* MSE is the **most commonly used regression loss** in deep learning.
* MAE is more **robust to outliers**.
* RMSE provides error in the **same unit as the target variable**.

---

## 🎓 Interview Insight

Common interview question:

**Why is MSE commonly used in regression problems?**

Answer:

MSE penalizes larger errors more strongly and provides a smooth gradient, making it suitable for **gradient-based optimization methods** used in neural networks.

Another question:

**What is the difference between MAE and MSE?**

MAE uses absolute differences, while MSE squares the error, which causes larger errors to have a **greater impact on the loss**.

---

## 🧠 One-Line Summary

> Regression loss functions measure the difference between predicted and actual continuous values, with MSE being the most commonly used in deep learning models.
