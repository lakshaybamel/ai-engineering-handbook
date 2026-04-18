# OpenAI API

## 🚀 Introduction

The **OpenAI API** allows developers to interact with powerful LLMs for tasks like:

* Text generation
* Image generation
* Chat-based applications

👉 It is widely used in production AI systems.

---

## 🧠 Simple Intuition

Think of OpenAI API as:

> A way to send prompts to advanced AI models and receive intelligent responses.

---

## ⚙️ Setup

### Install library

```bash
pip install openai
```

---

### Import and Configure

```python
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)
```

---

## 📌 Basic Text Generation

```python
response = client.responses.create(
    model="gpt-4.1",
    input="Explain artificial intelligence in simple terms"
)

print(response.output[0].content[0].text)
```

---

## ⚙️ Using Parameters

```python
response = client.responses.create(
    model="gpt-4.1",
    input="Explain machine learning",
    temperature=0.7,
    max_output_tokens=100
)

print(response.output[0].content[0].text)
```

---

## 💬 Using Roles (Chat Format)

```python
response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is AI?"}
    ]
)

print(response.output[0].content[0].text)
```

---

## 🖼️ Image Input Example

```python
response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg"
                }
            ]
        }
    ]
)

print(response.output[0].content[0].text)
```

---

## 🎨 Image Generation Example

```python
import base64

result = client.images.generate(
    model="gpt-image-1",
    prompt="A futuristic robot in a city",
    size="1024x1024"
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("output.png", "wb") as f:
    f.write(image_bytes)

print("Image saved as output.png")
```

---

## 📊 Key Features

* Text generation
* Chat-based interaction (roles)
* Image generation
* Multimodal support

---

## ⚠️ Important Notes

* Requires API key
* Paid service
* Different models for different tasks

---

## 🎯 Interview Key Points

* OpenAI API uses `responses.create()`
* Supports roles (system, user, assistant)
* Supports multimodal input
* Provides image generation API
* Used in production AI apps

---

## 🧠 One-Line Summary

> OpenAI API enables interaction with powerful AI models for text, image, and multimodal tasks.

---

## 🔚 Final Thought

OpenAI API is one of the most widely used tools for building **real-world AI applications**, from chatbots to creative systems.
