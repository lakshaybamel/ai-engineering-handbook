# SQL for Data

SQL (Structured Query Language) is used to retrieve structured data from relational databases.

In real AI/ML systems, data rarely starts inside Python.  
It exists in production databases and must be extracted correctly before analysis.

This module acts as a reference handbook for understanding how raw database data becomes a usable dataset.

---

## SQL in the AI Workflow

Application Data → Database → **SQL Queries** → Pandas → Feature Engineering → Machine Learning

SQL decides **which data enters the ML pipeline**.

Wrong query → wrong dataset → wrong model

---

## Module Contents

### 1. Database Fundamentals
📂 [Database Fundamentals](01-database-fundamentals/README.md)

Concepts covered:
- What is a database
- Tables and relationships
- SQL vs NoSQL
- Primary and foreign keys
- Constraints

---

### 2. CRUD Operations
📂 [CRUD Operations](02-crud-operations/README.md)

Concepts covered:
- INSERT
- SELECT
- UPDATE
- DELETE
- ALTER and TRUNCATE

---

### 3. Filtering and Sorting
📂 [Filtering and Sorting](03-filtering-and-sorting/README.md)

Concepts covered:
- WHERE conditions
- Operators
- LIMIT
- ORDER BY
- Pattern matching

---

### 4. Aggregation and Grouping
📂 [Aggregation & Group By](04-aggregation-groupby/README.md)

Concepts covered:
- COUNT, SUM, AVG
- GROUP BY
- HAVING
- Execution order

---

### 5. Joins
📂 [Joins](05-joins/README.md)

Concepts covered:
- INNER JOIN
- LEFT / RIGHT JOIN
- CROSS JOIN
- SELF JOIN
- Anti Join logic

---

### 6. Subqueries and Views
📂 [Subqueries & Views](06-subqueries-and-views/README.md)

Concepts covered:
- Nested queries
- Correlated subqueries
- Virtual tables (views)

---

### 7. Transactions and ACID
📂 [Transactions & ACID](07-transactions-acid/README.md)

Concepts covered:
- COMMIT / ROLLBACK
- SAVEPOINT
- Reliability principles

---

### 8. Indexes
📂 [Indexes](08-indexes/README.md)

Concepts covered:
- Indexing concept
- Composite index
- Performance impact

---

### 9. Stored Procedures
📂 [Stored Procedures](09-stored-procedures/README.md)

Concepts covered:
- Reusable database logic
- Parameters
- Calling procedures

---

### 10. SQL Thinking Patterns
📂 [Thinking Patterns](10-interview-patterns/README.md)

Concepts covered:
- duplicates
- second highest
- unmatched rows
- running totals

---

## How to Use This Section

This is a concept-first handbook:

Read concept → see example → recall syntax

The focus is understanding the logic of data retrieval rather than memorizing queries.

---

## Outcome

After completing this section you should be able to:

- Understand relational data structure
- Extract datasets correctly
- Combine multiple tables
- Summarize large records
- Prepare data for analysis

This forms the foundation before moving to visualization and machine learning.
