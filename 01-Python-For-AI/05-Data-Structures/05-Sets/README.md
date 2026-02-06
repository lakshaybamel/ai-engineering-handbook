# Sets in Python

A set is an unordered collection of unique elements.

Unlike lists or tuples:
- elements do not have index
- duplicate values are automatically removed

Sets are commonly used for filtering and uniqueness operations in data processing.

---

## Unordered & Unique Elements

```python
nums = {1, 2, 2, 3, 4, 4}
print(nums)
```

Output:<br>
{1, 2, 3, 4}

Duplicates are removed automatically.

---

## Creating Sets

```python
names = {"Lakshay", "Rahul", "Amit"}
```

---

## Empty Set vs Dictionary

```python
a = {}
print(type(a))   # dict

b = set()
print(type(b))   # set
```

Empty `{}` creates dictionary, not set.

---

## Mutability Rules

Sets are mutable — elements can be added or removed.

But elements inside set must be immutable (no lists).

```python
s = {1, 2, 3}
s.add(4)
```

Invalid:

```python
s.add([5, 6])   # error
```

---

## Key Understanding

Set = fast membership checking + uniqueness guarantee

---

# Set Operations

Sets allow adding and removing elements dynamically.

---

## add()

Adds an element to the set.

```python
s = {1, 2, 3}
s.add(4)
print(s)
```

---

## remove()

Removes element — error if not present.

```python
s.remove(2)
```

---

## discard()

Removes element — no error if not present.

```python
s.discard(10)
```

---

## pop()

Removes a random element (because unordered).

```python
s.pop()
```

---

## clear()

Removes all elements.

```python
s.clear()
```

---

## Length of Set

```python
print(len(s))
```

---

## Key Understanding

remove → strict deletion<br>
discard → safe deletion<br>
pop → unpredictable removal<br>

---

# Mathematical Set Operations

Sets support mathematical operations similar to set theory.

---

## Union (All elements)

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

---

## Intersection (Common elements)

```python
print(a & b)
```

---

### Difference (Elements in A not in B)

```python
print(a - b)
```

---

## Symmetric Difference (Non-common elements)

```python
print(a ^ b)
```

---

### Demonstration File

* [set_operations_demo.py](set_operations_demo.py)

# Looping & Membership

Since sets are unordered, elements are accessed using iteration.

---

## Iterating Through Set

```python
s = {10, 20, 30}

for value in s:
    print(value)
```

---

## Membership Test

```python
print(20 in s)
print(50 in s)
```

Fast lookup — main advantage of sets.

---

### Demonstration File

* [set_loop_demo.py](set_loop_demo.py)

---

# Practice Programs

* [unique_elements.py](unique_elements.py)
* [common_elements.py](common_elements.py)