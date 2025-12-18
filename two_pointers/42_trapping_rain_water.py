# sol 2. DP 
# stores max height to the left and right of the current element 
# in two separate arrays 
class Solution:
    def trap(self, height: List[int]) -> int:
        # find the max height to the left and right of the current index to calculate the number of water 

        left_max = [0] * len(height)
        right_max = [0] * len(height)
        ans = 0

        
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
            
        
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        
        print('left_max: {}'.format(left_max))
        print('right_max: {}'.format(right_max))


        for i in range(len(height)):
            a = min(left_max[i], right_max[i]) - height[i]
            if a > 0:
                ans += a
                 # this if statement is important, 
                 # because when i is at local maximum, it cannot trap water and a will be negative
        return ans
        
        
# sol 1, calculate left_max and right_max without dp 
# correct but will time out 
class Solution:
    def trap(self, height: List[int]) -> int:
        # sol 1, without dp, correct but will timeout
        # find the max height to the left and right of the current index to calculate the number of water 
        ans = 0



        for i in range(len(height)):
            left_max = 0
            right_max = 0
            for j in range(i-1,-1,-1):
                left_max = max(left_max, height[j])
            for j in range(i+1, len(height), 1):
                right_max = max(right_max, height[j])


            a = min(left_max, right_max) - height[i]
            if a > 0:
                ans += a
                 # this if statement is important, 
                 # because when i is at local maximum, it cannot trap water and a will be negative
        return ans
        
        


# sol 3. two pointer 
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) -1 
        left_max, right_max = 0,0

        while left < right: 
            # update left_max and right_max 
            if height[left] > left_max: 
                left_max = height[left]
            if height[right] > right_max: 
                right_max = height[right]
            
            # calculate water
            if left_max < right_max: 
                ans += left_max - height[left]
                left += 1
            else: 
                ans += right_max - height[right]
                right -= 1
        return ans

