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
        n = int(input())
        can = []
        maze = []
        dw = [-1, 0, 1, -1, 1, -1, 0, 1]
        dh = [-1, -1 ,-1, 0, 0, 1, 1, 1]
        for _ in range(n):
            l = map(int, list(input()))
            l = list(l)
            maze.append(l)
        for h in range(n):
            for w in range(n):
                for di in range(len(dw)):
                    s = ""
                    nh, nw = int(h), int(w)
                    s += str(maze[h][w])
                    for _ in range(n-1):
                        nh = nh + dh[di]
                        nw = nw + dw[di]
                        if nh < 0: nh = n-1
                        elif nw < 0: nw = n-1
                        elif nh >= n: nh = 0
                        elif nw >= n: nw = 0
                        s += str(maze[nh][nw])
                        #print(nh, nw)
                        #print(nh, nw, maze[nh][nw])
                    can.append(int("".join(s)))
        can.sort(reverse=True)
        print(can[0])
        #print(maze)

    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()


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
1161
1119
7111
1811"""
        output = """9786"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111"""
        output = """1111111111"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()