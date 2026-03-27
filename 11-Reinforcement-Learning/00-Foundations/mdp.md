# 📐 Markov Decision Process (MDP)

## 📌 Overview

A **Markov Decision Process (MDP)** is the mathematical framework used to define **Reinforcement Learning problems**.

It provides a formal way to describe:

* states
* actions
* rewards
* transitions

👉 Almost every RL problem can be modeled as an MDP.

---

## 🧠 Intuition

In RL, the agent interacts with the environment step-by-step.

At each step:

```
Current State → Action → Next State + Reward
```

MDP formalizes this interaction so that we can **analyze and solve RL problems mathematically**.

---

## 🧩 Components of MDP

An MDP is defined by a tuple:

```
(S, A, P, R, γ)
```

---

### 1️⃣ State Space (S)

All possible states the agent can be in.

Example:

```
All positions in a grid
```

---

### 2️⃣ Action Space (A)

All possible actions the agent can take.

Example:

```
Move left, right, up, down
```

---

### 3️⃣ Transition Probability (P)

Probability of moving from one state to another after taking an action.

```
P(s' | s, a)
```

👉 Probability of reaching state **s'** from state **s** after action **a**

---

### 4️⃣ Reward Function (R)

Reward received after taking an action.

```
R(s, a)
```

Example:

```
+10 → goal reached  
-1 → step penalty
```

---

### 5️⃣ Discount Factor (γ)

Represents how much future rewards are valued.

```
0 ≤ γ ≤ 1
```

* γ = 0 → only immediate reward matters
* γ → 1 → future rewards are important

---

## 🔑 Markov Property

The most important concept in MDP is the **Markov Property**.

👉 It states:

```
Future depends only on the present state, not the past
```

Formally:

```
P(sₜ₊₁ | sₜ, sₜ₋₁, ..., s₀) = P(sₜ₊₁ | sₜ)
```

---

## 📊 Example

### Grid World

Agent moves in a grid.

* State → position in grid
* Action → move direction
* Reward → +10 at goal

Example step:

```
State: (2,2)
Action: Right
Next State: (2,3)
Reward: -1
```

---

## 🎯 Objective in MDP

The goal is to find a **policy (π)** that maximizes total reward:

```
Maximize expected cumulative reward
```

---

## ⚙️ Return (Total Reward)

The total reward is called **Return (G)**:

```
G = R₁ + γR₂ + γ²R₃ + ...
```

👉 Future rewards are discounted over time.

---

## 🔄 MDP Flow

```text
State (S)
   ↓
Action (A)
   ↓
Environment
   ↓
Next State (S') + Reward (R)
```

---

## ⚠️ Important Points

* MDP is the **foundation of RL**
* It defines how agent and environment interact
* Markov property simplifies decision making
* Discount factor balances immediate vs future reward

---

## 🧠 One-Line Summary

> A Markov Decision Process (MDP) is a mathematical framework that models reinforcement learning problems using states, actions, rewards, transitions, and the Markov property.
