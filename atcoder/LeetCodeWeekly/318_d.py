from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

"""
dp[ind][Rcnt]:
 indまで選んだ時の、Rを向いているロボットの数Rcntの時のコスト
 Noneのときそれは存在しない
"""

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        import collections
        INF = 10**18
        fac = defaultdict(int)
        for a,b in factory:
            fac[a] += b
        rob = []
        for x in robot:
            if x in fac:
                fac[x] -= 1
                continue
            rob.append(x)
        faclist = []
        for k in fac.keys():
            for _ in range(fac[k]):
                faclist.append(k)
        robot = None
        factory = None
        fac = None
        rob.sort()
        faclist.sort()
        dp = [[INF] * 110 for _ in range(110) ]
        dp[0][0] = 0
        n = len(rob)
        from bisect import bisect_left, bisect_right
        for ind in range(n):
            robotx = rob[ind]
            for rcnt in range(105):
                lcnt = ind - rcnt
                if dp[ind][rcnt] == INF: continue
                # 右移動
                baseind = bisect_left(faclist, robotx)
                lind = baseind - 1 - (ind - rcnt)
                rind = baseind + rcnt
                print(ind, rcnt, lind, rind)
                if lind >= 0:
                    dp[ind+1][rcnt] = min(dp[ind+1][rcnt], dp[ind][rcnt] + abs(faclist[lind] - robotx))
                if rind < len(faclist):
                    dp[ind+1][rcnt+1] = min(dp[ind+1][rcnt+1], dp[ind][rcnt] + abs(faclist[rind] - robotx))
        ans = INF
        for i in range(105):
            ans = min(ans, dp[n][i])
        return ans




st = Solution()
print(st.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]])==4)
print(st.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]])==2)
print(st.minimumTotalDistance([9,11,99,101],
[[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]])== 6)

