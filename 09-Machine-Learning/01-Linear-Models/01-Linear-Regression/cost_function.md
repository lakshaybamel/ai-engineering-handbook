# 📉 Cost Function

## 📌 What is a Cost Function?

A Cost Function is a function that measures **how wrong our model's predictions are**.

👉 It tells us:
> "How far is the predicted value from the actual value?"

---

## 🧠 Intuition

We draw a line (Best Fit Line), but:

- Some predictions are correct  
- Some are wrong  

👉 Cost Function calculates **total error of all predictions**

---

## 📊 Error for One Data Point

```
error = actual value - predicted value
```

---

## 📊 Problem with Simple Error

If we directly sum errors:

```
(+ error) + (- error) = 0
```

👉 Errors cancel out → not useful

---

## ✅ Solution → Square the Error

We use:

```
(error)^2
```

👉 Makes all values positive  
👉 Penalizes larger errors more  

---

## 📉 Mean Squared Error (MSE)

Most commonly used cost function:

```
MSE = (1/n) * Σ(actual - predicted)^2
````

Where:
- `n` = number of data points  

---

## 🎯 Goal of Machine Learning Model

👉 Minimize the Cost Function

- Lower cost → better model  
- Higher cost → worse model  

---

## 📈 Cost Function Curve

- X-axis → model parameters (m, b)  
- Y-axis → cost  

👉 Shape is usually:
- **convex (U-shaped curve)**  

---

## 🔍 Why is Cost Function Important?

- Helps evaluate model performance  
- Guides optimization (Gradient Descent)  
- Ensures model improves over time  

---

## 🔗 Connection to Best Fit Line

- Best Fit Line = line with minimum error  
- Cost Function = tool to measure that error  

👉 Together:
> We use cost function to find the best fit line

---

## ⚠️ Key Points

- Always minimize cost  
- Sensitive to outliers (because of square)  
- Works well for regression problems  

---

## 🧠 One-Line Summary

> Cost Function measures how wrong the model is, and we try to minimize it.