class Solution:
    def checkValidString(self, s: str) -> bool:
        openIdx = []
        starIdx = []
        
        for i, v in enumerate(s):
            if v == '(':
                openIdx.append(i)
            elif v == ')':
                if openIdx:
                    openIdx.pop()
                elif starIdx:
                    starIdx.pop()
                else:
                    return False
            else:
                starIdx.append(i)
                
        # (* character left
        # ((*
        # *(
        
        while openIdx and starIdx:
            if openIdx[-1] > starIdx[-1]:
                return False
            
            openIdx.pop()
            starIdx.pop()
            
        return len(openIdx) == 0