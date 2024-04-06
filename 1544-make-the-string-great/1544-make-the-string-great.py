class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        curr = 0
        length = len(s)
        
        while curr < length:
            if len(s) < 2:
                break
            if s[curr].isupper():
                if curr == 0:
                    if s[curr+1].upper() == s[curr] and s[curr+1] != s[curr]:
                        s.pop(curr+1)
                        s.pop(curr)
                        curr = 0
                        length -= 2
                        continue
                elif curr == length-1:
                    if s[curr-1].upper() == s[curr] and s[curr] != s[curr-1]:
                        s.pop()
                        s.pop()
                        length -= 2
                        continue
                else:
                    if s[curr+1].upper() == s[curr] and s[curr+1] != s[curr]:
                        s.pop(curr+1)
                        s.pop(curr)
                        curr = 0
                        length -= 2
                        continue  
                    elif s[curr-1].upper() == s[curr] and s[curr] != s[curr-1]:
                        s.pop(curr-1)
                        s.pop(curr-1)
                        curr = 0 if curr < 2 else curr - 2
                        length -= 2
                        continue
            curr+=1
        return ''.join(s)
        