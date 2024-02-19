def derivative_forward(X, Y):
    """
    Calculates the derivatives of a function using the forward difference method.

    Args:
        data_points: A list of data points.
        function_values: A list of corresponding function values.

    Returns:
        A list of derivative values for each data point in data_points, except the last one.

    Raises:
        ValueError: If the input lists have different lengths.
    """

    if len(X) != len(Y):
        return ("Input lists must have the same length.")

    h = X[1] - X[0]
    derivatives = []

    for i in range(0, len(X) - 1):
        derivative = (Y[i + 1] - Y[i]) / h
        derivatives.append(derivative)

    return derivatives


def derivative_central(X, Y):
    """
Calculates the central difference derivatives of a function.

Args:
  data_points: A list of data points.
  function_values: A list of corresponding function values.

Returns:
  A list of calculated central difference derivatives for all data points
  except the first and last two.

Raises:
  ValueError: If the lengths of the input lists are not equal.
    """

    if len(X) != len(Y):
        return ("Input lists must have the same length.")

    h = X[1] - X[0]
    derivatives = []

    for i in range(0, len(X) - 2):
        derivative = (1 / (2 * h)) * (
                    -Y[i + 2] + 4 * Y[i + 1] - 3 * Y[i])
        derivatives.append(derivative)

    return derivatives
