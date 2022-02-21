from typing import List, Tuple
from pprint import pprint


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a = []
        b = []
        c = []
        for x in nums:
            if x < pivot: a.append(x)
            if x == pivot: b.append(x)
            if x > pivot: c.append(x)
        return a+b+c

st = Solution()


print(st.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))
print(st.pivotArray(nums = [-3,4,3,2], pivot = 2))
