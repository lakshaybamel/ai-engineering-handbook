# Jinja2 Templating in Flask

## 🚀 Introduction

Flask uses **Jinja2** as its templating engine.

👉 Jinja2 allows dynamic content inside HTML pages.

This means:

* Data from Python can be displayed in HTML
* Webpages become dynamic instead of static

---

## 🧠 Simple Intuition

Think of Jinja2 like:

> A bridge that sends Python data into HTML pages.

---

## 📌 Basic Flow

```text
Python Data → Jinja2 Template → Dynamic HTML Page
```

---

## ⚙️ Basic Flask Example

### `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "Lakshay"

    return render_template("index.html", username=name)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## ⚙️ HTML Template Example

### `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Jinja2 Example</title>
</head>
<body>

    <h1>Hello {{ username }}</h1>

</body>
</html>
```

---

## 📌 Variable Syntax

```html
{{ variable_name }}
```

👉 Used to display dynamic values.

---

## 📌 Conditional Statements

```html
{% if age >= 18 %}
    <h1>Adult</h1>
{% endif %}
```

---

## 📌 Loops in Jinja2

```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

---

## ⚙️ Example with Loop

### Flask Code

```python
@app.route("/")
def home():

    subjects = ["Python", "Flask", "AI"]

    return render_template(
        "index.html",
        subjects=subjects
    )
```

---

### HTML Template

```html
<ul>
{% for subject in subjects %}
    <li>{{ subject }}</li>
{% endfor %}
</ul>
```

---

## 📊 Why Jinja2 is Important

| Feature            | Benefit             |
| ------------------ | ------------------- |
| Dynamic content    | Flexible webpages   |
| Loops & conditions | Better UI logic     |
| Python integration | Easy data rendering |

---

## ⚠️ Important Notes

* Jinja2 syntax uses:

  * `{{ }}` for variables
  * `{% %}` for logic
* Works inside Flask templates

---

## 🎯 Interview Key Points

* Flask uses Jinja2 templating engine
* Used for dynamic HTML rendering
* Supports variables, loops, and conditions
* Works with `render_template()`

---

## 🧠 One-Line Summary

> Jinja2 allows Flask applications to create dynamic HTML pages using Python data.

---

## 🔚 Final Thought

Jinja2 makes Flask applications more interactive and dynamic by connecting backend Python logic with frontend HTML pages.
