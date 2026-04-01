import numpy as np
import math

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    A_t = np.transpose(A)
    B = A_t @ A

    a, b = B[0]
    c, d = B[1]

    # Better angle computation (numerically stable)
    if abs(a - d) < 1e-12:
        theta = math.pi / 4
    else:
        theta = 0.5 * np.arctan2(2*b, (a - d))

    # Use numpy array (important)
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    # Diagonal matrix
    D = np.transpose(R) @ B @ R

    # Direct eigenvalues from diagonal 
    lambda1 = D[0, 0]
    lambda2 = D[1, 1]

    # Singular values
    sigma1 = np.sqrt(max(lambda1, 0))
    sigma2 = np.sqrt(max(lambda2, 0))

    # Sort singular values 
    if sigma1 < sigma2:
        sigma1, sigma2 = sigma2, sigma1
        R = R[:, ::-1]  # swap columns of V

    S = np.array([sigma1, sigma2])
    V = R

    # Safe inverse 
    E_inv = np.array([
        [1/sigma1 if sigma1 > 1e-12 else 0, 0],
        [0, 1/sigma2 if sigma2 > 1e-12 else 0]
    ])

    # Compute U
    U = A @ V @ E_inv

    # Normalize U columns 
    for i in range(2):
        norm = np.linalg.norm(U[:, i])
        if norm > 1e-12:
            U[:, i] /= norm

    V_t = np.transpose(V)

    return (U, S, V_t)

