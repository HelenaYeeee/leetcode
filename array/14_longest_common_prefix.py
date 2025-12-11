# my solution -> beats 100% with a simple solution! good job
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        
        # loop through each word and find the common prefix by each character
        j=0
        while j < len(min(strs, key=len)):
            # the while condition is this because the longest common prefix can't be longer than the shortest word
            prefix_candidate = strs[0][j]
            for i in range(len(strs)): 
                
                if strs[i][j]  != prefix_candidate: 
                    return prefix 
            prefix += prefix_candidate 
            j += 1
        
        return prefix 


# leetcode's solution: 
# another way is to set the prefix candidate to be the first word,
# then keep reducing it until it matches the start of all words

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix

# there are other approaches too, like BFS, but it is unnecessarily complex for this problem 
