# Responses API

## 🚀 Introduction

The **Responses API** is used to interact with Large Language Models (LLMs) to generate outputs.

👉 It allows you to:

* Send input (prompt)
* Get generated response

---

## 🧠 Simple Intuition

Think of it like:

> You send a question to the model, and it returns an answer.

---

## 📌 Basic Flow

```text
User Input → API Request → LLM → Response
```

---

## ⚙️ How It Works

1. Send input (text/image)
2. API processes request
3. Model generates output
4. Response is returned

---

## 📌 Example (Concept)

```python
response = model.generate("What is AI?")
print(response)
```

---

## 🔹 Using with OpenAI (Example)

```python
from openai import OpenAI

client = OpenAI(api_key="Your API key here")

response = client.responses.create(
    model="gpt-5.4",
    input="Explain how AI works in a few words"
)

print(response.output_text)
```

---

## 🔹 Using with Gemini

```python
from google import genai

client = genai.Client(api_key="Your API key here")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

---

## 📊 Input Types

* Text
* Image
* Multimodal (text + image)

---

## 📊 Output Types

* Text response
* Structured output
* JSON (optional)

---

## ⚠️ Important Points

* Requires API key
* Response depends on prompt quality
* Different models give different outputs

---

## 🎯 Interview Key Points

* Used to interact with LLMs
* Takes input → returns generated output
* Supports text and multimodal input
* Works via API calls

---

## 🧠 One-Line Summary

> Responses API is used to send input to an LLM and receive generated output.

---

## 🔚 Final Thought

Responses API is the core way to **connect applications with LLMs**, enabling real-world AI features like chatbots and assistants.
