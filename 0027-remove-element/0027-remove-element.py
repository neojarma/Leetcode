class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        currLength = 0
        
        while currLength < len(nums):
            if nums[curr] == val:
                nums.pop(curr)
            else:
                curr += 1
                currLength += 1
                
        return len(nums)