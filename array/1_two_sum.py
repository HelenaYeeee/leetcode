# my solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for a in range(len(nums)):
            for b in range(a+1, len(nums)): 
                if nums[a] + nums[b] == target: 
                    return [a,b]

# optimized solution using two-pass hash table 
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         # use hash table (dictionary) to save lookup time 
#         hashmap = {}

#         # key is value in the list, value is the index 
#         for idx, val in enumerate(nums):
#             hashmap[val] = idx
        
#         # iterate over nums list and try to find the complement of the current element 
#         for idx, val in enumerate(nums): 
#             complement = target - val
#             print(complement)
#             if complement in hashmap and idx != hashmap[complement]:
#                 return [idx, hashmap[complement]]

#         return []



if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,4,7,11], 9))                
