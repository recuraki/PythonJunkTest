import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 998244353
    h, w, k = map(int, input().split())
    maze = []
    maze2 = []
    for hh in range(h):
        l = ["."] * w
        maze.append(l)
        l = [0] * w
        maze2.append(l)
    for i in range(k):
        a,b,c = input().split()
        a = int(a)-1
        b = int(b)-1
        maze[a][b] = c
    maze2[0][0] = 1
    for hh in range(h):
        for ww in range(w):
            maze2[hh][ww] %= mod
            if maze[hh][ww] == "X" or maze[hh][ww] == ".":
                nh = hh + 1
                nw = ww + 1
                if nw < w:
                    maze2[hh][nw] += maze2[hh][ww]
                if nh < h:
                    maze2[nh][ww] += maze2[hh][ww]
            if maze[hh][ww] == "D":
                nh = hh + 1
                if nh < h:
                    maze2[nh][ww] += maze2[hh][ww]
            if maze[hh][ww] == "R":
                nw = ww + 1
                if nw < w:
                    maze2[hh][nw] += maze2[hh][ww]
    goal = maze2[h-1][w-1]
    maze2 = []
    for _ in range(h):
        l = [goal] * w
        maze2.append(l)
    print(maze2)
    for hh in range(h):
        for ww in range(w):
            maze2[hh][ww] %= mod
            if maze[hh][ww] == ".":
                nh = hh + 1
                nw = ww + 1
                if nw < w:
                    maze2[hh][nw] += maze2[hh][ww] * 2
                if nh < h:
                    maze2[nh][ww] += maze2[hh][ww] * 2
            if maze[hh][ww] == "X":
                nh = hh + 1
                nw = ww + 1
                if nw < w:
                    maze2[hh][nw] += maze2[hh][ww]
                if nh < h:
                    maze2[nh][ww] += maze2[hh][ww]
            if maze[hh][ww] == "D":
                nh = hh + 1
                if nh < h:
                    maze2[nh][ww] += maze2[hh][ww]
            if maze[hh][ww] == "R":
                nw = ww + 1
                if nw < w:
                    maze2[hh][nw] += maze2[hh][ww]
    print(maze2)






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
        input = """2 2 3
1 1 X
2 1 R
2 2 R"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 5
2 3 D
1 3 D
2 1 D
1 2 X
3 1 R"""
        output = """150"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5000 5000 10
585 1323 R
2633 3788 X
1222 4989 D
1456 4841 X
2115 3191 R
2120 4450 X
4325 2864 X
222 3205 D
2134 2388 X
2262 3565 R"""
        output = """139923295"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()