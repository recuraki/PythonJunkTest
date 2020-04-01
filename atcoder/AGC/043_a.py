import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h, w = map(int, input().split())
    dat = []
    res = []
    for i in range(h):
        l = input()
        dat.append(l)
        res.append([99999] * w)
        # None: なし, 0:通路, 1:壁
    if dat[0][0] == "#":
        res[0][0] = 1
    else:
        res[0][0] = 0

    dx = [0, -1]
    dy = [-1, 0]

    for hh in range(h):
        for ww in range(w):
            for dir in range(len(dx)):
                px = ww + dx[dir]
                py = hh + dy[dir]
                if px >= -1 and py >= -1:
                    if dat[py][px] == dat[hh][ww]: # 地形が一緒
                        res[hh][ww] = min(res[hh][ww], res[py][px])
                    elif dat[hh][ww] == ".":
                        res[hh][ww] = min(res[hh][ww], res[py][px])
                    else:
                        res[hh][ww] = min(res[hh][ww], res[py][px] + 1)
    print(res[h-1][w-1])
    #print(res)




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
.##
.#.
##."""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2
#.
.#"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 4
..##
#...
###.
###."""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """5 5
.#.#.
#.#.#
.#.#.
#.#.#
.#.#."""
        output = """4"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_4")
        input = """6 6
.#.#.#
######
.####.
#####.
.####.
.####."""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()