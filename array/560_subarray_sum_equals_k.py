# my sol 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # correct but time out :(, how to optimize? 

        # two cases: 1. the list element value itslef = k 2. sum of a sequences of multi-element arrray = k

        count_case_1 = len([i for i in nums if i == k])

        count_case_2 = 0 

        for left in range(len(nums)):
            cul_sum = nums[left] #culmulative sum 
            for right in range(left+1, len(nums)):
                cul_sum += nums[right]
                if cul_sum == k: 
                    # print("left, right: {}, {}".format(left, right))
                    count_case_2 += 1
        # print(count_case_1, count_case_2)
        return count_case_1 + count_case_2


# sol 2 (best)
# using hash table (dict) so that we only do one-pass over the nums list
# the intuition comes from sol 3, which is a variant of cumulative sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        PrefixSum = 0

        hashmap[0] = 1 # base case
        
        for i in range(len(nums)):
            PrefixSum += nums[i]
            if PrefixSum - k in hashmap.keys():
                # note: add count by frequency of (PrefixSum - k), not by 1! 
                # this if statement can't be placed after the if else below, failed test case: nums=[1], k = 0
                count += hashmap.get(PrefixSum - k) 
            if PrefixSum not in hashmap.keys():
                hashmap.update({PrefixSum:1})
            else: 
                frequency = hashmap.get(PrefixSum)
                hashmap.update({PrefixSum:frequency+1})
            

            
        return count

            
# sol 3: cumulative sum 
# two pass using culmulative sum 
# in cul_sum, the ith element should be the culmulative sum of all element up to (i-1)th element  
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # create an list of cumulative sum 
        
        count = 0
        cul_sum = []
        cul_sum.append(0)
        
        for i in range(1, len(nums)+1):
            cul_sum.insert(i, cul_sum[i-1] + nums[i-1])
        
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if cul_sum[j+1] - cul_sum[i] == k: 
                    count += 1
        return count