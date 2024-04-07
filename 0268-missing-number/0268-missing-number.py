class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 3
        # 0,1,3   = 4
        # 0+1+2+3 = 6
        
        # 2
        # 0,1    =1
        # 0+1+2  =3
        
        should = sum(range(1, len(nums)+1))
        actual = sum(nums)
        return should - actual