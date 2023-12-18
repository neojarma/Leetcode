class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatest = max(candies) 
        
        for i in candies:
            result.append((i + extraCandies) >= greatest)
        
        return result
        