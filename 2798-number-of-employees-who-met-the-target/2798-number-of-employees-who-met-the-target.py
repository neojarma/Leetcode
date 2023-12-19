class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        srted = sorted(hours)

        if srted[-1] < target:
            return 0

        count = 0
        for i in range(len(srted)-1, -1, -1):
            if srted[i] >= target:
                count += 1
            
        return count
            