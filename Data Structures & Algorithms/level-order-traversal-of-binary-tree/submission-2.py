# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        nested = []
        while queue and root:
            length = len(queue)
            lst = []
            for _ in range(length):
                curr = queue.popleft()
                lst.append(curr.val)
                if curr:
                    if curr.left:
                        queue.append(curr.left)      
                    if curr.right:
                        queue.append(curr.right)
            if lst:
                nested.append(lst)
        return nested
        
