# 🚀 Calculate 2×2 Matrix Inverse

## 📌 Problem

Write a Python function that calculates the **inverse of a 2×2 matrix**.

The inverse of a matrix A is another matrix A⁻¹ such that:

A · A⁻¹ = I

where I is the identity matrix.

---

## 🧠 Core Concept

For a 2×2 matrix:

A = | a  b |
    | c  d |

The inverse is:

A⁻¹ = (1 / (ad - bc)) × |  d  -b |
                           | -c   a |

---

## 📐 Key Condition (IMPORTANT)

The matrix is invertible only if:

det(A) = ad - bc ≠ 0

- If determinant = 0 → Not invertible (singular matrix)  
- If determinant ≠ 0 → Invertible  

---

## 💡 Intuition

- Determinant represents scaling factor of transformation  
- If determinant = 0 → transformation collapses space  
- Inverse reverses the transformation  

---

## 🔍 Step-by-Step Algorithm

1. Extract elements a, b, c, d  
2. Compute determinant:
   det = a*d - b*c  
3. Check:
   if det == 0 → return None  
4. Apply formula:
   (1/det) × [[d, -b], [-c, a]]  
5. Return result  

---

## ⚙️ Python Implementation

```python
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
    """
    
    # Extract elements
    a, b = matrix[0]
    c, d = matrix[1]
    
    # Step 1: determinant
    det = a * d - b * c
    
    # Step 2: check invertibility
    if det == 0:
        return None
    
    # Step 3: compute inverse
    inverse = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]
    
    return inverse
```

---

## ▶️ Example

```python
matrix = [[4, 7],
          [2, 6]]

print(inverse_2x2(matrix))
```

---

## 📊 Output

```
[[0.6, -0.7],
 [-0.2, 0.4]]
```

---

## 🧠 Example Explanation

For matrix:

[[4, 7],
 [2, 6]]

Determinant:
det = (4×6) - (7×2) = 24 - 14 = 10

Apply formula:
(1/10) × [[6, -7], [-2, 4]]

Result:
[[0.6, -0.7], [-0.2, 0.4]]

---

## ⚠️ Edge Cases

- Determinant = 0 → return None  
- Non 2×2 matrix → optional validation  
- Floating precision issues  

---

## ❌ Common Mistakes

- Returning 'None' instead of None  
- Forgetting determinant check  
- Swapping values incorrectly  
- Using integer division  

---

## 🔥 Key Insights

- Inverse exists only for non-singular matrices  
- Based on adjoint method  
- Used in linear equations and transformations  

---

## 🧠 Interview Answer

“The inverse of a 2×2 matrix is computed using the adjoint divided by the determinant, and it exists only when the determinant is non-zero.”

---

## 🔍 Keywords

- Matrix Inverse  
- Determinant  
- Linear Algebra  
- Singular Matrix  
- Identity Matrix  

---

## 🏷️ Metadata

- Problem ID: 08 
- Title: Calculate 2×2 Matrix Inverse  
- Difficulty: Easy  
- Topic: Linear Algebra  
- Platform: Deep-ML  
