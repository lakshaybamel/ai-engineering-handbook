# 📉 Gradient Descent

## 📌 What is Gradient Descent?

Gradient Descent is an optimization algorithm used to **minimize the cost function**.

👉 It helps us find the **best parameters (m, b)** for the model.

---

## 🧠 Intuition

Imagine you are standing on a hill:

- Your goal → reach the lowest point (minimum cost)  
- You look at the slope and take a step downward  

👉 Repeat this process until you reach the bottom  

> This process is called **Gradient Descent**

---

## 🎯 Goal

To find values of parameters such that:

👉 Cost Function is **minimum**

---

## ⚙️ How It Works

1. Start with random values of parameters (m, b)  
2. Calculate the cost  
3. Compute the slope (gradient)  
4. Update parameters in opposite direction of slope  
5. Repeat until cost is minimized  

---

## 🔄 Update Rule

```
new_parameter = old_parameter - learning_rate × gradient
```

---

## 📌 Learning Rate (α)

- Controls step size  

### Cases:

- Very small → slow learning  
- Very large → may overshoot minimum  
- Optimal → fast and stable convergence  

---

## 📈 Convergence

- Process continues until:
  - cost stops decreasing  
  - or reaches minimum  

---

## 📉 Why “Descent”?

Because we move:
👉 **downwards on the cost curve**

---

## 🔗 Connection with Cost Function

- Cost Function → tells error  
- Gradient Descent → reduces error  

👉 Together they optimize the model  

---

## ⚠️ Key Points

- Requires proper learning rate  
- May get stuck in local minima (in complex models)  
- Works best with normalized/scaled data  

---

## 🧠 Types of Gradient Descent (Basic Overview)

- Batch Gradient Descent  
- Stochastic Gradient Descent (SGD)  
- Mini-Batch Gradient Descent  

---

## 🧠 One-Line Summary

> Gradient Descent is a method to minimize error by iteratively updating model parameters in the direction of decreasing 