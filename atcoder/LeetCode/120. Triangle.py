"""
2
3 4
6 5 7
4 1 8 3
解説を読むと、i or i+1に降りられる。
dpでよい。i 0..n-1で、+1のindexでminをとる。
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        inf = (1 << 61)
        n = len(triangle)
        dp = [[inf] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for lv in range(0, n - 1):
            for i in range(0, lv + 1):
                dp[lv + 1][i] = min(dp[lv + 1][i], dp[lv][i] + triangle[lv + 1][i])
                dp[lv + 1][i + 1] = min(dp[lv + 1][i + 1], dp[lv][i] + triangle[lv + 1][i + 1])
        # print(dp)
        return (min(dp[-1]))

