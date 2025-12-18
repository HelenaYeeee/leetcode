# sol 1. brute force 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i,j):
            # local function that checks whether substring from i to j 
            # is a palidrome
            left = i
            right = j
            while left < right:
                if s[left] != s[right]:
                    return False 
                left += 1
                right -= 1
                
            return True 
        #print(check(0,3))
        ans = s[0]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                #print("checking i={}, j={}, is_palidrome={},len(ans)={}".format(i,j,check(i,j), len(ans)))
                if check(i,j) and j-i+1 > len(ans):
                    ans = s[i:j+1]
        return ans            

# sol 2. DP, store whether substring from i to j is a palindrome in a 2d array 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        ans = [0,0] # i,j interval for the answer 
        

        # check len = 1 
        for i in range(n):
            dp[i][i] = True 
        
        # check len = 2 
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i,i+1]
        
        for diff in range(2, n):
            for i in range(0, n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i,j]

        i,j = ans
        return s[i:j+1]


# Sol 3 expanding from the centers 

# Expand from each center location and find the longest palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i,j):
            # input: i,j index 
            # output: length of palindrome in the input 
            left = i
            right = j

            while left>-1 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
            
            # when the loop ends, it implies that s[left] != s[right],
            # so the actual length should be one step backward
            length = right - left - 1 
            return length

        ans = [0,0]
        # check odd-length palindrome 
        for i in range(len(s)):
            length = expand(i,i)
            if length > ans[1]-ans[0]+1:
                dist = length // 2
                ans = [i-dist, i+dist]
        
        # check even-length palindrome 
        for i in range(len(s)-1):
            length = expand(i,i+1)
            if length > ans[1] - ans[0] + 1: 
                dist = length // 2 - 1
                ans = [i-dist,i+1+dist]
        return s[ans[0]:ans[1]+1]
