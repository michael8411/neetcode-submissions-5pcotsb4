# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        level = 0
        nested = []
        
        while len(queue) > 0 and root:
            lst = []
            length = len(queue) 
            for i in range(length):
                curr = queue.popleft()
                if curr:
                    lst.append(curr.val)
                if curr.left and curr:
                    queue.append(curr.left)
                if curr.right and curr:
                    queue.append(curr.right)
            nested.append(lst)
        return nested   
            
                
        
            