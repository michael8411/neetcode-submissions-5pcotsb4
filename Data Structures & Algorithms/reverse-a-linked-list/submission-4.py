class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        def helper(curr: Optional[ListNode], prev: Optional[ListNode]) ->  Optional[ListNode]:
            if curr is None:
                return prev

            next_node = curr.next
            curr.next = prev
            return helper(next_node, curr,)
        
        return helper(head, None)
 


        
        
        
        #     prev = None
        #     curr = head
            
        #     next_curr = self.reverseList(curr)
        #     curr.next = prev
        #     prev = curr
        #     curr = next_curr
        # return prev