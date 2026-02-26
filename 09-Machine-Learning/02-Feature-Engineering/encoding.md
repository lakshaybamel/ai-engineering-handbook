# 🔄 Encoding (Categorical Data)

## 📌 What is Encoding?

Encoding is the process of converting **categorical data (text)** into **numerical form** so that machine learning models can understand it.

---

## 🧠 Why Encoding is Needed?

Machine Learning models work with **numbers**, not text.

Example:
```
Gender = Male / Female
```

👉 Model cannot understand this directly

➡️ Convert to:

```
Male = 1
Female = 0
```

---

## 📊 Types of Categorical Data

### 1. Nominal Data
- No order  
- Example:
  - color (red, blue, green)  
  - city  

---

### 2. Ordinal Data
- Has order  
- Example:
  - low < medium < high  
  - education level  

---

## 🔷 Encoding Techniques

---

## 1. Label Encoding

### 📌 Concept
Convert categories into numbers

```
Low = 0
Medium = 1
High = 2
```

---

### 🧠 When to Use?

- Ordinal data (where order matters)

---

### ⚠️ Problem

For nominal data, model may assume:

```
2 > 1 > 0
```


👉 which is incorrect

---

## 2. One-Hot Encoding

### 📌 Concept
Create separate columns for each category

Example:

```
Color = Red, Blue, Green
```

Becomes:

```
Red Blue Green
1    0    0
0    1    0
0    0    1
```

---

### 🧠 When to Use?

- Nominal data  
- No order between categories  

---

### ⚠️ Problem

- Creates many columns  
- Can increase dimensionality  

---

## 3. get_dummies (Pandas)

### 📌 Implementation

```python 
id="enc-code-1"
df = pd.get_dummies(df, drop_first=True)
```

### 🧠 Why drop_first=True?

- Avoids multicollinearity  
- Prevents dummy variable trap  

---

### 🔗 Connection to Dummy Variable Trap

👉 One-hot encoding can create redundant features  
➡️ This is handled using:  
- `drop_first=True`  

(Explained in next file)

---

### 📊 Example

**Before encoding:**

| Gender | City   |
|--------|--------|
| Male   | Delhi  |
| Female | Mumbai |

**After encoding:**

| Gender_Male | City_Delhi | City_Mumbai |
|-------------|------------|-------------|
| 1           | 1          | 0           |
| 0           | 0          | 1           |

---

## ⚠️ Important Points

- Always encode categorical data before training  
- Choose technique based on data type  
- Avoid creating unnecessary features  

---

## 🧠 Interview Insight

👉 **Question:**<br>
Why not use label encoding for nominal data?  

👉 **Answer:**<br>
Because it introduces a false order among categories, which can mislead the model.  

---

## 🧠 One-Line Summary

> Encoding converts categorical data into numerical form so that machine learning models can process it.