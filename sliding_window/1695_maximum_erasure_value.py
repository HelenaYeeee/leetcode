# sol 1. sliding window 
# my sol (good enough)

class Solution:
    from collections import Counter
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0 
        left = 0 
        right = 0 
        n = len(nums)
        window_sum = 0 
        char_counter = Counter()

        while right < n:
            current_char = nums[right]
            window_sum += current_char
            char_counter[current_char] += 1

            while char_counter[current_char] > 1:
                # move left counter to the right until it doesn't contain duplicate char
                char_counter[nums[left]] -= 1
                window_sum -= nums[left]
                left += 1
            ans = max(ans, window_sum)
            right += 1
        
        return ans 
            
# sol 2 (best). sliding window + last seen index stored in dict 
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        last_index_map = dict() # key = element, value = last seen index
        prefix_sum = [0] * (n+1)

        ans = 0
        left = 0 
        right = 0 

        while right < n: 
            current_char = nums[right]
            prefix_sum[right+1] = prefix_sum[right] + current_char
            if current_char in last_index_map: 
                left = max(left, last_index_map[current_char] + 1) # note we move left pointer to last seen index + 1
            # update last index map
            last_index_map[current_char] = right
            # update ans 
            ans = max(ans, prefix_sum[right+1] - prefix_sum[left])
            
            right += 1
        return ans 



