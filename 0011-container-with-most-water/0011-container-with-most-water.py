class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        l, r = 0, len(height)-1
        while l < r:
            isLeft = True if height[l] < height[r] else False
            minVal = height[l] if height[l] < height[r] else height[r]
            
            length = r - l
            width = minVal
            res = max(length * minVal, res)
            
            if isLeft:
                l+=1
            else:
                r-=1
        
        return res