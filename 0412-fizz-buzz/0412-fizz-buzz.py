class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [""] * n 
    
        for i in range(0, n):
            j = i+1
            if j % 3 == 0 and j % 5 == 0:
                res[i] = "FizzBuzz"
            elif j % 3 == 0:
                res[i] = "Fizz"
            elif j% 5 == 0:
                res[i] = "Buzz"
            else:
                res[i] = str(j)

        return res