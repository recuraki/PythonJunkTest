# 2次元累積和 Two-dimensional cumulative  sum
"""
maze[h][w]2次元累積和を作成し、
[x0, [y0, (x1), y1)の区間のクエリ
★x0,y0は閉区間, x1,y1は開区間です
load: O(h*w)
query: O(1)
update: 未サポート
"""
class cumSum2D():
    mazeSum = []
    h, w = 0, 0
    def __init__(self):
        maze = []

    def load(self, maze):
        self.h, self.w = len(maze), len(maze[0])
        # 2次元累積和は端の計算が面倒なので、0の行と0の列は0でうめ、1,1からうめていく
        for _ in range(self.h + 1):
            self.mazeSum.append([0] * (self.w + 1))
        for y in range(self.h):
            for x in range(self.w):
                res = maze[y][x]
                res += self.mazeSum[y + 1][x]
                res += self.mazeSum[y][x + 1]
                res -= self.mazeSum[y][x]
                self.mazeSum[y + 1][x + 1] = res

    def query(self, x0, y0, x1, y1):
        """
        [x0, [y0 からx1), y1)の2次元累積和
        x0,y0は閉区間, x1,y1は開区間です
        """
        # 0のほうが原点に近くあってほしい
        if x0 > x1 or y0 > y1:
            raise ValueError
        res = self.mazeSum[y1][x1]
        res -= self.mazeSum[y1][x0]
        res -= self.mazeSum[y0][x1]
        res += self.mazeSum[y0][x0]
        return res

maze = []
maze.append([0, 0, 1, 0, 1])
maze.append([1, 0, 1, 0, 1])
maze.append([0, 0, 0, 1, 1])
maze.append([1, 1, 1, 1, 1])
maze.append([0, 0, 1, 0, 1])
from pprint import pprint
cs = cumSum2D()
 cs.load(maze)
pprint(maze)
pprint(cs.mazeSum)

def test1(x0, y0, x1, y1):
    print("({0},{1}) to ({2},{3}) = {4}".format(x0, y0, x1, y1, cs.query(x0, y0, x1, y1)))

test1(0, 0, 0, 0)
test1(0, 0, 1, 1)
test1(0, 0, 2, 2)
test1(0, 0, 3, 3)
test1(3, 3, 5, 5)
test1(1, 0, 3, 3)

"""
[[0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1],
 [0, 0, 0, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 0, 1, 0, 1]]
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 2],
 [0, 1, 1, 3, 3, 5],
 [0, 1, 1, 3, 4, 7],
 [0, 2, 3, 6, 8, 12],
 [0, 2, 3, 7, 9, 14]]
(0,0) to (0,0) = 0
(0,0) to (1,1) = 0
(0,0) to (2,2) = 1
(0,0) to (3,3) = 3
(3,3) to (5,5) = 3
(1,0) to (3,3) = 2
"""