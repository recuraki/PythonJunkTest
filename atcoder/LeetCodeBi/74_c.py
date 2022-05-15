from typing import List, Tuple
from pprint import pprint


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        from fractions import Fraction
        firsttotal = sum(nums)
        cur = firsttotal
        target = firsttotal / 2
        from heapq import heapify, heappush, heappop
        q = []
        for x in nums:
            heappush(q, -x)
        ans = 0
        while cur > target:
            ans += 1
            x = heappop(q)
            x = -x
            cur -= x
            cur += x / 2
            heappush(q, -x / 2)
        return ans






st = Solution()

print(st.halveArray(nums = [5,19,8,1])==3)
print(st.halveArray(nums = [3,8,20])==3)

