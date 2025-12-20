# sol 1 brute force 
# my sol, correct but time out 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # number of water =  min of left height and right height * distance between left and right 
        max_water = 0
        for left in range(len(height)-1):
            for right in range(left + 1, len(height)):
                container_height = min(height[left], height[right])
                container_width = right - left 
                water = container_height * container_width
                if water > max_water: 
                    max_water = water
        return max_water



# sol 2 two pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize two pointer on the extreme end of array, then move inward
        max_water = 0 
        left = 0
        right = len(height) - 1

        while left < right: 
            # 1. calculate water
            current_width = right - left
            current_height = min(height[left], height[right])
            current_water = current_height * current_width
            # 2. update max_water
            if current_water > max_water: 
                max_water = current_water

            # 3. decide how to move pointer 
            # since the amount of water is limited by the min of left/right height, 
            # moving pointer with more height doesn't bring any benefit,
            # we move the pointer with less height inward 
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1 
        return max_water

            

        
