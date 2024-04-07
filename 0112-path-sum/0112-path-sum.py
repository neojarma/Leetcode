# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root, curr):
            if not root:
                return False
            
                   
            curr = curr + root.val
            if not root.left and not root.right:
                if curr == targetSum:
                    return True
     
            return helper(root.left, curr) or helper(root.right, curr)
        
        return helper(root, 0)