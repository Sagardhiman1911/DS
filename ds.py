class Node:
    """
    An object for storing a single node for linked list
    Models two attribute - data and link to next_node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: {}>".format(self.data)


class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Return the number of nodes in list
        Takes O(n) time
        :return:
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new node containing data at head of list
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Takes O(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def remove_index(self, index):
        """
        Remove value at index.
        """
        current = self.head
        if index == 0:
            self.head = current.next_node
        else:
            position = index
            for i in range(index):
                previous = current
                current = current.next_node
                position -= 1

                if position == 0:
                    previous.next_node = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current

    def insert(self, data, index):
        """
        Insert data at index
        Takes O(n)
        """
        if index == 0:
            self.add(data)
        else:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def reverse(self):
        if self.head is None:
            return False
        else:
            prev = None
            current = self.head
            while current:
                next_n = current.next_node
                current.next_node = prev
                prev = current
                current = next_n
            self.head = prev

    def __repr__(self):
        nodes = list()
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: {}]".format(current.data))
            elif current.next_node is None:
                nodes.append("[Tail: {}]".format(current.data))
            else:
                nodes.append("[{}]".format(current.data))

            current = current.next_node
        return ' -> '.join(nodes)


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)

