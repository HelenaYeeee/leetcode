# sol 1. two pointers (best)
class Solution:
    def find_two_sum(self, nums, ans, i):
        # find pairs of elements in nums that adds up to element in index i  
        # and then add them to ans array 
        target = -1 * nums[i]
        left = i+1 
        right = len(nums)-1

        while left < right: 
            if nums[left] + nums[right] == target:
                ans.append((nums[i], nums[left], nums[right])) # append nums[i] instead of target
                left += 1
                right -= 1
                while left < len(nums)-1 and nums[left] == nums[left-1]:
                    left += 1
            elif nums[left] + nums[right] < target: 
                # this condition is equivalent to nums[left] + nums[right] + nums[i] < 0
                left += 1
            else: 
                # this condition is equivalent to nums[left] + nums[right] + nums[i] > 0
                right -= 1 




    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use two pointer solution where target = -nums[i]

        # first, sort the nums array 
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                self.find_two_sum(nums, ans, i)
        return ans 


# sol 2. hash set (without sorting the nums array)
# use complement method, the solution is extended from two sum 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use hash set to keep track of duplicate 
        dup = set()
        ans = set()
        seen = {} # key = element in nums, value = indicate whether we have encountered that element in current iteration

        for i, val1 in enumerate(nums):
            if val1 not in dup: 
                dup.add(val1)

                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen.keys() and seen[complement] == i: 
                        # find a sol! update "ans"
                        # note: here we need to sort the tuple to avoid duplicate 
                        ans.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
                    
        return [list(i) for i in ans]
        