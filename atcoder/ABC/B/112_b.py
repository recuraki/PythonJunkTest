import sys
from io import StringIO
import unittest

def resolve():
    n,t = map(int, input().split())
    m = 1001
    index = -1
    for i in range(n):
        c1, t1 = map(int, input().split())
        if t1 <= t:
            if m >= c1:
                m = c1
                index = i + 1
    if m != 1001:
        print(m)
    else:
        print("TLE")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3 70
7 60
1 80
4 50"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 3
1 1000
2 4
3 1000
4 500"""
        output = """TLE"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 9
25 8
5 9
4 10
1000 1000
6 1"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()