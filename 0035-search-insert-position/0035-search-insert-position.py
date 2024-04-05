class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r,mid = 0, len(nums)-1, len(nums)//2
        
        while l <= r:
            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
            
            mid = (r + l)//2
        
        return mid + 1
        