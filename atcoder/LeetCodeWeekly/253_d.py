from typing import List, Tuple
from pprint import pprint

class Solution:
    class BinaryIndexTreeSum:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def mama(self, i):
            s = 0
            while i > 0:
                s = max(s, self.tree[i])
                i -= i & -i
            return s

        def setValue(self, i, x):
            while i <= self.size:
                self.tree[i] = max(self.tree[i], x)
                i += i & -i


    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        st = self.BinaryIndexTreeSum(len(obstacles))
        res = []
        zatsu = sorted(set(obstacles))
        zatsuTable = dict()
        zatsuTableRev = dict()
        for ind, value in enumerate(zatsu):
            zatsuTable[value] = ind
            zatsuTableRev[ind] = value
        newl = []
        for x in obstacles:
            newl.append(zatsuTable[x])
        for i in range(len(newl)):
            x = newl[i]
            newx = st.mama(x) + 1

            st.setValue(x, newx)
            res.append(newx)
        return res



st = Solution()

print(st.longestObstacleCourseAtEachPosition(obstacles = [1,2,3,2]))
print(st.longestObstacleCourseAtEachPosition(obstacles = [2,2,1]))
print(st.longestObstacleCourseAtEachPosition(obstacles = [3,1,5,6,4,2]))

