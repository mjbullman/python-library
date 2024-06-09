from typing import List


def remove_value_inplace(nums: List[int], val: int) -> List:
    """
    Removes all occurrences of a specified value from the list in-place and returns the modified list
    containing only the elements not equal to the specified value.

    Parameters:
    nums (List[int]): The list of integers from which the specified value will be removed.
    val (int): The value to be removed from the list.

    Returns:
    List[int]: The modified list containing only the elements not equal to the specified value.
    """

    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return nums[0:i]


def remove_duplicates_in_place(nums: List[int]) -> List:
    """
    Removes duplicates from a sorted list in-place and returns the list containing only unique elements.

    Parameters:
    nums (List[int]): A sorted list of integers, possibly with duplicates.

    Returns:
    List[int]: The list with duplicates removed, containing only unique elements.
    """
    if not nums:
        return []

    i = 0

    for j, num in enumerate(nums):
        if nums[i] < nums[j]:
            i += 1
            nums[i] = nums[j]

    return nums[0:i + 1]


def majority_element(nums: List[int]) -> int:
    """
    Finds the majority element in a list of integers.
    The majority element is the element that appears more than n // 2 times.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    int: The majority element.
    """
    min_times = len(nums) // 2
    num_counts = {}

    for i in nums:
        num_counts[i] = num_counts.get(i, 0) + 1

        if num_counts[i] > min_times:
            return i


def rotate_in_place(nums: List[int], k: int) -> List:
    """
    Rotates the elements of the array nums in place by k steps to the right.

    Parameters:
    nums (List[int]): The list of integers to be rotated.
    k (int): The number of steps to rotate the array.

    Returns:
    List[int]: The rotated list.
    """
    if not nums or k == 0:
        return nums

    n = len(nums)
    k = k % n  # in case k is larger than the length of nums.

    # helper function to reverse a portion of the array.
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # step 1: reverse the entire array.
    reverse(0, n - 1)
    # step 2: reverse the first k elements.
    reverse(0, k - 1)
    # step 3: reverse the remaining elements.
    reverse(k, n - 1)

    return nums


def max_difference(nums: List[int]) -> int:
    """
     Finds the maximum difference from a list of integers by finding the lowest and highest values.

     Parameters:
     nums (List[int]): A list of integers.

     Returns:
     int: The maximum difference possible.
     """
    min_int = float('inf')
    max_diff = 0

    for i in nums:
        if i < min_int:
            min_int = i
        if i > min_int:
            diff = i - min_int
            if diff > max_diff:
                max_diff = diff

    return max_diff
