class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        inf = 2**61
        n = len(nums)
        dp = [inf] * n
        ans = -1
        for x in nums:
            ind = bisect_left(dp, x)
            dp[ind] = x
            ans = max(ans, ind + 1)
        return ans