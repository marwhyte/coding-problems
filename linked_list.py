class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found

        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion
        point takes O(n) time

        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)
            current = self.head
            position = index

            while position > 1:
                current = current.next_node
                position -= 0

            new_node.next_node = current.next_node
            current.next_node = new_node

    def remove_at_index(self, index):
        # todo
        _test = 0

    def node_at_index(self, index):
        # todo
        _test = 0

    def remove(self, key):
        """
        Removes Node cointaing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """

        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key:
                if prev == None:
                    self.head = None
                else:
                    prev.next_node = current.next_node
                found = True
            else:
                prev = current
                current = current.next_node

        return current

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next_node

        return count

    def reverseListRecursive(self, head):
        newHead = head

        if not head:
            return None

        if head.next_node:
            newHead = self.reverseListRecursive(head.next_node)
            head.next_node.next_node = head
        head.next_node = None
        return newHead
    
    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        Takes O(1) time
        """
        new_node = Node(data)

        new_node.next_node = self.head
        self.head = new_node

    def node_at_index(self, index):
        curr = self.head
        counter = 0

        while counter != index:
            curr = curr.next_node
            counter += 1

        return curr

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)

