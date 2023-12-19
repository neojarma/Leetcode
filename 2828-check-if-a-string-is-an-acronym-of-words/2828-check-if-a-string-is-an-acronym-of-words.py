class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        temp = ''
        
        for i in words:
            temp += i[0]
        
        return temp == s