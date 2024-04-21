class Solution:
    def findAnagrams(self, s: str, p: str):
        pMap = collections.Counter(p)
        sMap = collections.Counter(s[:len(p)])
        res = []
        if sMap == pMap:
            res.append(0)
        
        l = 0
        for r in range(len(p), len(s)):
            sMap[s[r]] = sMap.get(s[r], 0)+1
            sMap[s[l]] -= 1
            if sMap[s[l]] == 0:
                del sMap[s[l]]
            l += 1
            
            if sMap == pMap:
                res.append(l)

        return res