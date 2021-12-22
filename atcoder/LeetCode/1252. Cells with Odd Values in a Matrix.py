class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        ans = [[0] * n for _ in range(m)]
        for h, w in indices:
            for i in range(n): ans[h][i] += 1
            for i in range(m): ans[i][w] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if ans[j][i] % 2 == 1: res += 1
        return res
