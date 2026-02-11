# Transactions and ACID Properties

Databases are not just storage — they guarantee correctness.

When multiple operations happen together, they must behave as a single unit.
This is called a Transaction.

Example:
Bank transfer must either fully complete or not happen at all.

---

## What is a Transaction?

A transaction is a sequence of operations treated as one logical step.

Steps:
1. Begin transaction
2. Perform operations
3. Commit OR Rollback

---

## COMMIT

Permanently saves changes.

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;

COMMIT;
```

---

## ROLLBACK

Undo changes if something fails.

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;

ROLLBACK;
```

---

## SAVEPOINT

Allows partial rollback.

```sql
START TRANSACTION;

INSERT INTO orders VALUES (101, 1, 500);
SAVEPOINT after_order;

INSERT INTO payments VALUES (101, 'FAILED');

ROLLBACK TO after_order;
COMMIT;
```

---

## ACID Properties

ACID ensures database reliability.

### Atomicity
All operations succeed or none happen.

(No partial update)

### Consistency
Database remains valid before and after transaction.

(No invalid state)

### Isolation
Transactions do not interfere with each other.

(Multiple users safe)

### Durability
Committed data is permanently stored.

(Even after crash)

---

## Why This Matters in AI

Training data must be reliable.

Incorrect transactions create:

- duplicate records
- missing values
- inconsistent datasets

ACID properties ensure trustworthy datasets.