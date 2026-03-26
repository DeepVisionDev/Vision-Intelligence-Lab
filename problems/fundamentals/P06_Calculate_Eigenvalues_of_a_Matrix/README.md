# 🚀 Calculate Eigenvalues of a 2×2 Matrix in Python

## 📌 Problem

Write a Python function that calculates the **eigenvalues of a 2×2 matrix**.

The function should:

* Take a 2×2 matrix (list of lists)
* Compute its eigenvalues
* Return them as a list
* Sort values from **highest to lowest**

---

## 🧠 Core Concept

👉 Eigenvalues are special values ( \lambda ) such that:

```
A · v = λ · v
```

Where:

* ( A ) = matrix
* ( v ) = eigenvector
* ( \lambda ) = eigenvalue

---

## 📐 Mathematical Representation

For a 2×2 matrix:

```
| a  b |
| c  d |
```

### Step 1: Compute trace and determinant

```
trace = a + d
det = ad - bc
```

---

### Step 2: Characteristic Equation

```
λ² - (trace)λ + det = 0
```

---

### Step 3: Solve quadratic equation

```
λ = [trace ± √(trace² - 4·det)] / 2
```

---

## 💡 Intuition

👉 Instead of solving manually:

* Convert problem into quadratic equation
* Solve using roots
* These roots = eigenvalues

---

## 🔍 Step-by-Step Logic

1. Extract matrix elements
2. Compute:

   * Trace = sum of diagonal
   * Determinant
3. Form quadratic equation
4. Solve using `np.roots()`
5. Sort eigenvalues (descending)
6. Return result as list

---

## ⚙️ Approach

* Use:

  ```python
  np.roots([1, -trace, det])
  ```
* Then:

  ```python
  sorted(eigenvalues, reverse=True)
  ```

---

## 💻 Python Implementation

```python
import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    
    # Step 1: compute trace
    trace = matrix[0][0] + matrix[1][1]
    
    # Step 2: compute determinant
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    # Step 3: solve quadratic equation
    eigenvalues = np.roots([1, -trace, det])
    
    # Step 4: sort descending and convert to float
    eigenvalues = sorted([float(val) for val in eigenvalues], reverse=True)
    
    return eigenvalues
```

---

## ▶️ Example

```python
matrix = [[2, 1],
          [1, 2]]

print(calculate_eigenvalues(matrix))
```

---

## 📊 Output

```python
[3.0, 1.0]
```

---

## 🔥 Key Insight (VERY IMPORTANT)

👉 Eigenvalues of 2×2 matrix always come from:

```
λ² - trace·λ + det = 0
```

👉 So problem reduces to solving a **quadratic equation**

---

## ⚠️ Common Mistakes

❌ Forgetting determinant formula
❌ Not sorting output
❌ Returning NumPy array instead of list
❌ Ignoring float conversion

---

## 🧠 Interview Answer (Perfect)

> “For a 2×2 matrix, eigenvalues are obtained by solving the characteristic equation λ² − trace(A)λ + det(A) = 0.”

---

## 🔍 Keywords

* Eigenvalues
* Characteristic Equation
* Trace
* Determinant
* Linear Algebra
* NumPy

---

## 🔗 Source

Problem: 06
Title : Calculate Eigenvalues of a Matrix
Level: Medium
Topic: Linear Algebra
Platform: Deep-ML
