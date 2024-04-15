class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(input):
            res = ''
            for i in range(len(input)):
                if input[i] == '#':
                    if res:
                        res = res[:len(res)-1]
                else:
                    res += input[i]
            return res
        
        
        return helper(s) == helper(t)