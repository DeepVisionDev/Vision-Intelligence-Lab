# 🚀 Linear Regression Using Gradient Descent

## 📌 Problem

Write a Python function that performs **Linear Regression** using **Gradient Descent**.

### Input
- `X`: NumPy array of shape (m, n) → features (including column of ones for intercept)
- `y`: NumPy array of shape (m,) → target values  
- `alpha`: Learning rate  
- `iterations`: Number of iterations  

### Output
- Learned weights (θ) as a NumPy array

---

## 🧠 Core Concept

Linear regression models:

\[
h_\theta(x) = X\theta
\]

We minimize the **Mean Squared Error (MSE)**:

\[
L(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2
\]

---

## 📐 Gradient Formula

\[
\nabla L = \frac{1}{m} X^T (X\theta - y)
\]

---

## 🔄 Update Rule

\[
\theta := \theta - \alpha \cdot \frac{1}{m} X^T (X\theta - y)
\]

---

## 🔍 Step-by-Step Approach

1. Initialize weights:
   ```
   θ = 0
   ```

2. Repeat for given iterations:
   - Compute predictions:
     ```
     ŷ = Xθ
     ```
   - Compute error:
     ```
     e = ŷ - y
     ```
   - Compute gradient:
     ```
     g = (1/m) Xᵀe
     ```
   - Update weights:
     ```
     θ = θ - αg
     ```

3. Return final θ

---

## 💡 Intuition

- Move weights in direction that **reduces error fastest**  
- Step size controlled by **learning rate (α)**  
- Iteratively improves model  

---

## ▶️ Example

### Input

```python
X = np.array([[1, 1],
              [1, 2],
              [1, 3]])

y = np.array([3, 5, 7])

alpha = 0.1
iterations = 1000
```

---

### Output

```python
[1.0, 2.0]
```

---

## 🧠 Explanation

- Model learned:
\[
y = 1 + 2x
\]

- Gradient descent converges from `[0, 0]` → `[1, 2]`

---

## ⚠️ Important Notes

- X **must include bias column (ones)**  
- Weights initialized to zero  
- Uses **batch gradient descent**  

---

## ⚠️ Edge Cases

- Very large α → divergence  
- Very small α → slow convergence  
- Poorly scaled data → unstable training  

---

## ❌ Common Mistakes

- Forgetting bias column  
- Wrong matrix multiplication  
- Not reshaping y  
- Incorrect gradient formula  

---

## 🔥 Key Insights

- Works well for **large datasets**  
- No matrix inversion needed  
- More flexible than normal equation  

---

## 🧠 Interview Answer

> “Gradient descent iteratively updates weights by moving in the direction of the negative gradient of the loss function to minimize prediction error.”

---

## 🔍 Keywords

- Gradient Descent  
- Linear Regression  
- Optimization  
- Machine Learning  

---

## 🏷️ Metadata

- **Problem ID:** 14  
- **Title:** Linear Regression Using Gradient Descent  
- **Difficulty:** Easy  
- **Topic:** Machine Learning  
- **Platform:** Deep-ML  
