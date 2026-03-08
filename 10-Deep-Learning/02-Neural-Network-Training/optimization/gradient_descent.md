# 📉 Gradient Descent

## 📌 What is Gradient Descent?

**Gradient Descent** is an optimization algorithm used to **minimize the loss function** during neural network training.

The goal of training is to find the **best values of weights and biases** so that the model makes accurate predictions.

Gradient Descent updates model parameters by moving them in the direction that **reduces the loss**.

Basic idea:

```text
Compute Loss → Compute Gradient → Update Weights → Reduce Loss
```

This process repeats many times until the model learns the correct patterns.

---

## 🧠 Intuition

Imagine you are standing on a **mountain** and want to reach the **lowest point in the valley**.

You cannot see the entire mountain, but you can check the **slope around you**.

So you follow the **steepest downward direction** step by step.

```text
Top of Mountain → Walk Downhill → Reach Valley
```

In neural networks:

* mountain → loss function
* slope → gradient
* walking downhill → gradient descent updates

The algorithm gradually moves toward the **minimum loss**.

---

## ⚙️ How Gradient Descent Works

Gradient Descent follows these steps:

### 1️⃣ Compute Prediction

The model performs **forward propagation** and produces predictions.

---

### 2️⃣ Compute Loss

The loss function calculates how wrong the prediction is.

Example:

```text
Actual value = 10
Predicted value = 7
```

The loss function measures the **error**.

---

### 3️⃣ Compute Gradient

Backpropagation calculates the **gradient of the loss with respect to weights**.

Example:

```text
∂Loss / ∂w
```

The gradient tells us **how the loss changes when the weight changes**.

---

### 4️⃣ Update Parameters

Weights and biases are updated using the gradient.

Update rule:

```
w_new = w_old − learning_rate × gradient
```

Where:

* `learning_rate` controls how big the step is
* `gradient` tells the direction of steepest increase

Since we subtract the gradient, the model moves **toward lower loss**.

---

## 🔁 Training Loop

Training a neural network with gradient descent typically follows this cycle:

```text
Forward Propagation
        ↓
Compute Loss
        ↓
Backpropagation
        ↓
Gradient Descent Update
        ↓
Repeat
```

This process is repeated for many **iterations and epochs**.

---

## ⚙️ Learning Rate

The **learning rate** controls how large the update step is during training.

Example:

```text
w_new = w_old − η × gradient
```

Where:

```
η = learning rate
```

Choosing the correct learning rate is very important.

### Small Learning Rate

```text
Training is very slow
```

### Large Learning Rate

```text
Model may overshoot the minimum
```

So a balanced learning rate is required for stable training.

---

## 📊 Example

Suppose:

```
Current weight = 0.5
Learning rate = 0.01
Gradient = 2
```

Weight update:

```
w_new = 0.5 − (0.01 × 2)
```

```
w_new = 0.48
```

The weight moves slightly toward the **direction that reduces loss**.

---

## 🎯 Why Gradient Descent is Important

Gradient Descent is the **core optimization algorithm in deep learning**.

It allows neural networks to:

* learn patterns from data
* minimize prediction error
* improve model performance

Almost all deep learning models rely on **gradient-based optimization**.

---

## ⚠️ Key Points to Remember

* Gradient Descent is used to **minimize the loss function**.
* It updates **weights and biases using gradients**.
* Backpropagation computes the gradients used in gradient descent.
* Learning rate controls the **size of updates**.
* The algorithm iteratively moves toward the **minimum loss**.

---

## 🎓 Interview Insight

Common interview question:

**What is gradient descent in machine learning?**

Answer:

Gradient Descent is an optimization algorithm that updates model parameters by moving them in the direction that minimizes the loss function.

Another question:

**Why is learning rate important?**

Because it controls how quickly the model updates its parameters during training.

---

## 🧠 One-Line Summary

> Gradient Descent is an optimization algorithm that updates model parameters in the direction that reduces the loss, allowing neural networks to learn from data.
