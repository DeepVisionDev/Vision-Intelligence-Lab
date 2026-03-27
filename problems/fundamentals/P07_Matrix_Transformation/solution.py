import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
  # Convert all input matrix into numpy array
	A = np.array(A)
	S = np.array(S)
	T = np.array(T)
  # Check invertibility
	detS = np.linalg.det(S)
	detT = np.linalg.det(T)
	if detS==0 or detT == 0:
		return -1
  # Compute resultant matrix
	transformed_matrix = np.linalg.inv(T) @ A @ S 
	return transformed_matrix
