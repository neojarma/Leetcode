class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums1, collections.Counter(nums2)
        else:
            nums1, nums2 = nums2, collections.Counter(nums1)
        
        for num in nums1:
            if num in nums2:
                res.append(num)
                nums2[num] -= 1
                if nums2[num] == 0:
                    del nums2[num]

        return res
                