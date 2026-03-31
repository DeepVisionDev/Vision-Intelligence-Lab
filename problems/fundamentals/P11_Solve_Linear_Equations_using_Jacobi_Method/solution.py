import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = [0 for _ in range(len(b))]
	x_new = [0 for _ in range(len(b))]
	for k in range(n):
		for i in range(len(A)):
			sum_val = 0
			for j in range(len(A)):
				if j != i:
					sum_val += A[i][j] * x[j]
				x_new[i] = round((b[i] - sum_val) / A[i][i], 4)
		x = x_new.copy()
	return x
