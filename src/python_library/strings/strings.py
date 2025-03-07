def reverse(string: str) -> str:
    """
    Reverses the given string efficiently.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return string[::-1]


def find_substring(haystack: str, needle: str) -> int:
    """
   Returns the index of the first occurrence of needle in haystack,
   or -1 if needle is not part of haystack.

   Parameters:
   haystack (str): The string to be searched.
   needle (str): The substring to search for.

   Returns:
   int: The starting index of needle in haystack, or -1 if needle is not found.
   """
    len_needle: int = len(needle)
    len_haystack: int = len(haystack)

    for i in range(len_haystack - len_needle + 1):
        if haystack[i:i + len_needle] == needle:
            return i

    return -1


def length_of_longest_substring(string: str) -> int:
    """
   Finds the length of the longest substring without repeating characters.

   Parameters:
   string (str): The input string.

   Returns:
   int: The length of the longest substring without repeating characters.
   """
    char_index_map: dict = {}
    max_length: int = 0
    start: int = 0

    for end, char in enumerate(string):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length


def is_subsequence(sub_string: str, string: str) -> bool:
    """
    Determine if `sub_string` is a subsequence of `string`.

    Parameters:
    sub_string (str): The string to check as a subsequence.
    string (str): The string to check against.

    Returns:
    bool: True if `sub_string` is a subsequence of `string`, False otherwise.
    """

    len_sub_string = len(sub_string)
    len_string = len(string)
    i = 0

    # cannot be a subsequence if sub string larger than string.
    if len_sub_string > len_string:
        return False

    for j in range(len_string):
        if i < len_sub_string and sub_string[i] == string[j]:
            i += 1

    return i >= len_sub_string


def length_of_last_word(string: str) -> int:
    """
    Returns the length of the last word in the string `string`.

    Parameters:
    string (str): The input string.

    Returns:
    int: The length of the last word in `string`.
    """
    length = 0
    i = len(string) - 1

    # skip trailing spaces.
    while i >= 0 and string[i] == ' ':
        i -= 1

    # count the length of the last word.
    while i >= 0 and string[i] != ' ':
        length += 1
        i -= 1

    return length


def is_isomorphic(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    # create dictionaries to store the mapping of characters.
    s1_to_s2 = {}
    s2_to_s1 = {}

    for char_s1, char_s2 in zip(string1, string2):
        # if the character in s is already mapped to a different character in t.
        if char_s1 in s1_to_s2:
            if s1_to_s2[char_s1] != char_s2:
                return False
        # if the character in t is already mapped to a different character in s.
        else:
            s1_to_s2[char_s1] = char_s2

        if char_s2 in s2_to_s1:
            if s2_to_s1[char_s2] != char_s1:
                return False
        else:
            s2_to_s1[char_s2] = char_s1

    return True


def isPalindrome( string: str) -> bool:
    clean_string = ''.join(char for char in string if char.isalnum()).lower()
    left = 0
    right = len(clean_string) - 1

    if not clean_string:
        return True

    if len(clean_string) == 1:
        return True

    while left <= right:
        if clean_string[left] != clean_string[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

