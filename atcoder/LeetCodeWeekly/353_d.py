from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class BinaryIndexTreeSum0Origin:
    def __init__(self, n): # [1-n]を作る
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i): # [0, i)のsumを取る
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def addPoint(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def rangesumCloseOpen(self, i, j): # [i, j) の和 Close-Open
        assert i <= j
        return self.sum(j-1) - self.sum(i-1)

class RangeUpdate0Origin:
    def __init__(self, n):
        self.p = BinaryIndexTreeSum0Origin(n + 1)
        self.q = BinaryIndexTreeSum0Origin(n + 1)

    def addPoint(self, s, x):
        self.addCloseOpen(s, s+1, x)

    def addCloseOpen(self, s, t, x):
        #t += 1
        self.p.addPoint(s, -x * s)
        self.p.addPoint(t, x * t)
        self.q.addPoint(s, x)
        self.q.addPoint(t, -x)

    def sumCloseOpen(self, s, t): # [s, t]
        #t += 1
        return self.p.sum(t) + self.q.sum(t) * t - \
               self.p.sum(s) - self.q.sum(s) * s


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        bit = RangeUpdate0Origin(n)
        for i in range(n):
            bit.addPoint(i, nums[i])

        for i in range(n - k + 1):
            curval = bit.sumCloseOpen(i, i + 1)
            if curval < 0: return False
            bit.addCloseOpen(i, i+k, -curval)

        #for i in range(n):
        #    print(bit.sumCloseOpen(i, i+1))

        can = True
        for i in range(n):
            if bit.sumCloseOpen(i, i+1) != 0:
                can = False
                break
        return can


st = Solution()

print(st.checkArray(nums = [2,2,3,1,1,0], k = 3)==True)
print(st.checkArray(nums = [1,3,1,1], k = 2)==False)
print(st.checkArray(nums = [1,0,1,0,1], k = 2)==False)
print(st.checkArray(nums = [1,0,1,0,1], k = 1)==True)
print(st.checkArray(nums=[60,72,87,89,63,52,64,62,31,37,57,83,98,94,92,77,94,91,87,100,91,91,50,26], k=4) == True)

