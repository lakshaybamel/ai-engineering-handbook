# 🧠 Other Feature Engineering Techniques

## 📌 Overview

Feature Engineering is not limited to encoding and scaling.

Additional techniques help improve:
- model performance  
- data quality  
- generalization  

---

# 🔷 1. Handling Missing Values

## 📌 Problem

Real-world datasets often contain missing values:

```
NaN / null
```

---

## 🧠 Solutions

### 1. Remove Rows/Columns
- If missing values are very high  

---

### 2. Fill Values (Imputation)

- Numerical:
  - Mean  
  - Median  

- Categorical:
  - Mode  

---

## 🔷 Example

```python
id="miss-code-1"
df.fillna(df.mean(), inplace=True)
```

---

# 🔷 2. Feature Selection

## 📌 Concept
Selecting only important features for the model.

## 🧠 Why?
- Reduces overfitting  
- Improves performance  
- Reduces training time  

## 🔷 Methods
- Correlation-based selection  
- Lasso (feature selection)  
- Tree-based importance  

---

# 🔷 3. Handling Outliers

## 📌 Problem
Outliers = extreme values that distort model

## 🧠 Solutions
- Remove outliers  
- Cap values (clipping)  
- Use robust models  

## 🔷 Example (IQR Method)

```python
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
```

---

# 🔷 4. Feature Transformation

## 📌 Concept
Modify features to improve model learning

## 🧠 Examples
- Log transformation  
- Square root  
- Polynomial features  

## 🔷 Example

```python
df["log_feature"] = np.log(df["feature"] + 1)
```

---

# 🔷 5. Feature Creation

## 📌 Concept
Create new features from existing ones

## 🧠 Example
```
BMI = weight / height²
```
```
id="feat1"
```
---

## 🔷 Why Important?

- Adds more useful information  
- Improves model performance  

---

# 🔷 6. Binning

## 📌 Concept

Convert continuous data into categories

---

## 🧠 Example

```
Age → Young / Adult / Old
```

---

## 🔷 Example

```python
id="bin-code-1"
df["age_group"] = pd.cut(df["age"], bins=3, labels=["Low", "Medium", "High"])
```

---

## ⚠️ Important Points

- Feature Engineering directly impacts model performance  
- Better features → better predictions  
- Avoid unnecessary transformations  

---

## 🧠 Interview Insight

👉 **Question:**<br>
What is Feature Engineering?  

👉 **Answer:**<br>
It is the process of transforming raw data into meaningful features that improve machine learning model performance.  

---

## 🧠 One-Line Summary

> Feature Engineering improves model performance by transforming and selecting useful data features.