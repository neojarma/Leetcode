# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        
        while q:
            lenQ = len(q)
            temp = []
            
            for each in range(lenQ):
                
                num = q.popleft()
                if num:
                    temp.append(num.val)
                    if num.left:
                        q.append(num.left)

                    if num.right:
                        q.append(num.right)          
            
            if temp:
                res.append(temp)
        
        return res