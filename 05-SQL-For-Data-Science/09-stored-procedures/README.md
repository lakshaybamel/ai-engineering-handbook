# Stored Procedures

A stored procedure is a saved SQL program inside the database.

Instead of writing the same query repeatedly, we store logic once and execute it whenever needed.

It is similar to a function in programming.

---

## Why Stored Procedures?

- Reuse logic
- Reduce repeated queries
- Improve performance
- Centralize business rules

---

## Creating a Stored Procedure

```sql
DELIMITER //

CREATE PROCEDURE get_students()
BEGIN
    SELECT * FROM students;
END //

DELIMITER ;
```

---

## Calling a Procedure

```sql
CALL get_students();
```

---

## Procedure with Parameters

```sql
DELIMITER //

CREATE PROCEDURE get_city_students(IN city_name VARCHAR(50))
BEGIN
    SELECT * FROM students
    WHERE city = city_name;
END //

DELIMITER ;
```

Call:

```sql
CALL get_city_students('Delhi');
```

---

## Dropping a Procedure

```sql
DROP PROCEDURE get_students;
```

---

## Why This Matters in AI

In real systems, data is prepared inside databases.

Stored procedures can:

- clean data

- aggregate data

- generate datasets automatically

Before loading into Pandas or ML pipeline.