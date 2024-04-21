class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Map = collections.Counter(s1)
        s2Map = collections.Counter(s2[:len(s1)])
        if s1Map == s2Map: return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1
            s2Map[s2[l]] -= 1
            if s2Map[s2[l]] == 0: del s2Map[s2[l]]
            l += 1
            if s1Map == s2Map: return True
            
        return False