from src.python_library.lists.integer_lists import *


class TestRemoveIntegerFromListInplace:
    """
    A test class for the `remove_value_inplace` function.
    This class contains multiple test cases to ensure the function correctly identifies the majority element in
    various scenarios.
    """

    def test_remove_existing_value(self):
        nums = [3, 2, 2, 3]
        val = 3

        assert remove_value_inplace(nums, val) == [2, 2]

    def test_remove_non_existing_value(self):
        nums = [1, 2, 3, 4, 5]
        val = 6

        assert remove_value_inplace(nums, val) == [1, 2, 3, 4, 5]

    def test_remove_value_from_empty_list(self):
        nums = []
        val = 1

        assert remove_value_inplace(nums, val) == []

    def test_remove_all_elements(self):
        nums = [1, 1, 1, 1]
        val = 1

        assert remove_value_inplace(nums, val) == []

    def test_no_removal_needed(self):
        nums = [2, 3, 4]
        val = 1

        assert remove_value_inplace(nums, val) == [2, 3, 4]

    def test_remove_from_single_element_list(self):
        nums = [1]
        val = 1

        assert remove_value_inplace(nums, val) == []

    def test_mixed_elements(self):
        nums = [4, 1, 2, 1, 3, 1, 4]
        val = 1

        assert remove_value_inplace(nums, val) == [4, 2, 3, 4]


class TestRemoveDuplicates:
    """
        A test class for the `remove_duplicates_in_place` function.
        This class contains multiple test cases to ensure the function correctly identifies the majority element in
        various scenarios.
    """

    def test_examples(self):
        assert remove_duplicates_in_place([1, 1, 2]) == [1, 2]
        assert remove_duplicates_in_place([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]

    def test_empty_list(self):
        assert remove_duplicates_in_place([]) == []

    def test_single_element(self):
        assert remove_duplicates_in_place([1]) == [1]

    def test_all_unique_elements(self):
        assert remove_duplicates_in_place([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_all_same_elements(self):
        assert remove_duplicates_in_place([1, 1, 1, 1, 1]) == [1]

    def test_mixed_case(self):
        assert remove_duplicates_in_place([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]

    def test_large_numbers(self):
        assert remove_duplicates_in_place([1000, 1000, 2000, 3000, 3000, 4000]) == [1000, 2000, 3000, 4000]

    def test_negative_numbers(self):
        assert remove_duplicates_in_place([-3, -3, -2, -1, -1, 0, 1, 1, 2]) == [-3, -2, -1, 0, 1, 2]

    def test_single_duplicate_in_middle(self):
        assert remove_duplicates_in_place([1, 2, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_duplicates_at_ends(self):
        assert remove_duplicates_in_place([1, 1, 2, 3, 4, 4]) == [1, 2, 3, 4]

    def test_alternating_duplicates(self):
        assert remove_duplicates_in_place([1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == [1, 2, 3, 4, 5, 6]

    def test_no_duplicates(self):
        assert remove_duplicates_in_place([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    def test_all_elements_same(self):
        assert remove_duplicates_in_place([1, 1, 1, 1, 1, 1]) == [1]


class TestMajorityElement:
    """
        A test class for the `majority_element` function.
        This class contains multiple test cases to ensure the function correctly identifies the majority element in
        various scenarios.
    """

    def test_single_element(self):
        assert majority_element([1]) == 1

    def test_two_elements(self):
        assert majority_element([1, 1]) == 1

    def test_simple_case(self):
        assert majority_element([3, 2, 3]) == 3

    def test_even_length_list(self):
        assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2

    def test_large_majority(self):
        assert majority_element([1, 1, 1, 2, 2, 2, 2]) == 2

    def test_negative_numbers(self):
        assert majority_element([-1, -1, -1, 2, 2, 2, -1]) == -1

    def test_mixed_numbers(self):
        assert majority_element([1, 2, 3, 1, 1]) == 1

    def test_duplicates(self):
        assert majority_element([4, 4, 4, 4, 4, 2, 2, 2, 2]) == 4

    def test_large_input(self):
        assert majority_element([1]*5000 + [2]*4999) == 1


class TestRotateInPlace:
    """
    A test class for the `rotate_in_place` function.
    This class contains multiple test cases to ensure the function correctly rotates arrays in various scenarios.
    """

    def test_small_array(self):
        assert rotate_in_place([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

    def test_large_k(self):
        assert rotate_in_place([1, 2, 3, 4, 5], 10) == [1, 2, 3, 4, 5]

    def test_k_equals_length(self):
        assert rotate_in_place([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

    # def test_k_equals_zero(self):
    #     assert rotate_in_place([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

    def test_empty_array(self):
        assert rotate_in_place([], 3) == []

    def test_single_element_array(self):
        assert rotate_in_place([1], 1) == [1]

    def test_all_elements_same(self):
        assert rotate_in_place([1, 1, 1, 1, 1], 3) == [1, 1, 1, 1, 1]

    def test_large_array(self):
        assert rotate_in_place(list(range(1, 100001)), 50000) == list(range(50001, 100001)) + list(range(1, 50001))

