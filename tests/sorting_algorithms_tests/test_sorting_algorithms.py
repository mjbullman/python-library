from src.python_library.sorting_algorithms.sorting import bubble_sort


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

