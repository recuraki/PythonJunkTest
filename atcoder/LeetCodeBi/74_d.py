from typing import List, Tuple
from pprint import pprint


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        cum = cumSum1D()
        floor = "0" + floor + ("0" * carpetLen)
        n = len(floor)
        #print(floor)
        l = []
        for x in floor:
            if x == "0": l.append(0)
            else: l.append(1)
        cum.load(l)
        floor = None
        dp = [[0] * (numCarpets + 1) for _ in range(len(l))]
        total = 0
        for i in range(n):
            if l[i] == 1: total += 1
            dp[i][0] = total
        for i in range(carpetLen - 1): # 最初にカーペットの前の数
            for j in range(1, numCarpets+1):
                dp[i][j] = 0
        #print(dp)
        for i in range (carpetLen-1, n): # 全部やる
            for j in range(1, numCarpets+1):
                dp[i][j] = dp[i-1][j] # 1個前をひきつぐ
                if l[i] == 1: dp[i][j] += 1 # なにもしない場合は1なら+1される
                dp[i][j] = min(dp[i][j], dp[i-carpetLen][j-1])

        #print(dp)
        return min(dp[-1])






st = Solution()

print(st.minimumWhiteTiles(floor = "10110101", numCarpets = 2, carpetLen = 2)==2)
print(st.minimumWhiteTiles(floor = "11111", numCarpets = 2, carpetLen = 3)==0)
print(st.minimumWhiteTiles(floor = "111111", numCarpets = 2, carpetLen = 3)==0)
print(st.minimumWhiteTiles(floor = "111111", numCarpets = 1, carpetLen = 3)==3)
print(st.minimumWhiteTiles(floor = "111111", numCarpets = 3, carpetLen = 1)==3)
print(st.minimumWhiteTiles(floor = "110011", numCarpets = 3, carpetLen = 1)==1)

