import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, m = map(int, input().split())
    data = list(map(int, input().split()))
    datb = list(map(int, input().split()))
    res = 999999999999
    for i in range(m):
        x, y, c = map(int, input().split())
        t = data[x - 1] + datb [y - 1] - c
        res = min(res, t)
    data.sort()
    datb.sort()
    res = min(res, data[0] + datb[0])
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
        input = """2 3 1
3 3
3 3 3
1 2 1"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1 2
10
10
1 1 5
1 1 10"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 2 1
3 5
3 5
2 2 2"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()