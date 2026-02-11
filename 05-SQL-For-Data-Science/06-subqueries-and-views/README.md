# Subqueries and Views

Sometimes a query depends on the result of another query.

Instead of writing multiple steps, SQL allows nesting queries inside queries.
This is called a Subquery.

Views allow saving a query as a virtual table.

---

## Subqueries

A query written inside another query.

General structure:

```sql
SELECT column
FROM table
WHERE column OPERATOR (
    SELECT column FROM table
);
```

---

## Subquery in WHERE

Find students older than average age:

```sql
SELECT *
FROM students
WHERE age > (
    SELECT AVG(age) FROM students
);
```

---

## Subquery in SELECT

```sql
SELECT name,
       (SELECT AVG(age) FROM students) AS avg_age
FROM students;
```

---

## Subquery in FROM

Acts like a temporary table:

```sql
SELECT city, avg_age
FROM (
    SELECT city, AVG(age) AS avg_age
    FROM students
    GROUP BY city
) AS city_avg;
```

---

## Correlated Subquery

Runs once for each row of outer query.

Example: students older than city average

```sql
SELECT s1.*
FROM students s1
WHERE age > (
    SELECT AVG(age)
    FROM students s2
    WHERE s1.city = s2.city
);
```

---

## Views

A view is a saved SQL query treated like a table.

It does not store data — only stores query logic.

**Create view:**

```sql
CREATE VIEW adult_students AS
SELECT * FROM students WHERE age >= 18;
```

**Use view:**

```sql
SELECT * FROM adult_students;
```

**Delete view:**

```sql
DROP VIEW adult_students;
```

---

## Why This Matters in AI

Subqueries help create derived features.<br>
Views help reuse complex dataset logic.

Example:
Instead of repeating joins → create a view → load into Pandas.

