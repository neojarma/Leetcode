class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        big = {}
        small = []
        res = []
        
        if len(nums1) < len(nums2):
            small = nums1
            big = collections.Counter(nums2)
        else:
            small = nums2
            big = collections.Counter(nums1)
        
        for num in small:
            if num in big:
                res.append(num)
                big[num] -= 1
                if big[num] == 0:
                    del big[num]

        return res
                