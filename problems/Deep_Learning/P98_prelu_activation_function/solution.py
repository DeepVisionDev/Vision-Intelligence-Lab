def prelu(x: float, alpha: float = 0.25) -> float:
    """
    Implements the PReLU (Parametric ReLU) activation function.

    Args:
        x (float): Input value
        alpha (float): Slope parameter for negative values (default: 0.25)

    Returns:
        float: PReLU activation value
    """
    if x < 0:
        return x * alpha
    else:
        return x


# Example usage
if __name__ == "__main__":
    values = [-3, -1, 0, 2, 4]
    outputs = [prelu(v) for v in values]

    print("Input :", values)
    print("Output:", outputs)
