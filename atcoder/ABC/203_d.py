import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    #input = sys.stdin.readline
    from pprint import pprint
    def do():
        from heapq import heappop, heappush, heapify
        n, k = map(int, input().split())
        maze = []
        ss = set()
        for _ in range(n):
            l = list(map(int, input().split()))
            maze.append(l)
            for x in l:
                ss.add(x)
        pprint(maze)
        buf = []
        from copy import deepcopy
        for h in range(n):
            for w in range(n - k+1):
                l = maze[h][w:w+k]
                l.sort()
                buf.append(l[k//2-1])
        for w in range(n):
            for h in range(n - k+1):
                l = []
                for hh in range(h, h+k):
                    l.append(maze[hh][w])
                l.sort()
                buf.append(l[k//2-1])

        buf.sort()
        print(buf)


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
        input = """3 2
1 7 0
5 8 11
10 4 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3
1 2 3
4 5 6
7 8 9"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()