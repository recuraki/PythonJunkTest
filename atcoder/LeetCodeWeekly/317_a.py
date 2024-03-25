from typing import List, Tuple
from pprint import pprint


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt = []
        for x in nums:
            if x % 3 == 0 and x%2 == 0: cnt.append(x)
        if len(cnt) == 0:
            return 0
        ans = sum(cnt) // len(cnt)
        return ans


st = Solution()

print(st.averageValue( [1,3,6,10,12,15])==9)
print(st.averageValue([1,2,4,7,10])==0)

