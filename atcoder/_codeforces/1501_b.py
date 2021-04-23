import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        #print("---")
        n = int(input())
        dat = list(map(int, input().split()))
        res = [0] * n
        buf = [0] * n
        for i in range(n):
            x = dat[i]
            if x == 0:
                continue
            x = min(x, i+1)
            buf[i - (x-1)] = x
            #print(i, x)
            #print(buf)
        cur = 0
        for i in range(n):
            cur = max(cur, buf[i])
            if cur > 0:
                cur -= 1
                res[i] = 1
        print(" ".join(list(map(str, res))))

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
6
0 3 0 0 1 3
10
0 0 0 1 0 5 0 0 0 2
3
0 0 0"""
        output = """1 1 0 1 1 1
0 1 1 1 1 1 0 0 1 1
0 0 0"""
        self.assertIO(input, output)

    def test_input_12(self):
        print("test_input_12")
        input = """6
5
1 1 1 1 1
5
0 0 0 10 0
1
0
1
10
5
0 0 0 0 0
5
0 0 0 0 100
"""
        output = """1 1 1 1 1
1 1 1 1 0
0
1
0 0 0 0 0
1 1 1 1 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()