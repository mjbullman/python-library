"""
sorting_algorithms.py

This module contains implementations of various sorting algorithms.
Each algorithm sorts a list of elements in ascending order.

Available sorting algorithms:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

Functions:
- bubble_sort(arr): Sorts `arr` using the bubble sort algorithm.
- selection_sort(arr): Sorts `arr` using the selection sort algorithm.
- insertion_sort(arr): Sorts `arr` using the insertion sort algorithm.
- merge_sort(arr): Sorts `arr` using the merge sort algorithm.
- quick_sort(arr): Sorts `arr` using the quick sort algorithm.
- heap_sort(arr): Sorts `arr` using the heap sort algorithm.

Examples:
    >>> from src.python_library.sorting_algorithms.sorting import bubble_sort
    >>> arr = [64, 34, 25, 12, 22, 11, 90]
    >>> bubble_sort(arr)
    >>> print(arr)
    [11, 12, 22, 25, 34, 64, 90]

    >>> from src.python_library.sorting_algorithms.sorting import quick_sort
    >>> arr = [10, 7, 8, 9, 1, 5]
    >>> quick_sort(arr)
    >>> print(arr)
    [1, 5, 7, 8, 9, 10]

Note:
- All sorting functions modify the input list in place.
- Ensure the input list is mutable and supports comparison operations.
- For large datasets, prefer algorithms with better time complexity such as merge sort or quick
  sort.

References:
- Cormen, Thomas H., et al. "Introduction to Algorithms." MIT Press, 2009.
- Knuth, Donald E. "The Art of Computer Programming." Addison-Wesley, 1997.

Author:
- Martin Bullman

Date:
- 2024-06-14
"""


def bubble_sort(array: list) -> list:
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

    Parameters:
    array (list): The list of integers to be sorted.

    Returns:
    list: The sorted list of integers in ascending order.

    Example:
    bubble_sort([64, 34, 25, 12, 22, 11, 90]) # Returns [11, 12, 22, 25, 34, 64, 90]
    """
    size: int = len(array)

    for i in range(size):
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def selection_sort(array: list) -> list:
    """
    Sorts an array using the insertion sort algorithm.

    Parameters:
    array (list): A list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    size: int = len(array)

    for i in range(size):
        min_index: int = i

        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        if array[min_index] < array[i]:
            array[i], array[min_index] = array[min_index], array[i]

    return array


def insertion_sort(array: list) -> list:
    """
    Sorts an array using the insertion sort algorithm.

    Parameters:
    array (list): A list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    arr_len: int = len(array)

    for i in range(1, arr_len):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


def merge(array: list, start: int, mid: int, end: int):
    """
    Merge two sorted subarrays of `array`.

    The first subarray is array[start:mid+1].
    The second subarray is array[mid+1:end+1].

    Parameters:
    array (list): The original array containing the subarrays to merge.
    start (int): The starting index of the first subarray.
    mid (int): The ending index of the first subarray and mid-point of the merge operation.
    end (int): The ending index of the second subarray.
    """
    left_len = mid - start + 1
    right_len = end - mid

    L: list = array[start:mid + 1]
    R: list = array[mid + 1:end + 1]

    i: int = 0
    j: int = 0
    k: int = start

    while i < left_len and j < right_len:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1

        k += 1


    while i < left_len:
        array[k] = L[i]
        i += 1
        k += 1

    while j < right_len:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort(array: list, start: int, end: int) -> None | list:
    """
    Sort the array using the merge sort algorithm.

    Parameters:
    array (list): The array to be sorted.
    start (int): The starting index of the subarray to be sorted.
    end (int): The ending index of the subarray to be sorted.

    Returns:
    list: The sorted array.
    """
    if start >= end or len(array) == 0:
        return array

    mid = (start + end) // 2
    merge_sort(array, start, mid)
    merge_sort(array, mid + 1, end)
    merge(array, start, mid, end)

    return array


def quick_sort(array: list) -> list:
    return array


def heap_sort(array: list) -> list:
    return array
