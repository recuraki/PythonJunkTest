import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # aがながい、 bが1
    h,w,a,b = map(int, input().split())
    maze = []
    from copy import deepcopy
    for hh in range(h):
        l = [0] * w
        maze.append(l)
    def do(i, j, a, b, maze):# 次はiとjに置きたい。mazeはコピーする
        if (i == h):
            if a == 0 and b == 0:
                return 1
            else:
                return 0
        if (j == w):
            return do(i+1, 0, a, b, maze)
        if maze[i][j] != 0:
            return do(i, j+1, a, b, maze)
        # 1このを置く
        res = 0
        if b > 0:
            newmaze = deepcopy(maze)
            newmaze[i][j] = 1
            res += do(i, j+1, a, b-1, newmaze)
        # 横置き
        if a > 0 and j != (w-1):
            newmaze = deepcopy(maze)
            newmaze[i][j] = 1
            newmaze[i][j+1] = 1
            res += do(i, j+1, a - 1, b, newmaze)
        # たて
        if a > 0 and i != (h-1):
            newmaze = deepcopy(maze)
            newmaze[i][j] = 1
            newmaze[i+1][j] = 1
            res += do(i, j+1, a - 1, b, newmaze)
        return res
    finalres = do(0, 0, a, b, maze)
    print(finalres)


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
        input = """2 2 1 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 4 1"""
        output = """18"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 4 8 0"""
        output = """36"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()