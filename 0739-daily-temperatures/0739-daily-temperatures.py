class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] #hold the [temp and idx]
        
        for i, v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                sTemp, sIdx = stack.pop()
                res[sIdx] = i - sIdx
            stack.append([v,i])
        
        
        return res