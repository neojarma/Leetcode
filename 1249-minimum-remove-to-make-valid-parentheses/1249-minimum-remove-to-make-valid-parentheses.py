class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        main = []
        pair = []
        indexPair = []
        
        for i, x in enumerate(s):
            if x != '(' and x != ')':
                main.append(x)
            elif x == '(':
                main.append(x)
                pair.append(x)
                indexPair.append(len(main)-1)
            elif x == ')' and pair:
                main.append(x)
                pair.pop()
                indexPair.pop()
        
        for x in reversed(indexPair):
            main.pop(x)
            
        return ''.join(main)
                