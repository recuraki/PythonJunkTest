import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        h, w = map(int, input().split())
        maze = []
        for hh in range(h):
            l = input()
            l = l.replace("*", "1")
            l = l.replace(".", "0")
            l = list(map(int, l))
            maze.append(l)
        maze.reverse()
        res = 0
        for hh in range(h):
            if hh == 0:
                res += sum(maze[hh])
                continue
            for ww in range(w):
                if maze[hh][ww] == 0:
                    continue
                if ww == 0 or ww == w-1:
                    res += maze[hh][ww]
                    continue
                if maze[hh-1][ww-1] != 0 and maze[hh-1][ww+1] != 0 and maze[hh-1][ww] != 0:
                    maze[hh][ww] = min(maze[hh-1][ww-1], maze[hh-1][ww+1], maze[hh-1][ww]) + 1
                res += maze[hh][ww]



        #pprint(maze)
        print(res)

    q = int(input())
    for _ in range(q):
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
        input = """4
2 3
.*.
***
2 3
.*.
**.
4 5
.***.
*****
*****
*.*.*
5 7
..*.*..
.*****.
*******
.*****.
..*.*.."""
        output = """5
3
23
34"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
500 500
"""
        for i in range(500):
            input += "*"* 500 + "\n"
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()