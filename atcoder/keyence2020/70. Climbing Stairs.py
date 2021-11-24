class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 100
        dp[0] = 1
        for i in range(80):
            dp[i + 1] += dp[i]
            dp[i + 2] += dp[i]

        return dp[n]