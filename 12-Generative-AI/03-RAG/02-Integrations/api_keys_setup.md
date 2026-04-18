# API Keys Setup for RAG

## 🚀 Introduction

To use LLMs (like Gemini, GPT, Groq), we need **API keys**.

👉 API keys allow your application to:

* Access external AI models
* Send requests
* Receive responses

---

## 🧠 Simple Intuition

Think of API key as:

> A password that allows your code to communicate with an AI service.

---

## 📌 Why API Keys are Needed

* Authenticate your application
* Track usage
* Enable secure access to models

---

## 🔑 How to Set API Keys

---

## 🔹 1. Using Environment Variables (Recommended)

### Step 1: Set API Key

#### Windows:

```bash
setx API_KEY "your_api_key_here"
```

#### Mac/Linux:

```bash
export API_KEY="your_api_key_here"
```

---

### Step 2: Access in Python

```python
import os

api_key = os.getenv("API_KEY")
print(api_key)
```

---

## 🔹 2. Using `.env` File

Create a `.env` file:

```text
API_KEY=your_api_key_here
```

---

### Load in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
```

---

## 🔹 3. Direct in Code (Not Recommended)

```python
api_key = "your_api_key_here"
```

👉 Avoid this for security reasons

---

## 🔥 API Setup Examples

---

### 🔸 Gemini

```python
import google.generativeai as genai

genai.configure(api_key=api_key)
```

---

### 🔸 OpenAI

```python
from openai import OpenAI

client = OpenAI(api_key=api_key)
```

---

### 🔸 Groq

```python
from groq import Groq

client = Groq(api_key=api_key)
```

---

## ⚠️ Important Security Practices

* Never push API keys to GitHub
* Use `.env` or environment variables
* Add `.env` to `.gitignore`

---

## 📊 Best Practice

| Method                | Use     |
| --------------------- | ------- |
| Environment variables | ✅ Best  |
| `.env` file           | ✅ Good  |
| Hardcoding            | ❌ Avoid |

---

## 🎯 Interview Key Points

* API key is used for authentication
* Should not be exposed publicly
* Use environment variables
* Required for accessing LLM APIs

---

## 🧠 One-Line Summary

> API keys allow secure access to LLM services and should be managed safely using environment variables.

---

## 🔚 Final Thought

Proper API key management is essential for building **secure and production-ready AI applications**.
