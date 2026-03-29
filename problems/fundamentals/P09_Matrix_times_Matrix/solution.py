import numpy as np

def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:
    
    # Step 1: check dimension compatibility
    a_col = len(a[0])
    b_row = len(b)
    
    if a_col != b_row:
        return -1
    
    # Step 2: convert to numpy arrays
    a = np.array(a)
    b = np.array(b)
    
    # Step 3: matrix multiplication
    result = a @ b
    
    return result.tolist()
