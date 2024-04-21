class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arrS = list(s)
        
        for i in range(len(t)):
            if len(arrS) == 0: return True
            
            if t[i] == arrS[0]:
                arrS.pop(0)
                
        return len(arrS) == 0