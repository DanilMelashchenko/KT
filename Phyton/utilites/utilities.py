def calculate_average(numbers):
    """Returns the average of a list of numbers."""
    if not numbers:
        return 0
    
    total = sum(numbers)
    count = len(numbers)
    return total / count

def find_max(numbers):
    """Returns the maximum number from a list."""
    if not numbers:
        return None
    
    return max(numbers)