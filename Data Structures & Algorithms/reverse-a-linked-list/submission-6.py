class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        def reverse(curr, prev):
            if not curr:
                return prev
            temp_node = curr.next
            curr.next = prev
            prev = curr
            return reverse(temp_node, curr)  
        return reverse(head, None)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        #     if curr is None:
        #         return prev
            
        #     next_node = curr.next
        #     curr.next = prev
        #     return reverse(next_node, curr)
        # return reverse(head, None)
      
   
            
        # # def helper(curr, prev):
        # #     if curr is None:
        # #         return prev
        # #     next_node = curr.next
        # #     curr.next = prev
        # #     return helper(next_node, curr)
        # # return helper(head,None )
            

        
        
        
        # #     prev = None
        # #     curr = head
            
        # #     next_curr = self.reverseList(curr)
        # #     curr.next = prev
        # #     prev = curr
        #     curr = next_curr
        # return prev