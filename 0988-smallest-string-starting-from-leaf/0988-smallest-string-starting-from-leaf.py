# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        pair = []
        
        def helper(node, string):
            if not node:
                return 
            
            string += chr(node.val+97)
            if not node.left and not node.right:
                pair.append(string[::-1])
                return 
            
            helper(node.left, string) 
            helper(node.right,string)
            
        helper(root,'')
        pair.sort()
        return pair[0]