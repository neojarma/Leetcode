class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        
        small = nums1 if len(nums1) < len(nums2) else nums2
        big = nums2 if len(nums2) > len(nums1) else nums1
        
        for i in range(len(small)):
            for j in range(len(big)):
                if small[i] == big[j]:
                    res.add(small[i])        
        
        return list(res)