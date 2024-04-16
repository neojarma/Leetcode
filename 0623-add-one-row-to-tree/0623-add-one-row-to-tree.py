# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new

        def helper(node, lv, direction):
            if not node:
                return None

            lv += 1
            if lv == depth:
                new = TreeNode(val)
                if direction == 'l':
                    new.left = node.left
                    node.left = new
                    helper(node, lv-1, 'r')
                else:
                    new.right = node.right
                    node.right = new
                    return

            helper(node.left, lv, 'l')
            helper(node.right, lv, 'l')
            return root

        return helper(root, 1, 'l')
    