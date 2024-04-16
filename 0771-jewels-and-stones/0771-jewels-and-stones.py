class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        j = set(jewels)
        
        for x in stones:
            if x in j:
                counter+=1
        
        return counter