# ⚙️ Training a Convolutional Neural Network (CNN)

## 📌 Overview

After designing the CNN architecture, the next step is **training the model**.

Training a CNN means adjusting its **weights and filters** so that the network can correctly recognize patterns in images.

The training process involves repeatedly passing images through the network, calculating errors, and updating the model parameters to **minimize the prediction error**.

This process is similar to training other neural networks but applied specifically to **image data**.

---

## 🧠 CNN Training Pipeline

Training a CNN generally follows this pipeline:

```text
Load Dataset
      ↓
Preprocess Images
      ↓
Forward Pass (Prediction)
      ↓
Compute Loss
      ↓
Backpropagation
      ↓
Update Weights
      ↓
Repeat for Multiple Epochs
```

Each step gradually improves the model’s ability to recognize patterns in images.

---

## 📂 Step 1: Load the Dataset

The first step is to load the image dataset.

Datasets for CNN training usually contain:

* input images
* corresponding labels

Example:

```text
Image → Cat
Image → Dog
Image → Car
```

The dataset is usually split into:

```text
Training Set
Validation Set
Test Set
```

Typical split:

```text
70–80% → Training
10–15% → Validation
10–15% → Testing
```

---

## 🖼️ Step 2: Image Preprocessing

Before feeding images into a CNN, they must be **preprocessed**.

Common preprocessing steps include:

### Resizing

Images must have the **same dimensions**.

Example:

```text
224 × 224
```

---

### Normalization

Pixel values are scaled to a smaller range.

Example:

```text
0 → 255
```

Normalized to:

```text
0 → 1
```

This improves training stability.

---

### Data Augmentation (Optional)

Data augmentation artificially increases dataset size.

Examples:

* image rotation
* horizontal flipping
* cropping
* brightness changes

This helps reduce **overfitting**.

---

## 🔄 Step 3: Forward Pass

During the forward pass:

1. The input image enters the CNN.
2. Convolution layers extract features.
3. Pooling layers reduce dimensions.
4. Fully connected layers produce predictions.

Example:

```text
Image → CNN → Predicted Class
```

The output of the network is usually a **probability distribution over classes**.

---

## 📉 Step 4: Compute Loss

After predictions are made, the model calculates **loss**, which measures how wrong the predictions are.

Common loss functions:

### Cross Entropy Loss

Used for classification tasks.

Example:

```text
True Label → Cat
Predicted → Dog
```

Loss increases when predictions are incorrect.

The training objective is to **minimize this loss**.

---

## 🔙 Step 5: Backpropagation

Backpropagation calculates how much each weight contributed to the error.

Using the **chain rule**, gradients of the loss are computed for every parameter in the network.

This process tells the model:

```text
Which weights should increase or decrease
```

Backpropagation enables the network to **learn from its mistakes**.

---

## ⚡ Step 6: Update Weights

After computing gradients, the optimizer updates the network parameters.

Common optimizers include:

* Stochastic Gradient Descent (SGD)
* Adam
* RMSProp

Example update rule:

```text
New Weight = Old Weight − Learning Rate × Gradient
```

This step gradually improves the network's performance.

---

## 🔁 Step 7: Repeat for Multiple Epochs

The entire process is repeated for multiple **epochs**.

Definition:

```text
1 Epoch = One complete pass through the entire training dataset
```

Example:

```text
Epoch 1 → Initial learning
Epoch 50 → Better feature detection
Epoch 100 → Improved accuracy
```

As training progresses:

* loss decreases
* accuracy increases

---

## 📊 Monitoring Training

During training, several metrics are monitored.

Common metrics:

* training loss
* validation loss
* accuracy

Loss curves help visualize how well the model is learning.

Example trend:

```text
Epoch → Loss decreases
Epoch → Accuracy increases
```

This indicates successful training.

---

## ⚠️ Common Challenges in CNN Training

### Overfitting

The model performs well on training data but poorly on new data.

Solutions:

* data augmentation
* dropout
* regularization

---

### Underfitting

The model fails to learn meaningful patterns.

Solutions:

* increase model complexity
* train for more epochs
* adjust learning rate

---

### Slow Training

CNNs can be computationally expensive.

Solutions:

* GPU acceleration
* smaller batch sizes
* efficient architectures

---

## 🎯 Key Points

* CNN training involves **forward propagation, loss calculation, and backpropagation**.
* Optimizers update the network weights to minimize loss.
* Training is repeated across multiple **epochs**.
* Proper preprocessing and monitoring are essential for good performance.

---

## 🧠 One-Line Summary

> Training a CNN involves repeatedly passing images through the network, computing prediction errors, and updating the model’s parameters so that it can accurately recognize patterns in visual data.
