# Joins

Real-world data is split across multiple tables.

Example:

customers table → customer info  
orders table → order records

To analyze behavior, we must combine them.

This is called a JOIN.

Without joins, relational databases would be useless.

---

## Example Tables

### customers

| id | name |
|---|---|
| 1 | Lakshay |
| 2 | Aditya |
| 3 | Harsh |

### orders

| order_id | customer_id | amount |
|---|---|---|
| 101 | 1 | 500 |
| 102 | 2 | 700 |
| 103 | 1 | 300 |

---

## INNER JOIN

Returns matching rows from both tables.

```sql
SELECT c.name, o.amount
FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id;
```

Only customers who placed orders appear.

---

## LEFT JOIN

All records from left table + matching from right.

```sql
SELECT c.name, o.amount
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id;
```

Customers without orders show NULL.

---

## RIGHT JOIN

All records from right table + matching from left.

```sql
SELECT c.name, o.amount
FROM customers c
RIGHT JOIN orders o
ON c.id = o.customer_id;
```

---

## FULL OUTER JOIN

All records from both tables.

(Some databases simulate using UNION)

---

## CROSS JOIN

Cartesian product (all combinations)

```sql
SELECT *
FROM customers
CROSS JOIN orders;
```

Used rarely — mostly theoretical.

---

## SELF JOIN

Joining a table with itself.

Example: employee-manager relationship

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m
ON e.manager_id = m.id;
```

--- 

## Exclusive Join (Anti Join)

Find unmatched records.

Customers with no orders:

```sql
SELECT c.name
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
WHERE o.customer_id IS NULL;
```

---

## Why Joins Matter in AI

Data rarely exists in a single table.

Before ML:

- combine users
- combine transactions
- combine events

Joins build the final dataset used for training models.