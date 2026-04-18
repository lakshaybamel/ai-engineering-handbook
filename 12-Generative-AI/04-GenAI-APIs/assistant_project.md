# AI Assistant Project

## 🚀 Introduction

This project demonstrates how to build a **simple AI personal assistant** using LLM APIs.

👉 The assistant can:

* Answer questions
* Provide explanations
* Perform basic tasks

---

## 🧠 Simple Intuition

Think of it like:

> A chatbot that behaves like a smart assistant using an LLM.

---

## 📌 Objective

* Take user input
* Send it to LLM
* Generate response
* Display output

---

## 🔄 Workflow

```text
User Input → API Call → LLM → Response → Output
```

---

## ⚙️ Basic Implementation (Gemini)

```python
from google import genai
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

while True:
    question = input("Ask me anything: ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction="Act like a helpful personal assistant. Use plain text only.",
            temperature=0.7,
            max_output_tokens=500
        )
    )

    print(response.text.strip())
```

---

## ⚙️ Key Features

* Interactive chatbot
* Uses LLM API
* Supports continuous conversation
* Configurable behavior

---

## 📊 Enhancements (Optional)

* Add memory (chat history)
* Add UI (Flask / FastAPI)
* Integrate with RAG
* Add voice input/output

---

## ⚠️ Important Notes

* Requires API key
* Response depends on prompt
* Can be extended for real applications

---

## 🎯 Interview Key Points

* Demonstrates API integration
* Shows real-world use of LLMs
* Uses system instruction for behavior control
* Can be extended to full chatbot

---

## 🧠 One-Line Summary

> This project builds a simple AI assistant using LLM APIs to answer user queries interactively.

---

## 🔚 Final Thought

Building an AI assistant is one of the best ways to understand how LLMs are used in **real-world applications**, from chatbots to productivity tools.
