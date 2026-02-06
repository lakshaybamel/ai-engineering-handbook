# Dictionaries in Python

A dictionary is a collection of data stored as **key–value pairs**.

Instead of accessing elements using index (like lists), dictionaries use keys.

Dictionaries are heavily used in real-world programming:
- JSON data
- API responses
- database records
- machine learning features

---

## Key–Value Pairs

Each item has:

key → unique identifier  
value → actual data

Example:

```python
student = {
    "name": "Lakshay",
    "age": 23,
    "course": "AI"
}
```

---

## Creating a Dictionary

Using curly braces `{}`

```python
person = {"name": "Lakshay", "city": "Delhi"}
```

### Empty dictionary:

```python
data = {}
```

---

## Accessing Values

Using keys:

```python
print(person["name"])
print(person["city"])
```

---

## Mutable Nature

Dictionaries are mutable — values can be changed.

```python
person["city"] = "Jaipur"
print(person)
```

---

## Key Rules

* Keys must be unique
* Keys must be immutable (string, number, tuple)
* Values can be any type

---

## Key Understanding
Dictionary = real-world object representation

**Example:**<br>
Student → properties → values

---

# Dictionary Operations

Dictionaries allow adding, updating, and removing key–value pairs easily.

---

## Add / Update Values

Add new key:

```python
student = {"name": "Lakshay", "age": 23}
student["city"] = "Delhi"
```

Update existing key:

```python
student["age"] = 24
```

---

## Delete Values

Using del

```python
del student["city"]
```

---

## Checking Keys

Use `in` operator:

```python
print("name" in student)
print("marks" in student)
```

---

## Length of Dictionary

```python
print(len(student))
```

---

## Key Understanding

Dictionaries grow dynamically and are ideal for structured data storage.

---

# Dictionary Methods

Python provides built-in methods to work efficiently with dictionaries.

---

## keys()

Returns all keys.

```python
student = {"name": "Lakshay", "age": 23}
print(student.keys())
```

---

## values()

Returns all values.

```python
print(student.values())
```

---

## items()

Returns key-value pairs.

```python
print(student.items())
```

---

## get()

Safely access value without error.

```python
print(student.get("name"))
print(student.get("marks"))  # None instead of error
```

---

## update()

Merge another dictionary.

```python
student.update({"city": "Delhi"})
```

---

## pop()

Remove specific key.

```python
student.pop("age")
```

---

## popitem()

Removes last inserted pair.

```python
student.popitem()
```

---

## clear()

Removes all elements.

```python
student.clear()
```

---

## Demonstration File

* [dict_methods_demo.py](dict_methods_demo.py)

---

# Looping Through Dictionary

Dictionaries are commonly processed element by element.

---

## Iterate Keys

```python
student = {"name": "Lakshay", "age": 23, "city": "Delhi"}

for key in student:
    print(key)
```

---

## Iterate Values

```python
for value in student.values():
    print(value)
```

---

## Iterate Key–Value Pairs

```python
for key, value in student.items():
    print(key, ":", value)
```

---

### Demonstration File
* [dict_loop_demo.py](dict_loop_demo.py)

---

# Nested Dictionary

A dictionary can contain another dictionary as its value.  
This structure is commonly used in JSON data and APIs.

---

## Dictionary Inside Dictionary

```python
students = {
    "s1": {"name": "Lakshay", "age": 23},
    "s2": {"name": "Rahul", "age": 22}
}
```

---

## Accessing Nested Data

```python
print(students["s1"]["name"])
print(students["s2"]["age"])
```

Useful for structured datasets.

---

### Demonstration File
* [nested_dict_demo.py](nested_dict_demo.py)

---

# Practice Programs

* [student_record.py](student_record.py)
* [word_frequency.py](word_frequency.py)


