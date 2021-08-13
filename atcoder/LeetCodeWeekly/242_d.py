from typing import List, Tuple
from pprint import pprint


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        import itertools
        l = len(stones)
        if l == 2:
            return sum(stones)
        ##############
        can = sum(stones)
        can2 = -






st = Solution()

print(st.stoneGameVIII(stones = [-1,2,-3,4,-5]))
print(st.stoneGameVIII(stones = [7,-6,5,10,5,-2,-6]))
print(st.stoneGameVIII( stones = [-10,-12]))
