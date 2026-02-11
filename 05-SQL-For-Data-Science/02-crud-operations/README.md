# CRUD Operations (Create, Read, Update, Delete)

CRUD operations represent the fundamental actions performed on data inside a database.

Every application — and every ML pipeline — continuously performs these operations.

---

## C → CREATE (Insert Data)

Adding new records to a table.

```sql
INSERT INTO students (id, name, age, city)
VALUES (1, 'Lakshay', 23, 'Delhi');
```

Insert multiple rows:

```sql
INSERT INTO students (id, name, age, city)
VALUES
(2, 'Amit', 22, 'Mumbai'),
(3, 'Neha', 24, 'Pune');
```

---

## R → READ (Retrieve Data)

Reading data using `SELECT`.

Select all columns:

```sql
SELECT * FROM students;
```

Select specific columns:

```sqll
SELECT name, age FROM students;
```

---

## W → WRITE / UPDATE (Modify Data)

Changing existing records.

```sql
UPDATE students
SET city = 'Bangalore'
WHERE id = 1;
```

Important:
Always use `WHERE`, otherwise entire table updates.

---

## D → DELETE (Remove Data)

Remove specific record:

```sql
DELETE FROM students
WHERE id = 2;
```

Remove all rows:

```sql
DELETE FROM students;
```

---

## TRUNCATE vs DELETE

```sql
TRUNCATE TABLE students;
```

| DELETE              | TRUNCATE                          |
|---------------------|-----------------------------------|
| removes row-by-row  | removes entire table data instantly|
| can rollback        | cannot rollback                   |
| slower              | faster                            |

---

## ALTER Table (Modify Structure)

Add column:

```sql
ALTER TABLE students
ADD email VARCHAR(100);
```

Remove column:

```sql
ALTER TABLE students
DROP COLUMN email;
```

Modify column:

```sql
ALTER TABLE students
MODIFY age INT NOT NULL;
```

---

## Why CRUD Matters in ML

Before analysis:

- data is inserted from applications
- corrected when wrong
- deleted when invalid

Your ML dataset is the result of thousands of CRUD operations.

Understanding this explains why real-world data is messy.