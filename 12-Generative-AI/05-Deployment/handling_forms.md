# Handling Forms in Flask

## 🚀 Introduction

Forms are used in Flask to collect input from users.

👉 Examples:

* Login forms
* Search boxes
* Chatbot input
* AI prompt submission

---

## 🧠 Simple Intuition

Think of forms like:

> A way for users to send data from a webpage to the Flask backend.

---

## 📌 Basic Flow

```text
User Input → HTML Form → Flask Backend → Response
```

---

## ⚙️ HTML Form Example

### `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask Form</title>
</head>
<body>

    <form method="POST">
        <input type="text" name="username" placeholder="Enter name">
        <button type="submit">Submit</button>
    </form>

</body>
</html>
```

---

## ⚙️ Flask Backend Example

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        username = request.form["username"]

        return f"Hello, {username}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📌 Explanation

| Component     | Purpose             |
| ------------- | ------------------- |
| form          | Collects user data  |
| method="POST" | Sends data securely |
| request.form  | Access form data    |

---

## 🔄 GET vs POST

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve data |
| POST   | Send data     |

---

## 📊 Common Uses in AI Apps

* AI chatbot input
* Text summarization forms
* File upload forms
* Prompt submission

---

## ⚠️ Important Notes

* Use POST for sensitive data
* Input validation is important
* Flask handles form data using `request` object

---

## 🎯 Interview Key Points

* Forms collect user input
* Flask uses `request.form`
* GET and POST methods are commonly used
* Forms connect frontend and backend

---

## 🧠 One-Line Summary

> Forms in Flask allow users to send input data from webpages to the backend application.

---

## 🔚 Final Thought

Forms are an essential part of Flask applications, enabling interaction between users and AI-powered backend systems.
