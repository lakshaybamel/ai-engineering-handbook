# Parameters for Text Generation

## 🚀 Introduction

When using LLM APIs, we can control how the model generates responses using **parameters**.

👉 These parameters affect:

* Creativity
* Length
* Randomness
* Accuracy

---

## 🧠 Simple Intuition

Think of parameters as:

> Settings that control how the model behaves while generating text.

---

## 📌 Common Parameters

---

## 🔹 1. Temperature

* Controls randomness

### Range:

```text 
0 → deterministic (same output)
1 → more random
```

---

### Example:

* Low temperature → factual answer
* High temperature → creative answer

---

## 🔹 2. Max Tokens

* Limits output length

```text
max_tokens = 100
```

👉 Output will not exceed 100 tokens

---

## 🔹 3. Top-p (Nucleus Sampling)

* Controls diversity of output

```text
top_p = 0.9
```

👉 Model selects from top probable words

---

## 🔹 4. Top-k

* Limits number of candidate words

```text
top_k = 50
```

👉 Model chooses from top 50 options

---

## 🔹 5. Frequency Penalty

* Reduces repetition

👉 Higher value → less repetition

---

## 🔹 6. Presence Penalty

* Encourages new topics

👉 Higher value → more diverse output

---

## ⚙️ Example (OpenAI)

```python
response = client.responses.create(
    model="gpt-4.1",
    input="Explain AI",
    temperature=0.7,
    max_output_tokens=100
)
```

---

## ⚙️ Example (Gemini)

```python
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain AI",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 100
    }
)
```

---

## 📊 Parameter Effect Summary

| Parameter         | Effect              |
| ----------------- | ------------------- |
| Temperature       | Randomness          |
| Max Tokens        | Output length       |
| Top-p             | Diversity           |
| Top-k             | Candidate selection |
| Frequency penalty | Repetition control  |
| Presence penalty  | Topic diversity     |

---

## ⚠️ Important Notes

* Low temperature → more accurate
* High temperature → more creative
* Balance depends on use case

---

## 🎯 Interview Key Points

* Parameters control model behavior
* Temperature affects randomness
* Max tokens controls length
* Top-p and top-k control diversity
* Used to fine-tune responses

---

## 🧠 One-Line Summary

> Parameters control how an LLM generates text, affecting creativity, length, and diversity.

---

## 🔚 Final Thought

Understanding parameters helps you **fine-tune model output**, making AI responses more suitable for real-world applications.
