# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = set()
        
        def helper(node, string):
            if not node:
                return 
            
            string += chr(node.val+97)
            if not node.left and not node.right:
                reverseStr = string[::-1]
                if res:
                    prev = res.pop()
                    res.add(min(prev, reverseStr))
                else:
                    res.add(reverseStr)
                return 
            
            helper(node.left, string) 
            helper(node.right,string)
            
        helper(root,'')
        return res.pop()