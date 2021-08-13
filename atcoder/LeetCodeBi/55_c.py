from typing import List, Tuple
from pprint import pprint


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n+1)]
        for i in range(n ):
            dp[i+1][0] = dp[i][1] + nums[i]
            dp[i+1][1] = dp[i][0] - nums[i]

            dp[i+1][0] = max(dp[i][0], dp[i+1][0])
            dp[i+1][1] = max(dp[i][1], dp[i+1][1])

        return max(dp[n])

st = Solution()

print(st.maxAlternatingSum(nums = [4,2,5,3]))
print(st.maxAlternatingSum(nums = [5,6,7,8]))
print(st.maxAlternatingSum(nums = [6,2,1,2,4,5]))

