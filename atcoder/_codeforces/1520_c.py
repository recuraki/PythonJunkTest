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
        n = int(input())
        if n == 1:
            print("1")
            return
        if n == 2:
            print(-1)
            return
        maze = [[-1] * n for _ in range(n)]
        cur = 1
        flag = True
        for i in range(n):
            init = 0 if flag else 1
            for j in range(init, n, 2):
                maze[i][j] = cur
                cur += 1
            flag = not flag
        for i in range(n):
            for j in range(n):
                if maze[i][j] == -1:
                    maze[i][j] = cur
                    cur += 1
        #pprint(maze)
        for i in range(n):
            print(" ".join(list(map(str, maze[i]))))

    q = int(input())
    for _ in range(q):
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
        input = """3
1
2
3"""
        output = """1
-1
2 9 7
4 6 3
1 8 5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
4"""
        output = """xxx"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()