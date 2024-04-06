class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        prev = set(nums[0])
        for i in range(len(nums)-1):
            tempSet = set(nums[i])
            tempRes = []
            
            for j in range(len(nums[i+1])):
                if nums[i+1][j] in tempSet and nums[i+1][j] in prev:
                    tempRes.append(nums[i+1][j])
        
            prev = set(prev) if len(prev) < len(tempRes) else tempRes
            
        return sorted(list(prev))