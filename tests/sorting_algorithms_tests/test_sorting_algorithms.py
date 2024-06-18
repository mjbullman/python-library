from src.python_library.sorting_algorithms.sorting import *


class TestBubbleSortAlgorithm:
    def test_unsorted_list(self):
        assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

    def test_empty_list(self):
        assert bubble_sort([]) == []

    def test_single_element_list(self):
        assert bubble_sort([1]) == [1]

    def test_already_sorted_list(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_list(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_list_with_duplicates(self):
        assert bubble_sort([3, 1, 2, 1, 3, 2, 1]) == [1, 1, 1, 2, 2, 3, 3]

    def test_large_array(self):
        large_array = list(range(10000, 0, -1))
        sorted_large_array = list(range(1, 10001))
        assert bubble_sort(large_array) == sorted_large_array


class TestSelectionSort:
    def test_general_case(self):
        assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]

    def test_unsorted_list(self):
        assert selection_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]

    def test_empty_list(self):
        assert selection_sort([]) == []

    def test_single_element(self):
        assert selection_sort([1]) == [1]

    def test_two_elements(self):
        assert selection_sort([2, 1]) == [1, 2]

    def test_reverse_sorted(self):
        assert selection_sort([3, 2, 1]) == [1, 2, 3]

    def test_negative_numbers(self):
        assert selection_sort([-2, -5, -1, -3]) == [-5, -3, -2, -1]

    def test_all_same_elements(self):
        assert selection_sort([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_mixed_positive_negative(self):
        assert selection_sort([3, -1, 0, -5, 8, 7]) == [-5, -1, 0, 3, 7, 8]

    def test_floats(self):
        assert selection_sort([3.2, 1.5, 4.8, 2.3]) == [1.5, 2.3, 3.2, 4.8]

    def test_duplicates(self):
        assert selection_sort([5, 1, 5, 3, 2]) == [1, 2, 3, 5, 5]

    def test_large_array(self):
        large_array = list(range(1000, 0, -1))
        sorted_large_array = list(range(1, 1001))
        assert selection_sort(large_array) == sorted_large_array


class TestInsertionSort:
    def test_general_case(self):
        assert insertion_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]

    def test_unsorted_list(self):
        assert insertion_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]

    def test_empty_list(self):
        assert insertion_sort([]) == []

    def test_single_element(self):
        assert insertion_sort([1]) == [1]

    def test_two_elements(self):
        assert insertion_sort([2, 1]) == [1, 2]

    def test_reverse_sorted(self):
        assert insertion_sort([3, 2, 1]) == [1, 2, 3]

    def test_negative_numbers(self):
        assert insertion_sort([-2, -5, -1, -3]) == [-5, -3, -2, -1]

    def test_all_same_elements(self):
        assert insertion_sort([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_mixed_positive_negative(self):
        assert insertion_sort([3, -1, 0, -5, 8, 7]) == [-5, -1, 0, 3, 7, 8]

    def test_floats(self):
        assert insertion_sort([3.2, 1.5, 4.8, 2.3]) == [1.5, 2.3, 3.2, 4.8]

    def test_duplicates(self):
        assert insertion_sort([5, 1, 5, 3, 2, 6]) == [1, 2, 3, 5, 5, 6]

    def test_large_array(self):
        large_array = list(range(1000, 0, -1))
        sorted_large_array = list(range(1, 1001))
        assert insertion_sort(large_array) == sorted_large_array


class TestMergeSort:
    def test_empty_array(self):
        assert merge_sort([], 0, 0) == []

    def test_single_element_array(self):
        assert merge_sort([1], 0, 0) == [1]

    def test_sorted_array(self):
        assert merge_sort([1, 2, 3, 4, 5], 0, 4) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_array(self):
        assert merge_sort([5, 4, 3, 2, 1], 0, 4) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        assert merge_sort([38, 27, 43, 3, 9, 82, 10], 0, 6) == [3, 9, 10, 27, 38, 43, 82]

    def test_duplicate_elements(self):
        assert merge_sort([4, 1, 3, 4, 2, 1, 5, 2], 0, 7) == [1, 1, 2, 2, 3, 4, 4, 5]

    def test_negative_elements(self):
        assert merge_sort([-3, -1, -7, -4, -5, -2], 0, 5) == [-7, -5, -4, -3, -2, -1]

    def test_large_array(self):
        large_array = list(range(1000, 0, -1))
        sorted_large_array = list(range(1, 1001))
        assert merge_sort(large_array, 0, len(large_array) - 1) == sorted_large_array
