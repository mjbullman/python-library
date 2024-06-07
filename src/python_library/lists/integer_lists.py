from typing import List


def remove_integer_from_list_inplace(nums: List[int], val: int) -> List:
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
