# 🚀 Calculate Covariance Matrix

## 📌 Problem

Write a Python function to calculate the **covariance matrix** for a given set of vectors.

- Input: A list of lists, where each inner list represents a **feature** with its observations  
- Output: A covariance matrix (list of lists)

👉 Return the covariance matrix representing relationships between features.

---

## 🧠 Core Concept

The **covariance matrix** measures how multiple variables (features) vary together.

- If two variables increase together → **positive covariance**
- If one increases while the other decreases → **negative covariance**
- If independent → covariance ≈ 0

---

## 📐 Covariance Formula

For two variables \( X \) and \( Y \):

\[
cov(X, Y) = \frac{\sum_{k=1}^{m} (X_k - \bar{X})(Y_k - \bar{Y})}{m - 1}
\]

Where:
- \( X_k, Y_k \) → observations  
- \( \bar{X}, \bar{Y} \) → means  
- \( m \) → number of observations  

---

## 📊 Covariance Matrix Structure

For **n features**, covariance matrix is:

\[
\begin{bmatrix}
cov(X_1,X_1) & cov(X_1,X_2) & \cdots & cov(X_1,X_n) \\
cov(X_2,X_1) & cov(X_2,X_2) & \cdots & cov(X_2,X_n) \\
\vdots & \vdots & \ddots & \vdots \\
cov(X_n,X_1) & cov(X_n,X_2) & \cdots & cov(X_n,X_n)
\end{bmatrix}
\]

👉 Diagonal elements = **variance**  
👉 Matrix is always **symmetric**

---

## 💡 Intuition

- Measures **relationship between features**
- Helps understand:
  - How features move together
  - Data spread and direction
- Foundation for **PCA and ML models**

---

## 🔍 Step-by-Step Approach

1. Compute mean of each feature  
2. Subtract mean from each observation  
3. Multiply deviations pairwise  
4. Sum and divide by (m - 1)  
5. Fill covariance matrix  

---

## ▶️ Example

### Input

```python
[[1, 2, 3],
 [4, 5, 6]]
```

---

### Output

```python
[[1.0, 1.0],
 [1.0, 1.0]]
```

---

## 🧠 Explanation

- Means:
  - Feature 1 → 2.0  
  - Feature 2 → 5.0  

- Covariance:
  - cov(X₁, X₁) = 1.0  
  - cov(X₁, X₂) = 1.0  
  - cov(X₂, X₂) = 1.0  

👉 Final matrix:

```
[1.0  1.0
 1.0  1.0]
```

---

## ⚠️ Edge Cases

- Single observation → division by zero  
- Unequal vector lengths → invalid input  
- Empty input → handle separately  

---

## ❌ Common Mistakes

- Dividing by `m` instead of `(m - 1)`  
- Forgetting to subtract mean  
- Not using symmetric property  
- Mixing rows vs features  

---

## 🔥 Key Insights

- Covariance matrix is always:
  - **Square**
  - **Symmetric**
- Diagonal = variance  
- Used to detect **feature relationships**

---

## 🧠 Interview Answer

> “The covariance matrix captures pairwise relationships between features by measuring how their deviations from the mean vary together.”

---

## 🔍 Keywords

- Covariance  
- Variance  
- Covariance Matrix  
- Statistics  
- Machine Learning  

---

## 🏷️ Metadata

- **Problem ID:** 09  
- **Title:** Calculate Covariance Matrix  
- **Difficulty:** Easy  
- **Topic:** Statistics  
- **Platform:** Deep-ML  
