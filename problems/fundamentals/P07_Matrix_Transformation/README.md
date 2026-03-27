# 🚀 Matrix Transformation using ( T^{-1} A S ) in Python

## 📌 Problem

Write a Python function that transforms a matrix ( A ) using the operation:

```
A' = T⁻¹ A S
```

The function should:

* Take matrices ( A ), ( T ), and ( S )
* Check if ( T ) and ( S ) are invertible
* Perform the transformation
* Return `-1` if transformation is not possible

---

## 🧠 Core Concept

👉 Matrix transformation:

```
A' = T⁻¹ A S
```

* ( T^{-1} ) → inverse of matrix ( T )
* ( S ) → transformation matrix
* Changes the **basis/representation** of matrix ( A )

---

## 📐 Mathematical Representation

For matrices:

```
A = | a  b |
    | c  d |

T = | p  q |
    | r  s |

S = | x  y |
    | z  w |
```

Transformation:

```
A' = T⁻¹ × A × S
```

---

## 💡 Intuition

👉 Think step-by-step:

1. First apply transformation using ( S )
2. Then adjust using inverse of ( T )
3. Final result = transformed matrix

👉 Important:

* If ( T ) or ( S ) is **not invertible**, transformation fails

---

## 🔍 Step-by-Step Logic

1. Convert inputs to matrices (NumPy arrays)
2. Compute determinants of ( T ) and ( S )
3. Check:

   ```
   det(T) ≠ 0 and det(S) ≠ 0
   ```
4. If not invertible → return `-1`
5. Compute inverse of ( T )
6. Perform multiplication:

   ```
   A' = T⁻¹ @ A @ S
   ```
7. Return result

---

## ⚙️ Approach

* Use:

  ```python
  np.linalg.det()
  np.linalg.inv()
  ```
* Matrix multiplication using:

  ```python
  @ operator
  ```

---

## 💻 Python Implementation

```python
import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    
    A = np.array(A)
    T = np.array(T)
    S = np.array(S)
    
    # Step 1: check invertibility
    detT = np.linalg.det(T)
    detS = np.linalg.det(S)
    
    if detT == 0 or detS == 0:
        return -1
    
    # Step 2: compute transformation
    transformed_matrix = np.linalg.inv(T) @ A @ S
    
    return transformed_matrix.tolist()
```

---

## ▶️ Example

```python
A = [[1, 2],
     [3, 4]]

T = [[2, 0],
     [0, 2]]

S = [[1, 1],
     [0, 1]]

print(transform_matrix(A, T, S))
```

---

## 📊 Output

```python
[[0.5, 1.5],
 [1.5, 3.5]]
```

---

## 🔥 Key Insight (VERY IMPORTANT)

👉 Transformation = **change of basis**

👉 Valid only if:

```
det(T) ≠ 0 and det(S) ≠ 0
```

👉 Otherwise matrix loses information → invalid

---

## ⚠️ Common Mistakes

❌ Forgetting to check invertibility
❌ Using `*` instead of `@` for matrix multiplication
❌ Not converting to list before returning
❌ Floating-point comparison (`det == 0`) → better use tolerance

---

## 🧠 Interview Answer (Perfect)

> “Matrix transformation ( T^{-1}AS ) changes the basis of matrix ( A ). It requires invertible matrices ( T ) and ( S ), and is computed using inverse and matrix multiplication.”

---

## 🔍 Keywords

* Matrix Transformation
* Change of Basis
* Matrix Inverse
* Determinant
* Linear Algebra
* NumPy

---

## 🔗 Source

Problem ID: 07
Title : Matrix Transformation
Level: Medium
Topic: Linear Algebra
Platform: Deep-ML
