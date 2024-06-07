import src.python_library.lists.integer_lists as integer_lists


class TestRemoveIntegerFromListInplace():

    def test_remove_existing_value(self):
        nums = [3, 2, 2, 3]
        val = 3

        assert integer_lists.remove_integer_from_list_inplace(nums, val) == [2, 2]

    def test_remove_non_existing_value(self):
        nums = [1, 2, 3, 4, 5]
        val = 6

        assert integer_lists.remove_integer_from_list_inplace(nums, val) ==  [1, 2, 3, 4, 5]

    def test_remove_value_from_empty_list(self):
        nums = []
        val = 1

        assert integer_lists.remove_integer_from_list_inplace(nums, val) == []

    def test_remove_all_elements(self):
        nums = [1, 1, 1, 1]
        val = 1

        assert integer_lists.remove_integer_from_list_inplace(nums, val) == []

    def test_no_removal_needed(self):
        nums = [2, 3, 4]
        val = 1

        assert integer_lists.remove_integer_from_list_inplace(nums, val) == [2, 3, 4]

    def test_remove_from_single_element_list(self):
        nums = [1]
        val = 1

        assert integer_lists.remove_integer_from_list_inplace(nums, val) == []

    def test_mixed_elements(self):
        nums = [4, 1, 2, 1, 3, 1, 4]
        val = 1

        assert integer_lists.remove_integer_from_list_inplace(nums, val) == [4, 2, 3, 4]