# 🧠 Feedforward Neural Networks (FNN)

## 📌 Overview

A **Feedforward Neural Network (FNN)** is the simplest and most fundamental type of neural network used in deep learning.

In this architecture, information moves **in one direction only**:

```text
Input Layer → Hidden Layers → Output Layer
```

There are **no cycles or feedback connections**. Data flows forward through the network until a prediction is produced.

Feedforward networks are widely used for tasks such as:

* regression
* classification
* pattern recognition

---

## 🧠 Basic Structure of a Feedforward Network

A feedforward neural network consists of three main types of layers:

### 1️⃣ Input Layer

The input layer receives the **feature values from the dataset**.

Example:

```text
Age, Salary, Experience → Input Features
```

Each feature corresponds to one **input neuron**.

---

### 2️⃣ Hidden Layers

Hidden layers perform the **actual learning** in the neural network.

Each neuron performs two steps:

1. Compute weighted sum

```math
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

2. Apply activation function

Example activation functions:

* ReLU
* Sigmoid
* Tanh

Hidden layers allow the network to learn **complex patterns and relationships** in the data.

---

### 3️⃣ Output Layer

The output layer produces the **final prediction**.

The structure of the output layer depends on the task.

For example:

**Regression**

```text
1 output neuron
```

**Binary Classification**

```text
1 output neuron (sigmoid)
```

**Multi-class Classification**

```text
n output neurons (softmax)
```

---

## 🔄 How Feedforward Networks Work

The learning process follows these steps:

1️⃣ Input data enters the network  
2️⃣ Data passes through hidden layers  
3️⃣ Each neuron computes weighted sums  
4️⃣ Activation functions introduce non-linearity  
5️⃣ Output layer generates predictions  

This process is called **forward propagation**.

After the prediction is generated:

* loss is calculated
* gradients are computed
* weights are updated using **backpropagation**

---

## ⚙️ Example Architecture

Example feedforward neural network:

```text
Input Layer (4 features)
        ↓
Hidden Layer (16 neurons)
        ↓
Hidden Layer (8 neurons)
        ↓
Output Layer (1 neuron)
```

This architecture is commonly used for **basic deep learning tasks**.

---

## 🚀 Advantages of Feedforward Neural Networks

* simple architecture
* easy to implement
* works well for structured data
* foundation for many deep learning models

Many advanced neural network architectures are **built on top of feedforward networks**.

---

## ⚠️ Limitations

Feedforward networks have some limitations:

* cannot remember previous inputs
* cannot model sequential data
* struggle with spatial data such as images

Because of these limitations, specialized architectures were developed:

* **CNNs** for images
* **RNNs** for sequential data

---

## 🎯 Key Takeaway

> A Feedforward Neural Network is the simplest neural network architecture where data moves in one direction from input to output through hidden layers, enabling the model to learn patterns from data.
