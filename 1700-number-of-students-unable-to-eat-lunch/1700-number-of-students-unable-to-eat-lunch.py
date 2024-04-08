class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        c0 = 0
        c1 = 0
        for x in students:
            if x == 0:
                c0 += 1
            else:
                c1 += 1
                
        for x in sandwiches:
            if x == 0:
                if c0 > 0:
                    res -= 1
                    c0 -= 1
                else:
                    return res
            else:
                if c1 > 0:
                    res -= 1
                    c1 -= 1
                else:
                    return res
        
        return res