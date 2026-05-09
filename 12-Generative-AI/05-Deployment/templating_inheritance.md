# Template Inheritance in Flask

## 🚀 Introduction

Template inheritance in Flask allows multiple webpages to share a common layout.

👉 Instead of repeating:

* Navbar
* Footer
* CSS links

we create one **base template** and reuse it.

---

## 🧠 Simple Intuition

Think of it like:

> One master template controls the common structure of all webpages.

---

## 📌 Why Template Inheritance is Useful

* Avoids repeated code
* Makes project cleaner
* Easier to maintain large applications

---

## 📂 Basic Structure

```text
templates/
│
├── base.html
├── home.html
└── about.html
```

---

## ⚙️ Base Template

### `templates/base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>

    <h1>My Website</h1>

    {% block content %}
    {% endblock %}

</body>
</html>
```

---

## ⚙️ Child Template

### `templates/home.html`

```html
{% extends "base.html" %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Flask.</p>

{% endblock %}
```

---

## ⚙️ Flask Backend

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📌 Important Jinja2 Tags

| Tag             | Purpose                 |
| --------------- | ----------------------- |
| `{% extends %}` | Inherit template        |
| `{% block %}`   | Replace content section |

---

## 🔄 Flow

```text
Base Template → Child Template → Final Webpage
```

---

## 📊 Benefits

| Feature     | Benefit                |
| ----------- | ---------------------- |
| Reusability | Less repeated code     |
| Consistency | Same layout everywhere |
| Scalability | Better for large apps  |

---

## ⚠️ Important Notes

* Base template contains common structure
* Child templates override blocks
* Uses Jinja2 templating engine

---

## 🎯 Interview Key Points

* Template inheritance avoids duplicate HTML
* `extends` is used for inheritance
* `block` defines replaceable sections
* Useful in scalable Flask apps

---

## 🧠 One-Line Summary

> Template inheritance allows Flask applications to reuse common webpage layouts across multiple pages.

---

## 🔚 Final Thought

Template inheritance makes Flask projects cleaner, scalable, and easier to manage by reducing repeated HTML code.
