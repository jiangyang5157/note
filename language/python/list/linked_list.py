class LinkedListNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:

    root = None
    size = 0

    def __init__(self, data=None):
        if data is not None:
            self.root = LinkedListNode(data)
            self.size = 1

    def __str__(self):
        if self.is_empty():
            return "[]"

        current = self.root
        result = str(current)
        while current.next is not None:
            result += ' -> {}'.format(str(current.next))
            current = current.next

        return '[{}]'.format(result)

    def __iter__(self):
        current = self.root
        while current is not None:
            yield current
            current = current.next
        return

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.root is None:
            return True
        return False

    # O(1)
    def insert_in_front(self, data):
        node = LinkedListNode(data)

        if self.root is None:
            self.root = node
            self.size += 1
            return node

        node.next = self.root
        self.root = node
        self.size += 1
        return node

    # Returns removed node
    def remove_from_front(self):
        if self.is_empty():
            return False

        node = self.root
        self.root = self.root.next
        self.size -= 1
        return node

    # O(N)
    def insert_at_end(self, data):
        node = LinkedListNode(data)

        if self.root is None:
            self.root = node
            self.size += 1
            return node

        current = self.root
        while current.next is not None:
            current = current.next

        current.next = node
        self.size += 1
        return node

    def remove_from_last(self):
        if self.root is None:
            return False

        # A special case for when there's only one thing in the list.
        if self.root.next is None:
            node = None
            self.root = None
            self.size -= 1
            return node

        current = self.root
        while current.next.next is not None:
            current = current.next

        node = current.next
        current.next = None
        self.size -= 1
        return node

    # O(1)
    def insert_at_index(self, data, index=0):
        if index == 0:
            return self.insert_in_front(data)

        node = LinkedListNode(data)

        current = self.root
        count = 0 # How many nodes we've seen
        while (count < index and current is not None):
            if (count + 1 == index):
                node.next = current.next
                current.next = node
                self.size += 1
                return True
            current = current.next
            count += 1

        return False

    def remove_at_index(self, index=0):
        if self.is_empty():
            return False

        if (index == 0):
            return self.remove_from_front()

        current = self.root
        count = 0
        while count < index and current.next is not None:
            if (count + 1 == index):
                node = current.next
                current.next = current.next.next
                self.size -= 1
                return node
            current = current.next
            count += 1

        return False
