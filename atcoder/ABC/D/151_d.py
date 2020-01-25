import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
    dat.append(list("#" * (w+2)))
    for i in range(h):
        dat.append(list("#" + input() + "#"))
    dat.append(list("#" * (w+2)))
"""
def resolve():
    from pprint import pprint

    INF = 1000000
    dx = [1, -1, 0,  0]
    dy = [0,  0, 1, -1]

    # 入力
    h, w = map(int, input().split())
    maze = []
    for i in range(h):
        maze.append(list(input()))

    # ワーシャルフロイド用に枠を作る。
    # 2次元マップしてもいいが面倒なので、１次元にする。[0 - x][0 - y]を[0- x * y]にflattenする
    wsmap = lambda a, b: (a * w + b)
    dp = []
    # 辺がない時はINFを入れのでデフォルト値とする
    for i in range(h * w):
        dp.append([INF] * (h * w))

    # 迷路ををグラフにする。
    for y in range(h):
        for x in range(w):
            if maze[y][x] == "#": # そのマスが壁なら何もしない(他のマストの連結はないので)
                continue
            # ワーシャルフロイドでは自分自身へのコストは0にしておく。
            dp[wsmap(y, x)][wsmap(y, x)] = 0
            # ４方向に移動できるかの判定
            for dir in range(len(dx)):
                nx, ny = x + dx[dir], y + dy[dir]
                if -1 < nx and nx < w and -1 < ny and ny < h: # 枠をはみ出ないかチェック
                    if maze[ny][nx] != "#": # そのマスが壁でないなら
                        dp[wsmap(y, x)][wsmap(ny, nx)] = 1 # コストを1にする

    # ワーシャルフロイドする
    for kk in range(h * w):
        for ii in range(h * w):
            for jj in range(h * w):
                dp[ii][jj] = min(dp[ii][jj], dp[ii][kk] + dp[kk][jj])

    # これで結果が出たので
    import itertools
    res = itertools.chain(*dp)  # 二次元配列を一次元にして
    res = filter(lambda x: x != INF, res)  # INFを取り除き
    res = max(res)  # 最大値を得る
    print(res)








class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """3 3
...
...
..."""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5
...#.
.#.#.
.#..."""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_2")
        input = """5 4
....
.##.
.###
.##.
...."""
        output = """12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()