def reverse(string: str) -> str:
    """
    Reverses the given string efficiently.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return string[::-1]


def length_of_longest_substring(string: str) -> int:
    """
   Finds the length of the longest substring without repeating characters.

   Parameters:
   string (str): The input string.

   Returns:
   int: The length of the longest substring without repeating characters.
   """
    char_index_map = {}
    max_length = 0
    start = 0

    for end, char in enumerate(string):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length
