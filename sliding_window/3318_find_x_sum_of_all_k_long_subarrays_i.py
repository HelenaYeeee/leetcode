# my sol. sliding window + Counter
# accepted 

from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        left = 0
        right = k-1
        n = len(nums)

        while right < n:
            element_counter = Counter(nums[left:right+1])
            element_counter = sorted(element_counter.items(), key=lambda x: (x[1], x[0]), reverse=True)
            top_elements = element_counter[:x]
            subarray_sum = 0 
            for item in top_elements: 
                subarray_sum += item[0] * item[1]
            ans.append(subarray_sum)


            right += 1
            left += 1

        return ans 
