from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class ltcnt():
    def __init__(self):
        self.clear()
    def clear(self):
        self.cnt = defaultdict(int)
        self.cost = 0
    def calc(self, l):
        self.clear()
        for x in l:
            self.add(x)
        return self.cost
    def add(self, x):
        if self.cnt[x] == 0:
            self.cnt[x] += 1
            return
        if self.cnt[x] == 1:
            self.cnt[x] += 1
            self.cost += 2
            return
        self.cnt[x] += 1
        self.cost += 1

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        INF = 10**18
        n = len(nums)
        cost = [[0] * n for _ in range(n)]
        #print(cost)
        for i in range(n):
            cnt = ltcnt()
            cnt.clear()
            for j in range(i, n):
                cnt.add(nums[j])
                cost[i][j] = cnt.cost
        # cost計算終わり
        dp = [INF] * (n+1) # i-1まで決まっているときのコスト
        dp[0] = 0
        for ind in range(1, n+1): # indを決めたい
            for start in range(0, ind):
                #print(ind, start)
                dp[ind] = min(dp[ind], dp[start] + k + cost[start][ind-1])


        #print(dp)
        #for x in cost:
        #    print(x)
        return dp[n]



st = Solution()

print(st.minCost(nums = [1,2,1,2,1,3,3], k = 2)==8)
print(st.minCost( nums = [1,2,1,2,1], k = 2)==6)
print(st.minCost(nums = [1,2,1,2,1], k = 5) == 10)


"""
事前計算1000 * 1000で
cost[l][r]: lから

区間DPで
dp[l][r] = l-rが決まっているときの最小コスト
"""


