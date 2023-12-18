class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        buffer = 1
        for i in range(len(nums)):
            res[i] = buffer
            buffer *= nums[i]

        buffer2 = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= buffer2
            buffer2 *= nums[i]
        
        return res