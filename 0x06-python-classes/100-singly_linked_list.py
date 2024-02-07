#!/usr/bin/python3

"""
This module defines a Node class and a SinglyLinkedList class.
"""


class Node:
    """
    This class represents a node in a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with the given data and next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The reference to the next node. Default is None.

        Raises:
            TypeError: If data is not an integer or next_node
            is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the
        linked list in sorted order.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
