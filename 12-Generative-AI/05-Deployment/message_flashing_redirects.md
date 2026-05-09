# Message Flashing and Redirects in Flask

## 🚀 Introduction

Flask provides:

* **Message flashing** → display temporary messages
* **Redirects** → move users to another route/page

👉 These features improve user experience in web applications.

---

## 🧠 Simple Intuition

Think of it like:

> User performs an action → Flask shows a message → redirects to another page.

---

## 📌 Common Examples

* Login success message
* Form submission confirmation
* Error notifications
* Redirect after authentication

---

## 🔄 Basic Flow

```text
User Action → Flash Message → Redirect → Display Message
```

---

## ⚙️ Flash Message Example

### Flask Backend

```python
from flask import Flask, flash, redirect, url_for, render_template

app = Flask(__name__)

# secret key required for flashing
app.secret_key = "secret_key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():

    flash("Login successful!")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
```

---

## ⚙️ Display Flash Messages in HTML

### `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flash Messages</title>
</head>
<body>

{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
            <p>{{ message }}</p>
        {% endfor %}
    {% endif %}
{% endwith %}

</body>
</html>
```

---

## 📌 Redirect Example

```python
from flask import redirect, url_for

@app.route("/admin")
def admin():

    return redirect(url_for("home"))
```

---

## 📌 Important Functions

| Function   | Purpose                    |
| ---------- | -------------------------- |
| flash()    | Stores temporary message   |
| redirect() | Redirects to another route |
| url_for()  | Generates route URL        |

---

## 📊 Common Uses

* Authentication systems
* Form handling
* Error handling
* Notifications in AI apps

---

## ⚠️ Important Notes

* Flashing requires `secret_key`
* Flash messages are temporary
* Redirects improve navigation flow

---

## 🎯 Interview Key Points

* Flask supports temporary flash messages
* `redirect()` moves user to another route
* `url_for()` generates dynamic URLs
* Commonly used in login systems

---

## 🧠 One-Line Summary

> Flask uses flashing and redirects to improve user interaction and navigation in web applications.

---

## 🔚 Final Thought

Message flashing and redirects help create smoother and more user-friendly Flask applications by providing feedback and proper navigation flow.
