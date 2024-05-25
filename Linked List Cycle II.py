class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        
        # Step 1: Determine if there is a cycle using two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # No cycle detected
        if not fast or not fast.next:
            return None
        
        # Step 2: Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
