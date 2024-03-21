class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(strs, left, right):
            if left > right:
                return
            
            helper(strs, left+1, right-1)
            strs[left], strs[right] = strs[right], strs[left]
        
        helper(s, 0, len(s)-1)