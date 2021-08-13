from typing import List, Tuple
from pprint import pprint


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        import math
        rungs = [0] + rungs
        for i in range(len(rungs) - 1):
            d = rungs[i+1] - rungs[i]
            need = math.ceil(d / dist)
            need -= 1
            if need < 0: need = 0
            res += need
        return res




st = Solution()

print(st.addRungs(rungs = [1,3,5,10], dist = 2))
print(st.addRungs(rungs = [3,6,8,10], dist = 3))
print(st.addRungs(rungs = [3,4,6,7], dist = 2))
print(st.addRungs(rungs = [5], dist = 10))
