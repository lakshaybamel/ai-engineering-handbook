# 🧠 CNN Architecture

## 📌 Overview

A **Convolutional Neural Network (CNN)** is a specialized type of neural network designed to process **image data**.

Unlike traditional neural networks, CNNs are built with layers that are specifically designed to **capture spatial patterns in images**, such as edges, textures, shapes, and objects.

CNNs are widely used in **computer vision tasks**, including:

* image classification
* object detection
* face recognition
* medical image analysis

---

## 🧩 Basic Structure of a CNN

A typical CNN architecture consists of the following layers:

```text
Input Image
     ↓
Convolution Layer
     ↓
Activation Function
     ↓
Pooling Layer
     ↓
Fully Connected Layer
     ↓
Output Layer
```

Each layer performs a specific function to **extract and process visual features** from the image.

---

## 🖼️ Input Layer

The **input layer** receives the image data.

Images are represented as a **3D tensor**:

```text
Height × Width × Channels
```

Example:

```text
32 × 32 × 3
```

Where:

* 32 → image height
* 32 → image width
* 3 → RGB channels

For grayscale images, the number of channels is:

```text
1
```

---

## 🔍 Convolution Layer

The **convolution layer** is the core component of a CNN.

It applies **filters (kernels)** that slide across the image to detect patterns.

Example filter size:

```text
3 × 3
```

These filters help detect features such as:

* edges
* corners
* textures
* shapes

The output of this process is called a **feature map**.

---

## ⚡ Activation Function

After convolution, an **activation function** is applied.

The most commonly used activation function in CNNs is **ReLU (Rectified Linear Unit)**.

Formula:

```text
ReLU(x) = max(0, x)
```

ReLU introduces **non-linearity**, allowing the network to learn complex patterns.

---

## 🧮 Pooling Layer

The **pooling layer** reduces the spatial dimensions of the feature maps.

Common pooling type:

```text
Max Pooling
```

Example:

```text
2 × 2 pooling window
```

Benefits of pooling:

* reduces computational cost
* reduces number of parameters
* helps prevent overfitting

Pooling keeps the **most important information** while reducing image size.

---

## 🔗 Fully Connected Layer

After several convolution and pooling layers, the feature maps are **flattened into a vector**.

This vector is then passed to **fully connected layers**, similar to traditional neural networks.

These layers combine the extracted features to make **final predictions**.

---

## 🎯 Output Layer

The output layer produces the **final prediction**.

The structure depends on the task.

### Binary Classification

```text
1 output neuron
```

### Multi-Class Classification

```text
n output neurons
```

Example:

```text
Cat
Dog
Car
Plane
```

The output layer often uses **Softmax activation** to produce class probabilities.

---

## 🔄 Example CNN Flow

Example CNN architecture:

```text
Input Image (32×32×3)
        ↓
Convolution Layer
        ↓
ReLU Activation
        ↓
Pooling Layer
        ↓
Convolution Layer
        ↓
ReLU Activation
        ↓
Pooling Layer
        ↓
Flatten
        ↓
Fully Connected Layer
        ↓
Output Layer
```

This sequence allows the network to **gradually extract more complex features** from the image.

---

## 🚀 Why CNN Architecture Works Well for Images

CNNs are effective for image processing because they:

* preserve spatial relationships between pixels
* use fewer parameters through **parameter sharing**
* learn hierarchical visual features
* efficiently process large images

These characteristics make CNNs the **standard architecture for computer vision tasks**.

---

## 🎯 Key Points

* CNNs are specialized neural networks designed for **image data**.
* The architecture contains **convolution, activation, pooling, and fully connected layers**.
* Convolution layers extract visual features from images.
* Pooling layers reduce spatial dimensions.
* Fully connected layers perform the final classification.

---

## 🧠 One-Line Summary

> CNN architecture processes images through convolution, activation, pooling, and fully connected layers to extract hierarchical visual features and make predictions.
