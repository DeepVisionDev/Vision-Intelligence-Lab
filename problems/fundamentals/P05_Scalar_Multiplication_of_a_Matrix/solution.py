def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = matrix
	for i in range (len(matrix)):
		for j in range (len(matrix[i])):
			result[i][j]*=scalar
	return result
