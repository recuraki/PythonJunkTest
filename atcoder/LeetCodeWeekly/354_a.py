from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for ii in range(n):
            i = ii+1
            if n % i == 0:
                ans += nums[ii]**2
        return ans




st = Solution()

print(st.sumOfSquares([1,2,3,4])==21)
print(st.sumOfSquares([2,7,1,19,18,3])==63)

