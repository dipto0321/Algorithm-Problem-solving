def narcissistic(value):
    """
    Check if a number is a narcissistic number.

    A narcissistic (or Armstrong) number is a number that is the sum of its own digits each raised to the power of the number of digits.

    Args:
        value (int): The number to check.

    Returns:
        bool: True if the number is narcissistic, False otherwise.
    """
    digits = [int(x) for x in str(value)]
    digit_len = len(digits)
    total = sum(digit**digit_len for digit in digits)
    return total == value


print(narcissistic(153))
