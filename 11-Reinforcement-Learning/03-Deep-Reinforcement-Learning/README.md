# 🤖 Deep Reinforcement Learning

Deep Reinforcement Learning combines:

* **Reinforcement Learning (RL)**
* **Deep Learning (Neural Networks)**

to solve complex problems where traditional RL methods fail due to **large or high-dimensional state spaces**.

Instead of using Q-tables, Deep RL uses **neural networks to approximate value functions and policies**.

---

# 📂 Topics Covered

### 📘 Core Concepts

📄 [deep_rl_intro.md](deep_rl_intro.md)

Introduction to Deep Reinforcement Learning.

Topics covered:

* why Deep RL is needed
* limitations of classical RL
* neural networks for function approximation

---

### ⚡ Deep Q-Network (DQN)

📄 [dqn.md](dqn.md)

Core algorithm in Deep RL.

Topics covered:

* Q-learning with neural networks
* DQN architecture
* training process

---

### 🔁 Experience Replay

📄 [experience_replay.md](experience_replay.md)

Technique to improve training stability.

Topics covered:

* replay buffer
* random sampling
* breaking data correlation

---

### 🎯 Target Network

📄 [target_network.md](target_network.md)

Technique to stabilize learning.

Topics covered:

* online vs target network
* moving target problem
* periodic updates

---

### 📉 Epsilon Decay

📄 [epsilon_greedy_decay.md](epsilon_greedy_decay.md)

Improves exploration strategy.

Topics covered:

* ε-greedy policy
* exploration vs exploitation
* decay strategies

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ why classical RL fails in complex environments  
✔ how neural networks are used in RL  
✔ how DQN works internally  
✔ how training is stabilized using replay and target   networks  
✔ how exploration is improved using epsilon decay  

---

# 🧠 Key Takeaway

> Deep Reinforcement Learning uses neural networks along with techniques like experience replay and target networks to enable stable and scalable learning in complex environments.
