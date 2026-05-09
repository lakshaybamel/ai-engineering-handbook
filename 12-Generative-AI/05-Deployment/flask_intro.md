# Flask Framework

## 🚀 Introduction

Flask is a lightweight Python web framework used to build:

* Web applications
* APIs
* Backend services

👉 In AI projects, Flask is commonly used to:

* Deploy ML/AI models
* Create chatbot interfaces
* Build AI-powered web apps

---

## 🧠 Simple Intuition

Think of Flask as:

> A bridge between users and your AI model.

---

## 📌 Why Flask is Popular

* Simple and lightweight
* Easy to learn
* Flexible structure
* Great for APIs and AI apps

---

## 🔄 Basic Flow

```text
User → Flask App → AI Model → Response
```

---

## ⚙️ Installation

```bash
pip install flask
```

---

## ⚙️ Basic Flask Application

```python
from flask import Flask

# create flask app
app = Flask(__name__)

# route
@app.route("/")
def home():
    return "Hello, Flask!"

# run server
if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📌 Explanation

| Component    | Purpose       |
| ------------ | ------------- |
| Flask()      | Creates app   |
| @app.route() | Defines route |
| app.run()    | Starts server |

---

## 🌐 Running the Application

After running:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000/
```

---

## 📊 Common Uses in AI

* AI chatbots
* Text summarizers
* RAG applications
* Model APIs
* AI assistants

---

## ⚠️ Important Notes

* Flask is backend framework
* Works well with HTML/CSS/JS
* Often used with APIs

---

## 🎯 Interview Key Points

* Flask is a lightweight Python web framework
* Used to build APIs and web apps
* Common in AI model deployment
* Uses routes for request handling

---

## 🧠 One-Line Summary

> Flask is a lightweight Python framework used to build web applications and deploy AI/ML models.

---

## 🔚 Final Thought

Flask helps convert AI models from **local notebooks into real usable applications**, making it an important tool for AI engineers.
