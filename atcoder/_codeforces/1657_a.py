
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
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    sq = set()
    for i in range(100000):
        sq.add(i ** 2)

    def do():
        x, y = map(int, input().split())
        if x == y == 0:
            print(0)
            return
        a = x ** 2 + y ** 2
        if a in sq:
            print(1)
            return
        print(2)

    # n questions
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
        input = """3
8 6
0 0
9 15"""
        output = """1
0
2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()