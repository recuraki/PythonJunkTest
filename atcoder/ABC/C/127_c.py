import sys
from io import StringIO
import unittest

def resolve():
    n, m = map(int, input().split())
    mi = None
    ma = None
    fail = False
    for i in range(m):
        l, r = map(int, input().split())
        if mi is None:
            mi = r
        if ma is None:
            ma = l
        ma = max(l, ma)
        mi = min(r, mi)
        if mi < l:
            fail = True
        if r < ma:
            fail = True
    if fail:
        print("0")
    else:
        print(str(int(mi - ma) + 1))



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
        input = """4 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10 3
3 6
5 7
6 9"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """100000 1
1 100000"""
        output = """100000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()