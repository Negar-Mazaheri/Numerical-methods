def Lagrange(a, X, Y):
    """
    This function implements the Lagrange interpolation method.

    Args:
        a: The value at which the polynomial is evaluated.
        X: A list of x-coordinates.
        Y: A list of y-coordinates.

    Returns:
        The interpolated y-value at x=a.
    """

    if len(X) != len(Y):
        return("The number of x values must be equal to the number of y values.")

    yp = 0
    for i, xi in enumerate(X):
        # Use enumerate to avoid resetting the product in each loop
        product = 1
        for j, xj in enumerate(X):
            if i != j:
                product *= (a - xj) / (xi - xj)
        yp += product * Y[i]

    return yp


