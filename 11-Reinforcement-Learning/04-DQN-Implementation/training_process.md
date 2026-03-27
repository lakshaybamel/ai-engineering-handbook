# ⚙️ Training Process of DQN

## 📌 Overview

The **training process of a Deep Q-Network (DQN)** involves:

* interacting with the environment
* storing experiences
* sampling from replay buffer
* updating the neural network

The goal is to **learn optimal Q-values** so that the agent can take the best actions.

---

## 🧠 Intuition

DQN learns by repeating this cycle:

```text
Act → Observe → Store → Learn → Improve
```

👉 Over time, the agent improves its decisions based on experience.

---

## 🔁 Step-by-Step Training Process

---

### 1️⃣ Initialize Components

Before training starts:

* initialize **online network (Q-network)**
* initialize **target network**
* initialize **replay buffer**
* set hyperparameters

---

### 2️⃣ Start Episode

Reset the environment:

```text
state = initial_state
```

---

### 3️⃣ Choose Action (ε-greedy)

```text
With probability ε → random action (explore)
Else → best action (exploit)
```

---

### 4️⃣ Take Action

```text
next_state, reward, done = env.step(action)
```

👉 Agent interacts with environment.

---

### 5️⃣ Store Experience

Save transition in replay buffer:

```text
(state, action, reward, next_state, done)
```

---

### 6️⃣ Sample Batch

Once enough data is collected:

```text
Sample random batch from replay buffer
```

Example:

```text
batch_size = 32
```

---

### 7️⃣ Compute Target Q-values

Using **target network**:

```text
target = r + γ max Q(s', a')
```

If episode ends:

```text
target = r
```

---

### 8️⃣ Compute Predicted Q-values

Using **online network**:

```text
Q(s, a)
```

---

### 9️⃣ Compute Loss

```text
Loss = (target - predicted)^2
```

👉 Usually Mean Squared Error (MSE).

---

### 🔟 Backpropagation

* calculate gradients
* update network weights

```text
optimizer.step()
```

---

### 1️⃣1️⃣ Update Target Network

Periodically:

```text
θ_target = θ
```

👉 Keeps learning stable.

---

### 1️⃣2️⃣ Update Epsilon

```text
ε = decay(ε)
```

👉 Shift from exploration → exploitation.

---

### 1️⃣3️⃣ Repeat

Continue for:

* multiple steps
* multiple episodes

---

## 🔄 Full Training Loop

```text
For each episode:
    reset environment
    For each step:
        choose action (ε-greedy)
        take action
        store experience
        sample batch
        compute target
        update network
    update target network
    decay epsilon
```

---

## 📊 Key Components in Training

| Component      | Role                 |
| -------------- | -------------------- |
| Replay Buffer  | Stores experiences   |
| Target Network | Stabilizes learning  |
| ε-greedy       | Balances exploration |
| Loss Function  | Measures error       |
| Optimizer      | Updates weights      |

---

## 🚀 Advantages

* learns from past experiences
* stable training with replay buffer
* scalable to complex environments
* efficient learning

---

## ⚠️ Challenges

* requires tuning hyperparameters
* training can be slow
* unstable without proper techniques
* needs large data

---

## ⚠️ Important Points

* training is iterative
* uses experience replay
* uses target network
* balances exploration and exploitation
* improves over time

---

## 🧠 One-Line Summary

> The DQN training process involves interacting with the environment, storing experiences, sampling random batches, and updating the neural network to learn optimal actions over time.
