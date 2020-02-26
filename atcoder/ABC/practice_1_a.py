import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
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
            self.mazeSum = []

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

    n, k = map(int, input().split())
    dat = []
    mapW, mapB = [], []
    # Wでhitするmap と Bでhitするmap
    for _ in range(k):
        mapW.append([0] * k)
        mapB.append([0] * k)

    # 圧縮を行う
    for i in range(n):
        inp = input().split()
        # colorの列はW,B -> 0,1に変えておく
        x, y, c = int(inp[0]), int(inp[1]), 0 if inp[2] == "W" else 1
        x = x % (2*k)
        y = y % (2*k)
        # 第一象限か第三象限にいる場合はそのまま[0,k)の区間に詰め込む
        if (0 <= x < k and 0 <= y < k) or (k <= x  and k <= y):
            if c == 0:
                mapW[y % k][x % k] += 1
            else:
                mapB[y % k][x % k] += 1
        # 第二象限か第四象限の場合は判定する色を反転させて[0,k)の区間に詰め込む
        else:
            if c == 1:
                mapW[y % k][x % k] += 1
            else:
                mapB[y % k][x % k] += 1

    csw, csb = cumSum2D(), cumSum2D()
    csw.load(mapW)
    csb.load(mapB)

    fres = -1
    for yy in range(k+1):
        for xx in range(k+1):
            a = csw.query(0, 0, xx, yy)
            d = csw.query(xx, yy, k, k)
            b = csb.query(xx, 0, k, yy)
            c = csb.query(0, yy, xx, k)
            res = a+b+c+d
            fres = max(fres, res)
    print(fres)



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
        input = """4 3
0 1 W
1 2 W
5 3 B
5 4 B"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6 2
1 2 B
2 1 W
2 2 B
1 0 B
0 6 W
4 5 W"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1000
0 0 B
0 1 W"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()