# 🎲 Monte Carlo Methods in Reinforcement Learning

## 📌 Overview

**Monte Carlo (MC) Methods** are Reinforcement Learning techniques that learn from **complete episodes of experience**.

👉 Unlike Dynamic Programming, MC methods **do not require a model of the environment**.

👉 They learn by:

```text
Experience → Episode → Update → Improve
```

Monte Carlo methods estimate value functions using **actual returns observed after an episode ends**.

---

## 🧠 Intuition

Think of learning from playing a full game 🎮:

* You play the entire game
* At the end, you see the result (win/loss)
* You update your strategy based on that outcome

👉 This is exactly how Monte Carlo works:

```text
Wait until episode ends → learn from total reward
```

---

## 🧩 Key Idea

Monte Carlo methods estimate value using **average returns**.

```text
Value = average of total rewards from multiple episodes
```

👉 Instead of predicting, it uses **real experience**.

---

## ⚙️ How Monte Carlo Works

### Basic Steps:

```text
1. Run an episode (start → end)
2. Record states, actions, rewards
3. Compute total return
4. Update value estimates
5. Repeat
```

---

## 🎯 Return (G)

Monte Carlo methods use the concept of **Return (G)**:

```text
G = R₁ + γR₂ + γ²R₃ + ...
```

👉 Total reward collected from a state until the episode ends.

---

## 🧩 Types of Monte Carlo Methods

---

## 1️⃣ First-Visit Monte Carlo

👉 Update value only the **first time a state is visited** in an episode.

Example:

```text
Episode:
A → B → A → C
```

Update:

```text
Only first occurrence of A is updated
```

---

## 2️⃣ Every-Visit Monte Carlo

👉 Update value **every time a state is visited**.

Example:

```text
State A appears twice → update twice
```

---

## 📊 Example

### Game Example

Episode:

```text
State1 → State2 → State3 → Goal
```

Rewards:

```text
+1 → +1 → +10
```

Return:

```text
G = 1 + 1 + 10 = 12
```

👉 Update values of all visited states based on this return.

---

## ⚙️ Policy in Monte Carlo

Monte Carlo methods can:

---

### 1️⃣ Evaluate a Policy

* Compute value of states under a policy

---

### 2️⃣ Improve a Policy

* Choose actions with higher returns

---

### 3️⃣ Learn Optimal Policy

Using:

```text
Exploration + Experience
```

---

## 🔄 Monte Carlo Control

Monte Carlo can also learn **optimal policies**.

Steps:

```text
1. Generate episodes using current policy
2. Estimate Q-values from returns
3. Improve policy using Q-values
4. Repeat
```

---

## ⚠️ Exploration Requirement

Monte Carlo requires:

```text
Sufficient exploration of all states/actions
```

👉 Otherwise, it may miss better strategies.

---

## ⚖️ Advantages vs Dynamic Programming

| Feature         | Dynamic Programming | Monte Carlo  |
| --------------- | ------------------- | ------------ |
| Model required  | Yes                 | No           |
| Learning type   | Bootstrapping       | Full episode |
| Real experience | No                  | Yes          |

---

## ⚠️ Limitations

---

### 1️⃣ Needs Complete Episodes

* Cannot learn until episode ends

---

### 2️⃣ Slow Learning

* Requires many episodes

---

### 3️⃣ High Variance

* Results may vary due to randomness

---

## 🚀 Why Monte Carlo is Important

Monte Carlo methods are important because:

* no need for environment model
* learn from real experience
* foundation for advanced RL algorithms

---

## ⚠️ Important Points

* MC learns from **complete episodes**
* Uses **actual returns**, not estimates
* No model required
* Supports both evaluation and control
* Requires sufficient exploration

---

## 🧠 One-Line Summary

> Monte Carlo methods learn value functions in reinforcement learning by averaging total rewards from complete episodes without requiring a model of the environment.
