# 🚀 Scalar Multiplication of a Matrix in Python

## 📌 Problem

Write a Python function that multiplies a matrix by a scalar and returns the result.

The function should:

* Take a matrix (list of lists)
* Take a scalar value
* Multiply each element of the matrix by the scalar
* Return the resulting matrix

---

## 🧠 Core Concept

👉 Scalar multiplication means:

```
Each element of the matrix × scalar
```

---

## 📐 Mathematical Representation

For a matrix ( A ) and scalar ( k ):

```
B[i][j] = A[i][j] × k
```

---

## 💡 Intuition

👉 Think like this:

* Go through each row
* Go through each element in that row
* Multiply it by the scalar

---

## 🔍 Step-by-Step Logic

1. Traverse each row of the matrix
2. Traverse each element in that row
3. Multiply element by scalar
4. Store updated value
5. Return the modified matrix

---

## ⚙️ Approach

* Use two loops:

  * Outer loop → rows
  * Inner loop → columns
* Update each element using:

  ```python
  matrix[i][j] *= scalar
  ```

---

## 💻 Python Implementation

```python
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    
    result = matrix
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] *= scalar
    
    return result
```

---

## ▶️ Example

```python
matrix = [[1, 2],
          [3, 4]]

print(scalar_multiply(matrix, 2))
```

---

## 📊 Output

```python
[[2, 4],
 [6, 8]]
```

---

## 🔥 Key Insight (VERY IMPORTANT)

👉 Operation is applied **element-wise**
👉 Structure of matrix does NOT change

---

## ⚠️ Common Mistakes

❌ Forgetting nested loops
❌ Changing structure instead of values
❌ Not returning updated matrix

---

## 🧠 Interview Answer (Perfect)

> “Scalar multiplication is performed by multiplying each element of the matrix individually by the scalar value.”

---

## 🔍 Keywords

* Scalar Multiplication
* Matrix Operations
* Linear Algebra
* Python
* 2D Arrays

---

## 🔗 Source

Problem ID: 05 
Title : Scalar Multiplication of a Matrix
Level: Easy
Topic: Linear Algebra
Platform: Deep-ML

