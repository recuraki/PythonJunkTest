from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        t1 = sum(nums)
        t2 = 0
        for x in nums:
            for a in str(x):
                t2 += int(a)
        return abs(t1 - t2)


st = Solution()

print(st.differenceOfSum(nums = [1,15,6,3])==9)
print(st.differenceOfSum(nums = [1,2,3,4])==0)

