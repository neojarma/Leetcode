class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if token == '*':
                a = nums.pop(-1)
                b = nums.pop(-1)
                nums.append(b * a)
            elif token == '/':
                a = nums.pop(-1)
                b = nums.pop(-1)
                nums.append(int(b / a))
            elif token == '+':
                a = nums.pop(-1)
                b = nums.pop(-1)
                nums.append(b + a)
            elif token == '-':
                a = nums.pop(-1)
                b = nums.pop(-1)
                nums.append(b - a)
            else:
                nums.append(int(token))

        return nums[0]

        