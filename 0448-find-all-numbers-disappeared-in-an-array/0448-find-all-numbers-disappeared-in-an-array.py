class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = sorted(list(set(nums)))
        res = []
        
        ptr = 0
        
        for x in range(1, l+1):
            if ptr >= len(nums):
                res.append(x)
                continue
            
            if nums[ptr] != x:
                res.append(x)
            else:
                ptr+=1
                
        return res