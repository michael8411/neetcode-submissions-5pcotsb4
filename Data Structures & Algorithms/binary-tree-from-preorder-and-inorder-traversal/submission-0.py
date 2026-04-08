# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right






# Preorder: root, left, right
# inOrder: left, root, right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
            
        # 1. Initialize the root and the stack
        root = TreeNode(preorder[0])
        stack = [root]
        
        # Pointer to track our position in the inorder array
        inorder_idx = 0
        
        # 2. Iterate through the rest of the preorder array
        for i in range(1, len(preorder)):
            preorder_val = preorder[i]
            node = stack[-1]
            
            # If the top of stack doesn't match inorder, we keep going left!
            if node.val != inorder[inorder_idx]:
                node.left = TreeNode(preorder_val)
                stack.append(node.left)
            else:
                # We hit the bottom left. Pop from stack until we find 
                # the correct parent to attach the right child to.
                while stack and stack[-1].val == inorder[inorder_idx]:
                    node = stack.pop()
                    inorder_idx += 1
                
                # Attach the right child to the last popped node
                node.right = TreeNode(preorder_val)
                stack.append(node.right)
                
        return root