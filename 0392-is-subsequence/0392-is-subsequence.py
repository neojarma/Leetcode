class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        frst, scnd = 0,0
        
        while scnd < len(t):
            if frst == len(s):
                return True
            
            if s[frst] == t[scnd]:
                frst += 1
                
            scnd += 1
            
        return frst == len(s)