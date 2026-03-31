# 🚀 Solve Linear Equations using Jacobi Method

## 📌 Problem

Write a Python function that solves a system of linear equations:

Ax = b

using the **Jacobi Iterative Method**.

- Perform the iteration **n times**
- Initialize solution vector **x = [0, 0, ..., 0]**
- Round each intermediate value to **4 decimal places**
- Return the final approximate solution

---

## 🧠 Core Concept

The **Jacobi Method** is an **iterative technique** used to solve systems of linear equations.

Instead of solving directly, it **approximates the solution step by step**.

Each variable is updated using values from the **previous iteration only**.

---

## 📐 Jacobi Formula

For each variable:

x[i] = (1 / a[i][i]) * ( b[i] - Σ(a[i][j] * x[j]) ), where j ≠ i

---

## 💡 Intuition

- Solve each equation for one variable  
- Use **old values** of other variables  
- Update all variables simultaneously  
- Repeat until convergence (or fixed iterations)

---

## 🔍 Step-by-Step Algorithm

1. Initialize:
   ```
   x = [0, 0, ..., 0]
   ```

2. Repeat for n iterations:
   - For each variable i:
     ```
     x[i] = (b[i] - sum(a[i][j]*x[j])) / a[i][i]
     ```
     (j ≠ i)

3. Round each value to 4 decimal places  

4. Update solution vector  

5. Return final x  

---

## ▶️ Example

### Input

```python
A = [[5, -2, 3],
     [-3, 9, 1],
     [2, -1, -7]]

b = [-1, 2, 3]

n = 2
```

---

### Output

```python
[0.146, 0.2032, -0.5175]
```

---

## 🧠 Explanation

- Start with:
  ```
  x = [0, 0, 0]
  ```

- Iteration 1 → compute new values  
- Iteration 2 → refine values  

👉 After 2 iterations, approximate solution becomes:

```
[0.146, 0.2032, -0.5175]
```

---

## ⚠️ Important Conditions

- All diagonal elements must be **non-zero**
- Matrix should be **diagonally dominant** for convergence

---

## 📊 Convergence Insight

Jacobi method converges when:

|a[i][i]| > sum of |a[i][j]| (for j ≠ i)

👉 This is called **diagonal dominance**

---

## ⚠️ Edge Cases

- Zero diagonal element → division error  
- Non-converging matrix → inaccurate result  
- Large n → better approximation  

---

## ❌ Common Mistakes

- Using updated values in same iteration (that’s Gauss-Seidel ❌)  
- Not initializing with zeros  
- Forgetting rounding  
- Division by zero (a[i][i] = 0)  

---

## 🔥 Key Insights

- Iterative method → useful for **large systems**  
- Memory efficient compared to direct methods  
- Parallelizable (important in computing)

---

## 🧠 Interview Answer

> “The Jacobi method iteratively solves each equation by isolating variables and updating them using values from the previous iteration, making it suitable for large systems when convergence conditions are satisfied.”

---

## 🔍 Keywords

- Jacobi Method  
- Iterative Method  
- Linear Equations  
- Convergence  
- Diagonal Dominance  

---

## 🏷️ Metadata

- **Problem ID:** 11 
- **Title:** Solve Linear Equations using Jacobi Method  
- **Difficulty:** Medium  
- **Topic:** Linear Algebra  
- **Platform:** Deep-ML  

