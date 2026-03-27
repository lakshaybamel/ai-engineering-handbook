# ⚙️ Environment Setup for DQN

## 📌 Overview

Before implementing a **Deep Q-Network (DQN)**, we need to properly set up the **environment** in which the agent will interact.

The environment defines:

* states
* actions
* rewards
* transitions

👉 It is the **foundation of the entire reinforcement learning pipeline**.

---

## 🧠 Intuition

In Reinforcement Learning:

```text
Agent ↔ Environment
```

* Agent takes action
* Environment responds with:

  * next state
  * reward

👉 The agent learns from this interaction.

---

## 🧩 Components of Environment

### 1️⃣ State (s)

Represents the current situation of the agent.

Examples:

* position in grid
* game screen (image)
* sensor data

---

### 2️⃣ Action (a)

Possible decisions the agent can take.

Examples:

* move left / right
* jump
* accelerate / brake

---

### 3️⃣ Reward (r)

Feedback from the environment.

* positive → good action
* negative → bad action

---

### 4️⃣ Next State (s')

State after taking action.

```text
(s, a) → (s', r)
```

---

## ⚙️ Using Environments in Practice

In Deep RL, we usually use environments from:

* OpenAI Gym / Gymnasium
* custom environments

---

## 🧪 Example: Gym Environment

```python
import gym

env = gym.make("CartPole-v1")
state = env.reset()
```

---

## 🔁 Interaction Loop

Basic interaction with environment:

```python
state = env.reset()

done = False

while not done:
    action = env.action_space.sample()  # random action
    next_state, reward, done, info = env.step(action)
    
    state = next_state
```

---

## 🧠 What Happens Internally

At each step:

```text
Agent → Action
Environment → Next State + Reward
```

This loop continues until:

* goal is reached
* episode ends

---

## 📊 Observation Space

Defines what the agent observes.

Example:

```python
env.observation_space
```

---

## 🎯 Action Space

Defines possible actions:

```python
env.action_space
```

Types:

* Discrete → finite actions
* Continuous → range of values

---

## ⚠️ Important Considerations

* Environment must be **well-defined**
* Rewards should guide learning properly
* State representation should be meaningful
* Episode termination conditions must be clear

---

## 🚀 Why Environment Setup is Important

* defines learning problem
* impacts performance of DQN
* affects convergence
* determines complexity

---

## ⚠️ Important Points

* environment = interaction system
* defines states, actions, rewards
* used in every RL algorithm
* critical for training success

---

## 🧠 One-Line Summary

> Environment setup defines how the agent interacts with the world, providing states, actions, and rewards that guide the learning process in Deep Reinforcement Learning.
