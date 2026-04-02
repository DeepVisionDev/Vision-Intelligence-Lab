# 🚀 Determinant of a 4×4 Matrix using Laplace's Expansion

## 📌 Problem

Write a Python function to calculate the **determinant of a 4×4 matrix** using **Laplace’s Expansion (Cofactor Expansion)**.

- Input: A 4×4 matrix (list of lists)
- Output: Determinant (float or integer)

👉 The computation must be done **recursively** by reducing the matrix into smaller minors.

---

## 🧠 Core Concept

The **determinant** is a scalar value that represents:

- Scaling factor of transformation  
- Whether matrix is invertible  
- Volume transformation in space  

For larger matrices (like 4×4), we compute it using **Laplace Expansion**.

---

## 📐 Laplace Expansion Formula

Expanding along the first row:

\[
\det(A) = a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13} - a_{14}M_{14}
\]

Where:
- \( M_{ij} \) = minor (determinant of submatrix)
- Signs follow **alternating pattern**

---

## ➕➖ Sign Pattern (Cofactor Matrix)

\[
\begin{bmatrix}
+ & - & + & - \\
- & + & - & + \\
+ & - & + & - \\
- & + & - & +
\end{bmatrix}
\]

---

## 🔍 Key Definitions

### 🔹 Minor (Mᵢⱼ)
Matrix formed by removing row *i* and column *j*

### 🔹 Cofactor (Cᵢⱼ)

\[
C_{ij} = (-1)^{i+j} M_{ij}
\]

---

## 🔍 Step-by-Step Approach

1. Select a row (commonly first row)

2. For each element:
   - Remove its row and column → form minor (3×3 matrix)

3. Recursively compute determinant of minor

4. Multiply with:
   - Matrix element  
   - Sign factor  

5. Sum all values

---

## 🔁 Recursive Breakdown

4×4 determinant → 3×3 determinants  
3×3 determinant → 2×2 determinants  

👉 Base case:

\[
\det
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
= ad - bc
\]

---

## 💡 Intuition

- Break big matrix into smaller ones  
- Combine results with alternating signs  
- Like a **divide-and-conquer approach**

---

## ▶️ Example

### Input

```python
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
```

---

### Output

```python
0
```

---

## 🧠 Explanation

- Rows are linearly dependent  
- Matrix does not span full space  
- Determinant becomes **zero**

---

## ⚠️ Important Observations

- If determinant = 0 → matrix is **singular**  
- If determinant ≠ 0 → matrix is **invertible**  

---

## ⚠️ Edge Cases

- Non 4×4 matrix → invalid input  
- Floating-point precision issues  
- Large values → computationally expensive  

---

## ❌ Common Mistakes

- Incorrect sign handling  
- Wrong minor matrix construction  
- Forgetting recursion  
- Mixing row/column indices  

---

## 🔥 Key Insights

- Laplace expansion is:
  - Simple conceptually  
  - Expensive computationally (O(n!))  

- Best used for:
  - Small matrices  
  - Theoretical understanding  

---

## 🧠 Interview Answer

> “The determinant of a 4×4 matrix can be computed using Laplace expansion by recursively breaking it into 3×3 minors and applying alternating cofactor signs.”

---

## 🔍 Keywords

- Determinant  
- Laplace Expansion  
- Cofactor  
- Minor Matrix  
- Recursion  

---

## 🏷️ Metadata

- **Problem ID:** 13  
- **Title:** Determinant of a 4×4 Matrix using Laplace's Expansion  
- **Difficulty:** Hard  
- **Topic:** Linear Algebra  
- **Platform:** Deep-ML  
