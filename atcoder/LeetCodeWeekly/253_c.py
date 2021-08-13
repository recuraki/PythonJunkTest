
from typing import List, Tuple
from pprint import pprint


class Solution:
    def minSwaps(self, s: str) -> int:
        mi = 10**9
        ma = -1
        val = 0
        import math
        for x in s:
            if x=="[": val += 1
            else: val -= 1
            mi = min(mi, val)
            ma = max(ma, val)
        mi = -mi
        res = math.ceil(mi / 2)
        #print(mi, ma)
        return res

st = Solution()

print(st.minSwaps("][]["))
print(st.minSwaps("]]][[["))
print(st.minSwaps("[]"))

