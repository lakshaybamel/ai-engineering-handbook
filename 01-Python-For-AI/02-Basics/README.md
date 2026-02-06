# Python Basics

This section covers the fundamental building blocks of Python programming.  
Everything in Machine Learning later (arrays, tensors, models) ultimately depends on these core ideas.

---

## 1. Program Execution

A Python program runs from top to bottom line by line.

```python
print("Hello Lakshay Bamel")
print("Learning AI step by step")
```
Each line is an instruction executed sequentially.

---

## 2. Variables

A variable is a container that stores data in memory.

```python
name = "Lakshay"
age = 23
learning_ai = True
```

Python automatically decides the data type based on the assigned value.<br>
This is called dynamic typing.

We can change value anytime:
```python
age = 24
```

---

## 3. Data Types

Every value stored in Python has a type.

| Type | Meaning | Example |
| :--- | :--- | :--- |
| int | Whole numbers | 10 |
| float | Decimal numbers | 10.5 |
| str | Text | "Lakshay" |
| bool | True/False | True |
| NoneType | Empty value | None |

Check type:

```python
print(type(name))
print(type(age))
```

---

## 4. Keywords & Comments

### Keywords
Reserved words that have special meaning in Python.

**Examples:**
```python
if, else, True, False, None, while, for, def, class
```

We cannot use them as variable names.

### Comments
Comments are ignored by Python and used for explanation.

```Python
# This is a comment
age = 23  # storing age
```

---

## 5. Operators

Operators perform operations on values.

### Arithmetic Operators

| Operator | Meaning |
| :--- | :--- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Remainder |
| // | Floor Division |
| ** | Power |

**Example:**

```python
a = 10
b = 3

print(a + b)   # 13
print(a // b)  # 3 (removes decimal)
print(a ** b)  # 1000 (10 to the power 3)
```

### Relational (Comparison) Operators

They compare values and return True or False.

| Operator | Meaning |
| :--- | :--- |
| == | Equal |
| != | Not equal |
| > | Greater |
| < | Smaller |
| >= | Greater equal |
| <= | Smaller equal |

**Example:**

```python
print(10 > 5)    # True
print(10 == 10)  # True
print(7 != 3)    # True
```

### Logical Operators

Used to combine conditions.

#### AND
Both conditions must be True.

```python
age = 20
has_id = True
print(age >= 18 and has_id) # True
```

#### OR
At least one condition must be True.

```Python
print(age >= 18 or has_id) # True
```

#### NOT
Reverses the result (True becomes False, and vice versa).

```Python
print(not(age >= 18)) # False
```

---

## 6. Operator Precedence

Python follows a priority order (similar to BODMAS) to decide which operation to perform first:

1. **()** — Parentheses
2. **\*\*** — Exponentiation (Power)
3. **\*, /, //, %** — Multiplication, Division, Floor Division, Modulus
4. **+, -** — Addition, Subtraction
5. **==, !=, >, <, >=, <=** — Comparison Operators
6. **not** — Logical NOT
7. **and** — Logical AND
8. **or** — Logical OR

**Example:**

```python
print(2 + 3 * 4)   # Result: 14 (Multiplication happens before Addition)
print((2 + 3) * 4) # Result: 20 (Parentheses happen first)
```

---

## 7. Type Conversion & Casting

### Automatic Conversion
```python
print(10 + 2.5)   # int → float
```

### Manual Conversion
```python
age = int("23")
height = float("5.9")
name = str(123)
```

---

## 8. Taking User Input

In Python, the `input()` function allows us to take data from the user. **Note:** Input always returns data as a **string** by default.

```python
name = input("Enter your name: ")
print("Hello", name)
```

### Numeric Input
Since `input()` returns a string, you must use **Type Casting** if you want to perform mathematical operations:

```Python
a = int(input("Enter number: "))
b = int(input("Enter number: "))

print("Sum =", a + b)
```

---

## 9. Small Example – Average of Two Numbers

This example demonstrates taking user input, performing calculation with operator precedence, and printing the result.

```python
# Taking two numbers as input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calculating average
# We use parentheses () to ensure addition happens before division
avg = (a + b) / 2

print("Average =", avg)
```

---

## 10. Key Takeaways

To summarize this module, here are the core concepts every beginner must master:

* **Variables:** Store information in memory so it can be reused.
* **Data Types:** Define the behavior of data (how it interacts with operators).
* **Operators:** Perform mathematical or logical operations on values.
* **Input:** Allows user interaction, making programs dynamic.
* **Type Casting:** Essential for preventing errors when mixing different data types (like String and Int).