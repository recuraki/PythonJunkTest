
class floyd():

    maze = []

    def __init__(self):
        self.maze = []

    def build(self):
        # ワーシャルフロイド用に枠を作る。
        # 2次元マップしてもいいが面倒なので、１次元にする。[0 - x][0 - y]を[0- x * y]にflattenする
        wsmap = lambda a, b: (a * w + b)
        dp = []
        # 辺がない時はINFを入れのでデフォルト値とする
        for i in range(h * w):
            dp.append([INF] * (h * w))

    def load_maze(self, charWall = "#"):
        h, w = map(int, input().split())
        for i in range(h):
            self.maze.append(list(input()))
        # 迷路ををグラフにする。(２次次元)
        for y in range(h):
            for x in range(w):
                if self.maze[y][x] == charWall: # そのマスが壁なら何もしない(他のマストの連結はないので)
                    continue
                # ワーシャルフロイドでは自分自身へのコストは0にしておく。
                dp[wsmap(y, x)][wsmap(y, x)] = 0
                # ４方向に移動できるかの判定
                for dir in range(len(dx)):
                    nx, ny = x + dx[dir], y + dy[dir]
                    if -1 < nx and nx < w and -1 < ny and ny < h: # 枠をはみ出ないかチェック
                        if maze[ny][nx] != "#": # そのマスが壁でないなら
                            dp[wsmap(y, x)][wsmap(ny, nx)] = 1 # コストを1にする

import sys
from io import StringIO
stdout, stdin = sys.stdout, sys.stdin
inp = """5 4
....
.##.
.###
.##.
...."""
sys.stdin = StringIO(inp)
load_maze()
sys.stdout, sys.stdin = stdout, stdin
