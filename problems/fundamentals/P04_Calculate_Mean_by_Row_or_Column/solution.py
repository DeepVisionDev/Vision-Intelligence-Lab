import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	# convert matrix in array
	matrix = np.array(matrix)

	# calculate row and column
	row , col = matrix.shape

    # chack mode
	if mode == 'column':
		means = [np.sum(matrix[:,i]/row) for i in range (col) ]
	else:
		means = [np.sum(matrix[i,:]/col) for i in range (row) ]
	return means
