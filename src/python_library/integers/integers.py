def is_palindrome(x: int) -> bool:
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


def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer.

    Parameters:
    s (str): The Roman numeral string to convert.

    Returns:
    int: The integer representation of the Roman numeral.

    Raises:
    ValueError: If the input string is not a valid Roman numeral.
    """
    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
    }

    total = 0
    i = 0
    length = len(s)

    while i < length:
        if i + 1 < length and s[i:i + 2] in roman_numerals:
            total += roman_numerals[s[i:i + 2]]
            i += 2
        elif s[i] in roman_numerals:
            total += roman_numerals[s[i]]
            i += 1
        else:
            raise ValueError("Invalid Roman numeral")

    return total
