# APIs with JSON in Flask

## 🚀 Introduction

Flask can be used to build APIs that send and receive data in **JSON format**.

👉 JSON is the most common format used in:

* Web APIs
* AI applications
* Frontend-backend communication

---

## 🧠 Simple Intuition

Think of JSON like:

> A structured way to exchange data between applications.

---

## 📌 Example JSON

```json
{
    "name": "Lakshay",
    "role": "AI Student"
}
```

---

## 🔄 API Flow

```text
Client → Flask API → JSON Response
```

---

## ⚙️ Creating a Simple API

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def api():

    data = {
        "message": "Hello from Flask API"
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📌 Output

```json
{
    "message": "Hello from Flask API"
}
```

---

## ⚙️ Receiving JSON Data

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    text = data["text"]

    return jsonify({
        "received_text": text
    })

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📌 Example Request

```json
{
    "text": "Explain AI"
}
```

---

## 📌 Example Response

```json
    "received_text": "Explain AI"
}
```

---

## 📊 Common Uses in AI

* Chatbot APIs
* Text summarization APIs
* RAG systems
* AI model inference APIs

---

## ⚠️ Important Notes

* APIs commonly use JSON format
* `jsonify()` converts Python data to JSON
* `request.get_json()` reads JSON input

---

## 🎯 Interview Key Points

* Flask can build REST APIs
* JSON is standard API data format
* `jsonify()` returns JSON response
* `request.get_json()` reads JSON requests

---

## 🧠 One-Line Summary

> Flask APIs use JSON to exchange structured data between clients and backend applications.

---

## 🔚 Final Thought

JSON APIs are the foundation of modern AI and web applications, enabling communication between frontend systems and AI models.
