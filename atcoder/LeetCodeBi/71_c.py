from typing import List, Tuple
from pprint import pprint


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        os = startAt
        ans = 10 ** 18
        for t in range(0, 10000):
            s = str(t).zfill(4)
            se = int(s[0] + s[1]) * 60 + t%100
            #print(s, se)
            if se == targetSeconds:
                #print(t, "--")
                cost = 0
                startAt = os
                for ch in list(str(t)):
                    x = int(ch)
                    if startAt != x:
                        cost += moveCost
                        #print("m", moveCost)
                        startAt = x
                    cost += pushCost
                    #print("p", pushCost)
                ans = min(ans, cost)
        return ans





st = Solution()

print(st.minCostSetTime(startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600))
print(st.minCostSetTime(startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76))
