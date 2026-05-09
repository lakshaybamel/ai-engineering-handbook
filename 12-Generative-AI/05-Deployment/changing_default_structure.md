# Changing Default Structure in Flask

## 🚀 Introduction

Flask uses default folders:

* `templates/`
* `static/`

But sometimes developers want a **custom project structure** for better organization.

👉 Flask allows changing these default paths.

---

## 🧠 Simple Intuition

Think of it like:

> Instead of using Flask’s default folders, you tell Flask where your files are located.

---

## 📂 Default Structure

```text
project/
│
├── app.py
├── templates/
└── static/
```

---

## 📂 Custom Structure Example

```text
project/
│
├── app.py
│
├── frontend/
│   ├── html/
│   ├── css/
│   └── images/
```

---

## ⚙️ Changing Template Folder

```python
from flask import Flask

app = Flask(
    __name__,
    template_folder="frontend/html"
)
```

---

## ⚙️ Changing Static Folder

```python
from flask import Flask

app = Flask(
    __name__,
    static_folder="frontend/css"
)
```

---

## ⚙️ Changing Both Together

```python
from flask import Flask

app = Flask(
    __name__,
    template_folder="frontend/html",
    static_folder="frontend/static"
)
```

---

## 📌 Using Static Files

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

## 🔄 Flow

```text
Custom Folder → Flask Configuration → Application
```

---

## 📊 Why Change Structure?

| Reason              | Benefit             |
| ------------------- | ------------------- |
| Better organization | Cleaner projects    |
| Large applications  | Easier management   |
| Team projects       | Structured workflow |

---

## ⚠️ Important Notes

* Flask must know correct paths
* Wrong path → templates not found
* `url_for()` still works normally

---

## 🎯 Interview Key Points

* Flask allows custom folder structure
* `template_folder` changes template path
* `static_folder` changes static path
* Useful in large-scale applications

---

## 🧠 One-Line Summary

> Flask allows developers to customize template and static folder locations for better project organization.

---

## 🔚 Final Thought

Changing Flask’s default structure helps build **cleaner and more scalable applications**, especially in larger AI and web projects.
