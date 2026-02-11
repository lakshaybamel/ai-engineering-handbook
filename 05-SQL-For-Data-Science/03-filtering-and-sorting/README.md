# Filtering and Sorting Data

Databases often contain millions of records.  
We rarely need all data — we need relevant data.

Filtering allows selecting required rows.  
Sorting allows arranging them meaningfully.

This step is similar to filtering rows in Pandas.

---

## WHERE Clause

Used to filter rows based on conditions.

```sql
SELECT * FROM students
WHERE city = 'Delhi';
```

---

## Comparison Operators

| Operator | Meaning             |
|----------|---------------------|
| =        | equal               |
| !=       | not equal           |
| >        | greater than        |
| <        | less than           |
| >=       | greater or equal    |
| <=       | less or equal       |

Example:

```sql
SELECT * FROM students
WHERE age > 22;
```

---

## Logical Operators

Combine multiple conditions.

### AND

```sql
SELECT * FROM students
WHERE city = 'Delhi' AND age > 20;
```

### OR

```sql
SELECT * FROM students
WHERE city = 'Delhi' OR city = 'Mumbai';
```

## NOT

```sql
SELECT * FROM students
WHERE NOT city = 'Delhi';
```

---

## Frequently Used Operators

### BETWEEN

```sql
SELECT * FROM students
WHERE age BETWEEN 20 AND 25;
```

### IN

```sql
SELECT * FROM students
WHERE city IN ('Delhi', 'Mumbai');
```

### LIKE (pattern matching)

```sql
SELECT * FROM students
WHERE name LIKE 'A%';
```

`%` → any characters
`_` → single character

---

## LIMIT Clause

Restrict number of rows returned.

```sql
SELECT * FROM students
LIMIT 5;
```

Useful for previewing large datasets.

---

## ORDER BY Clause

Sort results.

Ascending (default):

```sql
SELECT * FROM students
ORDER BY age;
```

Descending:

```sql
SELECT * FROM students
ORDER BY age DESC;
```

Multiple columns:

```sql
SELECT * FROM students
ORDER BY city, age DESC;
```

---

## Why This Matters in AI

Before ML training:

- remove irrelevant records
- filter time ranges
- select categories
- sample subset

Filtering is the first step of feature selection.