import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    data = []
    datb = []
    res = 0
    import math
    for _ in range(n):
        a,b = map(int, input().split())
        data.append(a)
        datb.append(b)

    for i in range(n-1, -1, -1):
        a,b = data[i], datb[i]
        a += res
        t = math.ceil(a / b)
        t = b * t
        res += t - a
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
        input = """3
3 5
2 7
9 4"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
3 1
4 1
5 9
2 6
5 3
5 8
9 7"""
        output = """22"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()