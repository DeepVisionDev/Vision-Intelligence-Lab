import numpy as np 
import math

def determinant(matrix: list[list[float]]) -> float:
	n = len(matrix)
	if n == 2:
		return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	det = 0
	for col in range(n):
		minor = [row[:col] + row[col+1:] for row in matrix[1:]]
		det += ((-1)**col) * matrix[0][col] * determinant(minor)
	return det

def determinant_4x4(matrix: list[list[float]]) -> float:
    
    return determinant(matrix)
