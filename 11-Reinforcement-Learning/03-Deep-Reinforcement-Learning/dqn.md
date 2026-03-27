# ⚡ Deep Q-Network (DQN)

## 📌 Overview

**Deep Q-Network (DQN)** is a fundamental algorithm in **Deep Reinforcement Learning** that combines:

* **Q-Learning**
* **Deep Neural Networks**

👉 Instead of using a Q-table, DQN uses a **neural network to approximate Q-values**.

---

## 🧠 Intuition

In traditional Q-learning:

```text
Q(s, a) → stored in table
```

But when:

* state space is large
* inputs are complex (like images)

👉 Q-table becomes impossible to maintain.

---

### Solution

```text
Neural Network → approximates Q-values
```

So instead of storing values, we **learn a function**:

```text
Q(s, a; θ)
```

Where:

* θ = neural network parameters

---

## ⚙️ How DQN Works

The neural network takes:

```text
Input: State (s)
Output: Q-values for all actions
```

Example:

```text
Input: game screen
Output: [Q(left), Q(right), Q(jump)]
```

👉 Choose action with highest Q-value.

---

## 🔁 DQN Training Loop

Step-by-step:

1. observe current state (s)
2. pass state through neural network
3. get Q-values
4. choose action (ε-greedy)
5. take action → get reward (r) and next state (s')
6. store experience
7. update neural network

---

## 🧩 Key Components of DQN

DQN introduces important improvements over Q-learning:

---

### 1️⃣ Neural Network

Approximates:

```text
Q(s, a; θ)
```

Instead of using a table.

---

### 2️⃣ Experience Replay

Stores past experiences:

```text
(s, a, r, s')
```

👉 Helps:

* break correlation
* improve learning stability

---

### 3️⃣ Target Network

A separate network used to compute stable targets.

👉 Prevents unstable updates.

---

### 4️⃣ ε-Greedy Policy

Balances:

* exploration
* exploitation

---

## 🔁 DQN Update Rule

The loss function in DQN is:

```text
Loss = (target - predicted Q-value)^2
```

Where target is:

```text
target = r + γ max Q(s', a'; θ_target)
```

👉 We minimize this loss using gradient descent.

---

## ⚖️ DQN vs Q-Learning

| Feature     | Q-Learning | DQN                    |
| ----------- | ---------- | ---------------------- |
| Q-values    | Table      | Neural Network         |
| State space | Small      | Large                  |
| Scalability | Limited    | High                   |
| Input type  | Discrete   | Complex (images, etc.) |

---

## 🚀 Advantages

* Handles large state spaces
* Works with raw inputs (images, text)
* More scalable than Q-learning
* Foundation of modern Deep RL

---

## ⚠️ Limitations

* Training can be unstable
* Requires large data
* Computationally expensive
* Sensitive to hyperparameters

---

## 🎯 When To Use

Use DQN when:

* state space is large
* Q-table is not feasible
* input is high-dimensional
* deep learning can help

---

## ⚠️ Important Points

* DQN replaces Q-table with neural network
* Uses experience replay and target network
* Trained using gradient descent
* Core algorithm in Deep RL
* Basis for many advanced methods

---

## 🧠 One-Line Summary

> Deep Q-Network (DQN) uses a neural network to approximate Q-values, enabling reinforcement learning in complex environments where traditional Q-learning is not feasible.
