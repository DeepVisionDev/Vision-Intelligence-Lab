# 🚀 Matrix-Vector Dot Product in Python

## 📌 Problem
Write a Python function that computes the dot product of a matrix and a vector.

The function should:
- Return the resulting vector if dimensions are valid  
- Return `-1` if dimensions are incompatible  

---

## 🧠 Concept

A matrix-vector dot product multiplies each row of the matrix with the vector.

For a matrix of size **n × m**, the vector must have length **m**.

---

## 📐 Mathematical Representation

If:

A = n × m matrix  
b = vector of length m  

Then:

Result[i] = Σ (A[i][j] * b[j])

---

## 💡 Intuition

- Take one row of matrix  
- Multiply with vector  
- Sum the result  
- Repeat for all rows  

---

## 💻 Python Implementation

```python
def matrix_vector_dot(a, b):
    # Check dimension compatibility
    if len(a[0]) != len(b):
        return -1

    result = []
    for row in a:
        dot = 0
        for i in range(len(b)):
            dot += row[i] * b[i]
        result.append(dot)

    return result
```

