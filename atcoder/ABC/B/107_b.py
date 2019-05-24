import sys
from io import StringIO
import unittest

def resolve():
    h, w = map(int, input().split())
    blankw = [True] * w
    blankh = [False] * h
    data = []
    for i in range(h):
        s = input()
        line = []
        if s.find("#") == -1:
            blankh[i] = True
        for j in range(w):
            line.append(s[j])
            if s[j] == "#":
                blankw[j] = False
        data.append(line)

    for i in range(h):
        if blankh[i] is True:
            continue
        for j in range(w):
            if blankw[j] is True:
                continue
            print(data[i][j], end="")

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
        input = """4 4
##.#
....
##.#
.#.#"""
        output = """###
###
.##"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 3
#..
.#.
..#"""
        output = """#..
.#.
..#"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 5
.....
.....
..#..
....."""
        output = """#"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """7 6
......
....#.
.#....
..#...
..#...
......
.#..#."""
        output = """..#
#..
.#.
.#.
#.#"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()