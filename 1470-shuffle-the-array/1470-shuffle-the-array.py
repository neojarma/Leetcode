class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[:n]
        right = nums[n:]
        res = []
        
        for a, b in zip(left, right):
            res.append(a)
            res.append(b)
        
        return res