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
