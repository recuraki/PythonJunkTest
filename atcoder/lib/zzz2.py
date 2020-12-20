import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    h, w, m = map(int, input().split())
    maze = []
    for i in range(h):
        maze.append([])

    res = h * w
    for _ in range(m):
        y, x = map(int,input().split())
        x -= 1
        y -= 1
        maze[y].append(x)
        print(">",x, y)
    for i in range(h):
        maze[i].sort()
        maze[i].append(w)

    for hh in range(h):
        print(hh, maze[hh])
        for i in range(len(maze[hh]) - 1):
            l = maze[hh][i]
            r = maze[hh][i+1]
            #print(hh, l , r)








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
        input = """4 3 2
2 2
3 3"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 4 4
3 2
3 4
4 2
5 2"""
        output = """14"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """200000 200000 0"""
        output = """40000000000"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()