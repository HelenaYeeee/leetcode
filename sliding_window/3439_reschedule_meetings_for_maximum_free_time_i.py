# sol 1 (best). greedy + sliding window 
# we are allowed to move meetings "k" times, so we keep sliding window that includes k meetings 
# for each window position, evaluate the free time to the left of all meetings + to the right of the last meeting 

# gap = free time, I used it interchangeably
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        left = 0 
        right = 0 
        n = len(startTime) # n = number of meetings 
        free_left = 0 # length of free time interval to the left of meetings, only part of the final answer 
        ans = 0 # length of max free time interval, final answer

        free_right = 0 

        # move right pointer as much as possible until we included k meetings in our sliding window
        while right < k: 
            # calculate gap before the r-th meeting 
            if right == 0:
                # the left most meeting
                one_left_interval = startTime[right] 
            else: 
                # for all other meetings
                one_left_interval = startTime[right] - endTime[right-1]
            free_left += one_left_interval 
            right += 1
        
        # now we used all "k" chances to move meetings, 
        # calculate gap to the right of the last considered meeting 
        if right == n: 
            free_right = eventTime - endTime[-1]
        else: 
            free_right = startTime[right] - endTime[right - 1]
        ans = max(ans, free_left + free_right)

        # move left pointer and right pointer one at a time 
        while right < n: 
            # move left by 1
            if left == 0: 
                left_l = startTime[left]
            else: 
                left_l = startTime[left] - endTime[left - 1]
            free_left -= left_l
            left += 1

            # move right by 1
            if right == 0:
                left_r = startTime[right]
            else: 
                left_r = startTime[right] - endTime[right - 1]
            free_left += left_r
            right += 1

            # calculate free time to the right 
            if right == n: 
                free_right = eventTime - endTime[-1]
            else: 
                free_right = startTime[right] - endTime[right - 1]

            # update answer 
            ans = max(ans, free_left + free_right)
        return ans




# sol 2. greedy + prefix sum + sliding window 
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        prefix_sum = [0] * (n+1) # note that prefix_sum is of length (n+1)
        ans = 0 

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + (endTime[i] - startTime[i])
        
        for i in range(k-1, n):
            occupied = prefix_sum[i+1] - prefix_sum[i-k+1]
            window_end = eventTime if i == n-1 else startTime[i+1]
            window_start = 0 if i == k-1 else endTime[i-k]
            free_time = window_end - window_start - occupied
            ans = max(ans, free_time)
        
        return ans 
