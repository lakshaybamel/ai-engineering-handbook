# ⚡ Q-Learning (Off-Policy Reinforcement Learning)

Q-Learning is one of the most important **Reinforcement Learning algorithms** used to learn optimal actions in an environment.

It is an **off-policy algorithm**, meaning it learns the **optimal policy independently of the actions actually taken during training**.

👉 Unlike SARSA, Q-learning always assumes the agent will take the **best possible action in the future**.

---

# 📂 Files in This Section

### 📘 Algorithm Explanation

📄 [q_learning.md](q_learning.md)

Explains the Q-learning algorithm in detail.

Topics covered:

* Q-learning update rule
* off-policy learning
* difference from SARSA
* intuition behind optimal policy learning

---

### 📈 Learning Behavior

📄 [learning_behavior.md](learning_behavior.md)

Describes **what the agent learns using Q-learning**.

Topics covered:

* optimal vs safe behavior
* why Q-learning can be risky
* behavior in cliff-walking environment
* comparison with SARSA

---

### 📓 Implementation

📄 [q_learning.ipynb](q_learning.ipynb)

Complete implementation of Q-learning using a **Grid World environment**.

The notebook includes:

* environment setup
* Q-table initialization
* ε-greedy policy
* Q-learning training loop
* policy visualization

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ how Q-learning works step-by-step  
✔ what off-policy learning means  
✔ how optimal policies are learned  
✔ difference between SARSA and Q-learning  
✔ how to implement Q-learning from scratch  

---

# 🧠 Key Takeaway

> Q-learning learns the optimal policy by always updating action values using the best possible future reward, making it efficient but sometimes risky.
