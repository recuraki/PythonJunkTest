from typing import List, Tuple
from pprint import pprint


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dat = []
        for x in s: dat.append(ord(x) - ord("a"))
        print(dat)
        n = len(s)
        dp = [[0] * 26 for _ in range(n+1)]
        for i in range(len(s)):
            cur = dat[i]
            for j in range(26): dp[i+1][j] = dp[i][j]
            dp[i+1][cur] = max(1, dp[i+1][cur]) # ここから開始するパターン
            for j in range(-k, k+1):
                prev = cur + j
                if not (0 <= prev < 26): continue
                dp[i+1][cur] = max(dp[i+1][cur], dp[i][prev] + 1)
        return (max(dp[-1]))





st = Solution()

print(st.longestIdealString(s = "acfgbd", k = 2)==4)
print(st.longestIdealString( s = "abcd", k = 3)==4)
print(st.longestIdealString( s = "a", k = 3)==1)

