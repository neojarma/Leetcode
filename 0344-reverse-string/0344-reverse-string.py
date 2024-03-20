class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        r = len(s)-1
        for x in range(len(s)//2):
            l = s[x]
            s[x] = s[r]
            s[r] = l
            r-=1
        