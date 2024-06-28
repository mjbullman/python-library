import pytest
from src.python_library.data_structures.linked_list import LinkedList


class TestLinkedList:
    """
    A test class for the Linked List data structure class.
    """

    def test_initial_length(self):
        linked_list = LinkedList()
        assert linked_list.length() == 0

    def test_append(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append(20)
        assert linked_list.length() == 2
        assert linked_list.get(0) == 10
        assert linked_list.get(1) == 20

    def test_prepend(self):
        linked_list = LinkedList()
        linked_list.prepend(30)
        linked_list.prepend(40)
        assert linked_list.length() == 2
        assert linked_list.get(0) == 40
        assert linked_list.get(1) == 30

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append(20)
        linked_list.insert(1, 15)
        assert linked_list.length() == 3
        assert linked_list.get(0) == 10
        assert linked_list.get(1) == 15
        assert linked_list.get(2) == 20

    def test_insert_at_start(self):
        linked_list = LinkedList()
        linked_list.insert(0, 50)
        assert linked_list.get(0) == 50

    def test_insert_at_end(self):
        linked_list = LinkedList()
        linked_list.append(60)
        linked_list.insert(10, 70)  # Should append to the end
        assert linked_list.get(1) == 70

    def test_get(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append(20)
        assert linked_list.get(0) == 10
        assert linked_list.get(1) == 20
        with pytest.raises(Exception):
            linked_list.get(2)

    def test_remove(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append(20)
        linked_list.append(30)
        linked_list.remove(1)
        assert linked_list.length() == 2
        assert linked_list.get(0) == 10
        assert linked_list.get(1) == 30
        with pytest.raises(Exception):
            linked_list.remove(10)  # Index out of range

    def test_display(self):
        linked_list = LinkedList()
        linked_list.append(10)
        linked_list.append(20)
        linked_list.append(30)
        assert linked_list.display() == [10, 20, 30]

    def test_is_empty(self):
        linked_list = LinkedList()
        assert linked_list.is_empty()
        linked_list.append(10)
        assert not linked_list.is_empty()

if __name__ == "__main__":
    pytest.main()
