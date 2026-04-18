# Chunking in RAG

## 🚀 Introduction

**Chunking** is the process of splitting large documents into **smaller pieces (chunks)** in a RAG system.

👉 It is a critical step in the **ingestion pipeline**

---

## 🧠 Simple Intuition

Think of it like:

> Instead of storing a full book, break it into small paragraphs so you can quickly find relevant information.

---

## ❌ Problem Without Chunking

* Large documents are hard to process
* LLMs have **token limits**
* Retrieval becomes inaccurate

👉 Entire document may not be relevant

---

## ✅ Solution: Chunking

* Split documents into smaller parts
* Each chunk represents a meaningful piece of text

---

## 🔄 Where It Fits

```text
Raw Data → Chunking → Embeddings → Vector Store
```

---

## 📌 Example

Original text:

```text
Artificial Intelligence is transforming industries. It is used in healthcare, finance, and more...
```

After chunking:

```text
Chunk 1 → Artificial Intelligence is transforming industries.
Chunk 2 → It is used in healthcare, finance, and more.
```

---

## 🧩 Types of Chunking

---

### 🔹 1. Fixed-size Chunking

* Split text into equal sizes
* Example: 100 words per chunk

👉 Simple but may break context

---

### 🔹 2. Sentence-based Chunking

* Split based on sentences

👉 Maintains meaning

---

### 🔹 3. Overlapping Chunking

* Chunks overlap with each other

👉 Preserves context across chunks

Example:

```text
Chunk 1 → Sentence A + Sentence B  
Chunk 2 → Sentence B + Sentence C  
```

---

### 🔹 4. Semantic Chunking (Advanced)

* Split based on meaning
* Keeps related content together

---

## ⚙️ Chunking in Practice

Example (Python):

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)
```

---

## 📊 Why Chunking is Important

| Feature              | Benefit                   |
| -------------------- | ------------------------- |
| Smaller units        | Efficient processing      |
| Better retrieval     | More accurate results     |
| Token limit handling | Works within model limits |
| Context preservation | With overlap              |

---

## ⚠️ Important Considerations

* Chunk size should not be too small
* Too large chunks reduce accuracy
* Overlap improves context

---

## 🎯 Interview Key Points

* Chunking = splitting documents into smaller parts
* Required due to token limits
* Improves retrieval accuracy
* Types:

  * Fixed
  * Sentence-based
  * Overlapping
* Used before embeddings

---

## 🧠 One-Line Summary

> Chunking breaks large documents into smaller meaningful pieces to improve retrieval and handle model limitations in RAG systems.

---

## 📌 Quick Analogy

Think of searching in notes:

* Instead of scanning full book
* You search specific paragraphs

👉 That’s chunking

---

## 🔚 Final Thought

Good chunking directly improves retrieval quality — and better retrieval leads to better answers in RAG systems.
