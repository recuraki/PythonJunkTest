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
        def doTry(l, k, canfloor=2):
            # lの中で、連続するk個の"#"があるか？ただし、canfloor個までは"."が合っても良い O(N)
            l = list(l)
            if len(l) < k: return False
            cnt = 0
            for i in range(k):
                if l[i] == "#": cnt += 1
            if cnt >= (k - canfloor): return True
            for i in range(k, len(l)):  # 今から読み込むindex
                if l[i] == "#": cnt += 1
                if l[i - k] == "#": cnt -= 1
                if cnt >= (k - canfloor): return True
            return False

        def diagonalListFromLeft(maze):
            ans = []
            hsize = len(maze)
            wsize = len(maze[0])
            for w in range(wsize):
                h = 0
                l = []
                while 0 <= w < wsize and 0 <= h < hsize:
                    l.append(maze[h][w])
                    h, w = h + 1, w - 1
                ans.append(l)
            for h in range(1, hsize):
                w = wsize - 1
                l = []
                while 0 <= w < wsize and 0 <= h < hsize:
                    l.append(maze[h][w])
                    h, w = h + 1, w - 1
                ans.append(l)
            return ans

        def diagonalListFromRight(maze):
            ans = []
            hsize = len(maze)
            wsize = len(maze[0])
            for w in range(wsize - 1, -1, -1):
                h = 0
                l = []
                while 0 <= w < wsize and 0 <= h < hsize:
                    l.append(maze[h][w])
                    h, w = h + 1, w + 1
                ans.append(l)
            for h in range(1, hsize):
                w = 0
                l = []
                while 0 <= w < wsize and 0 <= h < hsize:
                    l.append(maze[h][w])
                    h, w = h + 1, w + 1
                ans.append(l)
            return ans

        n = int(input())
        maze = []
        for h in range(n):
            maze.append(list(input()))
        for h in range(n): # 横方向
            if doTry(maze[h], 6): return True
        for w in range(n): # 縦方向
            l = []
            for h in range(n): l.append(maze[h][w])
            if doTry(l, 6): return True
        for l in diagonalListFromLeft(maze):
            if doTry(l, 6): return True
        for l in diagonalListFromRight(maze):
            if doTry(l, 6): return True
        return False

    print("Yes" if do() else "No")





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
        input = """8
........
........
.#.##.#.
........
........
........
........
........"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
######
######
######
######
######
######"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
..........
#..##.....
..........
..........
....#.....
....#.....
.#...#..#.
..........
..........
.........."""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()