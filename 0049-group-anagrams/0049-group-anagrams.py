class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myMap = defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            myMap[word].append(i)

        return list(myMap.values())