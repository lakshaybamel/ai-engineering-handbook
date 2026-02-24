# 📈 Best Fit Line

## 📌 What is a Best Fit Line?

A Best Fit Line is a straight line that **best represents the relationship** between input (X) and output (y) in a dataset.

👉 It is the line that is **closest to all data points**.

---

## 🧠 Intuition

Imagine plotting data points on a graph.

👉 We want a line that:
- passes as close as possible to all points  
- captures the overall trend  

> This line is called the **Best Fit Line**

---

## 📊 Example

Predicting salary based on experience:

- More experience → higher salary  
- Data points may not lie perfectly on a line  

👉 Best Fit Line captures the **average trend**

---

## ⚙️ Mathematical Form

The equation of a line:

```
y = mx + b
```

Where:
- `m` = slope (how steep the line is)  
- `b` = intercept (where line crosses y-axis)  

👉 Model learns `m` and `b`

---

## 🎯 Goal of Linear Regression

To find the values of `m` and `b` such that:

👉 The line is as close as possible to all data points

---

## 📉 Error Concept

Each data point has some error:

```
error = actual value - predicted value
```

👉 Best Fit Line minimizes this error.

---

## 🧠 How "Best" is Defined?

We define "best" using:

👉 **Minimum total error**

Most commonly:
- Mean Squared Error (MSE)

---

## 📌 Why Not Just Draw Any Line?

Because:
- Different lines give different predictions  
- We want the most accurate one  

👉 So we choose the line with **minimum error**

---

## 🔍 Key Observations

- Not all points lie on the line  
- Line represents general trend  
- Outliers can affect the line  

---

## ⚠️ Limitations

- Works only for linear relationships  
- Sensitive to extreme values (outliers)  

---

## 🧠 One-Line Summary

> Best Fit Line is the line that minimizes prediction error and represents the overall trend of the data.