class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0] *len(position)
        merge = []
        
        for i in range(len(position)):
            merge.append((position[i], speed[i]))
            
        merge.sort()

        for i in range(len(merge)):
            time[i] = (target-merge[i][0])/merge[i][1]
        
        fleet = 0
        idx = len(time)-1
        
        while idx >= 0:
            curr = time[idx]
            fleet+=1
            while idx >= 0 and time[idx-1] <= curr:
                idx -= 1
            idx -= 1
        
        
        return fleet
        
        
        