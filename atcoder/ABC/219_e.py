import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    def do():
        dat = []
        dat.append(list(map(int, input().split())))
        dat.append(list(map(int, input().split())))
        dat.append(list(map(int, input().split())))
        dat.append(list(map(int, input().split())))
        maze = []
        for _ in range(5):
            maze.append([0] * 5)

        res = 0
        for pat in range(2**5):
            for i in range(5):
                for j in range(5):
                    if ((pat >> (5*j) >> i) & 1) == 1:
                        maze[j][i] = 0
                    else:
                        maze[j][i] = 1
            # check 偶数
            can = True
            for i in range(5):
                if maze[i].count(1)%2 == 1:
                    can = False
                    break
            if can is False: continue
            for i in range(5):
                cnt = 0
                for j in range(5):
                    if maze[j][i] == 1: cnt += 1
                if cnt % 2 == 1:
                    can = False
                    break
            if can is False: continue
            def f(l):
                res =[]
                a = None
                for i in range(5):
                    if l[i] == 1:
                        if a == None:
                            a = i
                        else:
                            res.append( [a, i] )
                            a = None
                return res

            flag = f(maze[0])
            for i in range(5):
                newflag = f(maze[1])
                for l, r in newflag:
                    for x in flag:
                        if x[0] ==






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
        input = """1 0 0 0
0 0 1 0
0 0 0 0
1 0 0 0"""
        output = """1272"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()