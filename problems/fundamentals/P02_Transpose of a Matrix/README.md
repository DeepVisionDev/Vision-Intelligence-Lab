# 🚀 Transpose of a Matrix in Python

## 📌 Problem
Write a Python function that computes the transpose of a given 2D matrix.

The function should:
- Return the transposed matrix  
- Swap rows into columns and columns into rows  

---

## 🧠 Concept

The transpose of a matrix converts:
- Rows → Columns  
- Columns → Rows  

For a matrix of size **m × n**, the transpose will be **n × m**

---

## 📐 Mathematical Representation

If:

A = matrix of size (m × n)

Then:

Aᵀ[i][j] = A[j][i]

---

## 💡 Intuition

- Take elements column-wise  
- Convert them into rows  
- Repeat for all columns  

👉 You are basically **flipping the matrix over its diagonal**

---

## ⚙️ Approach

1. Find number of rows `m` and columns `n`
2. Create a new matrix of size `(n × m)`
3. Traverse through each element
4. Swap indices: a[i][j]=a[j][i]
5. Return the result matrix

---

## 💻 Python Implementation

```python
def transpose_matrix(a):
 """
 Transpose a 2D matrix by swapping rows and columns.

 Args:
     a: A 2D matrix of shape (m, n)

 Returns:
     The transposed matrix of shape (n, m)
 """

 # calculate number of rows and columns
 m = len(a)
 n = len(a[0])

 # create result matrix of size (n x m)
 res = [[0 for _ in range(m)] for _ in range(n)]

 # swap indices
 for i in range(n):
     for j in range(m):
         res[i][j] = a[j][i]

 return res
```
