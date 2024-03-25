from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict



class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def rob(nums: List[int], k: int) -> int:
            dp = [[0] * 2 for _ in range(len(nums))]
            if nums[0] <= k: dp[0][1] = 1
            for i in range(1, len(nums)):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                if nums[i] <= k:
                    dp[i][1] = dp[i - 1][0] + 1
            return max(dp[-1][0], dp[-1][1])

        # [ok, ng) for max value
        # (ng, ok] for min value
        # CATION: ok is result  (NOT mid)
        ng = 0
        ok = 10 ** 9 + 1
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            if (rob(nums, mid) >= k):
                ok = mid;
            else:
                ng = mid;
        return(ok)


st = Solution()

print(st.minCapability(nums = [2,3,5,9], k = 2)==5)
print(st.minCapability(nums = [2,7,9,3,1], k = 2)==2)

