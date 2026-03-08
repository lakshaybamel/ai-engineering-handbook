# ⚙️ Optimizers in Deep Learning

## 📌 What are Optimizers?

An **Optimizer** is an algorithm used to **update the weights and biases of a neural network in order to minimize the loss function**.

During training, the model makes predictions and calculates the **loss (error)**.
Optimizers use the **gradients computed through backpropagation** to adjust the parameters so that the model improves.

Basic idea:

```text
Compute Loss → Compute Gradients → Optimizer Updates Weights
```

Optimizers control **how the neural network learns** during training.

---

## 🧠 Intuition

Think of optimizers as **strategies for reaching the lowest point of a valley**.

Example analogy:

```text
Mountain → Loss Function
Slope → Gradient
Walking Strategy → Optimizer
```

Different optimizers use different strategies to reach the **minimum loss faster and more efficiently**.

---

## ⚙️ Role of Optimizers in Training

Training a neural network involves the following steps:

```text
Forward Propagation
        ↓
Compute Loss
        ↓
Backpropagation (compute gradients)
        ↓
Optimizer updates weights
```

The optimizer determines **how the parameters change during each update step**.

---

## 📉 Basic Optimizer: Gradient Descent

The simplest optimizer is **Gradient Descent**.

Update rule:

```
w_new = w_old − learning_rate × gradient
```

Where:

* `gradient` indicates the direction of steepest increase in loss
* `learning_rate` controls the step size

The optimizer moves parameters **in the opposite direction of the gradient** to reduce the loss.

---

## 🔧 Why Advanced Optimizers Are Needed

Basic gradient descent has some limitations:

* slow convergence
* sensitive to learning rate
* difficulty handling noisy gradients
* struggles with complex loss surfaces

Modern optimizers solve these problems by:

* adapting learning rates
* using momentum
* stabilizing updates

These improvements help models **train faster and more efficiently**.

---

## 📊 Common Optimizers in Deep Learning

Several optimizers are widely used in neural network training.

### 1️⃣ Stochastic Gradient Descent (SGD)

SGD updates parameters using **one batch of data at a time**.

Advantages:

* simple
* widely used
* good generalization

Limitations:

* training can be slow
* updates may be noisy

---

### 2️⃣ Momentum

Momentum improves gradient descent by adding a **velocity term**.

Idea:

```text
Use previous updates to accelerate learning
```

Advantages:

* faster convergence
* smoother optimization path

---

### 3️⃣ RMSProp

RMSProp adjusts the learning rate based on **recent gradients**.

Advantages:

* stabilizes training
* works well for deep networks

---

### 4️⃣ Adam (Adaptive Moment Estimation)

Adam is one of the **most widely used optimizers in deep learning**.

It combines ideas from:

* Momentum
* RMSProp

Advantages:

* adaptive learning rates
* faster convergence
* works well for most deep learning tasks

Because of its reliability, **Adam is often the default optimizer in many neural network models**.

---

## 📊 Comparison of Optimizers

| Optimizer | Key Idea                              | Advantage              |
| --------- | ------------------------------------- | ---------------------- |
| SGD       | Basic gradient descent                | Simple and widely used |
| Momentum  | Uses previous updates                 | Faster convergence     |
| RMSProp   | Adaptive learning rate                | Stable training        |
| Adam      | Combines momentum + adaptive learning | Most popular optimizer |

---

## 🎯 Choosing the Right Optimizer

General guideline:

Use **SGD** when:

* training simple models
* better generalization is required

Use **Adam** when:

* training deep neural networks
* faster convergence is needed
* unsure which optimizer to choose

In practice, **Adam is often the first choice for many deep learning models**.

---

## ⚠️ Key Points to Remember

* Optimizers update **weights and biases during training**.
* They use gradients computed through **backpropagation**.
* Different optimizers use different strategies for updating parameters.
* Adam is one of the **most commonly used optimizers in deep learning**.

---

## 🎓 Interview Insight

Common interview question:

**What is an optimizer in deep learning?**

Answer:

An optimizer is an algorithm that updates the parameters of a neural network using gradients in order to minimize the loss function.

Another common question:

**Why is Adam optimizer popular?**

Because it combines momentum and adaptive learning rates, allowing faster and more stable training.

---

## 🧠 One-Line Summary

> Optimizers are algorithms that update neural network parameters using gradients to minimize the loss function and improve model performance during training.
