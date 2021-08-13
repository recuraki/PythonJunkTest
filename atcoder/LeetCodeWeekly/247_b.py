from typing import List, Tuple
from pprint import pprint




import math
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        h = len(grid)
        w = len(grid[0])
        maze = [[None] * w for _ in range(h)]
        for level in range(math.ceil(min(h, w) / 2)):
            #print(level)
            cycle = []
            for hh in range(level, h - level - 1):
                curh, curw = hh, level
                #print(level, "1: ", curh, curw)
                x = (curh, curw)
                cycle.append(x)
            for ww in range(level, w - level - 1):
                curh, curw = h - 1 - level, ww
                #print(level, "2: ", curh, curw)
                x = (curh, curw)
                cycle.append(x)
            for hh in range(h - 1 - level, level, -1):
                curh, curw = hh, w - 1 - level
                #print(level, "3: ", curh, curw)
                x = (curh, curw)
                cycle.append(x)
            for ww in range(w - 1 - level, level, -1):
                curh, curw = level, ww
                #print(level, "4: ", curh, curw)
                x = (curh, curw)
                cycle.append(x)
            #print(cycle)
            n = len(cycle)
            for i in range(n):
                curh, curw = cycle[i]
                nexth, nextw = cycle[(i+k) % n]
                #print(curh, curw, nexth, nextw)
                maze[nexth][nextw] = grid[curh][curw]
            if len(cycle) == 0:
                #print("sp")
                maze[level][level] = grid[level][level]
        return maze




st = Solution()

#print(st.rotateGrid(grid = [[40,10],[30,20]], k = 1))
#print(st.rotateGrid(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2))
#print(st.rotateGrid(grid = [[1,2,3],[5,6,7],[9,10,11]], k = 1))
#print(st.rotateGrid(grid = [[1,2,3,4,0],[5,6,7,8,0],[9,10,11,12,0],[13,14,15,16,0],[1,1,1,1,1]], k = 2))
print(st.rotateGrid([[10,1,4,8],[6,6,3,10],[7,4,7,10],[1,10,6,1],[2,1,1,10],[3,8,9,2],[7,1,10,10],[7,1,4,9],[2,2,4,2],[10,7,5,10]], 1))