def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    #calculate length of row and coloum
    m = len(a)
    n = len(a[0])

    # make res matrix with initial values zero
    res = res = [[0 for _ in range(m)] for _ in range(n)]
    
    #iterate over matrix and change index [i][j]=[j][i]
    #remember iteration should n * m
    for i in range(n):
        for j in range(m):
                res[i][j]=a[j][i]

    return res
