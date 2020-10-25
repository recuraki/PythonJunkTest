import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        q = int(input())
        for _ in range(q):
            n = int(input())
            maze = []
            for i in range(n):
                s = input()
                l = list(s)
                maze.append(l)
            a = maze[0][1]
            b = maze[1][0]
            c = maze[n-1][n-2]
            d = maze[n-2][n-1]
            posa = [1,2]
            posb = [2,1]
            posc = [n, n-1]
            posd = [n-1, n]
            res = []
            if a == b: # 0,0  or 1,1
                t = a
                if c == a:
                    res.append(posc) # reverse c
                if d == a:
                    res.append(posd) # reverse d
            else: # 0,1 or 1,0
                if c == d:
                    if b==c:
                        res.append(posb) # reserse b
                    elif a==c:
                        res.append(posa) # reverse a
                else:
                    res.append(posb)
                    if a==c:
                        res.append(posc)  # reverse c
                    if a==d:
                        res.append(posd)  # reverse c

            print(len(res))
            for i in range(len(res)):
                print(res[i][0], res[i][1])

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
4
S010
0001
1000
111F
3
S10
101
01F
5
S0101
00000
01111
11111
0001F"""
        output = """1
3 4
2
1 2
2 1
0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()