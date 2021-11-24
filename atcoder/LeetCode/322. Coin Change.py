class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 2 ** 61
        dp = ([inf] * amount) + [0]
        for x in coins:
            for i in range(amount, -1, -1):
                if (i - x) < 0: break
                if dp[i] == inf: continue
                dp[i-x] = min(dp[i-x], dp[i] + 1)
        if dp[0] == inf: return -1
        return dp[0]