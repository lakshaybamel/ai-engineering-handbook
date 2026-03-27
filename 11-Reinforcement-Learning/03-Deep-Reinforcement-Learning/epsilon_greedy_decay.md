# 🎯 Epsilon-Greedy Decay Strategy

## 📌 Overview

In Reinforcement Learning, agents must balance:

* **Exploration** → trying new actions
* **Exploitation** → using known best actions

The **ε-greedy strategy** is commonly used to handle this balance.

👉 However, using a fixed ε is not ideal.

This is where **Epsilon Decay** comes in.

---

## 🧠 Intuition

At the beginning of training:

```text
Agent knows nothing → needs more exploration
```

Later in training:

```text
Agent has learned → should exploit more
```

👉 So we gradually:

```text
Decrease ε over time
```

---

## ⚙️ ε-Greedy Policy

The ε-greedy strategy works as:

* With probability **ε** → choose random action (explore)
* With probability **1 - ε** → choose best action (exploit)

---

## 🔁 Why Decay ε?

If ε remains high:

* too much exploration
* slow convergence

If ε is too low early:

* agent may get stuck in suboptimal policy

👉 Solution:

```text
Start high → gradually decrease
```

---

## 📉 Epsilon Decay Strategy

We update ε after each episode or step.

---

### 1️⃣ Linear Decay

```text
ε = ε - decay_rate
```

Example:

```text
ε = 1.0 → 0.9 → 0.8 → ... → 0.1
```

---

### 2️⃣ Exponential Decay

```text
ε = ε * decay_rate
```

Example:

```text
ε = 1.0 → 0.99 → 0.98 → ...
```

---

### 3️⃣ Minimum Threshold

To ensure some exploration always exists:

```text
ε = max(min_epsilon, ε)
```

Example:

```text
min_epsilon = 0.01
```

---

## 🔁 Typical Workflow

```text
Start with high ε
    ↓
Explore environment
    ↓
Reduce ε gradually
    ↓
Shift towards exploitation
```

---

## 📊 Example

| Episode | ε Value | Behavior            |
| ------- | ------- | ------------------- |
| 1       | 1.0     | Full exploration    |
| 100     | 0.5     | Balanced            |
| 500     | 0.1     | Mostly exploitation |
| 1000    | 0.01    | Near optimal        |

---

## 🚀 Advantages

* balances exploration and exploitation
* improves convergence
* prevents early stagnation
* helps find optimal policy

---

## ⚠️ Limitations

* requires tuning decay rate
* too fast decay → poor exploration
* too slow decay → slow learning

---

## 🎯 When To Use

Epsilon decay is used in:

* Q-learning
* SARSA
* Deep Q-Network (DQN)
* almost all RL algorithms

---

## ⚠️ Important Points

* ε controls exploration
* decay makes learning efficient
* start high, reduce gradually
* always keep minimum ε
* critical for good performance

---

## 🧠 One-Line Summary

> Epsilon decay gradually reduces exploration over time, allowing the agent to explore early and exploit learned knowledge later for optimal performance.
