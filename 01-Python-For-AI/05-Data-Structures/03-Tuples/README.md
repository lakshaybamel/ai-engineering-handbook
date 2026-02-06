# Tuples in Python

A tuple is an ordered collection of elements similar to a list, but **immutable**.

Immutable means once created, values cannot be changed.

Tuples are used when data should remain constant.

---

## Creating Tuples

Tuples are created using parentheses `()`

```python
numbers = (1, 2, 3, 4)
names = ("Lakshay", "Rahul", "Amit")
```

---

## Single Element Tuple
A comma is required to create a tuple with one element.

```python
t = (5,)
print(type(t))
```

Without comma:

```python
t = (5)
print(type(t))   # int, not tuple
```

---

## Indexing

Works same as lists.

```python
names = ("Lakshay", "Rahul", "Amit")

print(names[0])
print(names[-1])
```

---

## Immutability

Tuple values cannot be modified.

```python
numbers = (1, 2, 3)
numbers[0] = 10   # Error
```

This makes tuples:
* faster
* safer
* usable as dictionary keys

---

## Key Understanding
Use list → when data changes<br>
Use tuple → when data should remain fixed

---

# Tuple Operations

Although tuples are immutable, we can still access and extract data from them.

---

## Accessing Elements

```python
data = ("Lakshay", 23, "AI")

print(data[0])
print(data[-1])
```

---

## Slicing

Works same as lists.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[::-1])
```

---

## Tuple Unpacking

Assign tuple values to multiple variables.

```python
person = ("Lakshay", 23, "Engineer")

name, age, role = person

print(name)
print(age)
print(role)
```

---

## Ignoring Values

Use `_` to ignore elements.

```python
person = ("Lakshay", 23, "Engineer")

name, _, role = person
print(name, role)
```

---

## Key Understanding
Tuples are useful when returning multiple values from functions or grouping fixed data.

---

# Tuple Methods

Since tuples are immutable, they have very few methods compared to lists.

---

## count()

Returns number of occurrences of a value.

```python
nums = (1, 2, 2, 3, 2)
print(nums.count(2))
```

---

## index()

Returns index of first occurrence.

```python
nums = (10, 20, 30, 20)
print(nums.index(20))
```

---

### Demonstration File
* [tuple_methods_demo.py](tuple_methods_demo.py)

---

# Tuple Packing & Unpacking

## Packing

When multiple values are grouped into a tuple automatically.

```python
data = 10, 20, 30
print(type(data))
```

Python packs values into a tuple.

---

## Unpacking

Extract values from tuple into variables.

```python
data = (10, 20, 30)
a, b, c = data

print(a, b, c)
```

---

## Multiple Assignment

Swap values easily using tuple unpacking.

```python
a = 5
b = 10

a, b = b, a
print(a, b)
```

---

### Demonstration File
* [tuple_unpacking_demo.py](tuple_unpacking_demo.py)

---

# Practice Programs

* [swap_using_tuple.py](swap_using_tuple.py)
* [min_max_tuple.py](min_max_tuple.py)