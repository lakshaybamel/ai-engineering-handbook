# ☁️ Google Colab Setup

## 📌 Overview

**Google Colab (Colaboratory)** is a cloud-based platform that allows you to write and execute **Python code in a Jupyter notebook environment directly in the browser**.

It is widely used for **Machine Learning and Deep Learning experiments** because it provides **free access to GPUs and TPUs**.

With Google Colab you can:

* Write Python code
* Run deep learning models
* Use GPUs for faster training
* Save notebooks to Google Drive
* Share notebooks easily

All of this works **without installing anything on your local machine**.

---

## 🧠 Why Use Google Colab?

Deep learning models often require **high computational power**.

Training models on a normal CPU can be **very slow**.

Google Colab solves this by providing:

* ⚡ Free GPUs
* ⚡ Cloud execution
* ⚡ Easy sharing

Example: Training a neural network

```
Local CPU → Slow training

Colab GPU → Much faster training
```

This makes it very useful for **students and beginners**.

---

## ⚙️ How to Open Google Colab

### Step 1

Go to:

```
https://colab.research.google.com
```

---

### Step 2

Sign in using your **Google account**.

---

### Step 3

Click:

```
New Notebook
```

A new **Jupyter-style notebook** will open in the browser.

---

## 🧪 Notebook Interface

A Colab notebook contains **two main types of cells**.

### Code Cell

Used to run Python code.

Example:

```python
print("Hello Deep Learning")
```

---

### Text Cell (Markdown)

Used to write explanations, documentation, and notes.

Example:

```markdown
# My Deep Learning Experiment
```

---

## ⚡ Enabling GPU

To use GPU acceleration in Google Colab:

### Step 1

Click:

```
Runtime
```

---

### Step 2

Select:

```
Change runtime type
```

---

### Step 3

Choose:

```
Hardware accelerator → GPU
```

Then click **Save**.

Your notebook will now run using **GPU hardware**.

---

## 🧪 Checking GPU Availability

You can verify that GPU is enabled using the following code:

```python
import torch

print(torch.cuda.is_available())
```

If the output is:

```
True
```

then GPU is available.

---

## 📂 Saving Notebooks

Colab notebooks are automatically saved to **Google Drive**.

File format:

```
.ipynb
```

You can also download the notebook to your computer.

Steps:

```
File → Download → Download .ipynb
```

---

## 📦 Installing Libraries in Colab

Sometimes you may need additional Python libraries.

You can install them using:

```python
!pip install library_name
```

Example:

```python
!pip install torch
```

Colab already comes with many ML libraries preinstalled such as:

* NumPy
* Pandas
* Matplotlib
* PyTorch
* TensorFlow

---

## 🔗 Using Google Drive Data

To access datasets stored in Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

This allows you to load datasets directly from your Drive.

---

## 🎯 Advantages of Google Colab

* No setup required
* Free GPU access
* Easy collaboration
* Works in any browser
* Integrates with Google Drive

This makes it an excellent tool for **deep learning experiments and projects**.

---

## ⚠️ Limitations

Although Colab is very useful, it has some limitations.

* Sessions can disconnect after long inactivity
* Limited GPU usage per day
* Files are temporary unless saved to Drive

For large-scale production training, dedicated servers or cloud platforms are usually used.

---

## ⚠️ Key Points to Remember

* Google Colab is a **cloud-based Jupyter notebook environment**.
* It allows running **Python code in the browser**.
* Provides **free GPUs and TPUs**.
* Useful for **machine learning and deep learning experiments**.
* No local setup is required.

---

## 🎓 Interview Insight

A common interview question:

**What is the advantage of using Google Colab for deep learning?**

Answer:

Google Colab provides **free GPU/TPU resources and a ready-to-use Python environment**, making it easy to train machine learning and deep learning models without local hardware setup.

---

## 🧠 One-Line Summary

> Google Colab is a cloud-based Jupyter notebook platform that allows running Python and deep learning models with free GPU support directly in the browser.
