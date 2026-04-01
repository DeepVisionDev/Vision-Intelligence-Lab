# 🚀 Singular Value Decomposition (SVD) of 2×2 Matrix

## 📌 Problem

Write a Python function that computes an **approximate Singular Value Decomposition (SVD)** of a real 2×2 matrix using **one Jacobi rotation**.

### Input
- A: NumPy array of shape (2, 2)

### Output
Return a tuple:
```
(U, S, Vt)
```

Where:
- **U** → 2×2 orthogonal matrix (left singular vectors)  
- **S** → array of 2 singular values  
- **Vt** → transpose of right singular vectors  

👉 The decomposition should satisfy:

\[
A \approx U \cdot \text{diag}(S) \cdot V^T
\]

---

## 🧠 Core Concept

Singular Value Decomposition (SVD) factorizes a matrix into:

\[
A = U \Sigma V^T
\]

- \( U \) → orthogonal matrix (left singular vectors)  
- \( \Sigma \) → diagonal matrix (singular values)  
- \( V \) → orthogonal matrix (right singular vectors)  

---

## 📐 Key Idea (2×2 Case)

For a **2×2 matrix**, SVD can be computed efficiently using:

👉 One **Jacobi rotation** on:

\[
A^T A
\]

- Eigenvectors of \( A^T A \) → columns of \( V \)  
- Eigenvalues → squares of singular values  

---

## 🔍 Step-by-Step Approach

### 1. Compute Symmetric Matrix

\[
B = A^T A
\]

---

### 2. Apply Jacobi Rotation

Use rotation matrix:

\[
R(\theta) =
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
\]

Choose angle:

- If \( B_{11} = B_{22} \) → \( \theta = \frac{\pi}{4} \)  
- Else:
\[
\theta = \frac{1}{2} \tan^{-1}\left(\frac{2B_{12}}{B_{11} - B_{22}}\right)
\]

---

### 3. Diagonalize Matrix

\[
D = R^T B R
\]

👉 Diagonal elements = eigenvalues

---

### 4. Compute Singular Values

\[
\sigma_i = \sqrt{\lambda_i}
\]

---

### 5. Compute Matrices

- \( V = R \)  
- \( U = A V \Sigma^{-1} \)  
- \( V^T = V^\top \)

---

## 💡 Intuition

- SVD decomposes transformation into:
  1. Rotation (V)
  2. Scaling (Σ)
  3. Rotation (U)

- Jacobi rotation helps **remove correlation** (off-diagonal terms)

---

## ▶️ Example

### Input

```python
A = [[2, 1],
     [1, 2]]
```

---

### Output (Approx)

```python
U ≈ [[ 0.707, -0.707],
     [ 0.707,  0.707]]

S = [3.0, 1.0]

Vt ≈ [[ 0.707,  0.707],
      [-0.707,  0.707]]
```

---

## 🧠 Explanation

- Matrix is symmetric → eigen decomposition simplifies SVD  
- Eigenvalues = 3, 1  
- Singular values = √eigenvalues = 3, 1  
- Orthogonal vectors form U and V  

---

## ⚠️ Constraints & Rules

- ❌ Do NOT use `numpy.linalg.svd()`  
- ✅ Use only basic NumPy operations  
- ✅ Perform only **one Jacobi rotation**  
- ✅ Handle near-zero singular values carefully  

---

## ⚠️ Edge Cases

- Singular values ≈ 0 → avoid division by zero  
- Sign ambiguity in U and V (both ± valid)  
- Non-symmetric matrices → still valid process  

---

## ❌ Common Mistakes

- Using built-in SVD (not allowed ❌)  
- Forgetting transpose in \( A^T A \)  
- Incorrect angle calculation  
- Not normalizing vectors in U  

---

## 🔥 Key Insights

- SVD works for **any matrix** (square or rectangular)  
- For 2×2 → single Jacobi rotation is sufficient  
- Widely used in:
  - PCA  
  - Image compression  
  - Recommendation systems  

---

## 🧠 Interview Answer

> “SVD decomposes a matrix into orthogonal rotations and scaling. For a 2×2 matrix, we can compute it efficiently by diagonalizing \( A^T A \) using a single Jacobi rotation.”

---

## 🔍 Keywords

- Singular Value Decomposition  
- Jacobi Rotation  
- Eigenvalues  
- Orthogonal Matrix  
- Linear Algebra  

---

## 🏷️ Metadata

- **Problem ID:** 12
- **Title:** Singular Value Decomposition (SVD) of 2×2 Matrix  
- **Difficulty:** Hard  
- **Topic:** Linear Algebra  
- **Platform:** Deep-ML  

