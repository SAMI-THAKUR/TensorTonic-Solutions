import numpy as np

def entropy_node(y):
    """
    Compute entropy for a node with arbitrary class labels.
    """
    y = np.array(y)

    _, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)

    return -np.sum(probs * np.log2(probs))