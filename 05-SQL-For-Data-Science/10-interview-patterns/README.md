# SQL Thinking Patterns

SQL questions are rarely about remembering syntax.
They test how you think about data relationships.

Most problems reduce to a few repeating patterns.

---

## Finding Duplicates

```sql
SELECT name, COUNT(*)
FROM students
GROUP BY name
HAVING COUNT(*) > 1;
```

Idea:
Group rows and filter groups.

---

## Remove Duplicates (keep first)

```sql
DELETE FROM students
WHERE id NOT IN (
    SELECT MIN(id)
    FROM students
    GROUP BY name
);
```

---

## Second Highest Value

```sql
SELECT MAX(salary)
FROM employees
WHERE salary < (
    SELECT MAX(salary) FROM employees
);
```

Pattern:
Use nested aggregation.

---

## Top N Records

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;
```

---

## Rows Without Matching Records

Customers who never ordered:

```sql
SELECT c.*
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
WHERE o.customer_id IS NULL;
```

Pattern:<br>
LEFT JOIN + NULL filter

---

## Running Total

```sql
SELECT id, salary,
SUM(salary) OVER (ORDER BY id) AS running_total
FROM employees;
```

Pattern:
Window functions

---

## Highest Per Group

Highest salary per department:

```sql
SELECT department, MAX(salary)
FROM employees
GROUP BY department;
```

---

## Subquery vs Join Logic

When:

- filtering based on aggregated value → subquery

- combining columns → join

---

## Mental Checklist

When solving SQL problems ask:

1. Am I filtering rows? → WHERE
2. Am I summarizing? → GROUP BY
3. Am I comparing groups? → HAVING
4. Combining tables? → JOIN
5. Using result of another query? → SUBQUERY

---

## Purpose of This Section

To remember patterns instead of memorizing solutions.

