from typing import List, Tuple
from pprint import pprint


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        for h in range(1, n-1):
            l = []
            for w in range(1, n-1):
                x = -10000000
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        x = max(grid[h+i][w+j], x)
                l.append(x)
            ans.append(l)
        return ans



st = Solution()

print(st.largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])==[[9,9],[8,6]])
print(st.largestLocal( grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])==[[2,2,2],[2,2,2],[2,2,2]])

