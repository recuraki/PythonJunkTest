"""
連続なので、基本的に前のを継承する。
[0] 選んでいない今
 -のとき0
[1] 何かを選んだ未来
"""


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0] = max(0, nums[0])
        dp[0][1] = nums[0] ** 2
        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i], dp[i - 1][0] + nums[i])
            dp[i][1] = max(dp[i - 1][0] + nums[i] ** 2, dp[i - 1][1] + nums[i], nums[i] ** 2)
        ans = -(2 ** 61)
        for i in range(0, len(nums)): ans = max(ans, max(dp[i]))
        return ans
