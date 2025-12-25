# sol 1 (recommended). greedy + stack
# two pass: 
# first remove the higher score substring, 
# get the remaining string
# then remove the lower score substring.
# use stack to evaluate whether a substring 
# can be removed or not.
# the approach of using stack stem from 
# "Q20. Valid Parentheses"

class Solution:
    def remove_substring(self, s, target_pair):
        # local function that uses stack to remove "target_pair" from "s" 
        stack = []

        for val in s:
            if val == target_pair[1] and stack and stack[-1] == target_pair[0]:
                stack.pop()
            else:
                stack.append(val)
        
        # reconstruct the remaining string after removing target pairs 
        return "".join(stack)

    def maximumGain(self, s: str, x: int, y: int) -> int:
        # greedy 
        # reason: the optimal solution comes from getting the point from the most valuable substring first
        total_score = 0 
        high_priority_pair = "ab" if x > y else "ba"
        low_priority_pair = "ba" if high_priority_pair == "ab" else "ab"

        # first pass - remove high priority pair 
        string_after_first_pass = self.remove_substring(s, high_priority_pair)
        removed_pairs_count = (len(s) - len(string_after_first_pass)) /2

        # calculate score from first pass 
        total_score += removed_pairs_count * max(x,y)

        # second pass - remove low priority pair 
        string_after_second_pass = self.remove_substring(string_after_first_pass, low_priority_pair)
        removed_pairs_count = (len(string_after_first_pass) - len(string_after_second_pass)) / 2

        # calculate score from second pass 
        total_score += removed_pairs_count * min(x,y)

        return int(total_score)


# sol 2. greedy, use two pointers (without stack)
# the main function is essentially the same as sol 1 
# I modified the for loop in remove_substring on top of leet sol -> more easy to understand 

# sol 1 > sol 2 because easier to write in interview, 
# and perf is similar
class Solution:
    def remove_substring(self, s, target_substring, points_per_removal):
        # local function to remove target substring and return the score gain after removal 
        # use two pointer to remove substring in place 

        write_index = 0 
        score = 0 
        

        for read_index in range(len(s)):
            s[write_index] = s[read_index]

            if write_index >= 1 \
                and s[write_index-1] == target_substring[0] \
                and s[write_index] == target_substring[1]:
                # we have at least two items and we found a match with target
                write_index -= 2 
                score += points_per_removal
            
            # update write_index 
            write_index += 1
        
        del s[write_index:]
        
        return score 



    def maximumGain(self, s: str, x: int, y: int) -> int:
        # main function, similar to sol 1
        total_score = 0
        s = list(s)

        if x > y:
            total_score += self.remove_substring(s, "ab", x)
            total_score += self.remove_substring(s, "ba", y)
        else: 
            total_score += self.remove_substring(s, "ba", y)
            total_score += self.remove_substring(s, "ab", x)
        return total_score

# sol 3. greedy with two counters 
# note that in "if x < y", s needs to be reversed so that 'ba' becomes 'ab'
# since we only care about the score, 
# reversing the string in place won't affect the result.
# also in the same if, don't forget to swap x and y 
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # let 'ab' score always >= 'ba' score
        if x < y: 
            s = s[::-1] 
            x,y = y,x
        
        a_count = 0
        b_count = 0
        total_score = 0

        for i in range(len(s)):
            if s[i] == 'a':
                a_count += 1
            elif s[i] == 'b':
                if a_count > 0:
                    # there is unmatched 'a' available, immediately form 'ab'
                    a_count -= 1
                    total_score += x
                else: 
                    # cannot form 'ab', increment b_count for future 'ba'
                    b_count += 1
            else: 
                # current character is not a or b, calculate all saved 'ba' score
                # and reset counter 
                total_score += min(a_count, b_count) * y
                a_count = 0
                b_count = 0
        total_score += min(a_count, b_count) * y
        return total_score