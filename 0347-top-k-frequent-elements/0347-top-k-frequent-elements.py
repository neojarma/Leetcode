class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = defaultdict(int)
        res = []
        count = []

        for i in nums:
            myMap[i] += 1
        
        srted = list(sorted(myMap.values(), reverse=True))
        desired = srted[:k]
        
        for i in desired:
            for j in myMap:
                if myMap[j] == i and j not in count:
                    res.append(j)
                    count.append(j)

        return res