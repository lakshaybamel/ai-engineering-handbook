# Templates and Static Files in Flask

## 🚀 Introduction

Flask uses:

* **Templates** → for dynamic HTML pages
* **Static files** → for CSS, JavaScript, images

👉 Together, they help build complete web applications.

---

## 🧠 Simple Intuition

Think of it like:

| Component    | Purpose                   |
| ------------ | ------------------------- |
| Template     | Structure of webpage      |
| Static files | Styling and functionality |

---

## 📂 Default Flask Structure

```text
project/
│
├── app.py
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    ├── script.js
    └── images/
```

---

## 📌 Templates Folder

* Stores HTML files
* Flask automatically searches here

---

## ⚙️ Example Template

### `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>

    <h1>Hello Flask</h1>

</body>
</html>
```

---

## ⚙️ Rendering Template in Flask

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📌 Static Folder

Stores:

* CSS files
* JavaScript files
* Images

---

## ⚙️ Example CSS File

### `static/style.css`

```css
body {
    background-color: lightblue;
}
```

---

## ⚙️ Linking Static Files

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

## 🔄 Flow

```text
Browser → Flask → HTML Template → Static Files
```

---

## 📊 Why Templates & Static Files are Important

| Feature   | Benefit       |
| --------- | ------------- |
| Templates | Dynamic pages |
| CSS       | Styling       |
| JS        | Interactivity |
| Images    | Better UI     |

---

## ⚠️ Important Notes

* Templates folder name must be `templates`
* Static folder name must be `static`
* Use `url_for()` for static files

---

## 🎯 Interview Key Points

* Flask uses templates for HTML rendering
* Static files store CSS/JS/images
* `render_template()` renders HTML
* `url_for()` links static files

---

## 🧠 One-Line Summary

> Templates and static files help Flask create dynamic and visually styled web applications.

---

## 🔚 Final Thought

Templates and static files are essential for converting Flask applications from simple APIs into complete user-friendly web applications.
