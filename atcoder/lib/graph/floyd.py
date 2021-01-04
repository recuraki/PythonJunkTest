# n対nの最短経路を求める
class floyd():
    maze = []
    INF = float("inf")

    def __init__(self, n):
        self.table = [[self.INF] * (n) for _ in range(n)]
        self.n = n
        for i in range(n):
            self.table[i][i] = 0
    def makeEdge(self, s, t, w):
        self.table[s][t] = w
    def solve(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.table[i][j] = min(self.table[i][j], self.table[i][k] + self.table[k][j])
        # if self -> self = negative = this graph has NEGATIVE CYCLE
        for i in range(self.n):
            if self.table[i][i] < 0:
                return -1
        return 0

def grl_1_c():
    v, e = map(int, input().split())
    g = floyd(v)
    for _ in range(e):
        a, b, w = map(int, input().split())
        g.makeEdge(a, b, w)
    x = g.solve()
    if x < 0:
        print("NEGATIVE CYCLE")
        return
    from pprint import pprint
    for i in range(v):
        l = []
        for x in g.table[i]:
            if x == g.INF:
                l.append("INF")
            else:
                l.append(str(x))
        print(" ".join(l))


def abc():
    def load_maze(self, charWall = "#"):
        wsmap = lambda a, b: (a * w + b)
        # 辺がない時はINFを入れのでデフォルト値とする
        dp = [self.INF] * (h*w)

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

grl_1_c()