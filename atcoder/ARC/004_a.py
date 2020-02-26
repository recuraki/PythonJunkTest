import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = []
    for _ in range(n):
        x, y = map(int, input().split())
        dat.append((x, y))
    res = -1
    for i in range(n):
        x1, y1 = dat[i]
        for j in range(i + 1, n):
            x2, y2 = dat[j]
            res = max(res, (x2-x1)**2 + (y2-y1)**2)
    import math
    print(math.sqrt(res))


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
1 1
2 4
4 3"""
        output = """3.605551"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
1 8
4 0
3 7
2 4
5 9
9 1
6 2
0 2
8 6
7 8"""
        output = """10.630146"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
0 0
0 100
100 0
100 100"""
        output = """141.421356"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """5
3 0
1 0
0 0
4 0
2 0"""
        output = """4.000000"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """4
2 2
0 0
1 1
3 3"""
        output = """4.242641"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()