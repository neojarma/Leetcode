class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = [''] * len(heights)
        mapp = {}
        
        index = 0
        for a, b in zip(names, heights):
            mapp[b] = a
        
        srted = sorted(heights, reverse=True)
        
        for i in range(len(srted)):
            result[i] = mapp[srted[i]]
        
        return result

        