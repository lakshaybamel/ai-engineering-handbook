# ⚙️ Weight and Bias Update in Neural Networks

## 📌 Overview

During training, a neural network learns by **adjusting its weights and biases** to reduce prediction error.

After **forward propagation** produces a prediction and **backpropagation** computes gradients, the model updates its parameters.

These updates gradually improve the model's performance.

Basic training cycle:

```
Forward Propagation → Loss Calculation → Backpropagation → Weight & Bias Update
```

The goal is to **minimize the loss function** by adjusting weights and biases.

---

## 🧠 Intuition

Think of training a neural network like **tuning knobs on a machine**.

* If the prediction is wrong, the model adjusts the knobs.
* These knobs are the **weights and biases**.

Example:

Predict house price

```
Predicted price = ₹40,00,000
Actual price    = ₹45,00,000
```

Since the prediction is lower, the model adjusts the weights so the next prediction is closer to the correct value.

Over many updates, the model **learns the correct pattern**.

---

## 🏗️ Role of Weights and Bias

A neuron performs this computation:

```
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

Where:

* `x` = input features
* `w` = weights
* `b` = bias
* `z` = weighted sum

Weights control the **importance of each feature**, while bias shifts the decision boundary.

During training, both **weights and biases are updated**.

---

## ⚙️ How Parameters Are Updated

Backpropagation computes the **gradient of the loss with respect to each parameter**.

Example:

```
∂Loss / ∂w
```

This gradient tells us:

> How the loss changes if the weight changes.

---

## 📉 Gradient Descent Update Rule

Weights are updated using optimization algorithms such as **Gradient Descent**.

Weight update formula:

```
w_new = w_old − learning_rate × ∂Loss/∂w
```

Bias update formula:

```
b_new = b_old − learning_rate × ∂Loss/∂b
```

Where:

* **learning_rate** controls the size of the update step
* **gradient** indicates the direction to reduce loss

---

## 🔁 Training Process

During training, the update process repeats many times.

```
Step 1 → Forward Propagation (make prediction)

Step 2 → Compute Loss

Step 3 → Backpropagation (compute gradients)

Step 4 → Update Weights and Bias

Step 5 → Repeat
```

After many iterations, the model learns parameters that **minimize the loss**.

---

## 📊 Example

Suppose a neuron has:

```
weight = 0.5
bias   = 0.2
learning_rate = 0.01
gradient = 2
```

Update rule:

```
w_new = 0.5 − (0.01 × 2)
```

```
w_new = 0.48
```

The weight moves slightly in the direction that **reduces the loss**.

---

## 🎯 Why Weight Updates Are Important

Weight updates allow the neural network to:

* learn patterns from data
* reduce prediction error
* improve model accuracy

Without updating weights, the network would **never improve**.

---

## ⚠️ Key Points to Remember

* Neural networks learn by **updating weights and biases**.
* Updates are computed using **gradients from backpropagation**.
* Optimization algorithms control how parameters are updated.
* Learning rate determines **how large each update step is**.

---

## 🎓 Interview Insight

Common interview question:

**What is the role of weight updates in neural networks?**

Answer:

Weight updates adjust the parameters of the network using gradients so that the **loss function decreases and the model predictions improve**.

Another question:

**Why is learning rate important?**

Because it controls how quickly the model updates its weights during training.

---

## 🧠 One-Line Summary

> Neural networks learn by updating weights and biases using gradients computed through backpropagation to minimize the loss function.
