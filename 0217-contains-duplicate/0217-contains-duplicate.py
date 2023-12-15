class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for i in nums:
            if myMap.get(i) == None:
                myMap[i] = 1
            else:
                return True
        
        return False
            
        