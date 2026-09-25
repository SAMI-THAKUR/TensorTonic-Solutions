import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    result = np.subtract(x, y)
    return float(np.sum(np.abs(result)))