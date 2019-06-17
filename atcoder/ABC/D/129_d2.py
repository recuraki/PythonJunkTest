import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    from collections import deque
    h, w = map(int, input().split())

    m = deque([])
    mv = deque([])
    mh = deque([])

    for i in range(h):
        mh.append(deque([0] * w))
    for i in range(h):
        mv.append(deque([0] * w))

    for i in range(h):
        m.append(input())

    for i in range(h):
        c = 0
        for j in range(w):
            if m[i][j] == "#":
                mh[i][j] = 0
                for k in range(c):
                    mh[i][j - k - 1] = c
                c = 0
            else:
                c += 1
        for k in range(c):
            mh[i][w - 1 - k] = c

    for i in range(w):
        c = 0
        for j in range(h):
            if m[j][i] == "#":
                mv[j][i] = 0
                for k in range(c):
                    mv[j - k - 1][i] = c
                c = 0
            else:
                c += 1
        for k in range(c):
            mv[h - 1 - k][i] = c

    res = 0
    for i in range (h):
        for j in range(w):
            res = max(res, mv[i][j] + mh[i][j])
    print(res - 1)


    #pprint(mh)
    #pprint(mv)



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
        input = """4 6
#..#..
.....#
....#.
#.#..."""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8 8
..#...#.
....#...
##......
..###..#
...#..#.
##....#.
#...#...
###.#..#"""
        output = """13"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()