# CelebA Dataset Setup

## 🚀 Introduction

The **CelebA Dataset** is one of the most popular datasets used for training GANs.

👉 It contains:

* celebrity face images
* facial attributes
* large-scale face data

GANs commonly use CelebA for:

* face generation
* synthetic image creation

---

## 🧠 Simple Intuition

Think of CelebA like:

> A large collection of human face images used to teach GANs how real faces look.

---

## 📌 About the Dataset

| Feature      | Value        |
| ------------ | ------------ |
| Dataset Name | CelebA       |
| Images       | 200,000+     |
| Type         | Face images  |
| Common Use   | GAN training |

---

## 📂 Why CelebA is Popular

* Large dataset
* High-quality face images
* Standard benchmark for GANs

---

## ⚙️ Installing Required Libraries

```bash
pip install torch torchvision matplotlib
```

---

## ⚙️ Import Libraries

```python
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
```

---

## ⚙️ Image Transformations

Transformations help:

* resize images
* normalize pixel values
* prepare data for GAN training

```python
transform = transforms.Compose([

    transforms.Resize((64, 64)),
    transforms.ToTensor(),

    transforms.Normalize(
        (0.5, 0.5, 0.5),
        (0.5, 0.5, 0.5)
    )
])
```

---

## ⚙️ Loading CelebA Dataset

```python
dataset = datasets.CelebA(
    root="./data",
    split="train",
    download=True,
    transform=transform
)
```

---

## ⚙️ Creating DataLoader

```python
dataloader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)
```

---

## 📌 Why DataLoader is Used

DataLoader helps:

* load data in batches
* shuffle images
* improve training efficiency

---

## 📊 Image Preprocessing

| Step      | Purpose             |
| --------- | ------------------- |
| Resize    | Fixed image size    |
| ToTensor  | Convert to tensor   |
| Normalize | Stable GAN training |

---

## ⚠️ Important Notes

* GANs require large datasets
* Image normalization is important
* CelebA download size is large

---

## 🎯 Interview Key Points

* CelebA is a face dataset
* Commonly used in GAN projects
* DataLoader handles batch loading
* Normalization improves training stability

---

## 🧠 One-Line Summary

> CelebA is a large-scale face image dataset widely used for training GANs and image generation models.

---

## 🔚 Final Thought

The CelebA dataset became a standard benchmark for GAN research because of its large collection of realistic human face images.
