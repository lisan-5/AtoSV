class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        ans = ListNode(head.val)
        
        curr = ans
        head = head.next
        
        while head:
            newNode = ListNode(head.val)
            newNode.next = curr
            curr = newNode
            head = head.next
        return curr
            
            
    
    
    
    
    
        
