from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


import itertools
class CumSum1D():
    def __init__(self):
        pass
    def load(self, a):
        self.sdat = list(itertools.accumulate(itertools.chain([0], a)))
    def query(self, l ,r): # query [a, b)
        return self.sdat[r] - self.sdat[l]


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        from bisect import bisect_left, bisect_right
        nums.sort()
        cum = CumSum1D()
        cum.load(nums)
        n = len(nums)
        ans = []
        #print(nums)
        for x in queries:
            sind = bisect_left(nums, x)
            # sind個小さいのがある
            ssum = cum.query(0, sind)
            scnt = sind
            scan = x * sind
            #print(x, ssum, scan, sind, scnt)

            lind = bisect_right(nums, x)
            lcnt = n - lind
            lcan = x * lcnt
            lsum = cum.query(lind, n)
            #print(x, lsum, lcan, lind, lcnt)
            #print(">", abs(ssum - scan) , abs(lsum - lcan))
            ans.append(abs(ssum - scan) + abs(lsum - lcan))
        #print(ans)
        return ans






st = Solution()

print(st.minOperations(nums = [3,1,6,8], queries = [1,5])==[14,10])
print(st.minOperations( nums = [2,9,6,3], queries = [10])==[20])
print(st.minOperations( nums = [1, 3,3,3, 5], queries = [1, 3, 5])==[10,4,10])

