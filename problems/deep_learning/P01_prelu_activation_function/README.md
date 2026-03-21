# PReLU Activation Function in Python (Parametric ReLU)

## 📌 Problem
Implement the PReLU (Parametric ReLU) activation function.

## 🧠 What is PReLU?

PReLU is an extension of the ReLU activation function used in deep learning.  
Instead of making all negative values zero, it allows a small slope for negative inputs.

## 📐 Formula

f(x) = x        if x > 0  
f(x) = αx       if x ≤ 0  

Where:
- α is a learnable parameter

## 💡 Intuition

ReLU can suffer from the "dead neuron problem" where neurons stop learning.  
PReLU solves this by allowing a small gradient when input is negative.

## 💻 Python Implementation

```python
import numpy as np

def prelu(x, alpha=0.1):
    x = np.array(x)
    return np.where(x > 0, x, alpha * x)
