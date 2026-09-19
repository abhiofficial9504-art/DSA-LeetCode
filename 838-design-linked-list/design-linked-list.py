class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head

        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        if index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        cur = self.head

        for _ in range(index - 1):
            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail = None

            return

        cur = self.head

        for _ in range(index - 1):
            cur = cur.next

        deleted_node = cur.next
        cur.next = deleted_node.next

        if deleted_node == self.tail:
            self.tail = cur

        self.size -= 1