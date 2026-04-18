# Image Generation in LLM APIs

## 🚀 Introduction

Image generation allows LLMs to **create images from text prompts**.

👉 You provide a description → model generates an image

---

## 🧠 Simple Intuition

Think of it like:

> You describe a scene, and the AI draws it for you.

---

## 📌 Use Cases

* AI art generation
* UI/UX mockups
* Marketing creatives
* Game assets

---

## 🔄 Basic Flow

```text
Text Prompt → API → Image Model → Generated Image
```

---

## ⚙️ Example (OpenAI)

```python
from openai import OpenAI
import base64

client = OpenAI(api_key=API_KEY_HERE)

prompt = "A futuristic city with flying cars at sunset"

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="1024x1024"
)

# get image bytes
image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# save image
with open("output.png", "wb") as f:
    f.write(image_bytes)

print("Image saved as output.png")
```

---

## ⚙️ Example (Gemini - Correct Approach)

👉 Gemini uses **image generation models (like imagen)**

```python
from google import genai
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

prompt = "A futuristic city with flying cars at sunset"

response = client.models.generate_images(
    model="imagen-3.0-generate-001",
    prompt=prompt,
    config=types.GenerateImagesConfig(
        number_of_images=1,
        size="1024x1024"
    )
)

# save image
for img in response.generated_images:
    img.image.save("output.png")

print("Image saved as output.png")
```

---

## 📊 Key Parameters

| Parameter        | Description          |
| ---------------- | -------------------- |
| prompt           | Description of image |
| size             | Image resolution     |
| number_of_images | Number of outputs    |

---

## ⚠️ Important Notes

* Better prompts → better images
* High resolution → more cost/time
* Model choice matters

---

## 🎯 Interview Key Points

* Image generation = text → image
* Uses diffusion / generative models
* OpenAI uses `images.generate()`
* Gemini uses `generate_images()` with Imagen
* Prompt quality is critical

---

## 🧠 One-Line Summary

> Image generation APIs convert text descriptions into images using generative AI models.

---

## 🔚 Final Thought

Image generation is a key part of modern AI, enabling systems to **create visuals from imagination**, not just text.
