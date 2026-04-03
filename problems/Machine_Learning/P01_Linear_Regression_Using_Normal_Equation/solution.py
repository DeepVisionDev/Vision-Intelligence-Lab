import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Convert to numpy arrays
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    # Compute Normal Equation
    X_t = X.T
    theta = np.linalg.inv(X_t @ X) @ X_t @ y

    # Round to 4 decimal places
    theta = np.round(theta, 4)

    return theta.tolist()
