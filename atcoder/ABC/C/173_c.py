import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from copy import deepcopy
    from pprint import pprint
    h, w , k = map(int, input().split())
    maze = []
    res = 0
    for _ in range(h):
        l = list(input())
        maze.append(l)
    for hpat in range(2**h):
        for wpat in range(2**w):
            dat = deepcopy(maze)
            for hh in range(h):
                if (hpat >> hh) & 1 == 1:
                    dat[hh] = ["-"] * w
            for ww in range(w):
                if (wpat >> ww) & 1 == 1:
                    for i in range(h):
                        dat[i][ww] = "-"
            #pprint(dat)
            cnt = 0
            for i in range(h):
                cnt += dat[i].count("#")
            if cnt == k:
                res += 1
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
        input = """2 3 2
..#
###"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 3 4
..#
###"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 2 3
##
##"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """6 6 8
..##..
.#..#.
#....#
######
#....#
#....#"""
        output = """208"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()