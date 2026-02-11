# Indexes

As tables grow large, searching rows becomes slow.

Without index:
Database scans every row (Full Table Scan)

With index:
Database jumps directly to matching rows

An index works like a book index.

---

## Creating an Index

```sql
CREATE INDEX idx_name
ON students(name);
```

Now searching by name becomes faster.

---

## Composite Index

Index on multiple columns.

```sql
CREATE INDEX idx_city_age
ON students(city, age);
```

Useful when queries filter using both columns.

---

## Unique Index

Ensures no duplicate values.

```sql
CREATE UNIQUE INDEX idx_email
ON students(email);
```

---

## Dropping Index

```sql
DROP INDEX idx_name ON students;
```

---

## When Index Helps

Good for:

- WHERE conditions

- JOIN columns

- ORDER BY

---

## When Index Hurts

Indexes consume memory and slow INSERT/UPDATE.

Too many indexes reduce performance.

---

## Why This Matters in AI

Data extraction queries may run on millions of rows.

Indexes allow fast dataset generation before training.