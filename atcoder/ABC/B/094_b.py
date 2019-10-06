import sys
from io import StringIO
import unittest

def resolve():
n,m,x = map(int, input().split())
dat = list(map(int, input().split()))
c_prev = 0
c_next = 0
for i in range(len(dat)):
    if dat[i] < x:
        c_prev += 1
    else:
        c_next += 1
print(min(c_prev, c_next))

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
        input = """5 3 3
1 2 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7 3 2
4 5 6"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10 7 5
1 2 3 4 6 8 9"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()