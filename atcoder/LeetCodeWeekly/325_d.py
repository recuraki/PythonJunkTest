from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

###################################
# Paste the template of question
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        p = 10**9 + 7
        ans = pow(2, len(nums), p)
        dp = [0] * 1001
        dp[0] = 1
        for x in nums:
            print(x)
            newdp = [0] * 1001
            for i in range(1001):
                newdp[i] += dp[i]
                nxt = min(1000, i+x)
                newdp[nxt] += dp[i]
            dp = newdp
        for i in range(k):
            ans -= dp[i]
        ans %= p
        print(ans)
        return ans





st = Solution()

print(st.countPartitions( nums = [1,2,3,4], k = 4)==6)
print(st.countPartitions(nums = [3,3,3], k = 4)==0)
print(st.countPartitions(nums = [6,6], k = 2)==2)
"""
dp[i][j]
 1つ目の箱がi
"""