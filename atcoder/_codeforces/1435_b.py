import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    q = int(input())
    for _ in range(q):
        n, m = map(int, input().split())
        firstn = []
        firstm = []
        dictn = dict()
        dictm = dict()
        for i in range(n):
            l = list(map(int, input().split()))
            firstn.append(l[0])
            dictn[l[0]] = l
        for i in range(m):
            l = list(map(int, input().split()))
            firstm.append(l[0])
            dictm[l[0]] = l
            if l[0] in dictn:
                origin = l[0]
        maze = []
        for i in range(n):
            l = [-1] * m
            maze.append(l)
        for i in range(m):
            maze[0][i] = dictn[origin][i]
        for i in range(m):
            keyval = maze[0][i]
            for k in range(n):
                maze[k][i] = dictm[keyval][k]
        for i in range(n):
            print(" ".join(list(map(str, maze[i]))))




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
        input = """2
2 3
6 5 4
1 2 3
1 6
2 5
3 4
3 1
2
3
1
3 1 2"""
        output = """1 2 3
6 5 4
3
1
2"""
        self.assertIO(input, output)

    def test_input_12(self):
        print("test_input_2")

        input = """1
3 3
4 5 3
6 9 8
2 1 7
7 3 8
1 5 9
2 4 6
"""
        output = """2 1 7
4 5 3
6 9 8"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()