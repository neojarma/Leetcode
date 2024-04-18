class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(l, r, s):
            print(len(s))
            if len(s) == n*2:
                res.append(''.join(s))
                return           
            
            if l < n:
                backtrack(l+1, r, s+['('])
            
            if r < l:
                backtrack(l, r+1, s+[')'])
        
        backtrack(0,0,[])
        return res