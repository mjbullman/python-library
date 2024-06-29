from typing import List, TypeVar

T = TypeVar("T")


def linear_search(array: List[T], item: T) -> int:
    """
    Perform a linear search on a list to find the index of a specified item.

    Parameters:
    array (List[T]): The list to search within.
    item (T): The item to search for.

    Returns:
    int: The index of the item if found, otherwise -1.
    """

    for i in range(len(array)):
        if array[i] == item:
            return i

    return - 1


def binary_search(sorted_array: T, key: T) -> int:
    """
    Perform a binary search on a sorted list to find the index of a specified item.

    Parameters:
    nums (List[T]): The sorted list to search within.
    key (T): The item to search for.

    Returns:
    Optional[int]: The index of the item if found, otherwise None.
    """
    return binary_search_helper(sorted_array, key, 0, len(sorted_array))


def binary_search_helper(sorted_array: T, key: T, start_idx: int, end_idx: int):
    middle_idx = (start_idx + end_idx) // 2

    if start_idx == end_idx:
        return -1

    if sorted_array[middle_idx] > key:
        return binary_search_helper(sorted_array, key, start_idx, middle_idx)
    elif sorted_array[middle_idx] < key:
        return binary_search_helper(sorted_array, key, middle_idx + 1, end_idx)
    else:
        return middle_idx
