from typing import List, Tuple
from pprint import pprint


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        import itertools
        def countstrs(s):
            return [(k, len(list(g))) for k, g in itertools.groupby(s)]
        ma = max(nums)
        c = countstrs(nums)
        ans = -1
        for x, cnt in c:
            if ma == x: ans = max(ans, cnt)
        return ans



st = Solution()

print(st.longestSubarray( nums = [1,2,3,3,2,2])==2)
print(st.longestSubarray(nums = [1,2,3,4])==1)

