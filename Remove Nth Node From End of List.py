class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next =  head
        ptr1 = dummy
        ptr2 = dummy
        
        for i in range(1, n+2, 1):
            ptr1 = ptr1.next
        
        while ptr1 != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr2.next = ptr2.next.next
        return dummy.next
        
        
    

        
