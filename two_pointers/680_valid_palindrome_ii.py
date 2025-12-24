# sol 1. two pointers 
# initalize two pionters at the extreme end of s 
# iterate inward 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, left, right):
            # check whether string s from index "left" to "right" is a palindrome 
            
            while left < right: 
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True 
        
        # main function here 
        left = 0
        right = len(s)-1

        while left < right: 
            if s[left] != s[right]:
                # try deleting a character at left or right position
                return is_palindrome(s, left+1, right) or is_palindrome(s, left, right-1)
            else: 
                left += 1
                right -= 1
        return True 

        


# sol 2
# my sol, correct but timeout 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            # check whether string s is a palindrome 
            left = 0 
            right = len(s)-1
            is_even_length = len(s) % 2 == 0 
            
            while left < right: 
                if s[left] != s[right]:
                    return False
                elif is_even_length and right == left + 1 and s[left] == s[right]:
                    return True 
                else:
                    left += 1
                    right -= 1
            return True 
        
        # main function here 
        if is_palindrome(s):
            # s is already a palindrome without modification 
            return True 
        for i in range(len(s)):
            # i = index candidate to remove 
            s_new = s[:i]+s[i+1:] # remove character at index i 
            if is_palindrome(s_new):
                return True 
        return False 
        
        # time complexity: O(n^2)
        # space complexity: O(1)
        