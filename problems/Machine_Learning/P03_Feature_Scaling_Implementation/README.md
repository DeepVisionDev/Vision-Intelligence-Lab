# 🚀 Feature Scaling Implementation

## 📌 Problem

Write a Python function that performs **feature scaling** on a dataset using:

- **Standardization (Z-score normalization)**
- **Min-Max Normalization**

### Input
- `data`: 2D NumPy array of shape (m, n)  
  - m → number of samples  
  - n → number of features  

### Output
- Tuple of two NumPy arrays:
  1. Standardized data  
  2. Min-Max normalized data  

👉 All values must be **rounded to 4 decimal places**

---

## 🧠 Core Concept

Feature scaling ensures that all features contribute **equally** to model training.

It is especially important for:
- Gradient Descent  
- KNN  
- SVM  
- Neural Networks  

---

## 📐 Standardization (Z-score)

Rescales data to have:
- Mean = 0  
- Standard deviation = 1  

\[
z = \frac{x - \mu}{\sigma}
\]

Where:
- \( x \) → original value  
- \( \mu \) → mean  
- \( \sigma \) → standard deviation  

---

## 📐 Min-Max Normalization

Rescales data to range **[0, 1]**:

\[
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
\]

Where:
- \( x_{min} \) → minimum value  
- \( x_{max} \) → maximum value  

---

## 🔍 Step-by-Step Approach

### 🔹 Standardization

1. Compute mean of each column  
2. Compute standard deviation  
3. Apply formula:
   ```
   (data - mean) / std
   ```
4. Round to 4 decimals  

---

### 🔹 Min-Max Normalization

1. Compute min and max of each column  
2. Apply formula:
   ```
   (data - min) / (max - min)
   ```
3. Round to 4 decimals  

---

## 💡 Intuition

- Standardization → centers data around zero  
- Min-Max → scales data into fixed range  

👉 Both help algorithms converge faster and perform better  

---

## ▶️ Example

### Input

```python
data = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])
```

---

### Output

```python
Standardized:
[[-1.2247, -1.2247],
 [ 0.0,     0.0   ],
 [ 1.2247,  1.2247]]

Min-Max:
[[0.0, 0.0],
 [0.5, 0.5],
 [1.0, 1.0]]
```

---

## 🧠 Explanation

- Standardization:
  - Mean = middle value → becomes 0  
  - Others scaled relative to std  

- Min-Max:
  - Min → 0  
  - Max → 1  
  - Middle → 0.5  

---

## ⚠️ Important Notes

- Scaling is done **column-wise (feature-wise)**  
- Input must be numeric  
- Always convert to float for division  

---

## ⚠️ Edge Cases

- Standard deviation = 0 → avoid division by zero  
- Max = Min → avoid division by zero  
- Already scaled data  

---

## ❌ Common Mistakes

- Scaling row-wise instead of column-wise  
- Not handling zero division  
- Forgetting rounding  
- Using integer division  

---

## 🔥 Key Insights

- Feature scaling improves:
  - Convergence speed  
  - Model performance  

- Standardization preferred for:
  - Gaussian-like data  

- Min-Max preferred for:
  - Neural networks  

---

## 🧠 Interview Answer

> “Feature scaling ensures that all features have equal importance by transforming them to a common scale using techniques like standardization and normalization.”

---

## 🔍 Keywords

- Feature Scaling  
- Standardization  
- Min-Max Normalization  
- Data Preprocessing  

---

## 🏷️ Metadata

- **Problem ID:** 16  
- **Title:** Feature Scaling Implementation  
- **Difficulty:** Easy  
- **Topic:** Machine Learning  
- **Platform:** Deep-ML  
