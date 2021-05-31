import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h,w,hh,ww = map(int, input().split())
    hh -= 1
    ww -= 1
    maze = []
    for hhhh in range(h):
        l = list(input())
        maze.append(l)
    res = 1



    hhhh = hh
    wwww = ww
    for hhhh in range(hh+1, h):
        if maze[hhhh][wwww] == ".":
            res += 1
        else:
            break

    hhhh = hh
    wwww = ww
    for hhhh in range(hh-1, -1, -1):
        if maze[hhhh][wwww] == ".":
            res += 1
        else:
            break

    hhhh = hh
    wwww = ww
    for wwww in range(ww+1, w):
        if maze[hhhh][wwww] == ".":
            res += 1
        else:
            break

    hhhh = hh
    wwww = ww
    for wwww in range(ww-1, -1, -1):
        if maze[hhhh][wwww] == ".":
            res += 1
        else:
            break

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
        input = """4 4 2 2
##..
...#
#.#.
.#.#"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5 1 4
#....
#####
....#"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 5 4 2
.#..#
#.###
##...
#..#.
#.###"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()