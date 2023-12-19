class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem = sum(nums)
        digit = 0
        
        for i in nums:
            digits = i
            while digits > 0:
                last = digits % 10
                digit += last             
                digits //= 10
            
        return abs(elem - digit)