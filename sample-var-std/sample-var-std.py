import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x_ = np.mean(x)
    x_diff = x - x_
    var = np.sum(x_diff ** 2) / (len(x)-1)
    return {
        "variance" : float(var),
        "standard_deviation" : float(np.sqrt(var))
    }