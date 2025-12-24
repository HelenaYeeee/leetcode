# my sol using stack (best)

class Solution:
    def isValid(self, s: str) -> bool:
        # use stack 
        # let () be symbol 1, [] be symbol 2, {} be symbol 3
        mapping = {"(": 1, "[": 2, "{": 3, ")": 1, "]": 2, "}":3}
        stack = []
        ans = True 

        for i, val in enumerate(s):
            if val in "([{":
                stack.append(mapping[val])
            else:
                if stack and mapping[val] == stack[-1]:
                    stack.pop()
                else: 
                    ans = False
        
        if stack: 
            ans = False
        
        return ans 