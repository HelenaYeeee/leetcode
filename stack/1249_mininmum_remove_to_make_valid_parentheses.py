# sol 1. stack + string builder 
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        stack = []
        index_to_remove = set() 

        for i, val1 in enumerate(s):
            if val1 in "()":
                if val1 == ")":
                    if not stack:
                        index_to_remove.add(i)
                    else: 
                        stack.pop() # ")" found a matching "("
                elif val1 == "(":
                    stack.append(i)
        
        # after for loop, any remaining element in stack is unmatched "(" that needs to be removed 
        index_to_remove = index_to_remove.union(set(stack))

        # iterate through string "s" and exclude index_to_remove
        s_new = []
        for i, val1 in enumerate(s):
            if i not in index_to_remove: 
                s_new.append(val1)
        ans = "".join(s_new)
        return ans
