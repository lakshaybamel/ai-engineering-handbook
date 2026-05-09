# Deploying an AI Assistant with Flask

## 🚀 Introduction

Flask can be used to deploy AI assistants as web applications.

👉 Instead of running AI models only in notebooks or terminals, Flask allows users to interact through a browser.

---

## 🧠 Simple Intuition

Think of it like:

> Flask creates a bridge between the user interface and the AI model.

---

## 📌 Basic Workflow

```text
User Input → Flask App → AI Model/API → Response → Webpage
```

---

## 📂 Basic Project Structure

```text
project/
│
├── app.py
├── templates/
│   └── index.html
│
└── static/
```

---

## ⚙️ HTML Frontend

### `templates/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>AI Assistant</title>
</head>
<body>

    <h1>AI Assistant</h1>

    <form method="POST">
        <input type="text" name="question" placeholder="Ask something">
        <button type="submit">Send</button>
    </form>

    {% if response %}
        <h3>Response:</h3>
        <p>{{ response }}</p>
    {% endif %}

</body>
</html>
```

---

## ⚙️ Flask Backend with Gemini API

### `app.py`

```python
from flask import Flask, render_template, request
from google import genai
from google.genai import types

app = Flask(__name__)

# initialize Gemini client
client = genai.Client(api_key="YOUR_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():

    response_text = ""

    if request.method == "POST":

        question = request.form["question"]

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction="Act like a helpful AI assistant.",
                temperature=0.7
            )
        )

        response_text = response.text

    return render_template(
        "index.html",
        response=response_text
    )

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🌐 Running the Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000/
```

---

## 📊 Features of This Application

* User-friendly interface
* AI-powered responses
* Real-time interaction
* Browser-based assistant

---

## 📊 Common Enhancements

| Feature        | Purpose             |
| -------------- | ------------------- |
| Chat history   | Memory              |
| Database       | Store conversations |
| Authentication | User accounts       |
| Deployment     | Host online         |

---

## ⚠️ Important Notes

* API key should be secured
* Avoid exposing secrets publicly
* Production deployment uses cloud platforms

---

## 🎯 Interview Key Points

* Flask can deploy AI assistants
* Frontend interacts with backend routes
* AI response is generated using APIs
* Forms send user prompts to Flask backend

---

## 🧠 One-Line Summary

> Flask allows AI assistants to be deployed as interactive web applications accessible through browsers.

---

## 🔚 Final Thought

Deploying AI assistants with Flask transforms AI models from local scripts into real-world applications that users can access and interact with easily.
