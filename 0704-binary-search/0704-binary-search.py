class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        l,r = 0,len(nums)-1

        while l <= r:
            if nums[mid] == target:
                return mid

            if nums[l] == target:
                return l

            if nums[r] == target:
                return r

            if target < nums[mid]:
                r = mid - 1
                mid = r // 2
            else:
                l = mid+1
                mid = r-(r-l)

        return -1
        