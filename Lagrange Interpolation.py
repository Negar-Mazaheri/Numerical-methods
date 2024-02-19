#!/usr/bin/env python
# coding: utf-8

# In[9]:


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



# In[11]:


# Get inputs from the user
X_input = input("Enter X values separated by spaces: ")
Y_input = input("Enter Y values separated by spaces: ")
a_input = input("Enter the value of 'a': ")

# Convert input strings to lists
X = [float(x) for x in X_input.split()]
Y = [float(y) for y in Y_input.split()]
a = float(a_input)

# Call the function with user inputs
result = Lagrange(a, X, Y)

# Display the result
print("Result:", result)


# In[ ]:





# In[ ]:




