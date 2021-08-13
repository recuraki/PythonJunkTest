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
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        ma = max(dat)
        mi = min(dat)
        ma = dat.index(ma)
        mi = dat.index(mi)
        mi, ma = min(mi,ma), max(mi,ma)
        res = 10**18
        res = min(res, ma + 1) # 左からとる
        res = min(res, n - mi) # 右からとる
        res = min(res, (mi + 1) + (n - ma ))
        print(res)
    q = int(input())
    for _ in range(q):
        do()
    # do()


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
        input = """5
5
1 5 4 3 2
8
2 1 3 4 5 6 8 7
8
4 2 3 1 8 6 7 5
4
3 4 2 1
4
2 3 1 4"""
        output = """2
4
5
3
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()