import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    
    m = len(a)
    n = len(a[0])
    
    if m * n != new_shape[0] * new_shape[1]:
        return []
    
    # Using numpy reshape (logic explained in README)
    reshaped_matrix = np.array(a).reshape(new_shape)
    
    return reshaped_matrix.tolist()
