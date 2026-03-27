# 📈 What Agent Learns with SARSA

## 📌 Overview

While **SARSA** defines how Q-values are updated, it is equally important to understand:

👉 **What kind of behavior the agent learns using SARSA**

SARSA is an **on-policy algorithm**, so it learns based on the **actual actions taken during training**.

This leads to a very important property:

```text
SARSA learns safe and cautious behavior
```

---

## 🧠 Intuition

Imagine walking near a cliff 🧗:

* A risky strategy → walk near the edge (short path but dangerous)
* A safe strategy → stay away from the edge (longer but safer)

👉 SARSA prefers:

```text
Safer path even if it is longer
```

Because it considers **exploration during learning**.

---

## ⚙️ Why SARSA Learns Safe Behavior

Recall SARSA update rule:

```text
Q(s, a) = Q(s, a) + α [ R + γQ(s', a') - Q(s, a) ]
```

👉 It uses:

```text
Q(s', a') → next action actually taken
```

If the policy is ε-greedy:

* Sometimes random (exploration)
* Sometimes best action (exploitation)

👉 So learning includes **risk of exploration**.

---

## 📊 Example: Cliff Walking Problem

Environment:

```text
Start → Safe Path → Goal
   ↓
  Cliff (very high negative reward)
```

---

### SARSA Behavior

SARSA considers that:

* Agent might explore
* Exploration near cliff = dangerous

So it learns:

```text
Stay away from cliff
```

---

### Resulting Policy

```text
Longer but safer path
```

Example:

```text
S → Up → Right → Right → Down → G
```

👉 Avoids risky area.

---

## ⚖️ Comparison Insight

### SARSA Learning Style:

| Behavior Type   | SARSA        |
| --------------- | ------------ |
| Risk handling   | Avoids risk  |
| Path selection  | Safe path    |
| Learning nature | Conservative |

---

## 🔄 Learning Process Insight

During training:

```text
1. Agent explores environment
2. Experiences penalties (if risky)
3. Updates Q-values accordingly
4. Learns to avoid risky states
```

👉 Over time:

```text
Policy becomes safer and stable
```

---

## 🧩 Role of Exploration

Because SARSA includes exploration in updates:

```text
Exploration affects learning
```

Example:

* If ε is high → more cautious learning
* If ε decreases → more stable behavior

---

## 🎯 Key Observation

SARSA does NOT assume optimal future behavior.

👉 It assumes:

```text
Future actions will follow the same policy
```

This makes it:

* realistic
* practical
* safer

---

## 🚀 When SARSA is Preferred

SARSA is useful when:

* environment has **dangerous states**
* safety is more important than speed
* mistakes are costly

Examples:

* robotics
* autonomous driving
* medical decision systems

---

## ⚠️ Important Points

* SARSA learns based on **actual experience**
* Considers exploration during learning
* Produces **safe and stable policies**
* Avoids risky actions
* On-policy learning

---

## 🧠 One-Line Summary

> SARSA learns safer and more conservative policies by considering the actual actions taken during training, including exploration, which helps avoid risky decisions.
