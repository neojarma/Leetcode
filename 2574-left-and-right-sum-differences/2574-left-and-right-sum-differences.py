class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        leftArr = [0] * n
        rightArr = [0] * n
        left = 0
        right = 0

        rightPoint = -1
        for i in range(len(nums)):
            left += nums[i]
            leftArr[i] = left

            right += nums[rightPoint]
            rightArr[rightPoint] = right
            rightPoint -= 1
        
        for i in range(len(res)):
            res[i] = abs(leftArr[i] - rightArr[i])

        return res