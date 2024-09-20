---
layout: post
title:  Converting Keras 1D Convulution to PyTorch
categories: ["Tech"]
tags: ["DeepLearning", "Keras", "PyTorch"]
author: Henry Leung
date: 2023-10-23T00:00:00-00:00
---

Recently I need to convert a model including 1D convolution layers trained with Keras v2 to PyTorch. 
Since Keras uses channels last $(N, L, C)$ and PyTorch uses channels first $(N, C, L)$, the weight matrix needs to be 
transposed in a consistent way such that the output of the two models are the same after flattening.

We can do a simple test to make sure we know how to transpose the weight matrix. Here we will create a simple model 
in Keras and PyTorch first and get the weight matrix from the Keras model and transpose it to PyTorch format,

```python
import torch
import numpy as np
import keras
from keras.layers import Conv1D, Dense, Flatten

np_rng = np.random.default_rng(seed=0)
keras.utils.set_random_seed(0)
x = np_rng.standard_normal((1, 128, 1))

# ======================= Keras =======================
conv1d_keras = Conv1D(filters=2, kernel_size=2)
dense1_keras = Dense(1)
# Forward pass of Keras model
print(dense1_keras(Flatten()(conv1d_keras(x))))

# ======================= PyTorch =======================
x_torch = torch.tensor(x, dtype=torch.float32)
x_torch = x_torch.permute(0, 2, 1)  # Pytorch expects channels first
conv1d_torch = torch.nn.Conv1d(kernel_size=2, in_channels=1, out_channels=2)
dense1_torch = torch.nn.Linear(in_features=254, out_features=1)

# Keras to Pytorch weights conversion
conv1d_torch.weight.data = torch.from_numpy(np.transpose(conv1d_keras.weights[0]))
conv1d_torch.bias.data = torch.from_numpy(np.transpose(conv1d_keras.weights[1]))
dense1_torch.weight.data = torch.from_numpy(np.transpose(dense1_keras.weights[0]))
dense1_torch.bias.data = torch.from_numpy(np.transpose(dense1_keras.weights[1]))

# Forward pass of PyTorch model
print(dense1_torch(torch.flatten(conv1d_torch(x_torch))))
```

which gives the output,

``
tensor([[0.7114]], grad_fn=<AddBackward0>)
``\
``
tensor([0.5577], grad_fn=<ViewBackward0>)
``

The output of the two models are DIFFERENT. But why? 
We have transposed the weight matrix, right? The reason is that the weight matrix of the Keras model 
is not in the same order as the PyTorch model even thought they share the same shape which cause the 
code to fail silently. To make sure the weight matrix is in the correct order after flattening, 
we need to make the matrix is in the order of channel last $(N, L, C)$ again before flattening! So the correct code of forward pass for PyTorch model should be,

```python
print(dense1_torch(torch.flatten(conv1d_torch(x_torch).permute(0, 2, 1))))
```

which gives the output,

``tensor([0.4469], grad_fn=<ViewBackward0>)``

Now both models share the same weight matrixes and produce the same output.