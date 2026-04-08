# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [0] ->  [1] ->  [2] ->  [3] ->  

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr, prev = head, None

        while curr != None:
            temp_node = curr.next
            curr.next = prev

            prev = curr
            curr = temp_node
            
        return prev
       
       
       
