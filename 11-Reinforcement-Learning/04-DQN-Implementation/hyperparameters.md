# ⚙️ Hyperparameters in DQN

## 📌 Overview

**Hyperparameters** are configuration values that control how a Deep Q-Network (DQN) is trained.

They are not learned by the model but are **set manually before training**.

👉 Choosing the right hyperparameters is critical for:

* stable training
* faster convergence
* better performance

---

## 🧠 Intuition

Think of hyperparameters as:

```text
Rules that guide how the agent learns
```

If chosen poorly:

```text
Training becomes unstable or slow ❌
```

If chosen well:

```text
Efficient and stable learning ✅
```

---

## 🔑 Important Hyperparameters in DQN

---

### 1️⃣ Learning Rate (α)

Controls how much the model updates weights.

```text
Small → slow learning  
Large → unstable learning
```

Example:

```text
learning_rate = 0.001
```

---

### 2️⃣ Discount Factor (γ)

Determines importance of future rewards.

```text
γ = 0   → only immediate reward  
γ ≈ 1   → long-term rewards matter
```

Example:

```text
gamma = 0.99
```

---

### 3️⃣ Epsilon (ε)

Controls exploration vs exploitation.

```text
ε = 1.0 → full exploration  
ε → 0   → more exploitation
```

---

### 4️⃣ Epsilon Decay

Controls how ε decreases over time.

```text
ε = ε × decay_rate
```

Example:

```text
epsilon_decay = 0.995
min_epsilon = 0.01
```

---

### 5️⃣ Batch Size

Number of samples used in one training step.

```text
Small batch → noisy learning  
Large batch → stable but slow
```

Example:

```text
batch_size = 32
```

---

### 6️⃣ Replay Buffer Size

Maximum number of stored experiences.

```text
Too small → less learning  
Too large → more memory usage
```

Example:

```text
buffer_size = 10000
```

---

### 7️⃣ Target Network Update Frequency

How often target network is updated.

```text
Frequent → unstable  
Less frequent → stable
```

Example:

```text
update_every = 1000 steps
```

---

### 8️⃣ Number of Episodes

Total training episodes.

```text
More episodes → better learning  
Too many → longer training time
```

Example:

```text
episodes = 500
```

---

### 9️⃣ Max Steps per Episode

Limits steps in one episode.

```text
Prevents infinite loops
```

Example:

```text
max_steps = 200
```

---

## 📊 Summary Table

| Hyperparameter   | Purpose                   |
| ---------------- | ------------------------- |
| Learning Rate    | Controls weight update    |
| Gamma (γ)        | Future reward importance  |
| Epsilon (ε)      | Exploration control       |
| Batch Size       | Training samples per step |
| Buffer Size      | Memory capacity           |
| Update Frequency | Target network stability  |
| Episodes         | Training duration         |

---

## 🚀 Tips for Choosing Hyperparameters

* start with standard values
* tune one parameter at a time
* monitor loss and rewards
* avoid extreme values
* use decay strategies

---

## ⚠️ Common Mistakes

* very high learning rate → divergence
* no epsilon decay → poor learning
* small buffer → insufficient data
* too frequent updates → instability

---

## ⚠️ Important Points

* hyperparameters control training behavior
* they must be tuned carefully
* different environments need different values
* crucial for performance

---

## 🧠 One-Line Summary

> Hyperparameters control how a DQN learns, and proper tuning of these values is essential for achieving stable and efficient reinforcement learning.
