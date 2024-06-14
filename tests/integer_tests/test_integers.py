from src.python_library.integers.integers import is_palindrome


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
