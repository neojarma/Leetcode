class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        totalZero = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                totalZero += 1
            elif totalZero > 0:
                targetZero = i - totalZero
                nums[targetZero], nums[i] = nums[i], nums[targetZero]
        
                