import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Convert into numpy array
	vectors = np.array(vectors)

	# Calculate means
	mean_v = [np.sum(vectors[i])/len(vectors[i]) for i in range (len(vectors))]

	# Calculate No of Vectors
	l = len(vectors)

	# Make result matrix intially with zero values
	result = [[0  for _ in range(l)]for _ in range(l)]

	# Calculate element wise vector - mean of vector
	vec_m = [vectors[i]-mean_v[i] for i in range(len(mean_v))]

	# Iterate over matrix  and compute Covariance(covariance matrix is always symmetric so we iterate only upper triangular matrix or lower triangular matrix )
	for i in range(l):
		for j in range(i,l):
			result[i][j] = np.sum(vec_m[i]*vec_m[j])/(len(vec_m[i])-1)
			result[j][i] = result[i][j]

   
	return result
