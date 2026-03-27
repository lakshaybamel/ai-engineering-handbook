# 🧠 Classical Reinforcement Learning Methods

Classical Reinforcement Learning methods form the **foundation of modern RL algorithms**.

These methods focus on learning optimal behavior using:

* value functions
* policies
* iterative updates

before moving to advanced methods like **Deep Reinforcement Learning (DQN, etc.)**.

---

# 📂 Topics Covered

## 📘 Core Methods

### 📄 [dynamic_programming.md](dynamic_programming.md)

Dynamic Programming methods assume a **known environment model**.

Topics covered:

* Bellman equations
* policy evaluation
* policy improvement
* value iteration

---

### 📄 [monte_carlo_methods.md](monte_carlo_methods.md)

Monte Carlo methods learn from **complete episodes**.

Topics covered:

* episode-based learning
* return calculation
* model-free learning
* advantages and limitations

---

### 📄 [temporal_difference_learning.md](temporal_difference_learning.md)

Temporal Difference (TD) learning combines:

* Monte Carlo methods
* Dynamic Programming

Topics covered:

* bootstrapping
* TD update rule
* incremental learning

---

## 🔁 Control Algorithms

### 📁 [sarsa/](sarsa/)

SARSA is an **on-policy learning algorithm**.

Topics covered:

* SARSA update rule
* safe policy learning
* implementation using Grid World

---

### 📁 [q_learning/](q_learning/)

Q-learning is an **off-policy learning algorithm**.

Topics covered:

* optimal policy learning
* greedy updates
* comparison with SARSA
* implementation from scratch

---

# 🎯 Learning Outcome

After completing this section you will understand:

✔ difference between model-based and model-free methods  
✔ how value functions are learned  
✔ how policies are improved over time  
✔ difference between on-policy and off-policy learning  
✔ how classical RL algorithms work step-by-step  

---

# 🧠 Key Takeaway

> Classical RL methods provide the core algorithms for learning optimal decisions through interaction with an environment, forming the base for all advanced reinforcement learning techniques.
