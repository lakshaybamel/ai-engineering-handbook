# 📉 Loss Functions

Loss functions are used to **measure how well a neural network is performing during training**.

When a model makes a prediction, the loss function calculates the **difference between the predicted value and the actual value**.

This difference is called the **error**.

Example:

```
Actual value    = 10
Predicted value = 8
```

The loss function computes **how wrong the prediction is**.

The goal of training a neural network is:

```
Minimize the loss
```

The model updates its **weights and biases** during training to reduce this error.

---

# 📚 Topics Covered

## 1️⃣ Loss Functions for Regression

📄 [regression_losses.md](regression_losses.md)

Regression problems involve predicting **continuous numerical values**.

Examples:

* house price prediction
* temperature prediction
* sales forecasting

This file explains common regression loss functions such as:

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

These loss functions measure the **difference between predicted and actual values**.

---

## 2️⃣ Loss Functions for Classification

📄 [classification_losses.md](classification_losses.md)

Classification problems involve predicting **categories or classes**.

Examples:

* spam / not spam
* cat / dog classification
* sentiment analysis

This file explains common classification loss functions such as:

* Binary Cross Entropy
* Categorical Cross Entropy

These loss functions measure how well the model predicts **class probabilities**.

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ What loss functions are  
✔ Why neural networks need loss functions  
✔ The difference between **regression and classification losses**  
✔ When to use different loss functions  

Loss functions are a critical component of neural network training because they guide the model toward **better predictions**.

---

# 🔗 Next Topics

Loss functions work together with **optimization algorithms** that update model parameters.

Next section:

* **Optimization Techniques** → [../optimization/README.md](../optimization/README.md)

These techniques explain **how neural networks update weights to minimize loss**.

---

# 🧠 Key Takeaway

> Loss functions measure how wrong a model’s predictions are and guide neural networks to improve by minimizing prediction error during training.
