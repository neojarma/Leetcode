# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        
        while q:
            mirrorStack = []
            lenQ = len(q)
            
            for i in range(lenQ):
                poppedNode = q.popleft()
                
                
                if poppedNode:
                    if poppedNode.left:
                        q.append(poppedNode.left)
                        mirrorStack.append(poppedNode.left.val)
                    else:
                        mirrorStack.append(None)
                        
                    if poppedNode.right:
                        q.append(poppedNode.right)
                        mirrorStack.append(poppedNode.right.val)
                    else:
                        mirrorStack.append(None)
            
            l, r = 0, len(mirrorStack)-1
            while l < r:
                if mirrorStack[l] != mirrorStack[r]:
                    return False
                l +=1
                r -=1
                
        return True