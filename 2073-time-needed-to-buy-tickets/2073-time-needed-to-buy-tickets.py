class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         0 1 2 person
#         2 3 2 ticket
        
#         4 3 1 2 3 1
#         2
# 1 
# 2-2 = 0
# 3-3=0

# 2 = 2 - (2-val-1)
# 0 =2 - (2-0)
# 0 = 3 - (3-0)
# x = 3 - (3-1)
# x = 3 - 2

#         i = i - (i-k) if negative then i
#         j = j - (k-i-1)
# 3 - (3-1) 1
        
#     [84,49,5,24,70,77,87,8]
#     3
    
        res = 0
        val = tickets[k]
        
        for i,v in enumerate(tickets):
            if i <= k:
                print(v)
                minus = v - val if v - val > 0 else 0
                t = v - (minus)
                # 5 - (5-24)
                # 5 - -21
                res += t if t > 0 else v
                # if t > 0:
                #     res += t
                # else:
                #     print(res)
                # res += v
            else:
                minus = val-1 if v - (val - 1) > 0 else v
                t = v - (v-(minus))
                # 1 - (1-4)
                # 1 - -3
                
                
                res += t   
        
        return res