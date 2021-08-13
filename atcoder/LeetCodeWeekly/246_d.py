from typing import List, Tuple
from pprint import pprint


class cumSum1D(object):
    sdat = []
    def init(self):
        pass
    def load(self, l):
        import itertools
        self.sdat = list(itertools.accumulate(itertools.chain([0], l)))
    def query(self, l, r):
        """
        query [l, r)
        """
        # assert l < r
        return self.sdat[r] - self.sdat[l]

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        from copy import deepcopy
        d1 = []
        for i in range(110):
            x = cumSum1D()
            d1.append(x)
        l = [[0] * (10**5 + 10) for _ in range(110)]
        for i in range(len(nums)):
            l[nums[i]][i] = 1
        for i in range(110):
            d1[i].load(l[i])
        res = []
        for l, r in queries:
            n1 = n2 = None
            can = []
            for i in range(110):
                if n1 is not None and n2 is not None:
                    break
                if d1[i].query(l, r+1) != 0:
                    can.append(i)
            diff = []
            for i in range(len(can) - 1):
                diff.append(can[i+1] - can[i])
            #print(l,r, can, diff)
            if len(diff) == 0:
                res.append(-1)
            else:
                diff.sort()
                x = deepcopy(diff[0])
                res.append(x)
        return res


st = Solution()

print(st.minDifference(nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]))
print(st.minDifference(nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]))
print(st.minDifference([10,13,15,9,13,8,8,7,14,12],
[[4,7],[3,4],[4,8],[3,7],[6,8],[0,8],[5,7],[7,8],[5,8],[5,8]]))

