# ⏱️ Temporal Difference (TD) Learning

## 📌 Overview

**Temporal Difference (TD) Learning** is a Reinforcement Learning method that combines ideas from:

* **Dynamic Programming (DP)**
* **Monte Carlo (MC)**

👉 It learns **step-by-step (online)** using current estimates, without waiting for the episode to finish.

TD learning is widely used in modern RL algorithms such as:

* SARSA
* Q-Learning
* Deep Q-Networks (DQN)

---

## 🧠 Intuition

Instead of waiting until the end of an episode (like Monte Carlo), TD learning updates values:

```text
Immediately after each step
```

👉 It learns from:

```text
Current reward + estimated future reward
```

Example:

```text
You make a move → get feedback → update immediately
```

---

## ⚙️ Core Idea

TD learning updates value using:

```text
Prediction → Target → Error → Update
```

👉 This error is called:

```text
Temporal Difference Error
```

---

## 📊 TD Update Rule

The basic TD update formula:

```text
V(s) = V(s) + α [ R + γV(s') - V(s) ]
```

Where:

* **V(s)** → current value of state
* **α** → learning rate
* **R** → reward
* **γ** → discount factor
* **V(s')** → next state value

---

## 🧠 TD Error

The key part is:

```text
TD Error = R + γV(s') - V(s)
```

👉 Meaning:

```text
Actual reward + future estimate - current estimate
```

This tells how wrong the current prediction is.

---

## 🔄 How TD Learning Works

### Step-by-step:

```text
1. Observe current state (s)
2. Take action (a)
3. Get reward (R) and next state (s')
4. Update value V(s)
5. Move to next state
6. Repeat
```

👉 No need to wait for episode to end.

---

## 📊 Example

### Grid World

Step:

```text
State: (0,0)
Action: Right
Reward: -1
Next State: (0,1)
```

Update:

```text
V(0,0) = V(0,0) + α [ -1 + γV(0,1) - V(0,0) ]
```

👉 Value improves step-by-step.

---

## ⚖️ TD vs Monte Carlo vs DP

| Feature        | Dynamic Programming   | Monte Carlo    | TD Learning   |
| -------------- | --------------------- | -------------- | ------------- |
| Model required | Yes                   | No             | No            |
| Update timing  | Full knowledge        | End of episode | Every step    |
| Learning type  | Bootstrapping         | No             | Bootstrapping |
| Speed          | Fast (small problems) | Slow           | Faster        |

---

## 🧩 Bootstrapping

TD uses **bootstrapping**, meaning:

```text
Use existing estimates to update values
```

👉 It does not rely only on actual rewards.

---

## 🎯 Advantages

* Learns **online (real-time)**
* Faster than Monte Carlo
* Does not require environment model
* Works well for large problems

---

## ⚠️ Limitations

---

### 1️⃣ Bias

* Uses estimates → may introduce bias

---

### 2️⃣ Less Accurate than MC (sometimes)

* Because it uses partial information

---

## 🚀 Why TD Learning is Important

TD learning is the foundation of:

* SARSA
* Q-Learning
* Deep Reinforcement Learning

👉 It is one of the **most practical RL methods**.

---

## ⚠️ Important Points

* Updates values after each step
* Uses bootstrapping
* Combines DP and MC ideas
* Does not require model
* Core of many RL algorithms

---

## 🧠 One-Line Summary

> Temporal Difference learning updates value estimates step-by-step using current rewards and estimated future values, enabling faster and more practical reinforcement learning.
