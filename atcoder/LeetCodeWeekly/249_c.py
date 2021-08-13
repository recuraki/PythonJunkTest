from typing import List, Tuple
from pprint import pprint


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        oh = m
        ow = n
        dp = [[[0] * 3 for _ in range(ow)]  for _ in range(oh)]
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        dp[0][0][2] = 1
        pprint(dp)
        for h in range(oh):
            for w in range(ow):
                if h==0 and w == 0: continue
                #print("proc", h, w)
                if h == 0:
                    dp[h][w][0] = dp[h][w-1][1] + dp[h][w-1][2]
                    dp[h][w][1] = dp[h][w-1][0] + dp[h][w-1][2]
                    dp[h][w][2] = dp[h][w-1][0] + dp[h][w-1][1]
                    for xxx in range(3): dp[h][w][xxx] %= mod
                    continue
                if w == 0:
                    dp[h][w][0] = dp[h-1][w][1] + dp[h-1][w][2]
                    dp[h][w][1] = dp[h-1][w][1] + dp[h-1][w][2]
                    dp[h][w][2] = dp[h-1][w][1] + dp[h-1][w][2]
                    for xxx in range(3): dp[h][w][xxx] %= mod
                    continue
                # 上 x 左
                dp[h][w][0] += dp[h-1][w][1] * dp[h][w-1][1]
                dp[h][w][0] += dp[h-1][w][2] * dp[h][w-1][2]
                dp[h][w][0] += dp[h-1][w][2] * dp[h][w-1][1]
                dp[h][w][0] += dp[h-1][w][1] * dp[h][w-1][2]

                dp[h][w][1] += dp[h-1][w][0] * dp[h][w-1][0]
                dp[h][w][1] += dp[h-1][w][2] * dp[h][w-1][2]
                dp[h][w][1] += dp[h-1][w][2] * dp[h][w-1][0]
                dp[h][w][1] += dp[h-1][w][0] * dp[h][w-1][2]

                dp[h][w][2] += dp[h-1][w][0] * dp[h][w-1][0]
                dp[h][w][2] += dp[h-1][w][1] * dp[h][w-1][1]
                dp[h][w][2] += dp[h-1][w][1] * dp[h][w-1][0]
                dp[h][w][2] += dp[h-1][w][0] * dp[h][w-1][1]
                for xxx in range(3): dp[h][w][xxx] %= mod
        pprint(dp)
        print(sum(dp[oh-1][ow-1]) % mod)

st = Solution()

print(st.colorTheGrid(m = 1, n = 5))
print(st.colorTheGrid(m = 5, n = 1))
#print(st.colorTheGrid(m = 1, n = 2))
print(st.colorTheGrid(m = 5, n = 5))
print(st.colorTheGrid(m = 2, n = 2))
