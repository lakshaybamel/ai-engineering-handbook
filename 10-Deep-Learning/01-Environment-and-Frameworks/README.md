# ⚙️ Deep Learning Environment & Frameworks

Before building deep learning models, we need the **right tools and environment** to implement neural networks efficiently.

Deep learning frameworks provide ready-to-use components for:

* building neural networks
* performing automatic differentiation
* training models efficiently
* utilizing **GPU acceleration**

This section introduces the **basic environment setup and tools** required to start working with deep learning.

---

# 📚 Topics Covered

## 1️⃣ PyTorch vs TensorFlow vs Keras

📄 [`pytorch_vs_tensorflow_vs_keras.md`](pytorch_vs_tensorflow_vs_keras.md)

Deep learning frameworks simplify the process of building and training neural networks.

This file explains:

* What deep learning frameworks are
* Differences between **PyTorch, TensorFlow, and Keras**
* Why PyTorch is widely used in research and education
* Which framework to choose for different use cases

👉 In this course, we will primarily use **PyTorch**.

---

## 2️⃣ Google Colab Setup

📄 [`google_colab_setup.md`](google_colab_setup.md)

Google Colab is a **cloud-based Jupyter notebook environment** that allows us to run Python code directly in the browser.

Topics covered:

* What Google Colab is
* How to create and run notebooks
* Enabling **GPU acceleration**
* Installing libraries
* Saving notebooks and accessing datasets

Colab is especially useful because it provides **free GPU resources for deep learning experiments**.

---

## 3️⃣ Building a Neuron (Implementation)

📓 [`building_a_neuron.ipynb`](building_a_neuron.ipynb)

This notebook demonstrates how a **single artificial neuron works in practice** using PyTorch.

Topics covered:

* Creating tensors in PyTorch
* Implementing a neuron using `nn.Linear`
* Understanding **weights and bias**
* Performing a forward pass through the neuron
* Inspecting model parameters

This notebook connects the **theoretical concepts of neurons** to their **actual implementation in code**.

---

# 🎯 Learning Outcome

After completing this section you will:

✔ Understand the major **deep learning frameworks**
✔ Know how to use **Google Colab for experiments**
✔ Implement a **basic neuron using PyTorch**

This prepares you for the next section where we explore **how neural networks actually learn**.

---

# 🔗 Next Section

➡️ Next module:

```
02-Neural-Network-Training
```

In the next section we will learn the **core mechanics of training neural networks**, including:

* Forward Propagation
* Backpropagation
* Loss Functions
* Optimizers
* Gradient Descent
* Vanishing Gradient Problem

These concepts explain **how neural networks update their weights and learn from data**.

---

# 🧠 Key Takeaway

> Deep learning frameworks like PyTorch make it possible to build and train neural networks efficiently without manually implementing complex mathematical operations.
