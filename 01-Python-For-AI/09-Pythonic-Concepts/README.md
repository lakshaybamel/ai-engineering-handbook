# Pythonic Code

Pythonic code means writing code in a way that follows Python’s philosophy:
simple, readable, and expressive.

Python is designed to be read by humans first and machines second.

---

## Readable vs Complex Code

### Non-Pythonic

```python
numbers = [1,2,3,4,5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

### Pythonic

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

Both work — but second is clearer.

---

## Why Pythonic Style Matters

* Easier to understand
* Faster debugging
* Standard industry practice
* Preferred in interviews
* Required in collaborative projects

Readable code reduces future errors.

---

## PEP8 Mindset

PEP8 is Python’s official style guideline.

Key ideas:

* meaningful variable names
* proper indentation
* spacing around operators
* avoid overly complex logic

Pythonic programming focuses on clarity over cleverness.

---

## Key Understanding

Good Python developers don’t just write working code —
they write understandable code.

---

# Multiple Assignment & Swapping

Python allows assigning multiple variables in a single statement.

---

## Unpacking Assignment

```python
a, b, c = 1, 2, 3
print(a, b, c)
```

---

## Swapping Variables

No temporary variable required.

```python
x = 5
y = 10

x, y = y, x
print(x, y)
```

---

## Chaining Assignments

Assign same value to multiple variables.

```python
a = b = c = 0
print(a, b, c)
```

---

### Demonstration File

* [multiple_assignment_demo.py](multiple_assignment_demo.py)

---

# enumerate() & zip()

These functions make looping cleaner and more readable.

---

## enumerate()

Provides index and value together.

```python
names = ["Lakshay", "Rahul", "Amit"]

for index, name in enumerate(names):
    print(index, name)
```
Better than using `range(len(list))`.

---

## zip()

Combines multiple sequences together.

```python
names = ["Lakshay", "Rahul"]
marks = [90, 85]

for name, mark in zip(names, marks):
    print(name, mark)
```

---

## Parallel Iteration

Allows looping multiple lists simultaneously.

---

### Demonstration File

* [enumerate_zip_demo.py](enumerate_zip_demo.py)

---

# Useful Built-in Functions

Python provides powerful built-in functions that reduce the need for manual loops.

---

## any()

Returns True if at least one element is True.

```python
values = [False, False, True]
print(any(values))
```

---

## all()

Returns True only if all elements are True.

```python
values = [True, True, True]
print(all(values))
```

---

## min() and max()

```python
numbers = [5, 2, 9, 1]
print(min(numbers))
print(max(numbers))
```

---

## sum()

```python
numbers = [1, 2, 3, 4]
print(sum(numbers))
```

---

### Demonstration File

* [builtins_demo.py](builtins_demo.py)

---

# Ternary Operator

Python allows writing simple conditions in a single line.

Syntax:

```python
value_if_true if condition else value_if_false
```

---

## Example

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

More readable for small conditions than full if-else blocks.

---

### Demonstration File

* [ternary_demo.py](ternary_demo.py)

---

# Advanced Comprehensions

Comprehensions allow creating collections in a concise and readable way.

---

## Nested List Comprehension

```python
matrix = [[1, 2, 3], [4, 5, 6]]

flatten = [num for row in matrix for num in row]
print(flatten)
```

---

## Dictionary Comprehension

```python
numbers = [1, 2, 3, 4]

squares = {x: x*x for x in numbers}
print(squares)
```

---

## Conditional Dictionary Comprehension

```python
even_squares = {x: x*x for x in numbers if x % 2 == 0}
print(even_squares)
```

---

### Demonstration File

* [advanced_comprehension_demo.py](advanced_comprehension_demo.py)

---

# Practice Programs

- [flatten_list.py](flatten_list.py)
- [word_length_map.py](word_length_map.py)
