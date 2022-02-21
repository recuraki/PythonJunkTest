import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():

        h, w = map(int, input().split())
        maze = []

        for _ in range(h):
            l = list(map(int, input().split()))
            maze.append(l)

        newmaze = []

        for ww in range(w):
            l = []
            for hh in range(h):
                l.append(maze[hh][ww])
            newmaze.append(l)

        h, w = w, h
        maze = newmaze
        for hh in range(h):
            print(" ".join(list(map(str, maze[hh]))))

    do()





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
1 2 3
4 5 6
7 8 9
10 11 12"""
        output = """1 4 7 10
2 5 8 11
3 6 9 12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2
1000000000 1000000000
1000000000 1000000000"""
        output = """1000000000 1000000000
1000000000 1000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()