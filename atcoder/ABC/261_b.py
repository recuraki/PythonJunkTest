import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        maze = []
        n = int(input())
        for _ in range(n):
            l = list(input())
            maze.append(l)

        for i in range(n):
            for j in range(n):
                if i == j: continue
                if maze[i][j] == 'W' and maze[j][i] == 'L': continue
                if maze[j][i] == 'W' and maze[i][j] == 'L': continue
                if maze[j][i] == 'D' and maze[i][j] == 'D': continue
                print("incorrect")
                return
        print("correct")

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
-WWW
L-DD
LD-W
LDW-"""
        output = """incorrect"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
-D
D-"""
        output = """correct"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()