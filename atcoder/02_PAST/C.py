import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    n = int(input())
    maze = []
    for _ in range(n):
        s = input()
        maze.append(list(s))
    maze.reverse()
    #print(maze)
    dx = [-1, 0, 1]
    for i in range(n-1):
        for j in range(2*n - 1):
            if maze[i][j] != "X":
                continue
            for di in dx:
                nx = j + di
                if 0 <= nx <= (2*n - 2):
                    if maze[i+1][nx] == "#":
                        maze[i + 1][nx] = "X"
    maze.reverse()
    for i in range(n):
        print("".join(maze[i]))


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
        input = """5
....#....
...##X...
..#####..
.#X#####.
#########"""
        output = """....X....
...XXX...
..XX###..
.#X#####.
#########"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
.#.
#X#"""
        output = """.X.
#X#"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
.........#.........
........###........
.......#####.......
......#######......
.....#########.....
....###########....
...#############...
..###############..
.#################.
X#X########X#X####X"""
        output = """.........X.........
........XXX........
.......XXXXX.......
......XXXXXXX......
.....XXXXXXXXX.....
....XXXXXXXXXXX....
...XXX##XXXXXXXX...
..XXX####XXXXXXXX..
.XXX######XXXXX##X.
X#X########X#X####X"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()