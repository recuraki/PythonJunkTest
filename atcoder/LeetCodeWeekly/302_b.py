from typing import List, Tuple
from pprint import pprint


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        ans = -1
        def f(x):
            s = str(x)
            ans = 0
            for i in list(s):
                ans += int(int(i))
            return ans
        for x in nums:
            d[f(x)].append(x)
        for k in d.keys():
            if len(d[k]) < 2: continue
            d[k].sort()
            ans = max(ans, d[k][-1] + d[k][-2])
        return ans





st = Solution()

print(st.maximumSum([18,43,36,13,7])==54)
print(st.maximumSum([10,12,19,14])==-1)

