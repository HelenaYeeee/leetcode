# typical code pattern for two pointers! important to memorize it
# Set up two pointers respectively in “word” and “abbr”, travel along it and determine how they move along based on conditions. 

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 # index to traverse word
        j = 0 # index to traverse abbr 

        m = len(word)
        n = len(abbr)

        while i < m and j < n: 
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False # leading zero is not allowed 
            elif abbr[j].isnumeric(): 
                k=j
                # when arriving at first non-zero numeric character in abbr, 
                # set k equalt to it and go along the numeric part  
                while k<n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k]) # why not k+1? because after exiting the while loop, it already implies that the current k is not numeric 
                j = k
            else:
                return False
        
        return i==m and j==n
