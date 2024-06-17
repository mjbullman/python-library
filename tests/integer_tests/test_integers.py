from src.python_library.integers.integers import *


class TestIsPalindrome:
    """
    A test class for the integer is_palindrome function.
    """

    def test_positive_palindrome(self):
        assert is_palindrome(121) == True

    def test_negative_number(self):
        assert is_palindrome(-121) == False

    def test_positive_non_palindrome(self):
        assert is_palindrome(123) == False

    def test_single_digit(self):
        assert is_palindrome(7) == True

    def test_large_palindrome(self):
        assert is_palindrome(1234321) == True

    def test_large_non_palindrome(self):
        assert is_palindrome(1234567) == False

    def test_zero(self):
        assert is_palindrome(0) == True


class TestRomanToInt:
    """
    A test class for the roman numeral to integer function.
    """
    
    def test_single_characters(self):
        assert roman_to_int('I') == 1
        assert roman_to_int('V') == 5
        assert roman_to_int('X') == 10
        assert roman_to_int('L') == 50
        assert roman_to_int('C') == 100
        assert roman_to_int('D') == 500
        assert roman_to_int('M') == 1000

    def test_subtractive_combinations(self):
        assert roman_to_int('IV') == 4
        assert roman_to_int('IX') == 9
        assert roman_to_int('XL') == 40
        assert roman_to_int('XC') == 90
        assert roman_to_int('CD') == 400
        assert roman_to_int('CM') == 900

    def test_mixed_combinations(self):
        assert roman_to_int('III') == 3
        assert roman_to_int('VIII') == 8
        assert roman_to_int('XXVII') == 27
        assert roman_to_int('XLII') == 42
        assert roman_to_int('XCIX') == 99
        assert roman_to_int('CXLIV') == 144
        assert roman_to_int('DCCCXLV') == 845
        assert roman_to_int('MMXXIV') == 2024

    def test_large_numbers(self):
        assert roman_to_int('MMM') == 3000
        assert roman_to_int('MMMCMXCIX') == 3999
        assert roman_to_int('MMMDCCCLXXXVIII') == 3888
        assert roman_to_int('MMMM') == 4000  # Note: While not standard, some systems might use it
        assert roman_to_int('MMMMCMXCIV') == 4994
