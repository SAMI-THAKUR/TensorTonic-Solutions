import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    x = np.array(x)
    # def apply_leaky(ele):
    #     if ele<0:
    #         return alpha*ele
    #     return ele
    apply_leaky = np.vectorize(lambda x: alpha*x if x<0 else x)
    return apply_leaky(x)