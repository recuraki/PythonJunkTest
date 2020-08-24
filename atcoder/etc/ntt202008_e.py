import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # 0 white, 1 black
    maze =[]
    h, w = map(int, input().split())
    y, x, c = map(int, input().split())
    for hh in range(h):
        l = map(int, input().split())
        l = list(l)
        maze.append(l)

    # up = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    import collections



    # 0 origin
    x -= 1
    y -= 1
    if maze[y][x] == c:
        #print("same color")
        pass
    else:
        q = [ [y, x] ]
        q = collections.deque(q)
        while len(q) > 0:
            cury, curx = q.pop()
            maze[cury][curx] = c # なにも考えずに塗る
            for d in range(len(dx)):
                ny, nx = cury + dy[d], curx + dx[d]
                if 0 <= ny <= h-1 and 0 <= nx <= w-1:
                    if maze[ny][nx] == c:
                        continue
                    q.append( [ny, nx] )

    # count
    res = 0
    for hh in range(h):
        res += maze[hh].count(1)
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
        input = """4 4
1 1 0
1 1 1 1
1 0 0 1
1 0 0 1
1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 4
2 2 0
1 1 1 1
1 0 0 1
1 0 0 1
1 1 1 1"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7 7
4 4 1
0 0 0 1 0 1 0
0 0 0 1 0 1 0
0 0 1 0 0 1 0
1 1 0 0 0 1 0
0 0 0 0 0 1 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0"""
        output = """41"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """11 36
6 8 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 0
0 0 1 0 0 0 1 1 1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0
0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 1 0 0 0 0 1 0 0
0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 0
0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 0 0 1 0 0
0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 0
0 0 1 0 0 0 1 1 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 1 0 0
0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"""
        output = """85"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """11 36
1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 0
0 0 1 0 0 0 1 1 1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0
0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 1 0 0 0 0 1 0 0
0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 0
0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 0 0 1 0 0
0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 0
0 0 1 0 0 0 1 1 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 1 0 0
0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"""
        output = """384"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()