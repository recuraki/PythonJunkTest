from typing import List, Tuple
from pprint import pprint


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        oh = len(grid1) # 標準高さ
        ow = len(grid1[0]) # 幅
        res = 0
        maze1 = []
        maze2 = []
        maze1.append([0] * (ow + 2))
        maze2.append([0] * (ow + 2))
        for i in range (oh):
            maze1.append([0] + grid1[i] + [0])
            maze2.append([0] + grid2[i] + [0])
        maze1.append([0] * (ow + 2))
        maze2.append([0] * (ow + 2))

        dx = [0, -1, 1, 0]
        dy = [-1, 0, 0, 1]

        import collections
        visited = [[False] * (ow+2) for _ in range(oh+2)]
        q = collections.deque([])

        for h in range(1, oh+1):
            for w in range(1, ow+1):
                if maze1[h][w] == 0:
                    visited[h][w] = True
                    continue
                if maze2[h][w] == 0:
                    visited[h][w] = True
                    continue

                q.append( (h, w) )
                canmake = True

                while len(q) > 0:
                    curh, curw = q.popleft()

                    maze2[curh][curw] = 0

                    for di in range(len(dx)):
                        nh, nw = curh + dy[di], curw + dx[di]

                        if maze2[nh][nw] == 1:
                            maze2[nh][nw] = 0
                            q.append((nh, nw))
                        else:
                            continue

                        if maze1[nh][nw] == 0:
                            canmake = False

                if canmake:
                    #print("canmake", h, w)
                    res += 1
        return res




st = Solution()

print(st.countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
print(st.countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))

print(st.countSubIslands([[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],[0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]], [[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]])== 0)
