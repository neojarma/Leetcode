class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        result = []
        
        for i in nums:
            temp += i
            result.append(temp)
        
        return result