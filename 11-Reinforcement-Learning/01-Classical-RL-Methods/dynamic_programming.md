# 🧮 Dynamic Programming in Reinforcement Learning

## 📌 Overview

**Dynamic Programming (DP)** is a method used in Reinforcement Learning to solve problems when the **environment model is known**.

👉 It helps compute the **optimal policy** by systematically evaluating and improving decisions.

DP is mainly used for:

* understanding RL fundamentals
* solving small problems (like Grid World)
* building intuition for advanced algorithms

---

## 🧠 Intuition

Dynamic Programming works on the idea:

```text
Break a complex problem into smaller subproblems
```

In RL:

👉 Instead of solving the whole problem at once
👉 We solve it **state by state**

Example:

```text
Best decision today depends on best decisions in future
```

---

## 🧩 Key Requirement

Dynamic Programming assumes:

```text
Full knowledge of environment (MDP)
```

This means we know:

* all states
* all actions
* transition probabilities
* reward function

👉 This is why DP is not always practical in real-world problems.

---

## ⚙️ Core Idea

DP uses **value functions** to evaluate how good a state or action is.

Two important functions:

* **Value Function (V)** → how good a state is
* **Q-Function (Q)** → how good an action is

---

## 🔄 Bellman Equation

The foundation of DP is the **Bellman Equation**.

```text
V(s) = max [ R + γ × V(s') ]
```

👉 Meaning:

```text
Value of current state = immediate reward + future value
```

---

## 🧩 Main DP Methods

---

## 1️⃣ Policy Evaluation

👉 Evaluate how good a policy is

Steps:

```text
1. Start with a policy
2. Compute value of each state
3. Repeat until values stabilize
```

---

## 2️⃣ Policy Improvement

👉 Improve the policy using computed values

Steps:

```text
Choose action with highest value
```

---

## 3️⃣ Policy Iteration

Combines both:

```text
Policy Evaluation → Policy Improvement → Repeat
```

👉 Eventually converges to **optimal policy**

---

## 4️⃣ Value Iteration

A more efficient method.

👉 Directly updates values:

```text
V(s) = max [ R + γ × V(s') ]
```

Steps:

```text
1. Initialize values
2. Update values using Bellman equation
3. Repeat until convergence
```

👉 Faster than policy iteration.

---

## 📊 Example: Grid World

Grid:

```text
S  .  .
.  X  .
.  .  G
```

Steps:

1. Assign initial values (0)
2. Update values using Bellman equation
3. Values propagate toward goal

Example:

```text
Low → Medium → High → Goal
```

👉 States closer to goal get higher value.

---

## 🎯 Objective

The goal of DP is:

```text
Find optimal policy π*
```

That maximizes:

```text
Total expected reward
```

---

## ⚠️ Limitations

Dynamic Programming has some limitations:

---

### 1️⃣ Requires Full Model

* Needs transition probabilities
* Not realistic in many problems

---

### 2️⃣ Not Scalable

* Large state spaces → very slow

---

### 3️⃣ Memory Intensive

* Needs to store values for all states

---

## 🚀 Why DP is Important

Even though it has limitations, DP is important because:

* builds strong RL intuition
* forms the base for:

  * Monte Carlo methods
  * Temporal Difference learning
* used in theoretical understanding

---

## ⚠️ Important Points

* DP requires full knowledge of environment
* Uses Bellman equation
* Includes policy iteration and value iteration
* Helps compute optimal policy
* Not suitable for large real-world problems

---

## 🧠 One-Line Summary

> Dynamic Programming solves reinforcement learning problems by using known environment models to iteratively evaluate and improve policies until the optimal policy is found.
