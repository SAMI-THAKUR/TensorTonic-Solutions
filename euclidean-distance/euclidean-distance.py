import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    diff = np.subtract(x,y)
    diff_sq = np.square(diff)
    diff_sq_sum = np.sum(diff_sq)
    return math.sqrt(diff_sq_sum)