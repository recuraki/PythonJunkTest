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
        n, m = map(int, input().split())
        res = 0
        while




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
        input = """5
3 5
4 6
3 2
69 696
123456 654321"""
        output = """4
3
0
640
530866"""
        #self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_11")
        input = """1
69 696"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()