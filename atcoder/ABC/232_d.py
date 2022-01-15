import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    import math
    INF = 1 << 63
    def do():
        oh, ow = map(int, input().split())
        # for maze
        dh = [0, 1]
        dw = [1, 0]
        maze = []
        maze.append(["#"] * (ow+2))
        for h in range(oh):
            l = list(input())
            maze.append(["#"] + l + ["#"])
        maze.append(["#"] * (ow+2))
        visited = [[False] * (ow + 2) for _ in range(oh + 2)]
        from collections import deque
        q = deque([(1,1,1)])
        visited[1][1] = True
        ans = -1
        while len(q) > 0:
            ch, cw, step = q.popleft()
            ans = max(ans, step)
            for di in range(len(dh)):
                nh = ch + dh[di]
                nw = cw + dw[di]
                if maze[nh][nw] == "#": continue
                if visited[nh][nw]: continue
                visited[nh][nw] = True
                q.append( (nh, nw, step + 1) )
        print(ans)
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
        input = """3 4
.#..
..#.
..##"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1
."""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 5
.....
.....
.....
.....
....."""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()