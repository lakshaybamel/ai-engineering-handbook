# 🧠 DQN Architecture

## 📌 Overview

The **Deep Q-Network (DQN) Architecture** defines how a neural network is used to approximate the **Q-value function** in Reinforcement Learning.

Instead of using a Q-table:

```text
Q(s, a)
```

DQN uses a neural network:

```text
Q(s, a; θ)
```

👉 This allows the model to handle **large and complex state spaces**.

---

## 🧠 Intuition

Think of the DQN as a function:

```text
Input → Neural Network → Q-values
```

* Input → state
* Output → Q-value for each possible action

👉 The agent chooses the action with the **highest Q-value**.

---

## ⚙️ Basic Architecture

A typical DQN consists of:

1. Input Layer
2. Hidden Layers
3. Output Layer

---

### 1️⃣ Input Layer

Takes the **state representation**.

Examples:

* numerical features (CartPole)
* image (Atari games)

Example:

```text
State = [position, velocity, angle, angular velocity]
```

---

### 2️⃣ Hidden Layers

These are **fully connected layers** (or CNN layers for images).

Purpose:

* learn patterns
* extract features
* model complex relationships

Example:

```text
Input → Dense → ReLU → Dense → ReLU
```

---

### 3️⃣ Output Layer

Outputs Q-values for all possible actions:

```text
[Q(s, a1), Q(s, a2), Q(s, a3), ...]
```

👉 Number of outputs = number of actions

---

## 🔁 Forward Pass

Given a state:

```text
State → Neural Network → Q-values
```

Example:

```text
Q-values = [1.2, 0.5, 2.3, 1.8]
```

👉 Best action = action with highest value:

```text
Action = argmax(Q-values)
```

---

## ⚙️ Training Objective

The network is trained to minimize:

```text
Loss = (target - predicted Q-value)^2
```

Where:

```text
target = r + γ max Q(s', a')
```

---

## 🧩 Architecture Variants

Depending on problem:

### For Simple Inputs

* Fully Connected Neural Network (MLP)

---

### For Images (Atari, Vision)

* Convolutional Neural Network (CNN)

Example:

```text
Image → CNN → Flatten → Dense → Output
```

---

## 🔁 Role of Two Networks

DQN uses:

* **Online Network** → predicts Q-values
* **Target Network** → provides stable targets

👉 Prevents unstable learning.

---

## 📊 Example Architecture (CartPole)

```text
Input (4 features)
    ↓
Dense (128 neurons) + ReLU
    ↓
Dense (128 neurons) + ReLU
    ↓
Output (2 actions)
```

---

## 🚀 Advantages

* handles large state spaces
* learns complex patterns
* scalable to real-world problems
* flexible architecture

---

## ⚠️ Limitations

* requires tuning
* computationally expensive
* can be unstable without techniques
* needs large data

---

## 🎯 When To Use

Use DQN architecture when:

* state space is large
* Q-table is not feasible
* deep learning is applicable
* environment is complex

---

## ⚠️ Important Points

* input = state
* output = Q-values
* uses neural networks instead of tables
* trained using gradient descent
* core of Deep RL

---

## 🧠 One-Line Summary

> DQN architecture uses a neural network to map states to Q-values for all actions, enabling reinforcement learning in complex environments.
