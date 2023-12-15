class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        srtd = sorted(nums)
        res = []

        for i in nums:
            res.append(srtd.index(i))

        return res