class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node before the 'left' position
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversing the sublist
        current = prev.next
        next = None
        for _ in range(right - left):
            next = current.next
            current.next = next.next
            next.next = prev.next
            prev.next = next
        
        return dummy.next
