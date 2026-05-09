# Query Strings in Flask

## 🚀 Introduction

Query strings are used to send small pieces of data through the URL.

👉 They are commonly used for:

* Search queries
* Filters
* Pagination
* User preferences

---

## 🧠 Simple Intuition

Think of query strings like:

> Extra information attached to a URL.

---

## 📌 Example URL

```text
http://127.0.0.1:5000/search?name=lakshay
```

Here:

* `search` → route
* `name=lakshay` → query string

---

## 🔄 Basic Flow

```text
Browser URL → Query String → Flask Backend → Response
```

---

## ⚙️ Flask Example

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():

    name = request.args.get("name")

    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📌 Accessing Query Parameters

```python
request.args.get("key")
```

👉 Retrieves value from URL query string.

---

## 📌 Multiple Query Parameters

### URL

```text
http://127.0.0.1:5000/search?name=lakshay&age=22
```

---

### Flask Code

```python
@app.route("/search")
def search():

    name = request.args.get("name")
    age = request.args.get("age")

    return f"Name: {name}, Age: {age}"
```

---

## 📊 Common Uses

* Search functionality
* Filtering results
* Sorting data
* API requests

---

## ⚠️ Important Notes

* Query strings are visible in URL
* Avoid sending sensitive data
* Mostly used with GET requests

---

## 🎯 Interview Key Points

* Query strings pass data through URLs
* Accessed using `request.args`
* Commonly used with GET requests
* Useful for filtering and searching

---

## 🧠 One-Line Summary

> Query strings allow Flask applications to receive small pieces of data through URLs.

---

## 🔚 Final Thought

Query strings are a simple and powerful way to pass user data between webpages and backend applications.
