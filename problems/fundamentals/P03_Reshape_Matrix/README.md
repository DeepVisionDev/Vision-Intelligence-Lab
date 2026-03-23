# 🚀 Reshape Matrix in Python

## 📌 Problem

Write a Python function that reshapes a given matrix into a specified shape.

The function should:

* Return the reshaped matrix
* Return an empty list `[]` if reshaping is not possible

---

## 🧠 Core Concept

Reshaping a matrix means:

* **Changing the structure (shape)**
* **Keeping the data and order SAME**

For a matrix of size **m × n**, it can be reshaped to **r × c** only if:

```
m × n = r × c
```

---

## 📐 Mathematical Representation

If:

* Original matrix `A` has shape `(m × n)`
* New matrix `B` has shape `(r × c)`

Then reshape is possible only if:

```
m * n = r * c
```

---

## 💡 Intuition (Very Important)

👉 Reshape works in **two steps**:

### 1. Flatten the matrix (row-wise)

Convert 2D → 1D

```
1  2  3  4
5  6  7  8
↓
[1,2,3,4,5,6,7,8]
```

---

### 2. Rebuild into new shape

Group elements according to new columns:

```
[1,2]
[3,4]
[5,6]
[7,8]
```

👉 **Data order NEVER changes — only grouping changes**

---

## 🔍 Step-by-Step Logic

1. Calculate total elements in original matrix
2. Check if reshape is possible
3. Flatten matrix row-wise
4. Build new matrix using slicing
5. Return reshaped matrix

---

## ⚙️ Approach

1. Get rows `m` and columns `n`
2. Check:

   ```python
   if m * n != r * c:
       return []
   ```
3. Flatten matrix:

   ```python
   flat = [num for row in a for num in row]
   ```
4. Create new matrix:

   ```python
   row = flat[i*c : (i+1)*c]
   ```
5. Return result

---

## 💻 Python Implementation

```python
def reshape_matrix(a, new_shape):
    """
    Reshape a 2D matrix without changing data order.
    """

    m = len(a)
    n = len(a[0])
    r, c = new_shape

    # Step 1: check if possible
    if m * n != r * c:
        return []

    # Step 2: flatten
    flat = [num for row in a for num in row]

    # Step 3: rebuild
    res = []
    for i in range(r):
        row = flat[i*c : (i+1)*c]
        res.append(row)

    return res
```

---

## ▶️ Example

```python
a = [[1,2,3,4],
     [5,6,7,8]]

print(reshape_matrix(a, (4,2)))
```

---

## 📊 Output

```python
[[1, 2],
 [3, 4],
 [5, 6],
 [7, 8]]
```

---

## 🔥 Key Insight (VERY IMPORTANT)

👉 Reshape = **Flatten + Rebuild**

```
2D → 1D → new 2D
```

---

## ⚠️ Common Mistakes

❌ Changing order of elements
❌ Confusing reshape with transpose

| Operation | Meaning             |
| --------- | ------------------- |
| Transpose | swap rows & columns |
| Reshape   | regroup elements    |

---

## 🧠 Interview Answer (Perfect)

> “Flatten the matrix row-wise and then rebuild it into the desired shape while preserving the order of elements.”

---

## 🔍 Keywords

* Matrix Reshape
* Linear Algebra
* Python
* 2D Arrays
* Flattening

---

## 🔗 Source

Problem ID: 03
Title: Reshape Matrix
Platform: Deep-ML

