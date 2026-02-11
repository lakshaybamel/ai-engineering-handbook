# Database Fundamentals

Before learning SQL syntax, we must understand what a database actually represents.

A database is a structured way to store real-world information so it can be retrieved, updated, and analyzed efficiently.

In AI/ML workflow:
Raw Data → Stored in Database → Queried using SQL → Processed in Pandas → Used in ML

---

## What is Data Collection?

Data Science always starts with data, not models.

Sources of data:
- Applications (user activity, orders, clicks)
- Sensors / IoT devices
- APIs
- Web scraping
- Logs
- Surveys

Most real-world data is stored inside databases.

---

## What is a Database?

A database is an organized collection of related data.

Example:
A shopping website needs to store:

- users
- products
- orders
- payments

Instead of random files, databases maintain relationships between them.

---

## What is a Table?

A table represents one entity.

Example: `students`

| id | name | age | city |
|---|---|---|---|
| 1 | Lakshay | 23 | Delhi |
| 2 | Amit | 22 | Mumbai |

Rows → records  
Columns → attributes (features in ML terms)

A table in database is similar to a DataFrame in Pandas.

---

## SQL vs NoSQL

### SQL (Relational Databases)
Structured data stored in tables with relationships.

Examples:
MySQL, PostgreSQL, SQLite

Characteristics:
- Fixed schema
- Strong consistency
- Relationships via keys

### NoSQL
Flexible structure (JSON-like documents)

Examples:
MongoDB, Cassandra

Characteristics:
- Flexible schema
- Faster scaling
- Used for unstructured data

In ML pipelines:
SQL → structured transactional data  
NoSQL → logs, text, large scale events

---

## What is SQL?

SQL = Structured Query Language

It is used to:
- create tables
- insert data
- retrieve data
- update data
- delete data

SQL does NOT store data.  
SQL communicates with the database.

---

## Creating a Database

```sql
CREATE DATABASE company;
USE company;
```

Creating a Table

```sql
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);
```

---

## Constraints

Constraints enforce rules on data.

They ensure data quality before ML processing.

### Primary Key

Uniquely identifies each record.

```sql
id INT PRIMARY KEY
```

No duplicate and no NULL values allowed.

### Foreign Key

Creates relationship between tables.

```sql
dept_id INT,
FOREIGN KEY (dept_id) REFERENCES departments(id)
```

---

## Why Databases Matter in AI

Machine Learning models depend on clean structured data.

Databases provide:

- consistency
- integrity
- relationships
- reliability

Without proper database structure → messy Pandas → poor models.

---

## Mental Model

Database → storage layer<br>
SQL → access language<br>
Pandas → processing layer<br>
ML → prediction layer<br>