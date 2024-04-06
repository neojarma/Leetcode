class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for x in s:
            if stack:
                equalLower = stack[-1].lower() == x.lower()
                equalUpper = stack[-1].upper() == x.upper()
                badString = stack[-1] != x
                
                if equalLower and equalUpper and badString:
                    stack.pop()
                    continue
            
            stack.append(x)
        
        return ''.join(stack)