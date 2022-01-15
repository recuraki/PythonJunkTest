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
        dh = [-1, 0, 0, 1]
        dw = [0, -1, 1, 0]
        maze = []
        maze.append([-1] * (ow+2) )
        for h in range(oh):
            l = list(input())
            for i in range(ow):
                if l[i] == ".": l[i] = -1
                else: l[i] = int(l[i])
            maze.append([-1] + l + [-1])
        maze.append([-1] * (ow+2) )
        #pprint(maze)
        for h in range(1, 1+oh):
            for w in range(1, 1 + ow):
                if maze[h][w] != -1: continue
                neighbor = set()
                neighbor.add(maze[h-1][w])
                neighbor.add(maze[h][w-1])
                neighbor.add(maze[h][w+1])
                neighbor.add(maze[h+1][w])
                for color in range(1, 6):
                    if color not in neighbor:
                        maze[h][w] = color
                        break
        for h in range(1, 1+oh):
            print("".join(list(map(str, maze[h][1:-1]))))

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
        input = """3 3
...
...
..."""
        output = """132
313
541"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 7
1.2.3.4
.5.1.2.
3.4.5.1
.2.3.4.
5.1.2.3"""
        output = """1425314
2531425
3142531
4253142
5314253"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 1
."""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()