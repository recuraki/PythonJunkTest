import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    dat = []
    for _ in range(n):
        dat.append(list(map(int, input().split())))
    datc = []
    for _ in range(m):
        datc.append(int(input()))

    for i in range(n):
        res = 0
        for j in range(m):
            res += dat[i][j] * datc[j]
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
        input = """3 4
1 2 0 1
0 3 0 1
4 1 1 0
1
2
3
0"""
        output = """5
6
9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()