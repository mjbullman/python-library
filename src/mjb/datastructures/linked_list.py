class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the list.
    """
    def __init__(self, data = None):
        """
        Initialize a new node.

        Parameters:
        data: The data to store in the node. Defaults to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head: A dummy head node for the linked list.
        count: The number of elements in the list.
    """
    def __init__(self):
        """
        Initialize a new linked list with a dummy head node and a count of elements.
        """
        self.head = Node()
        self.count = 0

    def insert(self, index, data):
        new_node = Node(data)
        current_node = self.head
        current_idx = 0

        while current_node.next is not None and current_idx < index:
            current_node = current_node.next
            current_idx += 1

        new_node.next = current_node.next
        current_node.next = new_node
        self.count += 1

    def prepend(self, data):
        """
        Insert a new node with the given data at the beginning of the list.

        Parameters:
        data: The data to insert.
        """
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.count += 1

    def append(self, data):
        """
        Insert a new node with the given data at the end of the list.

        Parameter:
        data: The data to insert.
        """
        new_node = Node(data)
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        self.count += 1

    def get(self, index):
        """
        Get the data of the node at the specified index.

        Parameter:
        index: The position of the node to retrieve.

        Returns:
        The data of the node at the specified index.

        Raises:
        Exception: If the index is out of range.
        """
        if index >= self.length():
            raise Exception('Index out of range')

        current_idx = 0
        current_node = self.head.next

        while current_node is not None:
            if current_idx == index:
                return current_node.data
            current_node = current_node.next
            current_idx += 1

        raise Exception('Index out of range')

    def remove(self, index):
        """
        Remove the node at the specified index.

        Parameter:
        index: The position of the node to remove.

        Raises:
        Exception: If the index is out of range.
        """
        if index >= self.length():
            raise Exception('Index out of range')

        current_idx = 0
        current_node = self.head

        while current_node.next is not None:
            last_node = current_node
            current_node = current_node.next

            if current_idx == index:
                last_node.next = current_node.next
                self.count -= 1
                return

            current_idx += 1

        raise Exception('Index out of range')

    def length(self):
        """
        Get the number of elements in the list.

        Returns:
        The number of elements in the list.
        """
        return self.count

    def display(self):
        """
        Get a list of all elements in the linked list.

        Returns:
        A list of all data elements in the linked list.
        """
        elements = []
        current_node = self.head.next

        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next

        return elements

    def is_empty(self):
        """
        Check if the linked list is empty.

        Returns:
        True if the list is empty, False otherwise.
        """
        return self.count == 0
