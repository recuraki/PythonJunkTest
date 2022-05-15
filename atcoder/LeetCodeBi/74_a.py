from typing import List, Tuple
from pprint import pprint


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for k in c.keys():
            if c[k] % 2 != 0:
                return False
        return True


st = Solution()

print(st.divideArray(nums = [3,2,3,2,2,2]))
print(st.divideArray( nums = [1,2,3,4]))

