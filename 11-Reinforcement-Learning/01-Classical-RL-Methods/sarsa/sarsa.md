# 🔁 SARSA Algorithm (State-Action-Reward-State-Action)

## 📌 Overview

**SARSA** is a Reinforcement Learning algorithm used to learn the **optimal policy**.

The name SARSA comes from the sequence:

```text
State → Action → Reward → Next State → Next Action
```

👉 SARSA is an **on-policy algorithm**, meaning it learns using the **same policy it follows**.

---

## 🧠 Intuition

Imagine learning to navigate a maze 🧩:

* You follow a certain strategy
* You observe what happens
* You improve based on that same strategy

👉 SARSA learns based on **what the agent actually does**, not the best possible action.

---

## 🧩 Key Idea

SARSA updates the **Q-value** using:

```text
Current experience + next action chosen by policy
```

👉 It considers:

```text
What action you actually took next
```

---

## ⚙️ SARSA Update Rule

The core update equation:

```text
Q(s, a) = Q(s, a) + α [ R + γQ(s', a') - Q(s, a) ]
```

Where:

* **s** → current state
* **a** → current action
* **R** → reward
* **s'** → next state
* **a'** → next action (chosen by policy)
* **α** → learning rate
* **γ** → discount factor

---

## 🔄 SARSA Learning Process

Step-by-step:

```text
1. Initialize Q-table
2. Choose action (using policy like ε-greedy)
3. Take action → observe reward and next state
4. Choose next action using same policy
5. Update Q-value using SARSA formula
6. Repeat
```

---

## 📊 Example

### Grid World

Step:

```text
State: (0,0)
Action: Right
Reward: -1
Next State: (0,1)
Next Action: Down
```

Update:

```text
Q(0,0,Right) = Q(0,0,Right) + α [ -1 + γQ(0,1,Down) - Q(0,0,Right) ]
```

👉 Notice:

* Uses **Q(s', a')**
* Depends on **next action chosen**

---

## 🧭 On-Policy Nature

SARSA is **on-policy**:

👉 It learns the value of the policy it is following.

This means:

```text
Learning = Behavior
```

👉 If policy is risky → learning reflects risk  
👉 If policy is safe → learning reflects safety

---

## ⚖️ SARSA vs Q-Learning (Preview)

| Feature     | SARSA     | Q-Learning   |
| ----------- | --------- | ------------ |
| Type        | On-policy | Off-policy   |
| Update uses | Q(s', a') | max Q(s', a) |
| Behavior    | Safe      | Aggressive   |

---

## 🎯 Behavior of SARSA

SARSA tends to:

* learn **safer paths**
* avoid risky actions
* consider exploration in learning

Example:

```text
Avoid paths near dangerous states
```

---

## 🚀 Where SARSA is Useful

* Environments with **risk or penalties**
* Situations where safe behavior is preferred
* Real-world systems where mistakes are costly

---

## ⚠️ Limitations

---

### 1️⃣ Slower Convergence

* Learns more cautiously

---

### 2️⃣ Depends on Policy

* Performance depends on exploration strategy

---

## ⚠️ Important Points

* SARSA is an **on-policy algorithm**
* Uses actual next action for update
* Learns safer policies
* Based on Temporal Difference learning
* Works with Q-values

---

## 🧠 One-Line Summary

> SARSA is an on-policy reinforcement learning algorithm that updates Q-values using the current action and the next action chosen by the same policy.
