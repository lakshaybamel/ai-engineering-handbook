# 🔁 SARSA (State-Action-Reward-State-Action)

SARSA is an **on-policy reinforcement learning algorithm** used to learn optimal actions in an environment.

Unlike some other methods, SARSA learns using the **actual actions taken by the agent**, including exploration.
This makes it more **realistic and safer** in environments where risky actions should be avoided.

---

# 📂 Files in This Section

### 📘 Algorithm Explanation

📄 [sarsa.md](sarsa.md)

Explains the SARSA algorithm in detail.

Topics covered:

* SARSA update rule
* on-policy learning
* intuition behind SARSA
* how SARSA differs from Q-learning

---

### 📈 Learning Behavior

📄 [sarsa_learning.md](sarsa_learning.md)

Describes **what the agent learns using SARSA**.

Topics covered:

* safe vs risky behavior
* effect of exploration
* behavior in cliff-walking environment
* why SARSA prefers safer paths

---

### 📓 Implementation

📄 [sarsa.ipynb](sarsa.ipynb)

Complete implementation of SARSA using a **Grid World environment**.

The notebook includes:

* environment setup
* Q-table initialization
* ε-greedy policy
* SARSA training loop
* policy visualization

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ how SARSA works step-by-step  
✔ what on-policy learning means  
✔ how exploration affects learning  
✔ why SARSA learns safer policies  
✔ how to implement SARSA from scratch  

---

# 🧠 Key Takeaway

> SARSA learns action values based on the actual policy followed by the agent, making it a safer and more conservative reinforcement learning algorithm.
