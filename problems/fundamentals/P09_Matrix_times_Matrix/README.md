# 🚀 Matrix × Matrix Multiplication

## 📌 Problem

Write a Python function to **multiply two matrices**.

Given two matrices **A** and **B**, compute:

C = A · B

👉 If the matrix dimensions are not compatible for multiplication, return `-1`.

---

## 🧠 Core Concept

Matrix multiplication is defined only when:

Number of columns in A = Number of rows in B

If:
- A is of size (m × n)
- B is of size (n × p)

Then:
- Result C will be of size (m × p)

---

## 📐 Mathematical Representation

For:

A = | a11  a12 |
    | a21  a22 |

B = | b11  b12 |
    | b21  b22 |

Multiplication:

A × B = | a11*b11 + a12*b21    a11*b12 + a12*b22 |
        | a21*b11 + a22*b21    a21*b12 + a22*b22 |

---

## 💡 Intuition

- Each element in result matrix = **dot product of row of A and column of B**
- Row × Column → single value
- Repeat for all combinations

---

## 🔍 Step-by-Step Algorithm

1. Get number of columns of A:
   ```
   len(A[0])
   ```

2. Get number of rows of B:
   ```
   len(B)
   ```

3. Check condition:
   ```
   if columns(A) != rows(B):
       return -1
   ```

4. Multiply matrices using:
   - Dot product logic OR
   - NumPy `@` operator

5. Return result matrix

---

## ⚙️ Python Implementation (Using NumPy)

```python
import numpy as np

def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:
    
    # Step 1: check dimension compatibility
    a_col = len(a[0])
    b_row = len(b)
    
    if a_col != b_row:
        return -1
    
    # Step 2: convert to numpy arrays
    a = np.array(a)
    b = np.array(b)
    
    # Step 3: matrix multiplication
    result = a @ b
    
    return result.tolist()
```

---

## ⚙️ Python Implementation (Without NumPy - Important for Interviews)

```python
def matrixmul(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        return -1

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result
```

---

## ▶️ Example 1

```python
A = [[1, 2],
     [2, 4]]

B = [[2, 1],
     [3, 4]]

print(matrixmul(A, B))
```

---

## 📊 Output

```
[[8, 9],
 [16, 18]]
```

---

## 🧠 Explanation

- First element:
  ```
  1×2 + 2×3 = 8
  ```

- Second element:
  ```
  1×1 + 2×4 = 9
  ```

- Third element:
  ```
  2×2 + 4×3 = 16
  ```

- Fourth element:
  ```
  2×1 + 4×4 = 18
  ```

---

## ▶️ Example 2 (Invalid Case)

```python
A = [[1, 2],
     [2, 4]]

B = [[2, 1],
     [3, 4],
     [4, 5]]

print(matrixmul(A, B))
```

---

## 📊 Output

```
-1
```

---

## ⚠️ Edge Cases

- Incompatible dimensions → return `-1`
- Empty matrices → handle separately (optional)
- Non-rectangular input → may cause error

---

## ❌ Common Mistakes

- Forgetting dimension check  
- Mixing row/column indices  
- Using `*` instead of `@` in NumPy  
- Incorrect loop order in manual implementation  

---

## 🔥 Key Insights

- Matrix multiplication is **not commutative**:
  ```
  A × B ≠ B × A
  ```
- Used in:
  - Machine Learning  
  - Computer Graphics  
  - Neural Networks  
  - Linear Transformations  

---

## 🧠 Interview Answer

“Matrix multiplication is performed by taking the dot product of rows of the first matrix with columns of the second matrix, and it is valid only when the number of columns of the first matrix equals the number of rows of the second.”

---

## 🔍 Keywords

- Matrix Multiplication  
- Dot Product  
- Linear Algebra  
- NumPy  
- Array Operations  

---

## 🏷️ Metadata

- Problem ID: 09
- Title: Matrix × Matrix  
- Difficulty: Medium  
- Topic: Linear Algebra  
- Platform: Deep-ML  

