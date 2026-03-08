# ⚙️ Optimization in Neural Networks

Optimization techniques are used to **train neural networks by minimizing the loss function**.

When a neural network makes predictions, the **loss function measures the error** between predicted and actual values.
Optimization algorithms then update the **weights and biases** to reduce this error.

Basic training cycle:

```text
Forward Propagation → Compute Loss → Backpropagation → Optimization Step
```

The goal of optimization is to find the **best set of parameters (weights and biases)** that minimize the loss function.

---

# 📚 Topics Covered

## 1️⃣ Gradient Descent

📄 [gradient_descent.md](gradient_descent.md)

Gradient Descent is the **core optimization algorithm used in deep learning**.

Topics covered:

* What gradient descent is
* How gradients are computed
* Weight update rule
* Role of learning rate
* How neural networks minimize loss

This algorithm forms the **foundation of neural network training**.

---

## 2️⃣ Optimizers

📄 [optimizers.md](optimizers.md)

Optimizers are algorithms that **update neural network parameters using gradients**.

Topics covered:

* Role of optimizers in training
* Common optimizers such as:

  * Stochastic Gradient Descent (SGD)
  * Momentum
  * RMSProp
  * Adam

These optimizers improve **training speed and stability**.

---

## 3️⃣ Modern Variants of Gradient Descent

📄 [modern_variants_of_gd.md](modern_variants_of_gd.md)

Modern variants of gradient descent help overcome limitations of basic gradient descent.

Topics covered:

* Batch Gradient Descent
* Stochastic Gradient Descent (SGD)
* Mini-Batch Gradient Descent
* Momentum-based optimization
* Adaptive learning rate methods

These techniques make it possible to train **large deep learning models efficiently**.

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ How neural networks **minimize loss functions**
✔ How gradients guide parameter updates
✔ Why optimizers are required for training
✔ Why modern optimization techniques improve deep learning performance

These concepts are essential for understanding **how neural networks learn during training**.

---

# 🔗 Next Section

After understanding optimization techniques, we move to building and training actual neural networks.

Next module:

**Artificial Neural Networks (ANN)**

In that section we will implement neural networks for:

* regression problems
* classification problems

---

# 🧠 Key Takeaway

> Optimization algorithms update neural network parameters using gradients to minimize the loss function and improve model predictions.
