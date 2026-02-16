# sol 1 (best). sliding window with Counter 
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        char_counter = Counter()
        ans = 0
        left = 0 
        right = 0

        while right < len(s): 
            current_char = s[right]

            char_counter[current_char] += 1
            

            while char_counter[current_char] > 1:
                # move left pointer until no duplicate char in right pointer
                char_counter[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
            right += 1
        return ans

# sol 2. sliding window optimized 
# This is built on top of sol 1. 
# Instead of using Counter to store the frequency of each char, 
# use a dictionary to store the last seen index of the char 
# so that when we see a duplicate char, we can directly move the left pointer
# to last seen index + 1

# Q: why last seen index + 1? 
# A: because last seen index already have the duplicate char

# slightly better performance 
# worst time complexity goes from 2n to n, but still O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # dict stores the index of current character + 1
        # this will be the location the left pointer move to when there is a duplicate in window 
        dictionary = {}
        ans = 0
        i=0

        for j in range(n):
            if s[j] in dictionary: 
                i = max(dictionary[s[j]], i)
            ans = max(ans, j-i+1)
            dictionary[s[j]] = j+1
        return ans 





# sol 3. brute force, will time out 
# two pointers - start index "i", end index "j"
# for each starting index "i", iterate j to the right of i 
# have a local function to check whether the substring (i,j) has duplicate char 
class Solution:
    def check_unique(self, s, i, j):
        # local function to check substring from i to j
        # return boolean to indicate whether there is duplicate char or not 
        char_set = set()
        for idx in range(i,j+1):
            if s[idx] in char_set:
                return False
            else: 
                char_set.add(s[idx])
        return True 


    def lengthOfLongestSubstring(self, s: str) -> int:
        # main function 
        if not s: 
            return 0 
        ans = 0 

        for i in range(len(s)):
            for j in range(i, len(s)):
                is_unique = self.check_unique(s,i,j)
                if is_unique: 
                    ans = max(ans, j-i+1)
        return ans 



# my sol 
# doesn't work, here I analyze the mistakes 
# the overall structure of sliding window is correct,  
# but they way I handle how the pointers move is wrong 

# for correct sol, see sol 1 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        char_set = set() # my mistake: using set is not enough, need to also keep track of frequency 
        ans = 0
        left = 0 
        right = 0

        while right < len(s): 
            # my mistake: logic below is wrong 
            if s[right] not in char_set: 
                char_set.add(s[right])
                
                if right - left > ans:
                    ans = right - left + 1
                right += 1
            elif left < right and s[left] in char_set:
                char_set.remove(s[left])
                left += 1
            else: 
                left += 1
                right += 1
        return ans


