# dp[a] is the # of coins to make amount a. dp[a - c] makes a - c
# this means that dp[a] only get calculated if it is a valid way to reach a.
# dp[a] only gets updated IFF dp[a - c] is valid, making dp[a] = a

# this works as we go up from 1, running through every possible coin iteration
# while saving the work of all repeated calculations/ iterations. otherwise we
# would have to do them all.
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # in case a - c = 0

        for a in range(1, amount + 1):
            for c in coins:
                remainder = a - c
                if remainder >= 0: # if we can use c
                    cur_coins = 1 + dp[remainder] # add 1 to the previous
                    dp[a] = min(dp[a], cur_coins)
        if dp[amount] != amount + 1:
            return dp[amount]
        return -1

solution = Solution()
print(solution.coinChange([1,5,10], 12))
