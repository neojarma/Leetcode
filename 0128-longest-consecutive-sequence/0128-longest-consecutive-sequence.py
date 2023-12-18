class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # hashset
        sets = set(nums)
        counter = 0

        for i in sets:
            curr = i
            consecutive = 1
            
            # only looking for smallest number in sequence
            if (curr - 1 not in sets):
                # find any consecutive number
                while (curr + 1 in sets):
                    # increment curr number
                    curr += 1
                    consecutive += 1
            
            counter = max(counter, consecutive)
            
        return counter