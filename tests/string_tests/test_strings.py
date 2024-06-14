from src.python_library.strings.strings import *


class TestReverseString:
    """
    Test class for the reverse_string function.
    """

    def test_regular_string(self):
        assert reverse("Hello, World!") == "!dlroW ,olleH"

    def test_empty_string(self):
        assert reverse("") == ""

    def test_single_character(self):
        assert reverse("a") == "a"

    def test_palindrome(self):
        assert reverse("madam") == "madam"

    def test_numbers(self):
        assert reverse("12345") == "54321"

    def test_special_characters(self):
        assert reverse("@#&*!") == "!*&#@"

    def test_mixed_case(self):
        assert reverse("AbCdEfG") == "GfEdCbA"


class TestFindSubstring:
    def test_needle_in_haystack(self):
        assert find_substring("hello", "ll") == 2

    def test_needle_not_in_haystack(self):
        assert find_substring("aaaaa", "bba") == -1

    def test_empty_needle(self):
        assert find_substring("hello", "") == 0

    def test_needle_at_start(self):
        assert find_substring("hello", "he") == 0

    def test_needle_at_end(self):
        assert find_substring("hello", "lo") == 3

    def test_needle_is_haystack(self):
        assert find_substring("hello", "hello") == 0

    def test_needle_longer_than_haystack(self):
        assert find_substring("hi", "hello") == -1

    def test_no_overlap(self):
        assert find_substring("abcdef", "def") == 3

    def test_single_character_match(self):
        assert find_substring("a", "a") == 0

    def test_single_character_no_match(self):
        assert find_substring("a", "b") == -1

    def test_repeated_characters(self):
        assert find_substring("aaa", "aa") == 0

    def test_multiple_occurrences(self):
        assert find_substring("mississippi", "iss") == 1


class TestLengthOfLongestSubstring:
    """
    Test class for the length_of_longest_substring function.
    """

    def test_examples(self):
        assert length_of_longest_substring("abcabcbb") == 3
        assert length_of_longest_substring("bbbbb") == 1
        assert length_of_longest_substring("pwwkew") == 3

    def test_empty_string(self):
        assert length_of_longest_substring("") == 0

    def test_single_character_string(self):
        assert length_of_longest_substring("a") == 1

    def test_string_with_all_unique_characters(self):
        assert length_of_longest_substring("abcdef") == 6

    def test_string_with_repeating_patterns(self):
        assert length_of_longest_substring("abccba") == 3
        assert length_of_longest_substring("aabbccdd") == 2

    def test_string_with_special_characters(self):
        assert length_of_longest_substring("a!b@c#d$") == 8

    def test_string_with_spaces(self):
        assert length_of_longest_substring("abc abcbb") == 4
        assert length_of_longest_substring(" ") == 1

    def test_long_string(self):
        assert length_of_longest_substring("abcdefghijklmnopqrstuvwxyz" * 1000) == 26

    def test_mixed_case_string(self):
        assert length_of_longest_substring("aAbBcC") == 6

    def test_numeric_string(self):
        assert length_of_longest_substring("123123123") == 3