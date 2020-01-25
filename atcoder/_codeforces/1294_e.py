import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def dp(s):
        if True:
            print(s)

    def dpp(s):
        if True:
            pprint(s)


    h, w = map(int,input().split())
    maze = []
    for i in range(h):
        maze.append(list(map(int, input().split())))

    tate_sa = []
    dat = []
    for y in range(h):
        l = []
        for x in range(w):
            e = maze[y][x]
            l.append(())





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
3 2 1
1 2 3
4 5 6"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1 2 3
4 5 6
7 8 9
10 11 12"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3 4
1 6 3 4
5 10 7 8
9 2 11 12"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()