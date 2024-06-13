def is_palindrome(self, x: int) -> bool:
    """
    Determines whether an integer is a palindrome without converting it to a string.

    Parameters:
    x (int): The integer to check.

    Returns:
    bool: True if x is a palindrome, False otherwise.
    """
    base_ten = 10

    if x < 0 or (x % base_ten == 0 and x != 0):
        return False

    number = 0

    while x > number:
        number = number * base_ten + x % base_ten
        x //= base_ten

    return x == number or x == number // base_ten