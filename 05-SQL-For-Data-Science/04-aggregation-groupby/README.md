# Aggregation and Group By

Raw data is rarely useful directly.  
We often need summaries:

- average salary
- total sales
- number of users
- highest score

Aggregation converts raw rows into meaningful information.

This is equivalent to `groupby()` in Pandas.

---

## Aggregate Functions

### COUNT

Counts rows.

```sql
SELECT COUNT(*) FROM students;
```

Count specific column:

```sql
SELECT COUNT(city) FROM students;
```

### SUM

```sql
SELECT SUM(age) FROM students;
```

### AVG

```sql
SELECT AVG(age) FROM students;
```

### MAX and MIN

```sql
SELECT MAX(age) FROM students;
SELECT MIN(age) FROM students;
```

### GROUP BY

Used to aggregate per category.

Example: count students per city

```sql
SELECT city, COUNT(*)
FROM students
GROUP BY city;
```

Average age per city:

```sql
SELECT city, AVG(age)
FROM students
GROUP BY city;
```

### HAVING Clause

Filters grouped results (after aggregation).

Difference:

|WHERE       |HAVING        |
|------------|--------------|
|filters rows|filters groups|

Example:

```sql
SELECT city, COUNT(*)
FROM students
GROUP BY city
HAVING COUNT(*) > 1;
```

---

## General Execution Order

SQL does not execute top-to-bottom.

Actual order:

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

Understanding this explains many SQL errors.

---

## Why This Matters in AI

Aggregation helps in:

- feature engineering
- trend analysis
- dataset understanding

Example:
Average spending per user → ML feature