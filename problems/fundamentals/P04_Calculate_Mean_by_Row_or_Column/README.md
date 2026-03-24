# 🚀 Calculate Mean by Row or Column in Python

## 📌 Problem

Write a Python function that calculates the **mean of a matrix** either by **row** or by **column**, based on a given mode.

The function should:

* Take a matrix (list of lists)
* Take a mode: `'row'` or `'column'`
* Return a list of mean values

---

## 🧠 Core Concept

👉 Mean (average) is defined as:

```
Mean = (sum of elements) / (number of elements)
```

---

## 📐 Mathematical Representation

For a matrix ( A ) of size ( m \times n ):

### 🔹 Row-wise mean:

```
mean_row_i = (A[i][0] + A[i][1] + ... + A[i][n-1]) / n
```

### 🔹 Column-wise mean:

```
mean_col_j = (A[0][j] + A[1][j] + ... + A[m-1][j]) / m
```

---

## 💡 Intuition

👉 Think like this:

### Row Mean:

* Take one row
* Add all elements
* Divide by number of columns

### Column Mean:

* Take one column
* Add all elements
* Divide by number of rows

---

## 🔍 Step-by-Step Logic

1. Convert matrix into array (optional, for easy slicing)
2. Find number of rows and columns
3. Check mode:

   * If `'row'` → compute mean of each row
   * If `'column'` → compute mean of each column
4. Return the list of means

---

## ⚙️ Approach

### For Column Mean:

* Fix column index `i`
* Take all elements: `matrix[:, i]`
* Divide sum by number of rows

### For Row Mean:

* Fix row index `i`
* Take all elements: `matrix[i, :]`
* Divide sum by number of columns

---

## 💻 Python Implementation

```python
import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    
    # convert matrix to numpy array
    matrix = np.array(matrix)
    
    # get shape
    row, col = matrix.shape
    
    # check mode
    if mode == 'column':
        means = [np.sum(matrix[:, i]) / row for i in range(col)]
    else:
        means = [np.sum(matrix[i, :]) / col for i in range(row)]
    
    return means
```

---

## ▶️ Example

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(calculate_matrix_mean(matrix, 'column'))
```

---

## 📊 Output

```python
[4.0, 5.0, 6.0]
```

---

## 🔥 Key Insight (VERY IMPORTANT)

👉 Column mean → operate **vertically**
👉 Row mean → operate **horizontally**

---

## ⚠️ Common Mistakes

❌ Dividing by wrong dimension
❌ Mixing row and column indexing
❌ Forgetting to convert to float

---

## 🧠 Interview Answer (Perfect)

> “To compute the mean, we sum elements along the required axis (row or column) and divide by the number of elements in that axis.”

---

## 🔍 Keywords

* Matrix Mean
* Row-wise Mean
* Column-wise Mean
* Linear Algebra
* NumPy

---

## 🔗 Source

Problem ID: 03
Title :Calculate Mean by Row or Column
Level: Easy
Topic: Linear Algebra
Platform: Deep-ML
