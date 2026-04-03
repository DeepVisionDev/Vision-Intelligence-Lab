# 🚀 Linear Regression Using Normal Equation

## 📌 Problem

Write a Python function that performs **Linear Regression** using the **Normal Equation**.

### Input
- `X`: Feature matrix (list of lists)
- `y`: Target vector (list)

### Output
- Coefficients (θ) as a list rounded to **4 decimal places**

---

## 🧠 Core Concept

Linear Regression models the relationship between input features and output:

\[
y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + ...
\]

The **Normal Equation** gives a direct mathematical solution:

\[
\theta = (X^T X)^{-1} X^T y
\]

---

## 📐 Explanation of Terms

- \( X \): Feature matrix  
- \( X^T \): Transpose of matrix  
- \( (X^T X)^{-1} \): Inverse matrix  
- \( y \): Target vector  
- \( \theta \): Model coefficients  

---

## 🔍 Step-by-Step Approach

1. Convert input to NumPy arrays  
2. Compute transpose:
   ```
   X^T
   ```
3. Compute:
   ```
   X^T X
   ```
4. Take inverse:
   ```
   (X^T X)^-1
   ```
5. Multiply:
   ```
   θ = (X^T X)^-1 X^T y
   ```
6. Round result to **4 decimal places**

---

## 💡 Intuition

- Finds best-fit line by minimizing squared error  
- No iteration needed (unlike gradient descent)  
- Works well for **small to medium datasets**

---

## ▶️ Example

### Input

```python
X = [[1, 1],
     [1, 2],
     [1, 3]]

y = [1, 2, 3]
```

---

### Output

```python
[0.0, 1.0]
```

---

## 🧠 Explanation

- Model:  
  \[
  y = 0.0 + 1.0x
  \]

- Perfect linear relationship → exact fit

---

## ⚠️ Important Notes

- First column of X should be **1s** (for intercept)  
- No need for:
  - Learning rate  
  - Iterations  

---

## ⚠️ Edge Cases

- Singular matrix → inverse not possible  
- Large feature set → expensive computation  
- Floating precision issues  

---

## ❌ Common Mistakes

- Forgetting transpose  
- Not adding bias column  
- Incorrect matrix multiplication order  
- Not rounding output  

---

## 🔥 Key Insights

- Closed-form solution (direct answer)  
- Faster for small datasets  
- Slower for high dimensions  

---

## 🧠 Interview Answer

> “Linear regression using the normal equation computes optimal parameters directly using matrix operations without iterative optimization.”

---

## 🔍 Keywords

- Linear Regression  
- Normal Equation  
- Matrix Inverse  
- Machine Learning  

---

## 🏷️ Metadata

- **Problem ID:** 14  
- **Title:** Linear Regression Using Normal Equation  
- **Difficulty:** Easy  
- **Topic:** Machine Learning  
- **Platform:** Deep-ML  
