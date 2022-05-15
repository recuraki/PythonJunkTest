from typing import List, Tuple
from pprint import pprint


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        m = len(artifacts)
        maze = [[-1] * n for _ in range(n)]
        for i in range(m):
            a, b, c, d = artifacts[i]
            for h in range(a, c+1):
                for w in range(b, d+1):
                    maze[h][w] = i
        for h, w in dig:
            maze[h][w] = -1
        buf = [True] * m
        for h in range(n):
            for w in range(n):
                if maze[h][w] == -1: continue
                buf[maze[h][w]] = False
        ans = 0
        for i in range(m):
            if buf[i]: ans += 1
        return ans




st = Solution()

print(st.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]])==1)
print(st.digArtifacts( n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]])==2)

