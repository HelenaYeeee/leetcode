# solution 1 - brute force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force, pass through the list two times
        # to find the max difference between buying on the current day and selling on any day after it 

        # Time complexity: O(n^2)
        # Space complexity: O(1)
        MaxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > MaxProfit:
                    MaxProfit = prices[j] - prices[i]
        
        return MaxProfit


# solution 2 - optimized 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # one-pass solution 
        # keep track of two variables: 
        # 1. max profit 
        # 2. minimum prices we've seen so far -> this may lead to max profit, or maybe not.. but it's fine, we just need to return the max profit 

        MaxProfit = 0
        MinPriceSoFar = float("inf") # set as max value, so that any stock price will overwrite it 

        for i in range(len(prices)):
            if prices[i] < MinPriceSoFar: 
                MinPriceSoFar = prices[i]
            elif prices[i] - MinPriceSoFar > MaxProfit: # this is elif because you can't buy & sell at the same day
                MaxProfit = prices[i] - MinPriceSoFar
        
        return MaxProfit
