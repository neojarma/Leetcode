class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = {}
        l = 0
        
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            isValid = (r - l + 1) - max(freq.values()) <= k
            if isValid:
                res = max(res, (r-l+1))
                continue
            
            freq[s[l]] -= 1
            l += 1
        
        return res