class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        # ({[ ]})

        for i in s:
            if i == '(' or i == '{' or i == '[':
                temp.append(i)
            else:
                if len(temp) == 0:
                    return False
                    
                last = temp[len(temp)-1]
                pair = brackets[last]

                if i != pair:
                    return False
                else:
                    temp.pop()

        return len(temp) == 0 