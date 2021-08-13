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
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        buf = 0
        res = -1
        for i in range(n-1):
            res = max(res, dat[i]*dat[i+1])
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
3
2 4 3
4
3 2 3 1
2
69 69
6
719313 273225 402638 473783 804745 323328"""
        output = """12
6
4761
381274500335"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()