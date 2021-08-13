from typing import List, Tuple
from pprint import pprint


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from copy import deepcopy
        oh = len(points)
        ow = len(points[0])
        pl = deepcopy(points[0])
        for h in range(1, oh):
            #print("h", h)
            cfromL = [-10] * ow
            cfromR = [-10] * ow
            x = -100
            for i in range(0, ow):
                x = max(x - 1, pl[i])
                cfromL[i] = x
            x = - 100
            for i in range(ow-1, -1, -1):
                x = max(x - 1, pl[i])
                cfromR[i] = x
            for i in range(ow):
                pl[i] = max(cfromL[i], cfromR[i])+ points[h][i]
            #print(cfromL)
            #print(cfromR)
            #print(pl)
        return max(pl)



st = Solution()

print(st.maxPoints(points = [[1,2,3],[1,5,1],[3,1,1]]))
print(st.maxPoints(points = [[1,5],[2,3],[4,2]]))
print(st.maxPoints(points = [[1,2,5,7,3,4]]))
print(st.maxPoints(points = [[1],[1]]))

print(st.maxPoints([[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]) == 15)