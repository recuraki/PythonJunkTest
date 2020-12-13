import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n, m = map(int, input().split())
        dat = list(map(int, input().split()))

        untilnum = 0
        for i in range(n):
            if dat[i] != (i+1):
                untilnum = i


        x = 1
        for mm in range(m):
            r, p = input().split()
            r = int(r) - 1
            p = float(p)
            if r >= untilnum:
                x *= (1-p)
        if untilnum == 0:
            print("1.0")
            return

        print(1-x)

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
        input = """5
4 3
4 3 2 1
1 0.3
3 1
4 0.6
5 3
4 2 1 3 5
3 0.8
4 0.6
5 0.3
6 5
1 3 2 4 5 6
4 0.9
5 0.3
2 0.4
6 0.7
3 0.5
4 2
1 2 3 4
2 0.5
4 0.1
4 2
1 2 3 4
2 0.5
4 0.1"""
        output = """0.600000
0.720000
0.989500
1.000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
3 1
100 100 100
4 0.5
"""
        output = """"""
        output=""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()