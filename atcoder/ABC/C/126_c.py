import sys
from io import StringIO
import unittest

def resolve():
    import math
    n,k = map(int, input().split())
    res = float(0)
    orig = math.ceil(math.log2(k) )
    count = 0
    for i in range(1, n+1):
        if i > k:
            count += pow(2,orig)
        else:
            # iからスコアがk以上になるにはt回連続で表じゃないといけない
            t = math.ceil(math.log2(k) - math.log2(i))
            tt = pow(2, orig - t )
            count += tt
    res = count / (n*pow(2,orig))
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
    def test_入力例_1(self):
        input = """3 10"""
        output = """0.145833333333"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """100000 5"""
        output = """0.999973749998"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()