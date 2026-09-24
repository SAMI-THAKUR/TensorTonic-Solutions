def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    # Write code here
    matches = [a for a, b in zip(y_true, y_pred) if a == b]
    fp = fn = len(y_true) - len(matches)
    tp = len(matches)
    return (2*tp)/((2*tp)+fp+fn)