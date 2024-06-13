

class TestIsPalindrome:
    """
    A test class for the integer is_palindrome function.
    """

    def test_positive_palindrome(self):
        assert self.solution.isPalindrome(121) == True

    def test_negative_number(self):
        assert self.solution.isPalindrome(-121) == False

    def test_positive_non_palindrome(self):
        assert self.solution.isPalindrome(123) == False

    def test_single_digit(self):
        assert self.solution.isPalindrome(7) == True

    def test_large_palindrome(self):
        assert self.solution.isPalindrome(1234321) == True

    def test_large_non_palindrome(self):
        assert self.solution.isPalindrome(1234567) == False

    def test_zero(self):
        assert self.solution.isPalindrome(0) == True