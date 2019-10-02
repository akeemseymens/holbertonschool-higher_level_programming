#!/usr/bin/python3
class Node:
    """Represent node list"""
    def __init__(self, data, next_node=None):
        """intialized node values"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getting data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setting data"""
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__data = value

    @property
    def next_node(self):
        """Getting next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setting next node"""
        if isinstance(value, Node) is False and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Represent singly linked list"""
    def __init__(self):
        """Initialized the linked list"""
        self.head = None

    def addNode(self, data):
        """add node"""
        curr = self.head
        if curr is None:
            n = Node()
            n.data = data
            self.head = n
            return

        if curr.data > data:
            n = Node()
            n.data = data
            n.next = curr
            self.head = n
            return

        while curr.next is not None:
            if curr.next.data > data:
                break
            curr = curr.next
        n = Node()
        n.data = data
        n.next = curr.next
        curr.next = n
        return

    def __str__(self):
        """string"""
        data = []
        curr = self.head
        while curr is not None:
            data.append(curr.data)
            curr = curr.next
        return "[%s]" %(', '.join(str(i) for i in data))

    def __repr__(self):
        """print list"""
        return self.__str__()
