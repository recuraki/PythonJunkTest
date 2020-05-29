import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys

    q = int(input())
    for _ in range(q):
        n, m, x, y = map(int, input().split())
        maze = []
        for i in range(n):
            s = input()
            maze.append(list(s))
        if x * 2 <= y: # 1x1 is best!
            cnt = 0
            for i in range(n):
                cnt += maze[i].count(".")
            print(cnt * x)
        else: # 1x2 can use
            cost = 0
            for i in range(n):
                j = 0
                while j < m:
                    if maze[i][j] == "*":
                        j += 1
                        continue
                    nj = j + 1
                    if nj >= m:
                        cost += x # use 1x1
                        j += 1
                        continue
                    if maze[i][nj] == ".": # use 1x2
                        cost += y
                        j += 2
                        continue
                    cost += x
                    j += 1
            print(cost)


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
        input = """5
1 1 10 1
.
1 2 10 1
..
2 1 10 1
.
.
3 3 3 7
..*
*..
.*.
3 3 7 3
...
...
..."""
        output = """10
1
20
18
30"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()