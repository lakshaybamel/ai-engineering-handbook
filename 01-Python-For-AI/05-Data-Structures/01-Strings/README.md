# Strings in Python

A string is a sequence of characters used to store text data.

Examples of text data:
- names
- sentences
- messages
- user input
- dataset labels

In AI and NLP, text processing is one of the most important tasks — and strings are the base of it.

---

## Creating Strings

Python allows multiple ways to create strings.

### Single Quotes

```python
name = 'Lakshay'
```

### Double Quotes

```python
message = "Learning AI"
```

### Triple Quotes (Multi-line)

```python
paragraph = """My name is Lakshay Bamel
I am learning Python for AI"""
```

All three create string objects.

---

## String Immutability

Strings cannot be changed after creation.

```python
name = "Lakshay"
name[0] = "R"   # Error
```

This causes an error because strings are immutable.

Instead we create a new string:

```python
name = "Lakshay"
new_name = "R" + name[1:]
print(new_name)
```

---

## Indexing

Each character in a string has a position number.

Example:

```
L  a  k  s  h  a  y
0  1  2  3  4  5  6
```

Access characters using index:

```python
name = "Lakshay"

print(name[0])   # L
print(name[3])   # s
```

---

## Negative Indexing

Python also supports reverse indexing.

```
L  a  k  s  h  a  y
-7 -6 -5 -4 -3 -2 -1
```

```python
print(name[-1])   # y
print(name[-3])   # h
```

---

## Key Understanding

Strings behave like ordered collections of characters.
But unlike lists, they cannot be modified — only replaced.

---

# String Operations

Strings support several useful operations for combining and analyzing text.

---

## Concatenation

Joining two or more strings using `+`

```python
first = "Lakshay"
last = "Bamel"

full_name = first + " " + last
print(full_name)
```

---

## Repetition

Repeat a string multiple times using `*`

```python
print("AI " * 3)
```

Output:<br>
AI AI AI

---

## Membership Operator

Check whether a character or substring exists inside a string using `in`

```python
text = "Learning AI"

print("AI" in text)
print("Python" in text)
Returns True or False
```

---

## Length of String

Use `len()` to count characters.

```python
name = "Lakshay"
print(len(name))
```

---

## Key Understanding

Strings allow combining, checking, and measuring text data — <br>
basic operations required before advanced text processing.

---

# String Slicing

Slicing extracts a portion of a string.

General syntax:

```python
string[start : end : step]
```

* start → starting index (included)
* end → ending index (excluded)
* step → jump between characters

---

## Positive Indexing

```python
text = "LakshayBamel"

print(text[0:7])   # Lakshay
print(text[7:12])  # Bamel
```

---

### Negative Indexing

```python
print(text[-5:])   # Bamel
print(text[:-5])   # Lakshay
```

---

## Step Slicing

```python
print(text[0:7:2])  # Lksa
print(text[::-1])   # reverse string
```

---

## Key Understanding

Slicing does not modify the original string —
it creates a new substring.

---

### Practice Program
See implementation:

* [string_slicing_demo.py](./string_slicing_demo.py)

---

# String Methods

Python provides built-in methods to manipulate and analyze text efficiently.

---

## lower() and upper()

Convert string to lowercase or uppercase.

```python
text = "Lakshay Bamel"
print(text.lower())
print(text.upper())
```

---

## strip()

Removes spaces from beginning and end.

```python
text = "   hello   "
print(text.strip())
```

---

## replace()

Replaces part of string.
```python
text = "I like Java"
print(text.replace("Java", "Python"))
```

---

## find()

Returns index of first occurrence.

```python
text = "machine learning"
print(text.find("learn"))
```

Returns -1 if not found.

---

## count()

Counts occurrences of substring.

```python
text = "banana"
print(text.count("a"))
```

---

## split()

Splits string into list.

```python
text = "AI is powerful"
words = text.split()
print(words)
```

---

### join()

Joins list into string.

```python
words = ["AI", "is", "powerful"]
sentence = " ".join(words)
print(sentence)
```

---

## Key Understanding

Strings are immutable — methods return new strings instead of modifying original.

---

### Demonstration File
- [string_methods_demo.py](string_methods_demo.py)

---

# String Formatting

String formatting allows inserting values into a string in a readable way.

Used heavily in:
- logging
- debugging
- AI prompts
- displaying results

---

## f-Strings (Recommended)

Introduced in Python 3.6 — cleanest method.

```python
name = "Lakshay"
age = 23

print(f"My name is {name} and I am {age} years old")
```
Expressions also allowed:

```python
a = 5
b = 3
print(f"Sum = {a + b}")
```

---

## format() Method

Older but still useful.

```python
name = "Lakshay"
age = 23

print("My name is {} and I am {} years old".format(name, age))
```

Indexed formatting:

```python
print("{1} is learning {0}".format("Python", "Lakshay"))
```

---

## Formatted Output (Numbers)

Control decimal places:

```python
pi = 3.14159
print(f"{pi:.2f}")
```

Padding:

```python
num = 5
print(f"{num:03}")
```

---

## Key Understanding
f-strings are fastest and most readable.<br>
Always prefer them in modern Python code.

---

### Demonstration File
- [string_formatting_demo.py](string_formatting_demo.py)

---

# Practice Programs

- [palindrome_check.py](palindrome_check.py)
- [vowel_count_string.py](vowel_count_string.py)
- [reverse_string.py](reverse_string.py)
