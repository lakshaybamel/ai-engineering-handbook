# Image Editing in LLM APIs

## 🚀 Introduction

Image editing allows AI models to **modify existing images using text instructions**.

👉 Instead of generating from scratch, you:

* Provide an image
* Give instructions
* Get edited output

---

## 🧠 Simple Intuition

Think of it like:

> You give an image and say "make the sky sunset" → AI edits it.

---

## 📌 Use Cases

* Background change
* Object removal
* Style modification
* Image enhancement

---

## 🔄 Basic Flow

```text
Input Image + Prompt → API → Edited Image
```

---

## ⚙️ Example (OpenAI)

```python
from openai import OpenAI

client = OpenAI()

prompt = "Add a sunset sky to this image"

result = client.images.edits(
    model="gpt-image-1",
    image=open("input.png", "rb"),
    prompt=prompt
)

# save edited image
image_base64 = result.data[0].b64_json

import base64
image_bytes = base64.b64decode(image_base64)

with open("edited.png", "wb") as f:
    f.write(image_bytes)

print("Edited image saved as edited.png")
```

---

## ⚙️ Example (Gemini - Current Capability)

👉 Gemini does **not directly support full image editing API like OpenAI**

👉 Instead, it works in 2 ways:

---

### 🔹 1. Describe Changes (Text Output)

```python
from google import genai
from PIL import Image

client = genai.Client(api_key=GEMINI_API_KEY)

image = Image.open("input.png")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        "Describe how to convert this image into a sunset scene",
        image
    ]
)

print(response.text)
```

---

### 🔹 2. Re-generate Image (Indirect Editing)

👉 You:

* Describe original image
* Add modification prompt
* Generate new image using Imagen

```python
prompt = "A photo of a city street with a sunset sky, warm lighting"

response = client.models.generate_images(
    model="imagen-3.0-generate-001",
    prompt=prompt
)

# save result
for img in response.generated_images:
    img.image.save("edited.png")
```

---

## 📊 Comparison

| Feature              | OpenAI | Gemini     |
| -------------------- | ------ | ---------- |
| Direct editing API   | ✅ Yes  | ❌ No       |
| Prompt-based editing | ✅ Yes  | ✅ Indirect |
| Image generation     | ✅ Yes  | ✅ Yes      |

---

## ⚠️ Important Notes

* Editing depends on prompt clarity
* OpenAI supports direct editing
* Gemini uses indirect approach (generate new image)

---

## 🎯 Interview Key Points

* Image editing = modify existing image
* OpenAI supports direct editing API
* Gemini uses indirect regeneration
* Prompt plays key role
* Used in creative AI applications

---

## 🧠 One-Line Summary

> Image editing APIs allow modifying existing images using text instructions, either directly or through regeneration.

---

## 🔚 Final Thought

Image editing brings AI closer to real-world creative tools, enabling users to **modify visuals using simple natural language commands**.
