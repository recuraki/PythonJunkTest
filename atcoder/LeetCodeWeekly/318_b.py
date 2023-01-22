from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

import collections
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cur = 0
        n = len(nums)
        se = collections.defaultdict(int)
        for i in range(k):
            x = nums[i]
            cur += x
            se[x] += 1
        if len(se) == k:
            ans = max(ans, cur)
        l = 0
        r = k - 1
        for i in range(1, n - k + 1):
            # leave
            se[nums[l]] -= 1
            if se[nums[l]] == 0: del se[nums[l]]
            cur -= nums[l]
            l += 1
            # enter
            r += 1
            se[nums[r]] += 1
            cur += nums[r]

            if len(se) == k:
                ans = max(ans, cur)
        print(ans)
        return ans

st = Solution()

print(st.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)==15)
print(st.maximumSubarraySum(nums = [4,4,4], k = 3)==0)
print(st.maximumSubarraySum(nums = [1,2,3], k = 1)==3)
print(st.maximumSubarraySum(nums = [3,2,1], k = 1)==3)
print(st.maximumSubarraySum(nums = [3], k = 1)==3)
print(st.maximumSubarraySum(nums = [3,2,1], k = 3)==6)

