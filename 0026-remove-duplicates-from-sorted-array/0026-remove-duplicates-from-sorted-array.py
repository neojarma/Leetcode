class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast, slow = 0,1
        length = len(nums)-1
        
        while fast < length:
            if nums[slow] != nums[fast]:
                slow += 1
                fast += 1
                continue
                
            nums.pop(fast)
            length -= 1
            
        return len(nums)