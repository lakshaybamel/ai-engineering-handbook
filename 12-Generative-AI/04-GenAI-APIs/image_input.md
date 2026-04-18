# Image Input in LLM APIs

## 🚀 Introduction

Modern LLMs support **image input**, allowing models to understand visual data.

👉 This is called **multimodal AI** (Text + Image)

---

## 🧠 Simple Intuition

Think of it like:

> You show an image to the model and ask questions about it.

---

## 📌 What Can Be Done

* Image description
* Object understanding
* Visual question answering
* Basic OCR

---

## 🔄 Basic Flow

```text
Image + Prompt → LLM → Response
```

---

## ⚙️ Example (OpenAI)

```python
from openai import OpenAI

client = OpenAI(api_key="API key here")

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What is in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg"
                }
            ]
        }
    ]
)

print(response.output_text)
```

---

## ⚙️ Example (Gemini)

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="API key here")

# fetch image from URL
image_url = "https://example.com/image.jpg"
image_response = requests.get(image_url)

# send image + prompt
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        "What is in this image?",
        types.Part.from_bytes(
            data=image_response.content,
            mime_type="image/jpeg"
        )
    ]
)

print(response.text)
```

---

## 📊 Input Types

* Image URL
* Image file
* Image bytes
* Image + text prompt

---

## 📊 Output

* Text description
* Answer based on image
* Combined reasoning

---

## ⚠️ Important Notes

* Image clarity affects accuracy
* Prompt matters a lot
* Large images may need resizing

---

## 🎯 Interview Key Points

* Image input = multimodal capability
* Can process text + image together
* Gemini uses `Part.from_bytes()` for images
* Used in vision-based AI systems

---

## 🧠 One-Line Summary

> Image input allows LLMs to understand and respond based on visual data along with text.

---

## 🔚 Final Thought

Multimodal AI enables systems to **see + understand**, making them far more powerful than text-only models.
