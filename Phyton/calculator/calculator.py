def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of a by b, handles division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    else:
        return a / b