# sol 1 (best). DP + sliding window 
# optimized from sol 2 
# see detailed notes on Notion
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n+1)
        dp[0] = 1

        s = 1 if k > 0 else 0 # s is a sliding window that stores the sum of all states contributing to state "i"

        for i in range(1, n+1):
            dp[i] = s * (1 / maxPts)
            if i < k: 
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k: 
                s -= dp[i - maxPts]
        return sum(dp[k:])




# sol 2. DP 
# will time out, but it helps to understand sol 1
# time complexity: O(n * max Pts)
# space complexity: O(n)
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # use an array dp to store the probabilities of having exactly i points at some moment of the game
        dp = [0] * (n+1)
        dp[0] = 1 

        # i = the sum of all the numbers you have drawn 
        # j = the latest number you draw
        for i in range(1, n+1):
            for j in range(1, maxPts + 1):
                if i-j >= 0 and i-j < k:
                    # the if condition ensure that the game is still going on 
                    # probability of drawing a value = 1 / maxPts 
                    # dp[i] = sum(the probability of transitioning from state i-j to i for all values of j)
                    dp[i] += dp[i-j] * (1 / maxPts)
        # From index k to n in "dp" is the state when the game is over, and Alice has <= n points 
        # Therefore, the answer is the sum of all these probabilities 
        return sum(dp[k:])