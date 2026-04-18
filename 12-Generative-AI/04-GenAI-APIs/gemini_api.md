# Gemini API

## 🚀 Introduction

The **Gemini API** is used to interact with Google’s LLMs for tasks like:

* Text generation
* Image understanding
* Multimodal inputs

👉 It is a powerful and **developer-friendly alternative** to other LLM APIs.

---

## 🧠 Simple Intuition

Think of Gemini API as:

> A way to send prompts to Google’s AI models and get intelligent responses.

---

## ⚙️ Setup

### Install library

```bash
pip install google-genai
```

---

### Import and Configure

```python
from google import genai

client = genai.Client(api_key=GEMINI_API_KEY)
```

---

## 📌 Basic Text Generation

```python
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain AI in simple words"
)

print(response.text)
```

---

## ⚙️ Using Configuration (Advanced)

```python
from google.genai import types

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain machine learning",
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful assistant.",
        temperature=0.7,
        max_output_tokens=500
    )
)

print(response.text)
```

---

## 🖼️ Image Input Example

```python
import requests
from google.genai import types

image_url = "https://images.pexels.com/photos/3476860/pexels-photo-3476860.jpeg"
image_response = requests.get(image_url)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        "Which country's flag is in the image?",
        types.Part.from_bytes(
            data=image_response.content,
            mime_type="image/jpeg"
        )
    ]
)

print(response.text)
```

---

## 🎨 Image Generation Example

```python
from google.genai import types

response = client.models.generate_images(
    model="imagen-3.0-generate-001",
    prompt="A futuristic city with flying cars",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        size="1024x1024"
    )
)

for img in response.generated_images:
    img.image.save("output.png")
```

---

## 📊 Key Features

* Text generation
* Multimodal input (text + image)
* Image generation (Imagen)
* Config-based control (temperature, tokens)

---

## ⚠️ Important Notes

* Requires API key
* Different models for different tasks
* Use correct model name (flash, pro, imagen)

---

## 🎯 Interview Key Points

* Gemini is Google’s LLM API
* Uses `genai.Client()`
* Supports multimodal input
* Uses `system_instruction` instead of roles
* Supports image generation via Imagen

---

## 🧠 One-Line Summary

> Gemini API allows developers to interact with Google’s AI models for text, image, and multimodal tasks.

---

## 🔚 Final Thought

Gemini API provides a **powerful and accessible way to build real-world AI applications**, especially with free-tier support for developers.
