# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return False
            
            if node.val == subRoot.val:
                if isEqual(node, subRoot):
                    return True
            
            return helper(node.left) or helper(node.right)
                
        def isEqual(r1, r2):
            if not r1 and not r2:
                return True
            
            if not r1 and r2 or not r2 and r1:
                return False
            
            if r1.val != r2.val:
                return False
            
            return isEqual(r1.left, r2.left) and isEqual(r1.right, r2.right)
        
        return helper(root)