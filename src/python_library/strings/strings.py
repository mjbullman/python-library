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

    for j in range(len_string):
        if i < len_sub_string and sub_string[i] == string[j]:
            i += 1

    return i >= len_sub_string


