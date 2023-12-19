class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        pair = {
            'type' : 0,
            'color': 1, 
            'name' : 2,
        }
        
        res = 0
        
        for i in range(len(items)):
            if (items[i][pair[ruleKey]] == ruleValue):
                res += 1
        
        return res