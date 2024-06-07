from src.python_library.strings.strings import length_of_longest_substring


class TestLengthOfLongestSubstring:

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