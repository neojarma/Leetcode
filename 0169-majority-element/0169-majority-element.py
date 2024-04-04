class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        candidate = nums[0]
        
        for num in nums:
            if counter == 0:
                counter += 1
                candidate = num
            elif candidate != num:
                counter -= 1
            else:
                counter += 1
                
            
        
        return candidate