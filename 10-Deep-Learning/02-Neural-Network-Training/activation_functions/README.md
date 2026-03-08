# ⚡ Activation Functions

Activation functions are a core component of **neural networks**.
They are applied to the output of neurons to introduce **non-linearity**, allowing neural networks to learn complex patterns from data.

Without activation functions, even very deep neural networks would behave like **simple linear models**, limiting their ability to solve real-world problems.

Basic neuron computation:

```
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

Activation function:

```
a = activation(z)
```

Where:

* `z` → weighted sum
* `a` → activated output

Activation functions transform the neuron output before passing it to the **next layer**.

---

# 📚 Topics Covered

## 1️⃣ Activation Functions Overview

📄 [activation_functions_overview.md](activation_functions_overview.md)

This file introduces the concept of **activation functions** and explains why they are necessary in neural networks.

Topics covered:

* What activation functions are
* Why neural networks need non-linearity
* Common activation functions
* Where activation functions are used in neural networks

---

## 2️⃣ ReLU and Its Variants

📄 [relu_and_variants.md](relu_and_variants.md)

ReLU (Rectified Linear Unit) is the **most widely used activation function in deep learning**.

This file explains:

* How ReLU works
* Why ReLU became popular
* The **Dying ReLU problem**
* Variants such as:

  * Leaky ReLU
  * PReLU
  * ELU

These variants help improve training stability in deep neural networks.

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ Why activation functions are necessary
✔ How activation functions introduce **non-linearity**
✔ Why **ReLU is widely used in deep learning**
✔ How different activation functions affect neural network training

This knowledge is essential for designing and training **deep neural network models**.

---

# 🔗 Next Topics

Activation functions work closely with other important components of neural networks, including:

* **Loss Functions** → [../loss_functions/README.md](../loss_functions/README.md)
* **Optimization Algorithms** → [../optimization/README.md](../optimization/README.md)

These topics explain **how neural networks learn and improve during training**.

---

# 🧠 Key Takeaway

> Activation functions introduce non-linearity into neural networks, enabling them to learn complex patterns and solve real-world problems.
