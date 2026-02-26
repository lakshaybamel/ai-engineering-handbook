# ⚠️ Dummy Variable Trap

## 📌 What is Dummy Variable Trap?

Dummy Variable Trap occurs when **one or more features become redundant due to high correlation** after encoding.

👉 This leads to **multicollinearity**

---

## 🧠 Intuition

After one-hot encoding:

If we have:

```
Gender = Male, Female
```

After encoding:

```
Male Female
 1    0
 0    1
```

👉 One column can be predicted from the other:

```
Female = 1 - Male
```

➡️ This creates **redundancy**

---

## ⚠️ Problem

- Features become highly correlated  
- Model gets confused  
- Coefficients become unstable  
- Affects performance of linear models  

---

## 🔍 Why It Happens?

Because:
> One-hot encoding creates **dependent variables**

---

## ✅ Solution

👉 Remove one column from each category

---

## 🔷 Using Pandas

```python
df = pd.get_dummies(df, drop_first=True)
```

---

### 🧠 Why drop_first=True?

- Removes one category  
- Eliminates redundancy  
- Prevents multicollinearity  

---

## 📊 Example

**Without drop_first:**

| Male | Female |
|------|--------|
| 1    | 0      |
| 0    | 1      |

**With drop_first:**

| Male |
|------|
| 1    |
| 0    |

👉 Female can be inferred automatically  

---

## ⚠️ When It Matters Most

- Linear Regression  
- Logistic Regression  
- Models sensitive to multicollinearity  

---

## 🧠 When It Doesn't Matter Much

- Tree-based models (Decision Trees, Random Forest)  

---

## 🧠 Interview Insight

👉 **Question:**<br>
What is dummy variable trap?  

👉 **Answer:**<br>
It is a situation where one-hot encoded variables are highly correlated, causing multicollinearity and affecting model performance.  

---

## 🧠 One-Line Summary

> Dummy Variable Trap occurs due to redundant features after encoding, and is avoided by dropping one category.