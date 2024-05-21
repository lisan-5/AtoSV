class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        prev = None
        curr = self.head
        for _ in range(index):
            prev = curr
            curr = curr.next
        newNode = ListNode(val)
        newNode.next = curr
        prev.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        prev = None
        curr = self.head
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.size -= 1
