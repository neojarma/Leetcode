# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        def helper(node):
            if not node:
                return node
            
            l = helper(node.left)
            r = helper(node.right)
            
            node.right, node.left = l, r
            return node
        
        return helper(root)