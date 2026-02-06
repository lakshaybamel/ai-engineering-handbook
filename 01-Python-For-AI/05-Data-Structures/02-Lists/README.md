# Lists in Python

A list is an ordered collection of elements stored in a single variable.

Unlike normal variables that store one value, lists can store multiple values together.

Lists are one of the most used data structures in Machine Learning because datasets are collections of values.

---

## Creating Lists

Lists are created using square brackets `[]`

```python
numbers = [1, 2, 3, 4, 5]
names = ["Lakshay", "Rahul", "Amit"]
```

---

## Heterogeneous Elements

Lists can store different data types together.

```python
data = ["Lakshay", 23, True, 5.9]
```

Python lists are dynamic — no fixed type required.

---

## Indexing

Each element in a list has a position called an index.

Index starts from 0

```python
names = ["Lakshay", "Rahul", "Amit"]

print(names[0])
print(names[1])
```

---

## Negative Indexing

Access elements from the end.

```python
print(names[-1])
print(names[-2])
```

---

## Mutability

Lists are mutable — values can be changed after creation.

```python
numbers = [1, 2, 3]
numbers[1] = 10

print(numbers)
```

Output:<br>
[1, 10, 3]

---

## Key Understanding

Lists are:

* ordered
* changeable
* allow duplicates

They are the base structure behind arrays and tensors used in AI libraries.

---

# List Operations

Lists allow reading, updating, inserting, and removing elements easily.

---

## Access Elements

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])
print(numbers[-1])
```

---

## Modify Elements

Since lists are mutable, values can be updated.

```python
numbers = [10, 20, 30]
numbers[1] = 99

print(numbers)
```

---

## Adding Elements

### append() → adds at end

```python
numbers = [1, 2, 3]
numbers.append(4)
```

### insert() → adds at specific index

```python
numbers.insert(1, 10)
```

### extend() → adds multiple elements

```python
numbers.extend([5, 6, 7])
```

---

## Deleting Elements

### remove() → deletes by value

```python
numbers.remove(10)
```

### pop() → deletes by index

```python
numbers.pop(2)
numbers.pop()
```

### del → deletes using keyword
```python
del numbers[0]
```

---

## Length of List

```python
print(len(numbers))
```

---

## Key Understanding
append → add one item<br>
insert → add at position<br>
extend → add many items<br>

remove → delete by value<br>
pop → delete by index<br>
del → delete element or entire list<br>

---

# List Slicing

Slicing allows extracting a portion of a list.

Syntax:

```python
list[start : stop : step]
```

* start → starting index (inclusive)
* stop → ending index (exclusive)
* step → jump interval

---

## Basic Slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:<br>
[20, 30, 40]

---

## Negative Indexing

```python
print(numbers[-3:])
```

Output:<br>
[30, 40, 50]

---

## Step Slicing

```python
print(numbers[::2])
```

Output:<br>
[10, 30, 50]

#### Reverse list:

```python
print(numbers[::-1])
```

---

## Copy vs Reference

### Reference (same memory)

```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)
```

Both change because they point to same list.

### Copy (new memory)

```python
a = [1, 2, 3]
b = a[:]
b[0] = 99
print(a)
```

Original list remains unchanged.

---

### Demonstration File
* [list_slicing_demo.py](list_slicing_demo.py)

---

# List Methods

Python provides built-in methods to manipulate list data efficiently.

---

## append()

Adds element at the end.

```python
nums = [1, 2, 3]
nums.append(4)
```

---

## insert()

Adds element at a specific index.

```python
nums.insert(1, 10)
```

---

## extend()

Adds multiple elements from another iterable.

```python
nums.extend([5, 6])
```

---

## remove()

Deletes first occurrence of a value.

```python
nums.remove(10)
```

---

## pop()

Removes element by index and returns it.

```python
nums.pop()
nums.pop(1)
```

---

## sort()

Sorts list in ascending order.

```python
nums.sort()
```

Descending order:

```python
nums.sort(reverse=True)
```

---

## reverse()

Reverses list order.

```python
nums.reverse()
```

---

## count()

Counts occurrences of value.

```python
nums.count(2)
```

---

## index()

Returns index of first occurrence.

```python
nums.index(3)
```

---

### Demonstration File
* [list_methods_demo.py](list_methods_demo.py)

---

# Looping Through Lists

Lists are commonly processed element by element.

---

## for Loop Traversal

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

---

## Using index with range()

```python
for i in range(len(numbers)):
    print(i, numbers[i])
```

---

## enumerate()

Provides index and value together.

```python
for index, value in enumerate(numbers):
    print(index, value)
```

Cleaner than range(len(list))

---

## Nested Loops (2D Lists)

```python
matrix = [
    [1, 2],
    [3, 4]
]

for row in matrix:
    for value in row:
        print(value)
```

Used in tables, grids, datasets.

---

### Demonstration File
* [list_loop_demo.py](list_loop_demo.py)

---

# List Comprehension

List comprehension provides a concise way to create lists using a single line of code.

It replaces loops used for list creation.

---

## Basic Comprehension

```python
numbers = [1, 2, 3, 4]

squares = [x*x for x in numbers]
print(squares)
```

Equivalent to:

```python
squares = []
for x in numbers:
    squares.append(x*x)
```

---

## Conditional Comprehension

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = [x for x in numbers if x % 2 == 0]
print(evens)
```

---

## Transformation

Modify values during creation.

```python
nums = [1, 2, 3]
labels = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(labels)
```

---

## Why Important

Used heavily in:

* data preprocessing
* filtering datasets
* feature extraction

---

### Demonstration File
* [list_comprehension_demo.py](list_comprehension_demo.py)

---

# Practice Programs

- [max_in_list.py](max_in_list.py)
- [remove_duplicates.py](remove_duplicates.py)
- [sum_list.py](sum_list.py)
