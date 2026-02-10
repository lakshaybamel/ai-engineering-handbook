# Pandas Quick Reference

A compact guide for commonly used Pandas operations.

---

## 1. Import & Setup

```python
import pandas as pd
```

Check version:

```python
pd.__version__
```

---

## 2. Series Basics

Create Series from list:

```python
s = pd.Series([10,20,30])
```

With custom index:

```python
s = pd.Series([10,20,30], index=["a","b","c"])
```

From dictionary:

```python
data = {"Delhi":40, "Mumbai":35}
s = pd.Series(data)
```

Access values:

```python
s["a"]
s[0]
```

Properties:

```python
s.index
s.values
```

Basic operations:

```python
s + 10
s * 2
```

Handling missing values:

```python
s.isnull()
s.notnull()
```

Statistics:

```python
s.mean()
s.max()
s.min()
```

---

## 3. DataFrame Basics

Create DataFrame:

```python
data = {
    "Name": ["Lakshay", "Harsh", "Aditya"],
    "Age": [21,24,22]
}

df = pd.DataFrame(data)
```

Columns & index:

```python
df.columns
df.index
```

Select column (Series):

```python
df["Name"]
```

Multiple columns:

```python
df[["Name","Age"]]
```

Add column:

```python
df["Salary"] = [50000,60000,55000]
```

Delete column:

```python
df.drop("Salary", axis=1)
```

Row selection:

```python
df.loc[0]
df.iloc[0]
```

Basic info:

```python
df.info()
df.describe()
```

---

## 4. Loading & Saving Data

Read CSV:

```python
df = pd.read_csv("file.csv")
```

Read JSON:

```python
df = pd.read_json("file.json")
```

Write CSV:

```python
df.to_csv("output.csv", index=False)
```

Write JSON:

```python
df.to_json("output.json", orient="records")
```

---

## 5. Inspecting Data

View data:

```python
df.head()
df.tail()
df.sample(5)
```

Shape & size:

```python
df.shape
len(df)
```

Column names:

```python
df.columns
```

Data types:

```python
df.dtypes
```

Summary statistics:

```python
df.describe()
```

Unique values:

```python
df["city"].unique()
df["category"].value_counts()
```

---

## 6. Selection & Indexing

Select column:

```python
df["price"]
```

Multiple columns:

```python
df[["product","price"]]
```

Select rows by label:

```python
df.loc[0]
df.loc[0:3]
```

Select rows by position:

```python
df.iloc[0]
df.iloc[0:3]
```

Select specific row & column:

```python
df.loc[0, "price"]
df.iloc[0, 2]
```

---

## 7. Filtering & Query

Conditional filtering:

```python
df[df["price"] > 5000]
df[(df["city"] == "Delhi") & (df["price"] > 2000)]
```

Using query:

```python
df.query("price > 5000")
df.query("city == 'Delhi'")
```

---

## 8. Handling Missing Values

Check missing values:

```python
df.isnull()
df.isnull().sum()
```

Fill missing values:

```python
df.fillna(0)
df["city"].fillna("Unknown", inplace=True)
```

Drop missing values:

```python
df.dropna()
df.dropna(subset=["price"])
```

---

## 9. Cleaning Data (Duplicates, Strings, Types)

Duplicates:

```python
df.duplicated()
df.drop_duplicates()
```

String cleaning:

```python
df["product"].str.lower()
df["product"].str.upper()
df["city"].str.strip()
df["name"].str.replace("Mr.", "")
```

Change data types:

```python
df["price"] = df["price"].astype(float)
df["date"] = pd.to_datetime(df["date"])
```

---

## 10. Column Operations & Transformation

Create new column:

```python
df["total"] = df["price"] * df["quantity"]
```

Apply function:

```python
def category(p):
    if p > 5000:
        return "High"
    return "Low"

df["level"] = df["price"].apply(category)
```

Map values:

```python
mapping = {"Delhi":"D", "Mumbai":"M"}
df["city_code"] = df["city"].map(mapping)
```

Replace values:

```python
df["category"] = df["category"].replace({"Electronics":"Tech"})
```

---

## 11. GroupBy & Aggregation

Group data:

```python
df.groupby("city")
```

Count:

```python
df.groupby("city")["order_id"].count()
```

Sum:

```python
df.groupby("city")["total"].sum()
```

Mean:

```python
df.groupby("category")["price"].mean()
```

Multiple aggregations:

```python
df.groupby("city")["total"].agg(["sum","mean","max"])
```

Group by multiple columns:

```python
df.groupby(["city","category"])["total"].sum()
```

Reset index:

```python
result = df.groupby("city")["total"].sum().reset_index()
```

---

## 12. Reshaping Data (Pivot, Melt)

Pivot table:

```python
df.pivot_table(values="total", index="city", columns="category", aggfunc="sum")
```

Melt:

```python
pd.melt(df, id_vars="city", var_name="variable", value_name="value")
```

Stack / Unstack:

```python
df.stack()
df.unstack()
```

---

## 13. Merge, Join & Concat

Merge (SQL style join):

```python
pd.merge(df1, df2, on="id", how="inner")
pd.merge(df1, df2, on="id", how="left")
pd.merge(df1, df2, on="id", how="right")
pd.merge(df1, df2, on="id", how="outer")
```

Join (index based):

```python
df1.set_index("id").join(df2.set_index("id"), lsuffix="_left", rsuffix="_right")
```

Concat (row-wise):

```python
pd.concat([df1, df2])
pd.concat([df1, df2], ignore_index=True)
```

Concat (column-wise):

```python
pd.concat([df1, df2], axis=1)
```

---

## 14. Sorting & Ranking

Sort values:

```python
df.sort_values("price")
df.sort_values("price", ascending=False)
```

Sort by multiple columns:

```python
df.sort_values(["city","price"])
```

Ranking:

```python
df["rank"] = df["price"].rank()
df["rank_desc"] = df["price"].rank(ascending=False)
```

---

## 15. Basic Visualization (syntax only)

Histogram:

```python
df["price"].hist()
```

Line plot:

```python
df["price"].plot()
```

Scatter plot:

```python
df.plot(kind="scatter", x="price", y="quantity")
```

Bar chart:

```python
df["category"].value_counts().plot(kind="bar")
```

Box plot:

```python
df.boxplot(column="price")
```

Pie chart:

```python
df["category"].value_counts().plot(kind="pie")
```