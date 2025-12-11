# sol 1: prefix sum + linear search 

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.total_sum = sum(w) # my mistake: I kept len(w) instead of sum(w)
        self.w = w

        # no need to add the first element as 0 (base case), 
        # because we don't need to subtract right to left as what we do in Q#560 subarray sums equal k 
        for i in range(len(w)):
            if not self.prefix_sum: 
                self.prefix_sum.append(w[i])
            else:
                self.prefix_sum.append(self.prefix_sum[i-1] + w[i])
        #print(self.prefix_sum)


    def pickIndex(self) -> int:
        # generate random int, set it as our search target
        # perform linear search to find the index of the first element where the value > target

        import random 
        target = random.randint(1,self.total_sum) # my mistake: I set start of random range as 0 instead of 1
        #print("target: {}".format(target))
        for i in range(len(self.w)):
            if self.prefix_sum[i] >= target: # my mistake: I used w[i] to compare with target instead of prefix_sum[i]
                return i
        
        return 0





# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# ------------------------

# sol 2: prefix sum + binary search 
# we only change the pickIndex function 

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.total_sum = sum(w) # my mistake: I kept len(w) instead of sum(w)
        self.w = w

        # no need to add the first element as 0 (base case), 
        # because we don't need to subtract right to left as what we do in Q#560 subarray sums equal k 
        for i in range(len(w)):
            if not self.prefix_sum: 
                self.prefix_sum.append(w[i])
            else:
                self.prefix_sum.append(self.prefix_sum[i-1] + w[i])
        #print(self.prefix_sum)


    def pickIndex(self) -> int:
        # generate random int, set it as our search target
        # perform linear search to find the index of the first element where the value > target

        import random 
        target = random.randint(1,self.total_sum) # my mistake: I set start of random range as 0 instead of 1
        
        # do binary search on prefix_sum to find the first element >= target
        low = 0 
        high = len(self.prefix_sum) 

        while low != high: 
            mid = low + (high - low) // 2
            if self.prefix_sum[mid] < target: 
                low = mid + 1
            else: 
                high = mid 
        return low
            





# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()