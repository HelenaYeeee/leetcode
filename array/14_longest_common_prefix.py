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
