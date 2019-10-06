import sys
from io import StringIO
import unittest

"""
123
456
789

3, 5

01234
11211
1#2#1
11211
"""

def resolve():
    global h, w, dat
    h, w = map(int, input().split())
    dat = []
    for i in range(h):
        dat.append(input())
    for y in range(h):
        for x in range(w):
            c = 0
            if dat[y][x] == "#":
                print("#", end="")
                continue

            if 0 < y:
                if dat[y - 1][x] == "#":  # 2
                    c += 1
                if 0 < x:
                    if dat[y - 1][x - 1] == "#":  # 1
                        c += 1
                if w - 1 > x:
                    if dat[y - 1][x + 1] == "#":  # 3
                        c += 1
            if 0 < x:
                if dat[y][x - 1] == "#":  # 4
                    c += 1
                if y < h - 1:
                    if dat[y + 1][x - 1] == "#":  # 7
                        c += 1

            if x < w - 1:
                if dat[y][x + 1] == "#":  # 6
                    c += 1
                if y < h - 1:
                    if dat[y + 1][x + 1] == "#":  # 9
                        c += 1

            if y < h - 1:
                if dat[y + 1][x] == "#":  # 8
                    c += 1
            print(c, end="")
        print("")


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3 5
.....
.#.#.
....."""
        output = """11211
1#2#1
11211"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 5
#####
#####
#####"""
        output = """#####
#####
#####"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#..."""
        output = """#####3
#8#7##
####5#
4#65#2
#5##21
#4#310"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()