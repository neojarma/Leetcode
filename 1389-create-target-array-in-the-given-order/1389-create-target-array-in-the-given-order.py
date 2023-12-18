class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for a, b in zip(nums, index):
            result.insert(b, a)
            
        return result