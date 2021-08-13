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

    INF = 1 << 63
    from math import gcd
    def do():
        a, b = map(int, input().split())
        res = INF
        for i in range(10):
            if gcd(a+i, b) != 1:
                res = min(res, i)
            if gcd(a, b+i) != 1:
                res = min(res, i)
            if gcd(a+i, b+i) != 1:
                res = min(res, i*2)
        print(res)



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
        input = """4
4 16
4 55
3 9
3 7"""
        output = """0
1
0
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()