class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        for x in digits:
            a += str(x)
            
        a = int(a) + 1
        res = []
        for x in str(a):
            res.append(int(x))
            
        return res