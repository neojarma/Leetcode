class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        while l < r:
            a = s[l].lower()
            b = s[r].lower()
            
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
            elif not a.isalnum():
                l += 1
                continue
            elif not b.isalnum():
                r -= 1
                continue
            
            l += 1 
            r -= 1
        
        return True