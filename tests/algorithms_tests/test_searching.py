from src.python_library.algorithms.searching import *


class TestLinearSearch:
    """
    A test class for the linear search algorithm.
    """

    def test_search_existing_element(self):
        array = [1, 2, 3, 4, 5]
        item = 3
        assert linear_search(array, item) == 2

    def test_search_non_existing_element(self):
        array = [1, 2, 3, 4, 5]
        item = 6
        assert linear_search(array, item) == -1

    def test_search_empty_array(self):
        array = []
        item = 3
        assert linear_search(array, item) == -1

    def test_search_first_element(self):
        array = [1, 2, 3, 4, 5]
        item = 1
        assert linear_search(array, item) == 0

    def test_search_last_element(self):
        array = [1, 2, 3, 4, 5]
        item = 5
        assert linear_search(array, item) == 4

    def test_search_multiple_occurrences(self):
        array = [1, 2, 3, 2, 1]
        item = 2
        assert linear_search(array, item) == 1  # Should return the first occurrence

    def test_search_strings(self):
        array = ["apple", "banana", "cherry"]
        item = "banana"
        assert linear_search(array, item) == 1

    def test_search_non_existing_string(self):
        array = ["apple", "banana", "cherry"]
        item = "date"
        assert linear_search(array, item) == -1

    def test_search_floats(self):
        array = [1.1, 2.2, 3.3, 4.4, 5.5]
        item = 3.3
        assert linear_search(array, item) == 2

    def test_search_non_existing_float(self):
        array = [1.1, 2.2, 3.3, 4.4, 5.5]
        item = 6.6
        assert linear_search(array, item) == -1

    def test_search_mixed_types(self):
        array = [1, "apple", 3.14]
        item = "apple"
        assert linear_search(array, item) == 1

    def test_search_non_existing_mixed_type(self):
        array = [1, "apple", 3.14]
        item = "banana"
        assert linear_search(array, item) == - 1


class TestBinarySearch:
    """
    A test class for the linear search algorithm.
    """

    def test_search_existing_element(self):
        array = [1, 2, 3, 4, 5]
        item = 3
        assert binary_search(array, item) == 2

    def test_search_non_existing_element(self):
        array = [1, 2, 3, 4, 5]
        item = 6
        assert binary_search(array, item) is None

    def test_search_empty_array(self):
        array = []
        item = 3
        assert binary_search(array, item) is None

    def test_search_first_element(self):
        array = [1, 2, 3, 4, 5]
        item = 1
        assert binary_search(array, item) == 0

    def test_search_last_element(self):
        array = [1, 2, 3, 4, 5]
        item = 5
        assert binary_search(array, item) == 4

    def test_search_middle_element(self):
        array = [1, 2, 3, 4, 5]
        item = 3
        assert binary_search(array, item) == 2

    def test_search_single_element_list_found(self):
        array = [1]
        item = 1
        assert binary_search(array, item) == 0

    def test_search_single_element_list_not_found(self):
        array = [1]
        item = 2
        assert binary_search(array, item) is None

    def test_search_large_list(self):
        array = list(range(1000))
        item = 500
        assert binary_search(array, item) == 500

    def test_search_floats(self):
        array = [1.1, 2.2, 3.3, 4.4, 5.5]
        item = 3.3
        assert binary_search(array, item) == 2

    def test_search_non_existing_float(self):
        array = [1.1, 2.2, 3.3, 4.4, 5.5]
        item = 6.6
        assert binary_search(array, item) is None

    def test_search_strings(self):
        array = ["apple", "banana", "cherry"]
        item = "banana"
        assert binary_search(array, item) == 1

    def test_search_non_existing_string(self):
        array = ["apple", "banana", "cherry"]
        item = "date"
        assert binary_search(array, item) is None

