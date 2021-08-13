import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    from decimal import Decimal
    def do():
        gosa = Decimal(10**(-200))
        print(gosa)
        a, b, c, v = map(Decimal, input().split())
        def f(a, b, c, v):
            pred = Decimal(0)
            if a >= gosa:
                half = Decimal(min(a, v)) / 2
                pred += a * f(max(0, a-v), b + half, c+half, v)
            if b >= gosa:
                half = Decimal(min(b, v)) / 2
                pred += b * f(a + half, max(0, b-v), c+half, v)
            return Decimal((a + b) + pred)

        print(1+f(a, b, c, v))


    q = int(input())
    for _ in range(q):
        do()


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        self.maxDiff = 10000000
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """4
0.2 0.2 0.6 0.2
0.4 0.2 0.4 0.8
0.4998 0.4998 0.0004 0.1666
0.3125 0.6561 0.0314 0.2048"""
        output = """1.532000000000
1.860000000000
5.005050776521
4.260163673896"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
0.2 0.2 0.6 0.2
"""
        output = """1.532000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()