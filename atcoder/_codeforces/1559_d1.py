import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        n, m1, m2 = map(int, input().split())
        dat = list(map(int, input().split()))

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
        input = """3 2 2
1 2
2 3
1 2
1 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 3 2
5 4
2 1
4 3
4 3
1 4"""
        output = """1
2 4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8 1 2
1 7
2 6
1 5"""
        output = """5
5 2
2 3
3 4
4 7
6 8"""
        self.assertIO(input
                      , output)
if __name__ == "__main__":
    unittest.main()