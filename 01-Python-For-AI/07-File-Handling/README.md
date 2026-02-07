# File Handling in Python

File handling allows programs to store data permanently instead of losing it when the program stops.

Normally variables store data in RAM (temporary memory).  
Files store data in disk (permanent storage).

---

## Why File Handling is Important

Used in real applications:

- saving user data
- storing logs
- datasets for machine learning
- configuration files
- exporting results

Without files, every program would forget its data after execution.

---

## Types of Files

### Text Files

Human-readable format.

Examples:
- `.txt`
- `.csv`
- `.json`

Data stored as characters.

---

### Binary Files

Not human-readable.

Examples:
- images
- audio
- videos
- models

Stored as bytes.

---

## File Path Basics

Path tells Python where the file is located.

### Relative Path
File in current project folder.

```python
open("data.txt")
```

### Absolute Path
Full location of file.

```python
open("C:/Users/Lakshay/Documents/data.txt")
```

---

### Key Understanding

Programs use files to communicate with the outside world — especially important before working with datasets in AI.

---

# Opening & Closing Files

Python uses `open()` to work with files.

Syntax:

```python
file = open("filename", "mode")
```

After work, file should be closed:

```python
file.close()
```

---

## File Modes

| **Mode** | **Meaning** |
| :--- | :--- |
| r | Read (default) |
| w | Write (overwrites file) |
| a | Append |
| x | Create new file |

---

### Read Mode

```python
f = open("data.txt", "r")
```

Error if file does not exist.

---

### Write Mode

```python
f = open("data.txt", "w")
```

Creates file if missing, deletes old content.

---

### Append Mode

```python
f = open("data.txt", "a")
```

Adds content at end.

---

### Exclusive Create Mode

```python
f = open("data.txt", "x")
```

Fails if file already exists.

---

### Demonstration File

* [file_open_modes_demo.py](file_open_modes_demo.py)

---

# Reading Files

Python provides multiple ways to read file content.

---

## read()

Reads entire file as a string.

```python
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()
```

---

## readline()

Reads one line at a time.

```python
f = open("data.txt", "r")
print(f.readline())
f.close()
```

---

### readlines()

Reads all lines into a list.

```python
f = open("data.txt", "r")
lines = f.readlines()
print(lines)
f.close()
```

---

### Demonstration File

* [file_read_demo.py](file_read_demo.py)

---

# Writing Files

Files can be modified using write and append modes.

---

## write()

Overwrites file content.

```python
f = open("data.txt", "w")
f.write("Hello World")
f.close()
```

---

## Append

Adds content to existing file.

```python
f = open("data.txt", "a")
f.write("New line added")
f.close()
```

---

### Demonstration File

* [file_write_demo.py](file_write_demo.py)

---

# with Statement

Using `with` automatically closes the file after use.

Safer than manual `close()` because it prevents memory leaks and file corruption.

---

## Automatic Closing

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

No need to call `f.close()`.

---

### Safe Handling

Even if an error occurs, the file is closed properly.

Best practice in real applications.

---

### Demonstration File

* [with_statement_demo.py](with_statement_demo.py)

---

# Working with JSON

JSON (JavaScript Object Notation) is a structured data format commonly used in APIs and datasets.

Python provides the `json` module to store and retrieve structured data.

---

## dump() — Write JSON

```python
import json

data = {"name": "Lakshay", "age": 23}

with open("data.json", "w") as f:
    json.dump(data, f)
```

---

## load() — Read JSON

```python
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
```

---

## Why Important

Machine learning datasets and API responses are often stored in JSON format.

---

### Demonstration File

* [json_demo.py](json_demo.py)

---

# Practice Programs

- [copy_file.py](copy_file.py)
- [file_word_count.py](file_word_count.py)